# Achadinhos da Shopee

> Vitrine delicada de achadinhos selecionados, alimentada por um JSON e atualizada por um único script Python/Pandas.

Este projeto foi pensado para que, no futuro, **Denise** só precise colocar um novo CSV bruto em `~/Documents/shopee/raw/` e rodar **um comando** para atualizar tudo: dados, site e o arquivo manual de links.

---

## ✦ Objetivo

- Ler o CSV bruto da Shopee em `~/Documents/shopee/raw/`
- Analisar com Python/Pandas
- Gerar arquivos internos de curadoria (auditáveis)
- Gerar CSVs/JSON finais que alimentam o site
- Manter um site estático delicado, elegante e atrativo

---

## ✦ Entrada esperada

Um único arquivo CSV em `~/Documents/shopee/raw/`, com pelo menos as colunas:

- `itemid` (chave única)
- `title`
- `description`
- `price`
- `sale_price`
- `discount_percentage`
- `item_rating`
- `global_category1`
- `global_category2`
- `product_link`
- `product_short link`
- `image_link`

A pasta `raw/` é **somente leitura**. Nada ali é movido, renomeado, sobrescrito ou gerado.

---

## ✦ Estrutura de pastas

```
~/Documents/shopee/
├── raw/                                  ← entrada (somente leitura)
└── claude_code/
    ├── data/
    │   ├── processed/                    ← arquivos intermediários
    │   └── final/                        ← CSVs/JSONs finais internos
    ├── logs/                             ← logs de cada execução
    ├── scripts/
    │   └── gerar_curadoria_shopee.py     ← SCRIPT PRINCIPAL
    ├── site/
    │   ├── index.html
    │   ├── css/style.css
    │   ├── js/app.js
    │   ├── assets/
    │   └── data/
    │       ├── achadinhos.json           ← JSON público que o site lê
    │       ├── achadinhos.csv
    │       └── links_shopee_manual.csv
    └── docs/
        ├── REGRAS_CURADORIA_PRODUTOS.md
        ├── COMO_ATUALIZAR_PRODUTOS.md
        └── REGRAS_LINGUAGEM_SITE.md
```

---

## ✦ Como a curadoria funciona (camada interna)

Use Python/Pandas para:

1. Localizar o CSV em `raw/` (1 único arquivo).
2. Contar linhas totais e produtos únicos por `itemid`.
3. Remover produtos sem `product_link`.
4. Filtrar `sale_price` entre R$ 20 e R$ 80.
5. Filtrar `item_rating` > 4.0.
6. Classificar `categoria_final` usando **somente** `global_category1` e `global_category2`.
7. Estimar `porte_estimado` (pequeno / grande / indefinido) usando **somente** `description`.
8. Calcular `score_potencial_comercial` (uso interno).
9. Manter no máximo **4 produtos por categoria**.
10. Preservar `price`, `sale_price` e `discount_percentage` quando existirem no CSV.
11. Gerar arquivos internos em `data/final/`.
12. Copiar arquivos públicos para `site/data/`.
13. Validar regras e registrar tudo no log.

Detalhes completos em `docs/REGRAS_CURADORIA_PRODUTOS.md`.

---

## ✦ Como o site é alimentado

O site é **estático** e os produtos **não ficam fixos no HTML**. O JS em `site/js/app.js` faz `fetch('data/achadinhos.json')` e renderiza os cards dinamicamente, agrupados por categoria, com pílulas de filtro, avaliação em estrelas, preço atual / preço original / desconto e botão de "Ver achadinho" apontando sempre para `product_link`.

A linguagem do site é editorial e leve, sem metadados técnicos visíveis (sem score, sem ranking, sem "mais vendido", sem "garantia de venda"). Veja `docs/REGRAS_LINGUAGEM_SITE.md`.

---

## ✦ Como atualizar no futuro

1. Substitua o CSV em `~/Documents/shopee/raw/`.
2. Rode:

   ```bash
   cd ~/Documents/shopee/claude_code
   python3 scripts/gerar_curadoria_shopee.py
   ```

3. Confira o log em `logs/` e os arquivos em `data/final/` e `site/data/`.
4. Para abrir o site localmente:

   ```bash
   cd ~/Documents/shopee/claude_code/site
   python3 -m http.server 8000
   # abra http://localhost:8000
   ```

Detalhes em `docs/COMO_ATUALIZAR_PRODUTOS.md`.

---

## ✦ Limitações conhecidas

- Apenas 4 produtos por categoria (limite editorial).
- Categorias são definidas por `global_category1`/`global_category2`. Produtos sem mapeamento claro são descartados e registrados no log.
- O "porte estimado" é apenas um sinal auxiliar lido da descrição; pode ficar `indefinido` em vários produtos.
- `price`, `sale_price` e `discount_percentage` são preservados como estão no CSV — **nunca** inventados.
- Links não são encurtados, expandidos nem convertidos em links de afiliado automaticamente. Denise cola o link gerado pela Shopee manualmente em `links_shopee_manual.csv`.

---

## ✦ Comandos rápidos

```bash
# 1) atualizar curadoria e site
cd ~/Documents/shopee/claude_code
python3 scripts/gerar_curadoria_shopee.py

# 2) abrir o site
cd site && python3 -m http.server 8000
```
