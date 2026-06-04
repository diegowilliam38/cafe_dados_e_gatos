# PROMPT 2 — ATUALIZAR JSON E CSVS COM NOVO CSV DA SHOPEE

Você é um agente de desenvolvimento sênior e analista de dados.

Sua função é atualizar os arquivos de dados de um projeto existente de achadinhos da Shopee usando Python/Pandas.

A estrutura do site já existe.

Você deve apenas analisar o novo CSV da Shopee, aplicar as regras de curadoria, gerar os arquivos CSV/JSON atualizados e copiar o JSON final para alimentar o site automaticamente.

Você deve executar diretamente a tarefa.

Não crie subagentes.

## OBJETIVO

Atualizar os dados do site a partir de um novo CSV bruto.

O site deve continuar sendo alimentado por:

"~/Documents/shopee/claude_code/site/data/produtos_site_por_categoria.json"

Nesta atualização:

Não recrie o projeto do zero.

Não refaça o site.

Não altere index.html.

Não altere CSS.

Não altere JavaScript.

Não altere textos públicos do site.

Não altere layout.

Não escreva conteúdo novo para o site.

Não adicione produtos manualmente no HTML.

Não mexa na linguagem pública do site.

Atualize apenas:

- arquivos processados
- arquivos finais CSV
- arquivos finais JSON
- links_shopee_manual.csv
- log da execução
- cópias necessárias em site/data/

## SEPARAÇÃO OBRIGATÓRIA ENTRE CAMADA INTERNA E SITE

A análise interna pode usar termos técnicos como:

- potencial comercial estimado
- score_potencial_comercial
- metodo_curadoria_version
- modelo_usado
- ambiente
- ferramenta_orquestracao

Esses termos podem aparecer em:

- CSVs internos
- JSONs internos
- logs
- documentação técnica
- script Python

Mas não devem ser inseridos em textos públicos do site.

Como este prompt é apenas de atualização de dados, não altere textos do site.

## METADADOS OBRIGATÓRIOS INTERNOS

Registrar nos arquivos finais internos e no log:

- metodo_curadoria_version: "shopee_potencial_v1_dd_mm_aaaa"
- modelo_usado: "Claude Code"
- ambiente: "claude_code"
- ferramenta_orquestracao: "Claude Code"

## ENTRADA

O novo CSV original estará em:

"~/Documents/shopee/raw/"

Antes de prosseguir:

1. Verifique se existe CSV em raw/.
2. Se não houver CSV em raw/, pare e chame Denise.
3. Se houver mais de um CSV em raw/, pare e chame Denise para escolher.
4. Conte quantos produtos existem na lista usando itemid como chave única.
5. Liste o número total de linhas e o número de produtos únicos antes de continuar.

## REGRAS DA PASTA RAW

raw/ é somente leitura.

Não alterar arquivos dentro de raw/.

Não mover arquivos de raw/.

Não renomear arquivos de raw/.

Não salvar arquivos novos dentro de raw/.

## ESTRUTURA EXISTENTE

Usar a estrutura:

- "~/Documents/shopee/claude_code/data/processed/"
- "~/Documents/shopee/claude_code/data/final/"
- "~/Documents/shopee/claude_code/logs/"
- "~/Documents/shopee/claude_code/site/data/"
- "~/Documents/shopee/claude_code/scripts/"

Se alguma pasta de dados necessária não existir, crie apenas a pasta ausente e registre no log.

Não alterar:

- "~/Documents/shopee/claude_code/site/index.html"
- "~/Documents/shopee/claude_code/site/css/"
- "~/Documents/shopee/claude_code/site/js/"
- "~/Documents/shopee/claude_code/site/assets/"

a menos que seja indispensável para corrigir uma falha real de carregamento do JSON. Se isso acontecer, explique antes no resumo final.

## SCRIPT PRINCIPAL

Usar preferencialmente o script existente:

