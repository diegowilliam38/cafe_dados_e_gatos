# Como organizar agentes Office no Hermes Desktop

## Objetivo

Esta pasta guarda os perfis dos agentes criados no Hermes Agent Desktop para uso no fluxo Office.

## Agentes

- Jane: escritora técnica para roteiros, posts, capítulos, documentação e textos publicáveis.
- Turing: especialista em codificação para código, debug, scripts, setup e documentação técnica.

## Princípio de prompt

Prompt curto, denso e operacional.

Evitar:

- persona inflada
- backstory teatral
- regras repetidas
- frases como "pense profundamente"
- prompt gigante com baixo sinal e muito ruído

## Estrutura

```text
agents_office/
├── jane/
│   ├── IDENTITY.md
│   ├── AVATAR.md
│   ├── SOUL.md
│   ├── AGENTS.md
│   ├── USER.md
│   ├── TOOLS.md
│   ├── MEMORY.md
│   └── HEARTBEAT.md
└── turing/
    ├── IDENTITY.md
    ├── AVATAR.md
    ├── SOUL.md
    ├── AGENTS.md
    ├── USER.md
    ├── TOOLS.md
    ├── MEMORY.md
    └── HEARTBEAT.md
```
