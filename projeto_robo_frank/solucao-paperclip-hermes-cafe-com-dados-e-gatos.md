# Solucao: Paperclip com Hermes tentando usar Anthropic

Este documento resume o problema encontrado ao usar o Paperclip com o Hermes Agent e como ele foi resolvido.

## Problema

Ao executar uma issue no Paperclip, o agente falhava com a mensagem:

```text
No Anthropic credentials found. Set ANTHROPIC_TOKEN or ANTHROPIC_API_KEY, run
'claude setup-token', or authenticate with 'claude /login'.
```

Isso parecia estranho porque o Hermes ja estava configurado como padrao para usar o modelo:

```text
gemma4:31b-cloud
```

com provider custom apontando para:

```text
http://localhost:11434/v1
```

## Diagnostico

O arquivo global do Hermes estava correto:

```yaml
model:
  default: gemma4:31b-cloud
  provider: custom
  base_url: http://localhost:11434/v1
  api_key: ollama
```

Tambem foi confirmado pela API local do Paperclip que o Hermes era detectado corretamente:

```json
{
  "model": "gemma4:31b-cloud",
  "provider": "custom",
  "source": "config"
}
```

Mesmo assim, os logs de execucao do Paperclip mostravam:

```text
[hermes] Starting Hermes Agent (model=anthropic/claude-sonnet-4, provider=anthropic [modelInference], timeout=300s)
```

Ou seja: o Paperclip estava chamando o Hermes, mas estava passando explicitamente um modelo da Anthropic para ele.

## Causa

O adaptador `hermes-paperclip-adapter` instalado pelo Paperclip tem um fallback interno:

```js
DEFAULT_MODEL = "anthropic/claude-sonnet-4"
```

No codigo do adaptador, a escolha do modelo funciona assim:

```js
const model = cfgString(config.model) || DEFAULT_MODEL;
```

Isso significa que, se o campo `adapterConfig.model` do agente estiver vazio, o adaptador nao usa o padrao global do Hermes. Em vez disso, ele cai no fallback `anthropic/claude-sonnet-4`.

Por isso o erro de credenciais Anthropic aparecia mesmo com o Hermes configurado para outro modelo.

## Correcao aplicada

A solucao foi gravar explicitamente o modelo correto na configuracao do agente do Paperclip.

O agente era:

```text
Robo Frank
```

ID:

```text
9ff65bf1-e0d3-4029-961b-9a9af1cca578
```

Foi aplicado este PATCH na API local do Paperclip:

```bash
curl -s -X PATCH http://127.0.0.1:3100/api/agents/9ff65bf1-e0d3-4029-961b-9a9af1cca578 \
  -H 'Content-Type: application/json' \
  --data '{"adapterConfig":{"model":"gemma4:31b-cloud"}}'
```

Depois disso, o agente ficou com:

```json
{
  "adapterConfig": {
    "model": "gemma4:31b-cloud",
    "timeoutSec": 300,
    "persistSession": true
  }
}
```

Nao foi definido `provider: custom` no `adapterConfig`, porque o adaptador do Paperclip nao reconhece `custom` como provider valido. Ao informar apenas o modelo, o adaptador cai em `provider=auto`, e o Hermes consegue resolver pelo proprio arquivo `~/.hermes/config.yaml`.

## Limpeza das issues travadas

Depois de corrigir o modelo, ainda havia issues antigas bloqueadas por tentativas anteriores com Anthropic. O pedido foi apagar todas as issues existentes.

Primeiro foi tentado usar o endpoint normal:

```bash
DELETE /api/issues/:id
```

Mas o Paperclip retornou erro interno porque algumas issues ainda eram referenciadas por tabelas auxiliares, como:

```text
issue_comments
issue_read_states
issue_documents
environment_leases
activity_log
agent_task_sessions
```

Entao a limpeza precisou ser feita diretamente no PostgreSQL local embutido do Paperclip, apagando primeiro os registros dependentes e depois as issues.

Ao final, a consulta pela API confirmou:

```json
[]
```

Ou seja, a lista de issues ficou vazia.

## Resultado

O problema principal foi resolvido em duas partes:

1. O agente do Paperclip passou a usar explicitamente `gemma4:31b-cloud`.
2. As issues antigas travadas foram removidas para permitir criar uma nova tarefa limpa.

Resumo da causa raiz:

```text
O Hermes estava configurado corretamente, mas o adaptador do Paperclip usava Anthropic como fallback quando o modelo do agente estava vazio.
```

Resumo da solucao:

```text
Definir adapterConfig.model explicitamente no agente do Paperclip.
```

