# PROMPT VÍDEO COMFYUI — OPENCLAW — SHOPEE

Sua tarefa é coordenar a criação de prompts e briefs para vídeos curtos no ComfyUI, usando os produtos já selecionados na curadoria da Shopee.

Esta etapa não deve gerar o vídeo diretamente.  
Esta etapa não deve alterar a curadoria, não deve recalcular ranking e não deve modificar os arquivos finais de produtos.

O objetivo é gerar materiais prontos para Denise usar no ComfyUI.

## Agente executor

Use a agente:

```text
Ada
```

Ada deve executar a análise criativa e preparar os prompts de vídeo.

## Objetivo

Criar prompts e briefs para vídeos curtos baseados nos produtos com **potencial comercial estimado**.

Gerar inicialmente:

```text
1 vídeo hero geral do blog
3 vídeos curtos individuais com base nos 3 primeiros produtos da lista
```

## Entrada

Leia o arquivo principal:

```text
~/Documents/shopee/openclaw/data/final/produtos_escolhidos.json
```

Use também, se existirem:

```text
~/Documents/shopee/openclaw/blog/pautas/02_pautas_blog.json
~/Documents/shopee/openclaw/blog/artigos/
~/Documents/shopee/openclaw/imagem/prompt_hero_blog_openclaw.md
```

Não use o CSV bruto da pasta `raw/` nesta etapa.

## Pastas de saída

Crie apenas se não existirem:

```text
~/Documents/shopee/openclaw/video_comfyui/
~/Documents/shopee/openclaw/video_comfyui/briefs/
~/Documents/shopee/openclaw/video_comfyui/prompts/
~/Documents/shopee/openclaw/video_comfyui/roteiros/
~/Documents/shopee/openclaw/video_comfyui/logs/
```

## Regra de escopo

Ada deve trabalhar apenas com produtos existentes em:

```text
~/Documents/shopee/openclaw/data/final/produtos_escolhidos.json
```

Não invente produtos.  
Não invente vendas.  
Não afirme que são os mais vendidos.

Use linguagem baseada em:

```text
potencial comercial estimado
boa nota no dataset
preço dentro do recorte analisado
categoria com prioridade comercial
boa aderência ao ticket de R$ 20 a R$ 80
```

## Regra de ouro para erros

Se qualquer etapa falhar:

```text
1. registre o erro no log
2. tente corrigir uma vez
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

## Etapa 1 — Leitura dos produtos

Ada deve ler os produtos escolhidos e identificar:

```text
top 3 produtos por rank_position
categorias dos produtos
preço
nota
imagem disponível, se houver
tags
descrição curta ou short_card_copy, se existir
why_selected, se existir
risk_notes, se existir
```

## Etapa 2 — Vídeo hero geral

Criar um briefing para 1 vídeo geral do blog.

Esse vídeo deve representar o conceito:

```text
curadoria de achadinhos da Shopee
produtos acessíveis
ticket entre R$ 20 e R$ 80
visual limpo
compra por impulso
potencial comercial estimado
```

Não precisa mostrar produtos específicos com fidelidade.  
Pode representar visualmente o universo dos produtos selecionados.

Configuração sugerida:

```text
formato: horizontal 16:9
duração: 6 a 10 segundos
uso: hero animado, banner ou abertura de blog
estilo: comercial limpo, moderno, leve e confiável
```

Gerar para o vídeo hero:

```text
brief criativo
roteiro por segundos
prompt visual para ComfyUI
prompt negativo
sugestão de movimento de câmera
sugestão de iluminação
sugestão de resolução
nome sugerido do arquivo final
```

Salvar em:

```text
~/Documents/shopee/openclaw/video_comfyui/briefs/01_video_hero_blog.md
~/Documents/shopee/openclaw/video_comfyui/prompts/01_prompt_comfyui_hero_blog.md
~/Documents/shopee/openclaw/video_comfyui/roteiros/01_roteiro_hero_blog.md
```

## Etapa 3 — Vídeos individuais dos top 3 produtos

Criar 1 briefing para cada um dos 3 primeiros produtos.

Cada vídeo deve destacar:

```text
tipo do produto
uso visual do produto
benefício prático
preço dentro do recorte analisado
boa nota no dataset
potencial comercial estimado
```

Não afirmar venda comprovada.

Configuração sugerida:

```text
formato: vertical 9:16
duração: 6 a 10 segundos
uso: Shorts, Reels, TikTok ou anúncio curto
estilo: produto em destaque, fundo limpo, comercial simples
```

Para cada produto, gerar:

```text
brief criativo
roteiro por segundos
prompt visual para ComfyUI
prompt negativo
texto curto opcional na tela
sugestão de movimento de câmera
sugestão de iluminação
sugestão de resolução
nome sugerido do arquivo final
```

Salvar em:

```text
~/Documents/shopee/openclaw/video_comfyui/briefs/02_video_produto_top1.md
~/Documents/shopee/openclaw/video_comfyui/briefs/03_video_produto_top2.md
~/Documents/shopee/openclaw/video_comfyui/briefs/04_video_produto_top3.md

