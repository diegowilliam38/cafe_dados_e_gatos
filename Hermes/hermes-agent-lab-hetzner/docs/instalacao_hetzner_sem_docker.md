# Instalação Hetzner

## Objetivo

Preparar uma VPS Ubuntu da Hetzner para rodar o ecossistema Hermes usado no projeto **Hermes Agent Lab na Hetzner**.

## Regra de arquitetura

```text
Docker apenas para SearXNG.

Hermes Agent sem Docker.
Hermes Gateway/API sem Docker.
Hermes Dashboard sem Docker.
Hermes Workspace sem Docker.
```

## Componentes

- VPS Ubuntu Hetzner
- Tailscale
- Firewall
- Ollama / Ollama Cloud
- Docker
- SearXNG em Docker
- Hermes Agent
- Hermes Gateway/API
- Hermes Dashboard
- Hermes Workspace
- OpenSpec

## Passo a passo completo

Use o material copy-paste:

```text
materiais/instalacao_hermes_hetzner_com_openspec.md
```

Esse arquivo contém os comandos completos usados na gravação.

## Nota sobre Hermes Workspace

Durante a instalação do Hermes Workspace, o `pnpm install` pode pedir autorização para executar scripts de build.

Quando aparecer o aviso, use:

```bash
pnpm approve-builds
```

Pacotes comuns nessa etapa:

```text
electron
electron-winstaller
esbuild
unrs-resolver
```

Se o comando disser que não há pacotes aguardando aprovação, continue a instalação normalmente.

## Cuidados

- Troque senhas e tokens de exemplo no ambiente real.
- Não publique arquivos `.env` reais.
- Não exponha portas internas sem necessidade.
- Prefira acesso privado via Tailscale.
- Não altere firewall ou tokens sem aprovação humana.




