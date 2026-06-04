"""
Shopee - Aplicar Links Manuais de Afiliada
===========================================

Script auxiliar para Denise. Quando ela atualiza a coluna
`link_gerado_shopee` em `site/data/links_shopee_manual.csv`, este script
aplica esses links em `site/data/achadinhos.json` e
`site/data/achadinhos.csv` SEM precisar rodar o pipeline completo de
curadoria.

Uso:
    python3 scripts/aplicar_links_manual.py

Pré-requisito:
    Ter rodado pelo menos uma vez `gerar_curadoria_shopee.py` e existir
    `site/data/links_shopee_manual.csv` com a coluna `link_gerado_shopee`.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

HOME = Path.home()
BASE_DIR = HOME / "Documents" / "shopee" / "claude_code"
DATA_FINAL = BASE_DIR / "data" / "final"
SITE_DATA_DIR = BASE_DIR / "site" / "data"
LOGS_DIR = BASE_DIR / "logs"

LINKS_MANUAL = SITE_DATA_DIR / "links_shopee_manual.csv"
ACHADINHOS_JSON = SITE_DATA_DIR / "achadinhos.json"
ACHADINHOS_CSV = SITE_DATA_DIR / "achadinhos.csv"


def main() -> int:
    inicio = datetime.now()
    log_path = LOGS_DIR / f"aplicar_links_{inicio.strftime('%Y%m%d_%H%M%S')}.log"
    linhas_log: list[str] = []

    def log(msg: str) -> None:
        print(msg)
        linhas_log.append(msg)

    log(f"== aplicar_links_manual.py · {inicio.isoformat()} ==")

    # 1) Ler links manuais
    if not LINKS_MANUAL.exists():
        log(f"ERRO: {LINKS_MANUAL} não encontrado.")
        log("Rode primeiro: python3 scripts/gerar_curadoria_shopee.py")
        return 1

    try:
        df_links = pd.read_csv(LINKS_MANUAL)
    except Exception as e:
        log(f"ERRO ao ler {LINKS_MANUAL}: {e}")
        return 1

    if "itemid" not in df_links.columns or "link_gerado_shopee" not in df_links.columns:
        log("ERRO: CSV manual sem colunas itemid/link_gerado_shopee.")
        return 1

    # limpar valores inválidos -> string vazia
    df_links["link_gerado_shopee"] = (
        df_links["link_gerado_shopee"].fillna("").astype(str).str.strip()
    )

    # 2) Carregar JSON do site
    if not ACHADINHOS_JSON.exists():
        log(f"ERRO: {ACHADINHOS_JSON} não encontrado.")
        return 1

    with ACHADINHOS_JSON.open(encoding="utf-8") as f:
        produtos = json.load(f)

    log(f"Produtos atuais no site: {len(produtos)}")

    # 3) Construir lookup itemid -> link_gerado_shopee
    lookup = dict(zip(df_links["itemid"].astype(str),
                      df_links["link_gerado_shopee"].astype(str)))

    # 4) Aplicar nos produtos
    aplicados = 0
    sem_link = 0
    for p in produtos:
        iid = str(p.get("itemid", ""))
        link = lookup.get(iid, "")
        p["link_gerado_shopee"] = link
        if link:
            aplicados += 1
        else:
            sem_link += 1

    # 5) Salvar JSON e CSV atualizados
    with ACHADINHOS_JSON.open("w", encoding="utf-8") as f:
        json.dump(produtos, f, ensure_ascii=False, indent=2)

    # CSV espelho para conferência
    pd.DataFrame(produtos).to_csv(ACHADINHOS_CSV, index=False)

    log(f"Links aplicados: {aplicados}")
    log(f"Produtos sem link_gerado_shopee: {sem_link}")
    log(f"JSON atualizado: {ACHADINHOS_JSON}")
    log(f"CSV atualizado:  {ACHADINHOS_CSV}")

    fim = datetime.now()
    log(f"Fim: {fim.isoformat()}")

    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(linhas_log))

    return 0


if __name__ == "__main__":
    sys.exit(main())
