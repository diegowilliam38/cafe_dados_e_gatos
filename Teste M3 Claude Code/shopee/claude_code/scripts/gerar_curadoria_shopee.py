"""
Shopee - Curadoria de Produtos
================================

Script principal e reutilizável para análise do CSV bruto da Shopee e
geração dos arquivos finais (CSV/JSON) que alimentam o site estático
de achadinhos.

Para atualizar a curadoria:
1. Substitua/subar o novo CSV em ~/Documents/shopee/raw/
2. Rode: python3 scripts/gerar_curadoria_shopee.py

Separação obrigatória:
- Camada interna (CSVs, JSONs internos, logs, script): pode usar termos
  técnicos (score, potencial, modelo, ambiente, etc.).
- Site público: usa somente linguagem editorial leve de achadinhos.
  Os metadados técnicos e termos de venda comprovada nunca aparecem lá.
"""

from __future__ import annotations

import json
import os
import re
import sys
import traceback
from datetime import datetime
from pathlib import Path

import pandas as pd

# ----------------------------------------------------------------------------
# Metadados obrigatórios
# ----------------------------------------------------------------------------

METADATA = {
    "metodo_curadoria_version": "shopee_potencial_v1_04_06_2026",
    "modelo_usado": "Claude Code",
    "ambiente": "claude_code",
    "ferramenta_orquestracao": "Claude Code",
}

# Categorias finais do site (definição oficial)
CATEGORIAS_FINAIS = [
    "moda",
    "beleza",
    "acessórios para celular",
    "casa",
    "cozinha",
    "organização",
    "pets",
    "papelaria",
    "infantil",
    "fitness",
]

LIMITE_POR_CATEGORIA = 4

# ----------------------------------------------------------------------------
# Caminhos
# ----------------------------------------------------------------------------

HOME = Path.home()
RAW_DIR = HOME / "Documents" / "shopee" / "raw"
BASE_DIR = HOME / "Documents" / "shopee" / "claude_code"
DATA_PROCESSED = BASE_DIR / "data" / "processed"
DATA_FINAL = BASE_DIR / "data" / "final"
LOGS_DIR = BASE_DIR / "logs"
SITE_DIR = BASE_DIR / "site"
SITE_DATA_DIR = SITE_DIR / "data"

# ----------------------------------------------------------------------------
# Heurística de categoria (somente global_category1 e global_category2)
# ----------------------------------------------------------------------------
# Observação: se não for possível classificar com confiança, o produto é
# registrado como categoria_final_nao_identificada e sai dos arquivos finais.
# ----------------------------------------------------------------------------

CAT1_TO_FINAL = {
    "Home & Living": ["casa"],
    "Beauty": ["beleza"],
    "Mobile & Gadgets": ["acessórios para celular"],
    "Sports & Outdoors": ["fitness"],
    "Pets": ["pets"],
    "Stationery": ["papelaria"],
    "Women Clothes": ["moda"],
    "Men Clothes": ["moda"],
    "Women Shoes": ["moda"],
    "Men Shoes": ["moda"],
    "Fashion Accessories": ["moda"],
    "Baby & Kids Fashion": ["infantil", "moda"],
    "Mom & Baby": ["infantil"],
    "Health": ["beleza"],
    "Hobbies & Collections": [],  # sem categoria final
    "Spare Parts and Accessories for Vehicles": [],  # sem categoria final
    "Home Appliances": ["casa"],
    "Food & Beverages": [],  # sem categoria final
    "Books & Magazines": [],  # sem categoria final
    "Computers & Accessories": [],  # sem categoria final
}