~/Documents/shopee/openclaw/video_comfyui/prompts/02_prompt_comfyui_produto_top1.md
~/Documents/shopee/openclaw/video_comfyui/prompts/03_prompt_comfyui_produto_top2.md
~/Documents/shopee/openclaw/video_comfyui/prompts/04_prompt_comfyui_produto_top3.md

~/Documents/shopee/openclaw/video_comfyui/roteiros/02_roteiro_produto_top1.md
~/Documents/shopee/openclaw/video_comfyui/roteiros/03_roteiro_produto_top2.md
~/Documents/shopee/openclaw/video_comfyui/roteiros/04_roteiro_produto_top3.md
```

## Estrutura dos prompts para ComfyUI

Cada prompt visual deve conter:

```text
descrição da cena
produto ou categoria em destaque
composição
estilo visual
câmera
movimento
iluminação
fundo
detalhes comerciais
atmosfera
resolução sugerida
duração sugerida
prompt negativo
```

Usar este modelo:

```markdown
# Prompt ComfyUI — <nome do vídeo>

## Produto ou tema
...

## Cena
...

## Estilo visual
...

## Câmera e movimento
...

## Iluminação
...

## Ação por segundos
0s-2s: ...
2s-5s: ...
5s-8s: ...

## Texto na tela
...

## Prompt final
...

## Prompt negativo
...

## Configuração sugerida
- proporção:
- duração:
- uso:
- nome de arquivo sugerido:
```

## Regras de qualidade visual

Evitar:

```text
muitos objetos
mãos deformadas
texto longo na imagem
produto distorcido
logos indevidos
marca Shopee exagerada
watermark
cenário poluído
promessa exagerada
aparência amadora
```

Se o modelo tiver dificuldade com texto, priorize vídeo sem texto.

## Log obrigatório

Ada deve registrar em:

```text
~/Documents/shopee/openclaw/video_comfyui/logs/video_comfyui_log.md
```

O log deve conter:

```text
arquivo de produtos usado
quantidade de produtos lidos
top 3 produtos usados
quantidade de briefs gerados
quantidade de prompts gerados
arquivos gerados
erros encontrados
tentativas de correção
limitações importantes
```

## Validação final do Turing

Após Ada finalizar, Turing deve validar se existem:

```text
~/Documents/shopee/openclaw/video_comfyui/briefs/01_video_hero_blog.md
~/Documents/shopee/openclaw/video_comfyui/prompts/01_prompt_comfyui_hero_blog.md
~/Documents/shopee/openclaw/video_comfyui/roteiros/01_roteiro_hero_blog.md

~/Documents/shopee/openclaw/video_comfyui/briefs/02_video_produto_top1.md
~/Documents/shopee/openclaw/video_comfyui/briefs/03_video_produto_top2.md
~/Documents/shopee/openclaw/video_comfyui/briefs/04_video_produto_top3.md

~/Documents/shopee/openclaw/video_comfyui/prompts/02_prompt_comfyui_produto_top1.md
~/Documents/shopee/openclaw/video_comfyui/prompts/03_prompt_comfyui_produto_top2.md
~/Documents/shopee/openclaw/video_comfyui/prompts/04_prompt_comfyui_produto_top3.md

~/Documents/shopee/openclaw/video_comfyui/roteiros/02_roteiro_produto_top1.md
~/Documents/shopee/openclaw/video_comfyui/roteiros/03_roteiro_produto_top2.md
~/Documents/shopee/openclaw/video_comfyui/roteiros/04_roteiro_produto_top3.md

~/Documents/shopee/openclaw/video_comfyui/logs/video_comfyui_log.md
```

Se todos existirem, Turing entrega o resumo final.

Se algum arquivo estiver ausente, Turing deve chamar Denise e explicar exatamente o problema.

## Resultado esperado

Ao final, Turing deve entregar somente:

```text
1. resumo curto da execução
2. top 3 produtos usados
3. quantidade de briefs gerados
4. quantidade de prompts gerados
5. caminhos dos arquivos finais
6. erros ou limitações encontradas
```