"~/Documents/shopee/claude_code/scripts/gerar_curadoria_shopee.py"

Se o script existir, use-o para gerar os dados.

Se o script estiver incompatível com as regras obrigatórias, corrija o mínimo necessário e registre no log.

Se o script não existir, crie o script seguindo as regras deste prompt e registre no log que o script precisou ser recriado.

## REGRAS PRINCIPAIS DE CURADORIA INTERNA

Use Python/Pandas para analisar o CSV.

Filtrar produtos com:

- sale_price entre R$ 20 e R$ 80
- item_rating maior que 4.0
- product_link disponível
- categoria_final identificada com base somente em global_category1 e global_category2

Remover produtos sem product_link.

Não usar product_short link como link principal do site.

O link oficial usado nos arquivos finais deve ser sempre:

product_link

## PREÇOS

Usar as colunas:

- price como preço original, se existir.
- sale_price como preço atual ou preço com desconto, se existir.
- discount_percentage como percentual de desconto, se existir.

Regras:

- O filtro de preço deve usar sale_price.
- Se sale_price não existir, usar price como fallback e registrar isso no log.
- O JSON do site deve manter sale_price como preço principal, quando existir.
- O JSON do site deve manter price como preço original, quando existir.
- O JSON do site deve manter discount_percentage, quando existir.
- Não inventar preço original.
- Não inventar preço com desconto.
- Não inventar percentual de desconto.
- Não calcular desconto manualmente se discount_percentage já existir.
- Se calcular desconto por ausência de discount_percentage, registrar no log que o desconto foi estimado a partir de price e sale_price.

## REGRA OBRIGATÓRIA SOBRE CATEGORIA

Para decidir se um produto pertence ou não a uma das categorias finais do site, use somente:

- global_category1
- global_category2

Não use:

- title
- description
- image_link

para definir categoria.

A coluna description pode ser usada somente para identificar se o produto é pequeno ou grande.

A descrição não deve ser usada para decidir se o produto é de moda, beleza, casa, cozinha, pets, papelaria, infantil, fitness, organização ou acessórios para celular.

O título também não deve ser usado para definir categoria.

## USO PERMITIDO DA DESCRIÇÃO

A coluna description pode ser usada apenas para criar um sinal auxiliar de tamanho do produto.

Criar, se possível, a coluna:

porte_estimado

Valores permitidos:

- pequeno
- grande
- indefinido

Use description apenas para buscar sinais de tamanho, volume, medida, kit, peso, capacidade ou dimensão.

Se não houver informação suficiente, usar:

indefinido

Não excluir produto apenas porque porte_estimado ficou indefinido.

## SCORE INTERNO

Criar a coluna interna:

score_potencial_comercial

Esse score representa apenas uma estimativa interna com base nos dados disponíveis no CSV.

Não afirmar venda real.

Não afirmar que o produto é mais vendido.

Não afirmar garantia de comissão.

Usar como sinais de score:

- item_rating
- sale_price
- discount_percentage
- global_category1
- global_category2
- product_link existente
- image_link existente
- porte_estimado

Não usar description para score de categoria.

Não usar title para score de categoria.

O title pode ser usado apenas para limpeza e exibição do nome do produto.

## CATEGORIAS FINAIS DO SITE

Classificar os produtos em uma das categorias abaixo:

- moda
- beleza
- acessórios para celular
- casa
- cozinha
- organização
- pets
- papelaria
- infantil
- fitness

Cada categoria pode ter no máximo:

4 produtos

Se uma categoria tiver mais de 4 produtos elegíveis, manter apenas os 4 com maior score_potencial_comercial.

Se tiver menos de 4, manter somente os disponíveis.

Não inventar produtos.

Não duplicar produtos.

Não completar categoria artificialmente.

## HEURÍSTICA DE CATEGORIA

Usar apenas:

- global_category1
- global_category2

Se não for possível classificar com confiança usando apenas global_category1 e global_category2, excluir dos arquivos finais e registrar no log:

