# Systemd e Nginx

## Objetivo

Orientar a organização de serviços do Hermes e proxy reverso quando necessário.

Neste projeto:

```text
Docker apenas para SearXNG.
Hermes Agent sem Docker.
Hermes Gateway/API sem Docker.
Hermes Dashboard sem Docker.
Hermes Workspace sem Docker.
```

## Serviços Hermes

Os exemplos ficam em:

```text
exemplos/systemd/
```

Revise caminhos, usuário e comandos antes de copiar para a VPS.

## Nginx

Use Nginx apenas se precisar expor o Workspace por domínio ou HTTPS.

Para uso privado, prefira Tailscale.

## HTTP e HTTPS

Em ambiente HTTP:

```env
COOKIE_SECURE=0
```

Em ambiente HTTPS:

```env
COOKIE_SECURE=1
```

## Segurança

- Não exponha Gateway/API publicamente sem necessidade.
- Não exponha Ollama publicamente.
- Não exponha SearXNG publicamente sem necessidade.
- Não altere firewall sem revisão humana.
- Não publique domínio, IP, token ou senha real em exemplos.


