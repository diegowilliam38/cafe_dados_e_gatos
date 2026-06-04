# PROMPT 1 — CRIAR SITE E ESTRUTURA INICIAL

Você é um agente de desenvolvimento sênior, analista de dados e editor técnico.

Sua função é criar um projeto completo e reaproveitável para análise de produtos da Shopee usando Python/Pandas e gerar um site estático alimentado por JSON.

A única entrada inicial é um arquivo CSV bruto localizado em:

"~/Documents/shopee/raw/"

Você deve executar diretamente a tarefa.

Não crie subagentes.

## OBJETIVO

Criar um projeto que:

1. Leia o CSV bruto da Shopee.
2. Analise os produtos com Python/Pandas.
3. Gere arquivos internos de curadoria.
4. Gere CSVs e JSON finais para alimentar o site.
5. Crie um site estático de achadinhos da Shopee.
6. Faça o site ler os produtos automaticamente a partir do JSON.
7. Permita atualização futura apenas trocando o CSV bruto e rodando o processo de atualização.

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

Mas o site público não deve exibir esses termos.

No site público, não usar:

- potencial comercial estimado
- score_potencial_comercial
- score
- ranking técnico
- metodo_curadoria_version
- modelo_usado
- ambiente
- ferramenta_orquestracao
- mais vendido
- campeão de vendas
- produto que mais vende
- venda comprovada
- sucesso garantido
- garantia de venda
- garantia de comissão

No site público, usar linguagem editorial e comercial leve, como:

- Achadinhos Shopee
- Dica de Presente
- Selecionados da Semana
- Garimpos da Shopee
- Ideias para Casa
- Sugestões para conhecer
- Favoritos para organizar
- Itens úteis para o dia a dia
- Escolhas para você conferir
- Produtos que chamaram atenção

## METADADOS OBRIGATÓRIOS INTERNOS

Registrar nos arquivos finais internos e no log:

- metodo_curadoria_version: "shopee_potencial_v1_dd_mm_aaaa"
- modelo_usado: "Claude Code"
- ambiente: "claude_code"
- ferramenta_orquestracao: "Claude Code"

Esses metadados não devem aparecer visualmente no site público.

## ENTRADA

O CSV original estará em:

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

## PASTAS DE SAÍDA

Criar apenas se não existirem:

- "~/Documents/shopee/claude_code/data/processed/"
- "~/Documents/shopee/claude_code/data/final/"
- "~/Documents/shopee/claude_code/logs/"
- "~/Documents/shopee/claude_code/site/data/"
- "~/Documents/shopee/claude_code/site/assets/"
- "~/Documents/shopee/claude_code/site/css/"
- "~/Documents/shopee/claude_code/site/js/"
- "~/Documents/shopee/claude_code/scripts/"
- "~/Documents/shopee/claude_code/docs/"

## SCRIPT PRINCIPAL

Crie um script Python reutilizável em:

"~/Documents/shopee/claude_code/scripts/gerar_curadoria_shopee.py"

Esse script deve executar toda a curadoria usando Python/Pandas.

O objetivo é que, nas próximas atualizações, Denise não precise recriar o projeto. Ela deve apenas colocar um novo CSV em raw/ e rodar o processo de atualização.

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
- O site deve exibir sale_price como preço principal.
- O site pode exibir price como preço original, se existir e for maior que sale_price.
- O site pode exibir discount_percentage, se existir.
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

Não exibir esse score no site público, a menos que seja em atributo técnico não visível.

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

## ARQUIVOS FINAIS INTERNOS

Gerar em:

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

Criar:

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

Gerar:

produtos_site_por_categoria.json

Esse JSON será usado pelo site.

Ele pode conter campos técnicos necessários para renderização, mas o site não deve exibir metadados técnicos nem termos internos.

O JSON deve permitir que o site exiba:

- categoria_final
- title_clean
- price
- sale_price
- discount_percentage
- item_rating
- image_link
- product_link
- porte_estimado

O JSON pode manter score_potencial_comercial para ordenação interna, mas o site não deve mostrar esse campo ao usuário.

## SITE

Criar um site estático em:

"~/Documents/shopee/claude_code/site/"

O site deve ser alimentado pelo arquivo:

"site/data/produtos_site_por_categoria.json"

O site não deve ter os produtos fixos manualmente no HTML.

O HTML deve carregar os produtos a partir do JSON.

Criar pelo menos:

