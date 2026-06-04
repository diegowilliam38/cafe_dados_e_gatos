# Regras internas de curadoria

Este documento registra todas as regras usadas na camada interna do
projeto. As regras aqui podem usar termos técnicos (score, potencial,
modelo, ambiente). Esses termos **não** devem aparecer no site público.

---

## 1) Entrada

- Um único CSV em `~/Documents/shopee/raw/`.
- `raw/` é **somente leitura**: nada é movido, renomeado, sobrescrito.
- Se houver 0 ou mais de 1 CSV: parar e chamar Denise.

## 2) Chaves e contagens

- `itemid` é a chave única.
- Contar `total_linhas` e `produtos_unicos_itemid` antes de qualquer filtro.
- Remover duplicatas por `itemid` (mantendo a primeira ocorrência).

## 3) Filtros obrigatórios

Manter apenas produtos que atendam **todos**:

- `product_link` presente e não vazio.
- `sale_price` entre R$ 20,00 e R$ 80,00 (inclusive).
- `item_rating` > 4.0.

Fallback de preço:

- Se `sale_price` não existir no CSV, usar `price` e registrar no log.
- Não inventar preço.

## 4) Categoria final

Categorias finais do site (lista oficial, ordem preferencial de desempate):

1. moda
2. beleza
3. acessórios para celular
4. casa
5. cozinha
6. organização
7. pets
8. papelaria
9. infantil
10. fitness

Regras:

- Categoria definida **somente** por `global_category1` e `global_category2`.
- `global_category2` (mais específico) tem **prioridade** sobre `global_category1`.
- `title` e `image_link` **nunca** definem categoria.
- `description` **nunca** define categoria.
- Se não houver categoria_final identificável, descartar e registrar
  no log como `categoria_final_nao_identificada`.

## 5) Porte estimado (description)

Criar a coluna `porte_estimado` com valores: `pequeno`, `grande`, `indefinido`.

- Usar **somente** `description`.
- Não usar `title` para porte.
- Não usar categoria para porte.
- Produtos com `porte_estimado = indefinido` **não** são removidos.

## 6) Score interno

Criar a coluna `score_potencial_comercial` (uso INTERNO apenas).

Sinais utilizados (todos internos):

- `item_rating` (peso alto)
- `sale_price` no "sweet spot" 20-80
- `discount_percentage`
- presença de `image_link`
- presença de `product_link`
- `porte_estimado`

Sinais **não** utilizados:

- `description` para score de categoria
- `title` para score de categoria

Restrições:

- Não exibir no site.
- Não afirmar venda real.
- Não afirmar "mais vendido".
- Não afirmar garantia de comissão.

## 7) Limite editorial

- No máximo **4 produtos por categoria**.
- Se houver mais de 4 elegíveis em uma categoria, manter os 4 de maior
  `score_potencial_comercial`.
- Não inventar, duplicar ou completar categoria artificialmente.

## 8) Preços nos arquivos finais

- `price` → preço original, se existir no CSV.
- `sale_price` → preço atual / com desconto, se existir no CSV.
- `discount_percentage` → desconto informado, se existir no CSV.
- **Não** inventar nenhum desses campos.
- **Não** calcular desconto manualmente se `discount_percentage` já existir.
- Se o desconto for estimado por cálculo a partir de `price` e `sale_price`,
  registrar no log que o desconto foi estimado.

## 9) Links

- `product_link` é o único link oficial.
- **Não** usar `product_short link` como link principal.
- **Não** encurtar, **não** expandir, **não** alterar links.
- **Não** criar link de afiliado automaticamente.
- Sem `product_link` → remover dos arquivos finais e registrar no log.

## 10) Limpeza de título

- Criar `title_clean`: remoção de quebras de linha e excesso de espaços.
- Não inventar marca.
- Não inventar característica.
- Não prometer resultado.

## 11) Arquivos finais (camada interna)

Gerados em `data/final/`:

- `produtos_curadoria_final.csv`
- `produtos_curadoria_final.json`
- `produtos_site_por_categoria.csv`
- `produtos_site_por_categoria.json`
- `links_shopee_manual.csv` (com colunas `itemid`, `categoria_final`,
  `title_clean`, `product_url`, `link_gerado_shopee` — esta última sempre
  vazia para Denise preencher manualmente).

## 12) Arquivos copiados para o site (camada pública)

Em `site/data/`:

- `achadinhos.json` (ex `produtos_site_por_categoria.json`)
- `achadinhos.csv`
- `links_shopee_manual.csv`

> A nomenclatura pública foi trocada de `produtos_site_por_categoria.*`
> para `achadinhos.*` para reforçar a linguagem editorial do site.

## 13) Metadados obrigatórios

Sempre registrados no log:

- `metodo_curadoria_version`
- `modelo_usado`
- `ambiente`
- `ferramenta_orquestracao`

Esses campos são internos e não devem aparecer no site público.

## 14) Separação obrigatória interna × site

Termos permitidos **apenas** na camada interna (script, logs, CSVs
internos, JSONs internos, documentação técnica):

- `potencial comercial estimado`
- `score_potencial_comercial`
- `score`
- `ranking técnico`
- `metodo_curadoria_version`
- `modelo_usado`
- `ambiente`
- `ferramenta_orquestracao`

No site público, usar linguagem editorial: "Achadinhos Shopee",
"Dica de Presente", "Selecionados da Semana", "Garimpos para conferir",
"Ideias úteis para o dia a dia", etc. Veja `docs/REGRAS_LINGUAGEM_SITE.md`.
