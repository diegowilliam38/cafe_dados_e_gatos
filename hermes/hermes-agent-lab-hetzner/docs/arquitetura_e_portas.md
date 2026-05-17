# Arquitetura e portas

## Objetivo

Descrever a arquitetura técnica do **Hermes Agent Lab na Hetzner**.

TikTok/Shopee aparecem como teste experimental no final do vídeo.

A infraestrutura principal é Hermes na Hetzner.

## Visão geral

```text
VPS Ubuntu Hetzner
|-- Tailscale
|-- Firewall
|-- Ollama / Ollama Cloud
|-- Docker
|   `-- SearXNG
|-- Hermes Agent sem Docker
|-- Hermes Gateway/API
|-- Hermes Dashboard sem Docker
|-- Hermes Workspace sem Docker
|-- OpenSpec
|-- Navegador controlado
`-- Agentes criados no Workspace
```

## Portas

| Porta | Serviço | Exposição recomendada |
|---:|---|---|
| `22` | SSH | restrita por firewall/Tailscale |
| `3000` | Hermes Workspace | Tailscale ou proxy seguro |
| `8080` | SearXNG | Tailscale ou local |
| `8642` | Hermes Gateway/API | Tailscale ou local |
| `9119` | Hermes Dashboard | Tailscale ou local |
| `11434` | Ollama | local |

## Regra de exposição

Não exponha portas públicas sem necessidade.

Prefira acesso via Tailscale.

## Fluxo lógico

```text
Usuário no navegador
  |
  v
Hermes Workspace :3000
  |
  v
Hermes Gateway/API :8642
  |
  +--> Ollama / Ollama Cloud
  +--> SearXNG :8080
  +--> Hermes Dashboard :9119
```

## Caso de uso

O fluxo técnico apoia:

- pesquisa de produtos afiliados
- pesquisa de tendências TikTok
- roteiros curtos
- calendário de conteúdo
- revisão de promessas
- organização em Kanban
- documentação para GitHub

## Navegador controlado

O navegador controlado pode apoiar pesquisa assistida em páginas públicas ou páginas abertas pela pessoa humana.

Ele não deve ser usado para burlar login, captcha, paywall, restrição de plataforma ou coletar dados privados.



