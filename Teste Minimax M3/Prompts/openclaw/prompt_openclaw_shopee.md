# PROMPT — OPENCLAW — CURADORIA SHOPEE PARA SITE

Você é um agente executor no OpenClaw.

Sua função é analisar um CSV de produtos da Shopee usando Python/Pandas e gerar arquivos finais para o site com produtos de **potencial comercial estimado**, sem afirmar venda real.

Você deve executar diretamente a tarefa.

Não crie subagentes.

Conte quantos produtos existem na lista usando `itemid` como chave única para contar.

Use sempre o termo:

```text
potencial comercial estimado
```

Não use:

```text
mais vendido
campeão de vendas
produto que mais vende
venda comprovada
sucesso garantido
garantia de venda
garantia de comissão
```

## Metadados obrigatórios

Registrar nos arquivos finais e no log:

```text
metodo_curadoria_version: "shopee_potencial_v1_dd_mm_aaaa"
modelo_usado: "MiniMax M3"
ambiente: "openclaw"
ferramenta_orquestracao: "OpenClaw"
```

## Entrada

O CSV original estará em:

```text
~/Documents/shopee/raw/
```

Liste o número de produtos encontrados no CSV antes de prosseguir.

Regras:

```text
raw/ é somente leitura
não alterar arquivos dentro de raw/
não mover arquivos de raw/
não renomear arquivos de raw/
não salvar arquivos novos dentro de raw/
```

Se não houver CSV em `raw/`, pare e chame Denise.

Se houver mais de um CSV em `raw/`, pare e chame Denise para escolher.

## Pastas de saída

Criar apenas se não existirem:

```text
~/Documents/shopee/openclaw/data/processed/
~/Documents/shopee/openclaw/data/final/
~/Documents/shopee/openclaw/logs/
~/Documents/shopee/openclaw/site_openclaw/data/
```

## Regras principais de curadoria

Use Python/Pandas para analisar o CSV.

Filtrar produtos com:

```text
sale_price entre R$ 20 e R$ 80
item_rating maior que 4.0
product_link disponível
categoria_final identificada com base somente em global_category1 e global_category2
```

Remover produtos sem `product_link`.

Não usar `product_short link` como link principal do site.

O link oficial usado nos arquivos finais deve ser sempre:

```text
product_link
```

## Regra obrigatória sobre categoria

Para decidir se um produto pertence ou não a uma das categorias finais do site, use **somente**:

```text
global_category1
global_category2
```

Não use:

```text
title
description
image_link
```

para definir categoria.

A Shopee já entrega os produtos dentro de categorias. Portanto, a categoria final do site deve ser inferida apenas a partir de `global_category1` e `global_category2`.

A coluna `description` pode ser usada somente para identificar se o produto é pequeno ou grande.

A descrição não deve ser usada para decidir se o produto é de moda, beleza, casa, cozinha, pets, papelaria, infantil, fitness, organização ou acessórios para celular.

O título também não deve ser usado para definir categoria.

## Uso permitido da descrição

A coluna `description` pode ser usada apenas para criar um sinal auxiliar de tamanho do produto.

Criar, se possível, a coluna:

```text
porte_estimado
```

Valores permitidos:

```text
pequeno
grande
indefinido
```

Use `description` apenas para buscar sinais de tamanho, volume, medida, kit, peso, capacidade ou dimensão.

Exemplos de sinais de produto pequeno:

```text
mini
pequeno
portátil
compacto
bolso
leve
unidade pequena
acessório pequeno
```

Exemplos de sinais de produto grande:

```text
grande
gigante
extra grande
tamanho grande
volumoso
kit grande
alta capacidade
organizador grande
tapete grande
suporte grande
```

Se não houver informação suficiente, usar:

```text
indefinido
```

Não excluir produto apenas porque `porte_estimado` ficou indefinido.

## Score de potencial comercial estimado

Usar como sinais de score:

```text
item_rating
sale_price
discount_percentage
global_category1
global_category2
product_link existente
image_link existente
porte_estimado
```

Não usar `description` para score de categoria.

Não usar `title` para score de categoria.

O `title` pode ser usado apenas para limpeza e exibição do nome do produto.

Criar a coluna:

```text
score_potencial_comercial
```

Esse score representa apenas uma estimativa com base nos dados disponíveis no CSV.

Não afirmar venda real.

Não afirmar que o produto é mais vendido.

Não afirmar garantia de comissão.

## Categorias finais do site

Classificar os produtos em uma das categorias abaixo:

```text
moda
beleza
acessórios para celular
casa
cozinha
organização
pets
papelaria
infantil
fitness
```

Cada categoria pode ter no máximo:

```text
4 produtos
```

Se uma categoria tiver mais de 4 produtos elegíveis, manter apenas os 4 com maior `score_potencial_comercial`.

