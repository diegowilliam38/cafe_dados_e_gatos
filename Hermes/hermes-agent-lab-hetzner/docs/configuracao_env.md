# Configuração ENV

## Objetivo

Documentar os arquivos `.env` usados pelo Hermes Agent e pelo Hermes Workspace.

Não coloque tokens reais, senhas reais ou IPs reais no GitHub.

## Hermes Agent

Arquivo real na VPS:

```bash
~/.hermes/.env
```

Exemplo didático:

```env
SEARXNG_URL=http://127.0.0.1:8080
API_SERVER_ENABLED=true
API_SERVER_HOST=0.0.0.0
API_SERVER_PORT=8642
API_SERVER_KEY=12345678
API_SERVER_CORS_ORIGINS=*
```

Troque `12345678` no ambiente real.

## Hermes Workspace

Arquivo real na VPS:

```bash
~/hermes-workspace/.env
```

Exemplo didático:

```env
HERMES_API_URL=http://IP_TAILSCALE_DA_VPS:8642
HERMES_DASHBOARD_URL=http://IP_TAILSCALE_DA_VPS:9119
HERMES_API_TOKEN=12345678
HERMES_PASSWORD=12345678
COOKIE_SECURE=0
HOST=0.0.0.0
PORT=3000
```

Troque `12345678` no ambiente real.

## Regra crítica

```text
API_SERVER_KEY e HERMES_API_TOKEN devem ter o mesmo valor.

HERMES_PASSWORD é a senha usada para login no Workspace.

API_SERVER_KEY não é senha de login.
```

## Placeholders

Use placeholders em documentação pública:

```text
IP_PUBLICO_DA_VPS
IP_TAILSCALE_DA_VPS
TROQUE_ESTA_CHAVE_API
TROQUE_ESTA_SENHA_DO_WORKSPACE
```

## Segurança

- Não versionar `.env` reais.
- Não publicar tokens.
- Não publicar senhas.
- Não publicar IPs sensíveis.
- Revisar prints antes de publicar vídeo ou tutorial.


