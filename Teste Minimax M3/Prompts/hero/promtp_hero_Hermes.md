# PROMPT IMAGEM HERO — HERMES — BLOG SHOPEE

Frank você é responsável por coordenar a preparação do material para gerar a imagem principal do Hero do blog da Shopee.

Nesta etapa, o foco é apenas **imagem**.  
Não altere a curadoria de produtos, não refaça ranking, não mexa no site e não gere código do frontend.

A agente **Ada** já foi cadastrada manualmente e deve ser usada como agente executora nesta tarefa.

## Objetivo

Criar um **prompt final de imagem** para ser usado em um gerador como MiniMax M3 na criação da imagem Hero do blog.

A imagem deve representar visualmente o universo dos produtos escolhidos e usar os **3 primeiros produtos da lista final** como referência principal.

## Agente executor

Use a agente:

```text
Ada
```

Ada deve:

```text
ler o arquivo final de produtos
identificar os 3 primeiros produtos da lista
resumir os produtos de referência
interpretar o tema visual dominante
criar um prompt final para imagem Hero
gerar uma versão curta opcional
listar negativas de geração
salvar o resultado em arquivo markdown
```

Frank deve apenas coordenar, validar e reportar o resultado final.

## Entrada

Leia o arquivo:

```text
~/Documents/shopee/hermes/data/final/produtos_escolhidos.json
```

Se necessário para conferência, use também:

```text
~/Documents/shopee/hermes/data/final/produtos_escolhidos.csv
```

## Regra principal

Use os **3 primeiros produtos da lista final** como referência temática e visual.

Considere principalmente estes campos:

```text
rank_position
title_original
title_clean
category
subcategory
sale_price
item_rating
image_url
product_url
site_tags
why_selected
risk_notes
```

## Como usar os 3 primeiros produtos

Os 3 primeiros produtos devem orientar:

```text
tema visual da imagem
tipo de produto em destaque
clima comercial do blog
paleta e atmosfera visual
composição principal do Hero
```

Não é obrigatório reproduzir fielmente os produtos.  
A imagem pode ser uma representação estilizada, limpa e visualmente atraente inspirada nesses produtos.

Se os 3 primeiros produtos forem da mesma categoria, a imagem pode focar nesse universo.

Se forem de categorias diferentes, a imagem deve representar o conceito de:

```text
achadinhos bem avaliados
baixo ticket
produtos visuais
curadoria inteligente
```

## Direção visual

A imagem Hero deve seguir estas características:

```text
formato horizontal
proporção 16:9
visual moderno
aparência limpa
estilo editorial/comercial
sensação de blog profissional
tema leve e atrativo
bom espaço visual
sem poluição
```

A imagem deve transmitir:

```text
curadoria de achadinhos
produtos acessíveis
compra por impulso
descoberta de produtos interessantes
visual confiável e agradável
```

## Elementos visuais desejados

A composição pode incluir:

```text
1 elemento principal inspirado nos produtos líderes
2 ou 3 produtos secundários inspirados no top 3
fundo claro ou elegante
composição organizada
detalhes sutis de lifestyle/e-commerce
sensação de descoberta e curadoria
```

Se fizer sentido, incluir elementos como:

```text
embalagens, acessórios, utensílios, itens de beleza, organização ou tecnologia leve
```

desde que isso seja coerente com os 3 primeiros produtos.

## Regras de qualidade

Evitar:

```text
imagem poluída
muitos objetos
texto longo
layout confuso
visual genérico demais
mãos deformadas
objetos distorcidos
aparência infantilizada demais
logos indevidos
watermark
marca Shopee em destaque exagerado
```

Se houver texto na imagem, usar pouco texto.

No máximo algo curto como:

```text
Achadinhos com Potencial
```

ou

```text
Curadoria de Achadinhos
```

Se o modelo tiver dificuldade com texto, priorize a imagem sem texto.

## Regra de ouro para erros

Se qualquer etapa falhar:

```text
1. registre o erro no log
2. peça para Ada tentar corrigir uma vez
3. se a segunda tentativa também falhar, pare
4. chame Denise
5. explique claramente o erro
```

Ao chamar Denise, informe:

```text
etapa com erro
mensagem de erro
arquivo ou comando envolvido
o que já foi tentado
qual decisão humana é necessária
```

Não tente corrigir o mesmo problema mais de 2 vezes.

## Saída esperada

Gere:

```text
1. um resumo curto dos 3 produtos usados como referência
2. uma interpretação visual do conjunto
3. um prompt final único pronto para imagem
4. uma versão curta opcional do prompt
5. uma lista curta de negativas
```

## Formato da saída

Salvar em:

```text
~/Documents/shopee/hermes/imagem/prompt_hero_blog_hermes.md
```

Crie também, se não existir:

```text
~/Documents/shopee/hermes/imagem/
```

## Estrutura desejada do arquivo

O arquivo final deve conter:

```markdown
# Hero do Blog — Prompt de Imagem

## Top 3 produtos usados como referência
- ...
- ...
- ...

## Interpretação visual
...

## Prompt final
...

## Prompt curto opcional
...

## Negativas
- ...
- ...
- ...
```

## Validação final do Hermes

Após Ada finalizar, Frank deve validar se existe:

```text
~/Documents/shopee/hermes/imagem/prompt_hero_blog_hermes.md
```

Se o arquivo existir, Frank entrega o resumo final.

Se o arquivo estiver ausente, Frank deve chamar Denise e explicar exatamente o problema.

## Instrução final


O objetivo é gerar a **melhor imagem possível para a Hero do blog**.
