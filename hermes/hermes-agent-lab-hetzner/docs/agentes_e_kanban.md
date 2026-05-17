# Agentes e Kanban

## Objetivo

Organizar o fluxo operacional do projeto **Hermes TikTok Commerce Lab**.

Na gravação, o fluxo prático usou o profile `default` como orquestrador e workers especializados criados via CLI.

## Checkpoint padrão

Todo agente deve concluir tarefas neste formato:

```text
STATE:
RESULT:
FILES_CHANGED:
RISKS:
NEXT_ACTION:
NEEDS_REVIEW:
```

## Regra de aprovação humana

Nenhum agente pode publicar, apagar, sobrescrever, enviar mensagem, executar ação externa, alterar produção, expor porta pública, alterar firewall, trocar senha/token, remover dados, automatizar publicação ou tomar decisão irreversível sem aprovação humana explícita.

## Estrutura usada na gravação

```text
default = CEO / Orquestrador

workers:
hermes-pesquisador-tiktok
hermes-validador-searxng
hermes-organizador-produtos
hermes-criador-conteudo
hermes-designer-pipclip
hermes-revisor-final
```

## Fluxo operacional oficial

```text
default/orquestrador
-> hermes-pesquisador-tiktok
   KANBAN_STATUS: Produto encontrado

-> hermes-validador-searxng
   KANBAN_STATUS: Validando com SearXNG

-> hermes-organizador-produtos
   KANBAN_STATUS: Aguardando escolha humana

-> pausa obrigatória
   humano escolhe produto

-> hermes-criador-conteudo
   KANBAN_STATUS: Criando roteiro

-> pausa obrigatória
   humano aprova roteiro

-> hermes-designer-pipclip
   KANBAN_STATUS: Criando prompt PipClip

-> hermes-revisor-final
   KANBAN_STATUS: Revisado

-> pausa obrigatória
   publicação manual, fora da automação
```

## Responsabilidades

### default / CEO / Orquestrador

Coordena o fluxo, lê o OpenSpec, cria cards, delega tarefas, controla escopo e para o processo quando precisar de aprovação humana.

### hermes-pesquisador-tiktok

Pesquisa produtos, sinais públicos, tendências e oportunidades de conteúdo quando a fonte estiver acessível.

Quando a VPS ou a plataforma bloquear acesso, deve solicitar entrada humana com links, prints, imagens ou dados básicos.

### hermes-validador-searxng

Valida externamente produtos, claims, reclamações, reviews e sinais de risco usando SearXNG ou fontes fornecidas pela pessoa humana.

### hermes-organizador-produtos

Organiza candidatos em tabela, separa fato de hipótese e prepara a lista para escolha humana.

### hermes-criador-conteudo

Cria ângulos, hooks, roteiros curtos, CTA, legenda e textos de tela depois da escolha humana.

Quando o roteiro for virar prompt PipClip, deve entregar:

- gancho inicial
- roteiro falado curto
- texto na tela curto
- CTA final
- legenda
- hashtags, quando solicitado
- duração recomendada: 10s, 15s ou 30s

### hermes-designer-pipclip

Transforma produto aprovado e roteiro aprovado em prompt visual no padrão PipClip.

Formato obrigatório:

```text
Estilo:
Cena:
Câmera:
Iluminação:
Ação por segundos:
Texto na tela:
Som ambiente:
Negativas:
```

O designer não deve criar prompt antes da aprovação humana do roteiro.

### hermes-revisor-final

Revisa roteiro, prompt, texto de tela, CTA, claims, risco visual, transparência e promessa comercial.

Parecer final:

```text
APPROVED
CHANGES_REQUESTED
BLOCKED
```

Sempre explicar o motivo.

## Colunas do Kanban

```text
Produto encontrado
Validando com SearXNG
Aguardando escolha humana
Criando roteiro
Criando prompt PipClip
Revisado
Aguardando publicação manual
Publicado manualmente
Problemas / Ajustes
```

## Modo humano assistido

Use quando TikTok, Shopee, Creative Center, Seller Center ou outro site bloquear acesso pela VPS.

```text
1. Humano acessa a fonte pelo navegador local.
2. Humano coleta link, print, imagem ou dado básico.
3. Worker analisa o material recebido.
4. Worker registra fonte, limitação e risco.
5. Orquestrador atualiza o Kanban.
6. Processo continua somente com revisão humana.
```

## Materiais relacionados

- [Criação dos agentes via CLI](../materiais/criar_agentes_via_cli.md)
- [Rodando o projeto operacional](../materiais/rodando_projeto_operacional.md)
- [Nota pós-gravação sobre VPS fora do Brasil](../materiais/nota_pos_gravacao_vps_fora_do_brasil.md)