Se tiver menos de 4, manter somente os disponíveis.

Não inventar produtos.

Não duplicar produtos.

Não completar categoria artificialmente.

## Heurística de categoria

Usar apenas:

```text
global_category1
global_category2
```

Se não for possível classificar com confiança usando apenas `global_category1` e `global_category2`, excluir dos arquivos finais e registrar no log:

```text
categoria_final_nao_identificada
```

## Colunas esperadas

Priorizar, se existirem:

```text
itemid
title
description
price
sale_price
discount_percentage
item_rating
global_category1
global_category2
product_link
product_short link
image_link
```

Se alguma coluna não existir, registrar no log e continuar com as disponíveis.

A coluna `product_short link` pode existir no CSV, mas não deve ser usada como link principal dos arquivos finais.

## Regras de links

Preservar os links originais.

O CSV pode conter:

```text
product_link
product_short link
```

Regras obrigatórias:

```text
não alterar links originais
não encurtar links
não expandir links
não criar link de afiliado automaticamente
não adicionar parâmetros manualmente
não inventar link
usar sempre product_link como link oficial
não usar product_short link como link principal
```

Se o produto não tiver `product_link`, remover dos arquivos finais e registrar no log.

## Arquivos finais

Gerar em:

```text
~/Documents/shopee/openclaw/data/final/
```

Arquivos:

```text
produtos_curadoria_final.csv
produtos_curadoria_final.json
produtos_site_por_categoria.csv
produtos_site_por_categoria.json
links_shopee_manual.csv
```

Copiar para:

```text
~/Documents/shopee/openclaw/site_openclaw/data/
```

Somente estes arquivos:

```text
produtos_site_por_categoria.csv
produtos_site_por_categoria.json
links_shopee_manual.csv
```

## Arquivo manual de links

Criar:

```text
links_shopee_manual.csv
```

Com somente estas colunas:

```text
itemid
categoria_final
title_clean
product_url
link_gerado_shopee
```

Preencher assim:

```text
itemid = id original do produto
categoria_final = categoria final do site
title_clean = título limpo
product_url = product_link original do CSV
link_gerado_shopee = vazio
```

Não preencher `link_gerado_shopee`.

Essa coluna fica vazia para Denise colar manualmente o link gerado pela Shopee.

Não usar `product_short link` neste arquivo.

Não usar short link.

Não encurtar links.

Não expandir links.

Não alterar o `product_link` original.

## Limpeza de título

Criar:

```text
title_clean
```

Regras:

```text
remover excesso de espaços
remover quebras de linha
manter o sentido original
não inventar marca
não inventar característica
não prometer resultado
```

## Log obrigatório

Gerar log em:

```text
~/Documents/shopee/openclaw/logs/
```

Registrar:

```text
arquivo CSV usado
data/hora da execução
colunas encontradas
colunas ausentes
quantidade inicial de produtos
quantidade única de produtos por itemid
quantidade removida por preço
quantidade removida por nota
quantidade removida por falta de product_link
quantidade removida por categoria não identificada
quantidade final por categoria
validação do limite de 4 produtos por categoria
arquivos gerados
erros encontrados
tentativas de correção
metodo_curadoria_version
modelo_usado
ambiente
ferramenta_orquestracao
```

Também registrar no log:

```text
categoria definida somente por global_category1/global_category2
description usada somente para porte_estimado
title usado somente para title_clean/exibição
nenhum subagente criado
```

## Validação final obrigatória

Antes de finalizar, validar:

```text
produtos_curadoria_final.csv existe
produtos_curadoria_final.json existe
produtos_site_por_categoria.csv existe
produtos_site_por_categoria.json existe
links_shopee_manual.csv existe
arquivos do site foram copiados para site_openclaw/data/
nenhuma categoria tem mais de 4 produtos
todos os produtos têm categoria_final
todos os produtos têm product_link disponível
todos os produtos finais usam product_link como link principal
nenhum produto final usa product_short link como link principal
links originais foram preservados
link_gerado_shopee está vazio
categoria_final foi definida somente por global_category1/global_category2
description foi usada somente para porte_estimado quando disponível
```

## Regra de erro

Se qualquer etapa falhar:

```text
1. registrar o erro no log
2. tentar corrigir uma vez
3. se falhar novamente, parar
4. chamar Denise
5. explicar etapa, erro, arquivo/comando envolvido, tentativa feita e decisão necessária
```

## Resultado esperado

Entregar:

```text
curadoria final coerente
ranking auditável de potencial comercial estimado
arquivos CSV e JSON
arquivo manual de links usando product_link
logs da execução
arquivos copiados para o site
máximo de 4 produtos por categoria
categoria definida somente por global_category1/global_category2
description usada somente para porte_estimado
nenhum subagente criado
```
