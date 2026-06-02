# Teste M3

Esta pasta organiza materiais de teste do `MiniMax M3` em mais de um contexto.

Não se trata apenas da ferramenta de áudio.  
O conjunto atual mistura:

- testes de prompts para `Hermes`
- testes de prompts para `OpenClaw`
- testes de uso via `VS Code / Cline`
- fluxos para curadoria Shopee
- fluxos para criação de blog/site
- prompts para imagem Hero
- prompts para vídeo no ComfyUI
- pacote separado para laboratório de vozes MiniMax

## Estrutura principal

Dentro desta pasta existe a subpasta:

```text
Teste M3/
```

Ela está organizada em:

- `hermes/`
- `openclaw/`
- `VS_Code_Cline/`

## O que existe em cada área

### `hermes/`

Material de teste do fluxo Hermes com `MiniMax M3` para projeto Shopee.

Arquivos lidos:

- `prompt_hermes_shopee.md`
  - curadoria de produtos com potencial comercial estimado
  - arquitetura com agentes `Frank` e `Jane`
  - saídas em dados finais, logs e arquivos auxiliares
- `prompt_blog_hermes_shopee.md`
  - criação de blog/site com base na curadoria
- `prompt_imagem_hero_hermes.md`
  - criação de prompt final para imagem Hero
- `prompt_video_comfyui_hermes_shopee.md`
  - criação de briefs e prompts para vídeos curtos no ComfyUI

### `openclaw/`

Material equivalente para o fluxo `OpenClaw`, também com `MiniMax M3`.

Arquivos lidos:

- `prompt_openclaw_shopee.md`
  - curadoria inicial dos produtos
- `prompt_blog_openclaw_shopee.md`
  - criação de blog/site
- `prompt_imagem_hero_openclaw.md`
  - prompt de imagem Hero
- `prompt_video_comfyui_openclaw_shopee.md`
  - prompts e briefs para vídeo

### `VS_Code_Cline/`

Prompts pensados para execução via `Cline` no `VS Code`, usando os materiais já gerados nos fluxos anteriores.

Arquivos lidos:

- `criacao_blog_hermes.md`
- `criacao_blog_openclaw.md`

Esses arquivos focam na montagem do blog de afiliados com base nos dados, artigos, SEO e assets já preparados.

## Tema central dos testes

O eixo principal desta pasta é comparar ou estruturar o uso do `MiniMax M3` em tarefas como:

- leitura e curadoria de CSV da Shopee
- classificação por `potencial comercial estimado`
- organização de arquivos finais para site
- criação de blog comercial/editorial
- geração de prompts visuais para Hero
- geração de prompts para vídeo curto
- orquestração em ambientes diferentes:
  - `Hermes`
  - `OpenClaw`
  - `Cline / VS Code`

## Regra metodológica recorrente

Nos prompts lidos aparece uma regra consistente:

- não tratar os produtos como `mais vendidos`
- não afirmar venda comprovada
- usar a expressão:

```text
potencial comercial estimado
```

Isso mostra que o teste não é apenas técnico sobre modelo, mas também metodológico e editorial.

## Ferramenta de voz MiniMax

Em paralelo a esses testes, foi preparado um pacote separado para experimentar vozes portuguesas da MiniMax.

Esse pacote não substitui os materiais acima.  
Ele é um complemento para teste de voz e escolha de `voice_id`.

Pacotes preparados:

- Linux
- Windows

Repositório preparado:

```text
cafe_dados_e_gatos/Teste MinimMax M3/
```

## Leitura prática desta pasta

Se a ideia for seguir um fluxo, a leitura mais natural hoje parece ser:

1. `hermes/prompt_hermes_shopee.md` ou `openclaw/prompt_openclaw_shopee.md`
2. prompt de blog correspondente
3. prompt de imagem Hero correspondente
4. prompt de vídeo correspondente
5. prompts de `VS_Code_Cline/` para montar o site final com os arquivos já produzidos

## Resumo

Esta pasta hoje representa um laboratório de teste do `MiniMax M3` para:

- operação de agentes
- curadoria de produtos
- produção editorial
- criação de blog/site
- planejamento de imagem e vídeo
- e, em trilha paralela, teste de vozes