# CAT2 mais específico tem prioridade sobre CAT1
CAT2_TO_FINAL = {
    "Kitchenware": ["cozinha"],
    "Dinnerware": ["cozinha"],
    "Kitchen Appliances": ["cozinha"],
    "Home Organizers": ["organização"],
    "Storage & Organisation": ["organização"],
    "Sports & Outdoor Recreation Equipments": ["fitness"],
    "Toys": ["infantil"],
    "Notebooks & Papers": ["papelaria"],
    "Stationery Supplies": ["papelaria"],
    "Pet Care": ["pets"],
    "Pet Supplies": ["pets"],
    "Tools & Home Improvement": ["casa"],
    "Decoration": ["casa"],
    "Furniture": ["casa"],
    "Home Care Supplies": ["casa"],
    "Hair Care": ["beleza"],
    "Hand, Foot & Nail Care": ["beleza"],
    "Beauty Tools": ["beleza"],
    "Food Supplement": ["beleza"],
    "Makeup": ["beleza"],
    "Tops": ["moda"],
    "Bottoms": ["moda"],
    "Dresses": ["moda"],
    "Outerwear": ["moda"],
    "Accessories": ["moda"],
}


def carregar_links_manuais_anteriores(logger: Logger) -> dict:
    """Carrega link_gerado_shopee de uma execução anterior, se existir.
    Preserva o trabalho manual da Denise entre execuções. Procura primeiro
    em site/data/ (onde Denise costuma editar) e, em fallback, em
    data/final/."""
    candidatos = [SITE_DATA_DIR / "links_shopee_manual.csv",
                  DATA_FINAL / "links_shopee_manual.csv"]
    for path in candidatos:
        if path.exists():
            try:
                df_old = pd.read_csv(path)
                if "itemid" in df_old.columns and "link_gerado_shopee" in df_old.columns:
                    # manter apenas itemids com link não-vazio
                    df_valid = df_old[df_old["link_gerado_shopee"].notna()]
                    df_valid = df_valid[df_valid["link_gerado_shopee"].astype(str).str.strip() != ""]
                    links = dict(zip(df_valid["itemid"].astype(str),
                                     df_valid["link_gerado_shopee"].astype(str)))
                    logger.add("links_manuais_anteriores_carregados",
                               f"{len(links)} (de {path})")
                    return links
            except Exception as e:
                logger.add("aviso_links_manuais", f"falha ao ler {path}: {e}")
    logger.add("links_manuais_anteriores_carregados", "0 (nenhum arquivo anterior)")
    return {}



def classificar_categoria(row: pd.Series) -> str | None:
    """Define a categoria_final usando SOMENTE global_category1 e
    global_category2. Retorna None se não classificar com confiança.

    Regra de prioridade:
    1) Se global_category2 casar com categoria_final específica
       (ex.: Kitchenware -> cozinha), usa essa.
    2) Caso contrário, usa a categoria final vinda de global_category1.
    """
    cat1 = str(row.get("global_category1", "") or "").strip()
    cat2 = str(row.get("global_category2", "") or "").strip()

    if cat2 in CAT2_TO_FINAL and CAT2_TO_FINAL[cat2]:
        return CAT2_TO_FINAL[cat2][0]
    if cat1 in CAT1_TO_FINAL and CAT1_TO_FINAL[cat1]:
        return CAT1_TO_FINAL[cat1][0]
    return None


# ----------------------------------------------------------------------------
# Porte estimado (usa SOMENTE description)
# ----------------------------------------------------------------------------

PORTE_SINAIS_GRANDE = [
    "grande", "king", "queen", "gigante", "familia", "família",
    "conjunto", "kit", "completo", "organizador",
]
PORTE_SINAIS_PEQUENO = [
    "pequeno", "mini", "portatil", "portátil", "compacto", "pocket",
    "chaveiro", "adesivo", "caneta", "pulseira",
]
PORTE_SINAIS_MEDIDA = [
    r"\b\d+\s*(cm|mm|ml|l|kg|g|un|pcs|pe[çc]as?)\b",
]


