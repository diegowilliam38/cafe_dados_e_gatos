# Como atualizar os produtos

Este projeto foi feito para que Denise consiga atualizar tudo com
**uma única execução de script**, sem precisar reconstruir o site.

---

## ✦ O fluxo completo (visão geral)

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Coloque o CSV novo em ~/Documents/shopee/raw/            │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Rode o script principal:                                 │
│    cd ~/Documents/shopee/claude_code                        │
│    python3 scripts/gerar_curadoria_shopee.py                │
│    → gera ~40 produtos com link_gerado_shopee = "" (vazio)  │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Abra site/data/links_shopee_manual.csv                   │
│    A coluna product_url tem o link original de cada item.   │
│    Vá na Shopee, gere seu link de afiliada e cole em        │
│    link_gerado_shopee.                                      │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. Rode o script auxiliar:                                  │
│    python3 scripts/aplicar_links_manual.py                  │
│    → aplica os links em site/data/achadinhos.json e .csv    │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. Atualize o navegador em http://localhost:8055            │
│    O botão "Ver achadinho ✿" agora usa seu link de afiliada │
└─────────────────────────────────────────────────────────────┘
```

---

## Passo a passo

1. **Substitua** o CSV em `~/Documents/shopee/raw/` pelo novo.
   - Apenas 1 arquivo CSV por vez na pasta.
   - A pasta `raw/` é somente leitura: nada é apagado, renomeado ou
     movido pelo script.

2. **Rode** o script principal:

   ```bash
   cd ~/Documents/shopee/claude_code
   python3 scripts/gerar_curadoria_shopee.py
   ```

3. **Confira**:
   - O log recém-criado em `logs/execucao_AAAAMMDD_HHMMSS.log`.
   - Os arquivos internos em `data/final/`.
   - Os arquivos públicos em `site/data/achadinhos.json` e
     `site/data/achadinhos.csv`.

4. **Abra o site** localmente:

   ```bash
   cd ~/Documents/shopee/claude_code/site
   python3 -m http.server 8055
   # abra http://localhost:8055 no navegador
   ```

5. (Opcional) **Atualize links de afiliada**: preencha manualmente a
   coluna `link_gerado_shopee` em `site/data/links_shopee_manual.csv`
   com o link gerado pela Shopee para cada produto. Depois rode:

   ```bash
   python3 scripts/aplicar_links_manual.py
   ```

   Esse script rápido aplica os links em `site/data/achadinhos.json`
   sem precisar rodar toda a curadoria de novo.

---

## Sobre os links de afiliada

- O script principal `gerar_curadoria_shopee.py` **preserva** os
  `link_gerado_shopee` antigos por `itemid`. Produtos que já estavam
  na curadoria passada mantêm o link; produtos novos entram em branco
  para você preencher.
- O botão do site usa o `link_gerado_shopee` quando ele existe; caso
  contrário, usa o `product_link` original.
- Quando você só quer atualizar os links (sem mexer no CSV bruto),
  rode `aplicar_links_manual.py` — é mais rápido e não roda a
  curadoria inteira.

---

## O que o script faz sozinho

- Detecta o CSV em `raw/`.
- Conta linhas e produtos únicos.
- Filtra por preço, nota, presença de `product_link`.
- Classifica a categoria final por `global_category1`/`global_category2`.
- Estima porte via `description` (sem usar title).
- Calcula `score_potencial_comercial` (interno, não aparece no site).
- Aplica limite de 4 por categoria.
- Salva CSVs/JSONs internos.
- Copia os arquivos públicos para `site/data/`.
- Roda validações e grava log completo.

## O que o script NÃO faz

- Não move, apaga ou renomeia o CSV de `raw/`.
- Não cria links de afiliado.
- Não inventa preços, descontos ou marcas.
- Não usa `product_short link` como link principal.
- Não completa categorias vazias artificialmente.

## Em caso de erro

Se qualquer etapa falhar, o script registra o erro no log, tenta uma
correção e, se persistir, encerra com mensagem clara pedindo ação da
Denise. O log contém:

- etapa que falhou
- erro original
- tentativa de correção
- decisão necessária

## Scripts disponíveis

| Script                              | Quando usar |
|-------------------------------------|-------------|
| `scripts/gerar_curadoria_shopee.py` | Atualizar produtos a partir de um novo CSV em `raw/`. Preserva links antigos. |
| `scripts/aplicar_links_manual.py`   | Aplicar links de afiliada recém-colados em `site/data/links_shopee_manual.csv` sem rodar a curadoria inteira. |