categoria_final_nao_identificada

## COLUNAS ESPERADAS

Priorizar, se existirem:

- itemid
- title
- description
- price
- sale_price
- discount_percentage
- item_rating
- global_category1
- global_category2
- product_link
- product_short link
- image_link

Se alguma coluna não existir, registrar no log e continuar com as disponíveis, desde que seja possível executar a curadoria mínima.

## COLUNAS OBRIGATÓRIAS NOS DADOS FINAIS

Os arquivos finais:

- produtos_curadoria_final.csv
- produtos_curadoria_final.json
- produtos_site_por_categoria.csv
- produtos_site_por_categoria.json

devem manter, quando existirem no CSV original, as colunas:

- itemid
- categoria_final
- title_clean
- price
- sale_price
- discount_percentage
- item_rating
- image_link
- product_link
- porte_estimado
- score_potencial_comercial

Regras:

- price deve representar o preço original, se existir no CSV.
- sale_price deve representar o preço atual ou preço com desconto, se existir no CSV.
- discount_percentage deve representar o desconto informado no CSV, se existir.
- Não remover price dos arquivos finais quando ele existir no CSV.
- Não remover sale_price dos arquivos finais quando ele existir no CSV.
- Não remover discount_percentage dos arquivos finais quando ele existir no CSV.
- Não inventar preço original.
- Não inventar preço com desconto.
- Não inventar percentual de desconto.

## REGRAS DE LINKS

Preservar os links originais.

Regras obrigatórias:

- não alterar links originais
- não encurtar links
- não expandir links
- não criar link de afiliado automaticamente
- não adicionar parâmetros manualmente
- não inventar link
- usar sempre product_link como link oficial
- não usar product_short link como link principal

Se o produto não tiver product_link, remover dos arquivos finais e registrar no log.

## ARQUIVOS A ATUALIZAR

Atualizar em:

"~/Documents/shopee/claude_code/data/final/"

Arquivos obrigatórios:

- produtos_curadoria_final.csv
- produtos_curadoria_final.json
- produtos_site_por_categoria.csv
- produtos_site_por_categoria.json
- links_shopee_manual.csv

Copiar para:

"~/Documents/shopee/claude_code/site/data/"

Somente estes arquivos:

- produtos_site_por_categoria.csv
- produtos_site_por_categoria.json
- links_shopee_manual.csv

## ARQUIVO MANUAL DE LINKS

Atualizar:

links_shopee_manual.csv

Com somente estas colunas:

- itemid
- categoria_final
- title_clean
- product_url
- link_gerado_shopee

Preencher assim:

- itemid = id original do produto
- categoria_final = categoria final do site
- title_clean = título limpo
- product_url = product_link original do CSV
- link_gerado_shopee = vazio

Não preencher link_gerado_shopee.

Essa coluna fica vazia para Denise colar manualmente o link gerado pela Shopee.

Não usar product_short link neste arquivo.

Não usar short link.

Não encurtar links.

Não expandir links.

Não alterar o product_link original.

## LIMPEZA DE TÍTULO

Criar:

title_clean

Regras:

- remover excesso de espaços
- remover quebras de linha
- manter o sentido original
- não inventar marca
- não inventar característica
- não prometer resultado

## JSON DO SITE

Atualizar:

produtos_site_por_categoria.json

Esse JSON alimenta automaticamente o site.

O JSON deve conter apenas os campos necessários para renderizar os produtos e manter rastreabilidade técnica quando necessário.

O site pode receber o JSON, mas não deve exibir metadados técnicos.

O JSON deve permitir exibir:

- categoria_final
- title_clean
- price
- sale_price
- discount_percentage
- item_rating
- image_link
- product_link
- porte_estimado

Pode conter score_potencial_comercial para ordenação interna, mas o site não deve mostrar esse campo ao usuário.

Não incluir textos públicos novos no JSON que usem:

- potencial comercial estimado
- score
- ranking
- venda comprovada
- mais vendido
- campeão de vendas
- sucesso garantido
- garantia de comissão

## LOG OBRIGATÓRIO

Gerar novo log em:

"~/Documents/shopee/claude_code/logs/"

Registrar:

- arquivo CSV usado
- data/hora da execução
- colunas encontradas
- colunas ausentes
- quantidade inicial de produtos
- quantidade única de produtos por itemid
- quantidade removida por preço
- quantidade removida por nota
- quantidade removida por falta de product_link
- quantidade removida por categoria não identificada
- quantidade final por categoria
- validação do limite de 4 produtos por categoria
- arquivos gerados
- arquivos atualizados
- arquivos preservados
- erros encontrados
- tentativas de correção
- metodo_curadoria_version
- modelo_usado
- ambiente
- ferramenta_orquestracao

Também registrar no log:

- categoria definida somente por global_category1/global_category2
- description usada somente para porte_estimado
- title usado somente para title_clean/exibição
- nenhum subagente criado
- site atualizado por JSON
- produtos não foram fixados manualmente no HTML
- site não foi recriado
- HTML/CSS/JS públicos foram preservados, salvo correção indispensável registrada
- arquivos finais mantêm price, quando existir no CSV original
- arquivos finais mantêm sale_price, quando existir no CSV original
- arquivos finais mantêm discount_percentage, quando existir no CSV original

## VALIDAÇÃO FINAL OBRIGATÓRIA

Antes de finalizar, validar:

- produtos_curadoria_final.csv existe
- produtos_curadoria_final.json existe
- produtos_site_por_categoria.csv existe
- produtos_site_por_categoria.json existe
- links_shopee_manual.csv existe
- arquivos do site foram copiados para site/data/
- nenhuma categoria tem mais de 4 produtos
- todos os produtos têm categoria_final
- todos os produtos têm product_link disponível
- todos os produtos finais usam product_link como link principal
- nenhum produto final usa product_short link como link principal
- links originais foram preservados
- link_gerado_shopee está vazio
- categoria_final foi definida somente por global_category1/global_category2
- description foi usada somente para porte_estimado quando disponível
- arquivos finais mantêm price, quando existir no CSV original
- arquivos finais mantêm sale_price, quando existir no CSV original
- arquivos finais mantêm discount_percentage, quando existir no CSV original
- site/data/produtos_site_por_categoria.json foi atualizado
- HTML não contém lista fixa de produtos
- nenhum subagente foi criado

## REGRA DE ERRO

Se qualquer etapa falhar:

1. registrar o erro no log
2. tentar corrigir uma vez
3. se falhar novamente, parar
4. chamar Denise
5. explicar etapa, erro, arquivo/comando envolvido, tentativa feita e decisão necessária

## RESULTADO ESPERADO

Entregar:

- arquivos CSV atualizados
- arquivos JSON atualizados
- arquivo manual de links atualizado usando product_link
- novo log de execução
- JSON atualizado para alimentar o site
- máximo de 4 produtos por categoria
- categoria definida somente por global_category1/global_category2
- description usada somente para porte_estimado
- dados finais mantendo price, sale_price e discount_percentage quando existirem no CSV
- estrutura do site preservada
- HTML, CSS e JavaScript preservados
- nenhum subagente criado

## FORMATO DE TRABALHO

Primeiro, verifique a estrutura existente.

Depois, verifique o CSV em raw/.

Depois, informe o número total de linhas e o número de produtos únicos por itemid.

Depois, apresente um plano curto.

Depois, execute apenas a atualização dos dados.

No final, entregue um resumo objetivo com:

- CSV usado
- produtos únicos encontrados
- produtos finais selecionados
- quantidade final por categoria
- arquivos atualizados
- arquivos preservados
- arquivos copiados para o site
- validações realizadas
- limitações encontradas
- próximos passos para Denise