def estimar_porte(descricao: str) -> str:
    """Estima porte do produto (pequeno / grande / indefinido) a partir
    SOMENTE da descrição. Não usa title, image_link nem categorias."""
    if not isinstance(descricao, str) or not descricao.strip():
        return "indefinido"
    texto = descricao.lower()
    if any(s in texto for s in PORTE_SINAIS_GRANDE):
        if any(re.search(p, texto) for p in PORTE_SINAIS_MEDIDA):
            return "grande"
        return "grande"
    if any(s in texto for s in PORTE_SINAIS_PEQUENO):
        return "pequeno"
    if any(re.search(p, texto) for p in PORTE_SINAIS_MEDIDA):
        return "grande"
    return "indefinido"


# ----------------------------------------------------------------------------
# Score interno
# ----------------------------------------------------------------------------

def calcular_score(row: pd.Series) -> float:
    """Calcula score_potencial_comercial (uso INTERNO apenas).
    Sinais: rating, sale_price, discount, presença de link/imagem,
    categoria, porte_estimado. Não usa title/description para score
    de categoria."""
    score = 0.0

    # Rating (peso alto)
    try:
        rating = float(row.get("item_rating", 0) or 0)
        if rating > 0:
            score += (rating - 4.0) * 30  # ~30 pts por ponto acima de 4
    except (ValueError, TypeError):
        pass

    # sale_price no "sweet spot" (20-80)
    try:
        sp = float(row.get("sale_price", 0) or 0)
        if 20 <= sp <= 80:
            score += 25
        elif 15 <= sp <= 100:
            score += 10
    except (ValueError, TypeError):
        pass

    # Desconto
    try:
        d = float(row.get("discount_percentage", 0) or 0)
        if d >= 30:
            score += 15
        elif d >= 15:
            score += 8
    except (ValueError, TypeError):
        pass

    # Presença de imagem
    if isinstance(row.get("image_link"), str) and row["image_link"].strip():
        score += 8

    # Presença de link
    if isinstance(row.get("product_link"), str) and row["product_link"].strip():
        score += 5

    # Porte
    porte = row.get("porte_estimado", "indefinido")
    if porte == "pequeno":
        score += 5
    elif porte == "grande":
        score += 3

    return round(score, 4)


# ----------------------------------------------------------------------------
# Limpeza de título
# ----------------------------------------------------------------------------

def limpar_titulo(titulo: str) -> str:
    if not isinstance(titulo, str):
        return ""
    t = titulo.replace("\n", " ").replace("\r", " ")
    t = re.sub(r"\s+", " ", t).strip()
    # sem inventar marca/característica, só normalização de espaços
    return t


# ----------------------------------------------------------------------------
# Logger
# ----------------------------------------------------------------------------

class Logger:
    def __init__(self, path: Path):
        self.path = path
        self.lines: list[str] = []
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def add(self, key: str, value) -> None:
        self.lines.append(f"[{key}] {value}")

    def save(self) -> None:
        with self.path.open("w", encoding="utf-8") as f:
            f.write("\n".join(self.lines))
        print(f"LOG salvo em: {self.path}")


# ----------------------------------------------------------------------------
# Pipeline principal
# ----------------------------------------------------------------------------

