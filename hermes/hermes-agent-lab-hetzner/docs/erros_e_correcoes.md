# Erros e correções

## Objetivo

Registrar problemas comuns durante a instalação e operação do laboratório Hermes na Hetzner.

## Workspace não autentica

Verifique:

```bash
grep HERMES_PASSWORD ~/hermes-workspace/.env
grep COOKIE_SECURE ~/hermes-workspace/.env
```

Em HTTP, use:

```env
COOKIE_SECURE=0
```

Depois reinicie o Workspace.

## Workspace não conecta ao Gateway

Verifique:

```bash
grep API_SERVER_KEY ~/.hermes/.env
grep HERMES_API_TOKEN ~/hermes-workspace/.env
curl http://127.0.0.1:8642/health
```

Regra:

```text
HERMES_API_TOKEN deve ter o mesmo valor de API_SERVER_KEY.
```

## SearXNG não responde

SearXNG roda em Docker neste projeto.

Entre na pasta:

```bash
cd ~/searxng
```

Confira containers:

```bash
docker compose ps
```

Veja logs:

```bash
docker compose logs -f
```

Teste:

```bash
curl -I http://127.0.0.1:8080
```

## Hermes Gateway não sobe

Verifique:

```bash
hermes --version
hermes doctor
cat ~/.hermes/.env
```

Não publique o conteúdo real do `.env`.

## Dashboard não abre

Confira a ajuda da versão instalada:

```bash
hermes dashboard --help
```

Confira se a porta esperada está em uso:

```bash
ss -ltnp | grep ':9119'
```

## Porta ocupada

Use:

```bash
ss -ltnp
```

Identifique o serviço antes de alterar portas ou parar processos.

## Antes de pedir ajuda

Remova:

- tokens
- senhas
- IPs reais
- logs com dados sensíveis
- conteúdo de `.env` real