- site/index.html
- site/css/style.css
- site/js/app.js
- site/data/produtos_site_por_categoria.json

O site deve exibir os produtos por categoria.

Cada card de produto deve usar, quando disponível:

- title_clean
- categoria_final
- sale_price como preço principal
- price como preço original, se existir e for maior que sale_price
- discount_percentage, se existir
- item_rating
- image_link
- product_link
- porte_estimado

Cada card pode usar textos públicos como:

- Ver achadinho
- Conferir na Shopee
- Ver dica
- Abrir produto

O botão do produto deve usar sempre product_link.

Não usar product_short link como link do botão.

## LINGUAGEM PÚBLICA DO SITE

O site deve parecer uma vitrine editorial de achadinhos, não um relatório técnico.

Usar títulos e chamadas como:

- Achadinhos Shopee
- Dicas de Presente
- Selecionados da Semana
- Garimpos para Conferir
- Ideias úteis para o dia a dia
- Achadinhos por categoria

Texto público sugerido:

"Uma seleção de achadinhos para você conhecer, organizada por categorias."

"Confira ideias de produtos úteis, criativos e interessantes encontrados na Shopee."

"Antes de comprar, confira preço, prazo, avaliações e condições diretamente na Shopee."

Aviso público obrigatório no site:

"Os preços, disponibilidade e condições podem mudar. Confira sempre as informações atualizadas diretamente na Shopee antes de comprar."

Não usar no site:

- potencial comercial estimado
- score_potencial_comercial
- score
- ranking
- curadoria técnica
- modelo usado
- ambiente
- ferramenta de orquestração
- mais vendido
- campeão de vendas
- venda comprovada
- sucesso garantido
- garantia de comissão

## DOCUMENTAÇÃO

Criar:

- README.md
- docs/REGRAS_CURADORIA_PRODUTOS.md
- docs/COMO_ATUALIZAR_PRODUTOS.md
- docs/REGRAS_LINGUAGEM_SITE.md

O README deve explicar:

- objetivo do projeto
- entrada esperada
- pastas usadas
- como a curadoria funciona internamente
- como o site é alimentado por JSON
- como atualizar produtos no futuro
- limitações da análise
- comando para rodar o script Python

O arquivo docs/REGRAS_CURADORIA_PRODUTOS.md deve documentar todas as regras internas de curadoria.

O arquivo docs/COMO_ATUALIZAR_PRODUTOS.md deve explicar que futuras atualizações devem rodar o script reutilizável e atualizar o JSON do site.

O arquivo docs/REGRAS_LINGUAGEM_SITE.md deve explicar que termos técnicos e metadados internos não devem aparecer no site público.

## LOG OBRIGATÓRIO

Gerar log em:

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
- site alimentado por JSON
- produtos não foram fixados manualmente no HTML
- site não exibe metadados técnicos
- site não exibe score_potencial_comercial
- site não usa linguagem proibida de venda comprovada
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
- site/index.html existe
- site/js/app.js existe
- site/css/style.css existe
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
- site usa produtos_site_por_categoria.json como fonte de dados
- HTML não contém lista fixa de produtos
- site não exibe potencial comercial estimado
- site não exibe score_potencial_comercial
- site não exibe metadados técnicos
- site não usa linguagem proibida
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

- estrutura do projeto
- script Python/Pandas reutilizável
- curadoria interna auditável
- arquivos CSV e JSON
- arquivo manual de links usando product_link
- logs da execução
- site estático alimentado por JSON
- site com linguagem pública de achadinhos
- site sem metadados técnicos visíveis
- site sem termos de venda comprovada
- arquivos copiados para o site
- máximo de 4 produtos por categoria
- categoria definida somente por global_category1/global_category2
- description usada somente para porte_estimado
- dados finais mantendo price, sale_price e discount_percentage quando existirem no CSV
- nenhum subagente criado

## FORMATO DE TRABALHO

Primeiro, verifique o CSV em raw/.

Depois, informe o número total de linhas e o número de produtos únicos por itemid.

Depois, apresente um plano curto.

Depois, crie a estrutura, o script, os arquivos finais, o site e a documentação.

No final, entregue um resumo objetivo com:

- CSV usado
- produtos únicos encontrados
- produtos finais selecionados
- quantidade final por categoria
- arquivos criados
- arquivos copiados para o site
- validações realizadas
- limitações encontradas
- próximos passos para Denise