def main() -> int:
    inicio = datetime.now()
    log_path = LOGS_DIR / f"execucao_{inicio.strftime('%Y%m%d_%H%M%S')}.log"
    logger = Logger(log_path)

    logger.add("inicio", inicio.isoformat())
    logger.add("csv_bruto_dir", str(RAW_DIR))
    logger.add("base_dir", str(BASE_DIR))
    for k, v in METADATA.items():
        logger.add(k, v)

    # ------------------------------------------------------------
    # 1) Localizar CSV em raw/
    # ------------------------------------------------------------
    if not RAW_DIR.exists():
        msg = f"ERRO: pasta {RAW_DIR} não encontrada."
        logger.add("erro", msg)
        logger.save()
        return _falhar(logger, msg)

    csvs = sorted(RAW_DIR.glob("*.csv"))
    if not csvs:
        msg = f"ERRO: nenhum CSV em {RAW_DIR}."
        logger.add("erro", msg)
        logger.save()
        return _falhar(logger, msg)
    if len(csvs) > 1:
        msg = f"ERRO: mais de um CSV em {RAW_DIR}: {[c.name for c in csvs]}"
        logger.add("erro", msg)
        logger.save()
        return _falhar(logger, msg, chamar_denise=True)

    csv_path = csvs[0]
    logger.add("csv_usado", csv_path.name)

    # ------------------------------------------------------------
    # 1.5) Carregar links manuais anteriores (preserva trabalho da Denise)
    # ------------------------------------------------------------
    links_manuais_anteriores = carregar_links_manuais_anteriores(logger)

    # ------------------------------------------------------------
    # 2) Ler CSV
    # ------------------------------------------------------------
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        msg = f"ERRO ao ler CSV: {e}"
        logger.add("erro", msg)
        logger.save()
        return _falhar(logger, msg)

    logger.add("total_linhas", len(df))
    logger.add("produtos_unicos_itemid", df["itemid"].nunique())
    logger.add("colunas_encontradas", ", ".join(df.columns))

    colunas_esperadas = [
        "itemid", "title", "description", "price", "sale_price",
        "discount_percentage", "item_rating", "global_category1",
        "global_category2", "product_link", "product_short link",
        "image_link",
    ]
    ausentes = [c for c in colunas_esperadas if c not in df.columns]
    if ausentes:
        logger.add("colunas_ausentes", ", ".join(ausentes))

    # ------------------------------------------------------------
    # 3) Saneamento de chaves
    # ------------------------------------------------------------
    df = df.dropna(subset=["itemid"]).copy()
    df = df.drop_duplicates(subset=["itemid"], keep="first").reset_index(drop=True)
    logger.add("apos_dedupe_itemid", len(df))

    # ------------------------------------------------------------
    # 4) Remover produtos sem product_link
    # ------------------------------------------------------------
    antes = len(df)
    df = df[df["product_link"].notna() & (df["product_link"].astype(str).str.strip() != "")]
    logger.add("removidos_sem_product_link", antes - len(df))

    # ------------------------------------------------------------
    # 5) Definir sale_price para filtro
    # ------------------------------------------------------------
    usou_fallback = False
    if "sale_price" not in df.columns:
        df["sale_price"] = df.get("price", 0)
        usou_fallback = True
    else:
        df["sale_price"] = df["sale_price"].fillna(df.get("price", 0))

    df["sale_price_num"] = pd.to_numeric(df["sale_price"], errors="coerce").fillna(0)
    if usou_fallback:
        logger.add("info", "sale_price ausente: usando price como fallback no filtro.")

    # ------------------------------------------------------------
    # 6) Filtro de preço (R$ 20 a R$ 80)
    # ------------------------------------------------------------
    antes = len(df)
    df = df[(df["sale_price_num"] >= 20) & (df["sale_price_num"] <= 80)]
    logger.add("removidos_por_preco", antes - len(df))

    # ------------------------------------------------------------
    # 7) Filtro de rating (> 4.0)
    # ------------------------------------------------------------
    df["item_rating_num"] = pd.to_numeric(df.get("item_rating", 0), errors="coerce").fillna(0)
    antes = len(df)
    df = df[df["item_rating_num"] > 4.0]
    logger.add("removidos_por_nota", antes - len(df))

    # ------------------------------------------------------------
    # 8) Categoria final
    # ------------------------------------------------------------
    df["categoria_final"] = df.apply(classificar_categoria, axis=1)
    antes = len(df)
    sem_cat = df["categoria_final"].isna().sum()
    df = df.dropna(subset=["categoria_final"])
    logger.add("removidos_por_categoria_nao_identificada", int(sem_cat))

    # ------------------------------------------------------------
    # 9) Porte estimado (apenas description)
    # ------------------------------------------------------------
    df["porte_estimado"] = df.get("description", "").astype(str).apply(estimar_porte)

    # ------------------------------------------------------------
    # 10) Score interno
    # ------------------------------------------------------------
    df["score_potencial_comercial"] = df.apply(calcular_score, axis=1)

    # ------------------------------------------------------------
    # 11) title_clean
    # ------------------------------------------------------------
    df["title_clean"] = df.get("title", "").astype(str).apply(limpar_titulo)

    # ------------------------------------------------------------
    # 12) Garantir colunas opcionais
    # ------------------------------------------------------------
    for col, default in [
        ("price", None), ("sale_price", None),
        ("discount_percentage", None), ("item_rating", None),
        ("image_link", None), ("product_link", None),
    ]:
        if col not in df.columns:
            df[col] = default

    # ------------------------------------------------------------
    # 13) Limite de 4 por categoria (mantém os melhores por score)
    # ------------------------------------------------------------
    antes = len(df)
    df = (
        df.sort_values("score_potencial_comercial", ascending=False)
        .groupby("categoria_final", as_index=False, group_keys=False)
        .head(LIMITE_POR_CATEGORIA)
        .reset_index(drop=True)
    )
    logger.add("apos_limite_4_por_categoria", len(df))
    logger.add(
        "validacao_limite_4_por_categoria",
        "OK" if df.groupby("categoria_final").size().max() <= 4 else "FALHA",
    )

    # ------------------------------------------------------------
    # 14) Salvar arquivos finais (camada interna)
    # ------------------------------------------------------------
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    DATA_FINAL.mkdir(parents=True, exist_ok=True)

    colunas_finais = [
        "itemid", "categoria_final", "title_clean",
        "price", "sale_price", "discount_percentage",
        "item_rating", "image_link", "product_link",
        "porte_estimado", "score_potencial_comercial",
    ]
    # manter colunas extras (descrição, etc.) em arquivo intermediário
    df_filtrado = df[colunas_finais].copy()

    # Aplicar link_gerado_shopee vindo de execuções anteriores
    df_filtrado["link_gerado_shopee"] = (
        df_filtrado["itemid"].astype(str).map(links_manuais_anteriores).fillna("")
    )
    links_preenchidos = (df_filtrado["link_gerado_shopee"] != "").sum()
    logger.add("links_gerados_preservados",
               f"{int(links_preenchidos)} de {len(df_filtrado)}")

    df_filtrado.to_csv(DATA_PROCESSED / "produtos_filtrados.csv", index=False)
    df_filtrado.to_csv(DATA_FINAL / "produtos_curadoria_final.csv", index=False)
    df_filtrado.to_json(
        DATA_FINAL / "produtos_curadoria_final.json",
        orient="records", force_ascii=False, indent=2,
    )

    # Quantidade por categoria
    qtd_por_cat = df_filtrado.groupby("categoria_final").size().to_dict()
    logger.add("quantidade_por_categoria", json.dumps(qtd_por_cat, ensure_ascii=False))

    # ------------------------------------------------------------
    # 15) Arquivo por categoria para o site (inclui link_gerado_shopee)
    # ------------------------------------------------------------
    site_csv = DATA_FINAL / "produtos_site_por_categoria.csv"
    site_json = DATA_FINAL / "produtos_site_por_categoria.json"
    df_filtrado.to_csv(site_csv, index=False)
    df_filtrado.to_json(site_json, orient="records", force_ascii=False, indent=2)

    # ------------------------------------------------------------
    # 16) Arquivo manual de links
    # ------------------------------------------------------------
    links = df_filtrado[["itemid", "categoria_final", "title_clean",
                          "product_link", "link_gerado_shopee"]].copy()
    links = links.rename(columns={"product_link": "product_url"})
    links.to_csv(DATA_FINAL / "links_shopee_manual.csv", index=False)

    # ------------------------------------------------------------
    # 17) Copiar para site/data
    # ------------------------------------------------------------
    SITE_DATA_DIR.mkdir(parents=True, exist_ok=True)
    # Mapeamento: nome interno -> nome público (sem "curadoria")
    site_files = {
        "produtos_site_por_categoria.json": "achadinhos.json",
        "produtos_site_por_categoria.csv": "achadinhos.csv",
        "links_shopee_manual.csv": "links_shopee_manual.csv",
    }
    for src_name, dst_name in site_files.items():
        src = DATA_FINAL / src_name
        dst = SITE_DATA_DIR / dst_name
        dst.write_bytes(src.read_bytes())
    logger.add("copia_site_data", "OK (3 arquivos)")

    # ------------------------------------------------------------
    # 18) Validação final
    # ------------------------------------------------------------
    validacoes = {
        "produtos_curadoria_final.csv existe": (DATA_FINAL / "produtos_curadoria_final.csv").exists(),
        "produtos_curadoria_final.json existe": (DATA_FINAL / "produtos_curadoria_final.json").exists(),
        "produtos_site_por_categoria.csv existe": (DATA_FINAL / "produtos_site_por_categoria.csv").exists(),
        "produtos_site_por_categoria.json existe": (DATA_FINAL / "produtos_site_por_categoria.json").exists(),
        "links_shopee_manual.csv existe": (DATA_FINAL / "links_shopee_manual.csv").exists(),
        "site/data achadinhos.json existe": (SITE_DATA_DIR / "achadinhos.json").exists(),
        "site/data achadinhos.csv existe": (SITE_DATA_DIR / "achadinhos.csv").exists(),
        "max_4_por_categoria": df_filtrado.groupby("categoria_final").size().max() <= 4,
        "todos_tem_categoria_final": df_filtrado["categoria_final"].notna().all(),
        "todos_tem_product_link": df_filtrado["product_link"].notna().all(),
    }
    # link_gerado_shopee é opcional e preenchido manualmente;
    # após primeira execução ele é preservado, então não validamos
    # que está vazio.
    for k, v in validacoes.items():
        logger.add(f"validacao:{k}", "OK" if v else "FALHA")

    # Metadados obrigatórios no log
    logger.add("regra_categoria", "somente global_category1 e global_category2")
    logger.add("regra_description", "usada somente para porte_estimado")
    logger.add("regra_title", "usado somente para title_clean/exibição")
    logger.add("regra_subagentes", "nenhum subagente foi criado")
    logger.add("regra_site_json", "site alimentado por produtos_site_por_categoria.json")
    logger.add("regra_site_html", "produtos não fixados manualmente no HTML")
    logger.add("regra_site_metadados", "site não exibe metadados técnicos visíveis")
    logger.add("regra_site_score", "site não exibe score_potencial_comercial")
    logger.add("regra_site_linguagem", "site não usa linguagem de venda comprovada")
    logger.add("regra_finais_preco", "price/sale_price/discount_percentage preservados do CSV")
    logger.add("regra_links", "links originais preservados, sem encurtamento, sem afiliado")
    logger.add("regra_link_principal", "product_link é o único link oficial")

    logger.add("fim", datetime.now().isoformat())
    logger.save()

    # resumo no stdout
    print("\n=== RESUMO ===")
    print(f"CSV usado: {csv_path.name}")
    print(f"Produtos finais: {len(df_filtrado)}")
    print(f"Por categoria: {qtd_por_cat}")
    print(f"Arquivos finais em: {DATA_FINAL}")
    print(f"Arquivos copiados para site: {SITE_DATA_DIR}")
    print(f"Log: {log_path}")
    return 0


def _falhar(logger: Logger, msg: str, chamar_denise: bool = True) -> int:
    print(msg)
    if chamar_denise:
        print("Chamando Denise para decidir próximo passo.")
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        tb = traceback.format_exc()
        print("ERRO INESPERADO:", e)
        print(tb)
        sys.exit(1)
