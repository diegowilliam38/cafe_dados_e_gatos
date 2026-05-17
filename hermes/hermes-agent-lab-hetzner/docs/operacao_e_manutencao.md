# Operação e manutenção

## Objetivo

Este documento resume como operar o projeto depois que Hermes Agent, Gateway, workers, SOUL.md, Kanban e OpenSpec estiverem configurados.

Para o passo a passo completo da gravação, use:

- [Rodando o projeto operacional](../materiais/rodando_projeto_operacional.md)
- [Criação dos agentes via CLI](../materiais/criar_agentes_via_cli.md)
- [Nota pós-gravação sobre VPS fora do Brasil](../materiais/nota_pos_gravacao_vps_fora_do_brasil.md)

## Rotina rápida

Verifique serviços e portas:

```bash
./scripts/status_servicos.sh
./scripts/checar_portas.sh
```

## Testes básicos

Hermes Gateway/API:

```bash
curl http://127.0.0.1:8642/health
```

Hermes Workspace:

```bash
curl -I http://127.0.0.1:3000
```

SearXNG:

```bash
curl -I http://127.0.0.1:8080
```

Ollama:

```bash
curl http://127.0.0.1:11434/api/tags
```

## Fluxo operacional gravado

```text
default/orquestrador
-> pesquisador TikTok
-> validador SearXNG
-> organizador de produtos
-> escolha humana
-> criador de conteúdo
-> aprovação humana do roteiro
-> designer PipClip
-> revisor final
-> publicação manual fora da automação
```

## Limitação de VPS fora do Brasil

Durante a gravação, a infraestrutura funcionou, mas alguns sites de produto ou plataformas sociais podem bloquear a VPS por região, IP de datacenter, login, captcha ou proteção antifraude.

Quando isso acontecer:

- não burlar bloqueio
- não contornar captcha
- não mascarar IP para violar regra de plataforma
- não fazer scraping agressivo
- usar modo humano assistido
- trabalhar com links, prints, imagens e dados fornecidos manualmente
- registrar a limitação no Kanban

## Revisão antes de publicar conteúdo

Antes de publicar vídeo, roteiro, legenda ou criativo:

- revisar promessa comercial
- validar fonte de produto ou tendência
- evitar claims sem comprovação
- evitar linguagem de renda garantida
- checar uso de imagem, marca ou pessoa
- pedir aprovação humana

## SearXNG em Docker

Entrar na pasta:

```bash
cd ~/searxng
```

Ver containers:

```bash
docker compose ps
```

Ver logs:

```bash
docker compose logs -f
```

Atualizar no futuro:

```bash
docker compose down
docker compose pull
docker compose up -d
```

## Backups

Preserve apenas arquivos necessários e sanitizados.

Não publique:

- `.env` reais
- logs brutos
- tokens
- senhas
- IPs sensíveis
