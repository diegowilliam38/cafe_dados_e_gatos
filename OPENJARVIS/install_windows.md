# OpenJarvis - Browser App e Desktop App

Este guia segue o fluxo oficial do projeto:

- Docs: https://open-jarvis.github.io/OpenJarvis/getting-started/installation/
- Repo: https://github.com/open-jarvis/OpenJarvis

## Importante

- Rode `ollama`, `uv` e `OpenJarvis` no WSL.
- O `404` em `http://127.0.0.1:8000/` e normal. Essa raiz nao e a interface.
- Para validar a API, use:
  - `http://127.0.0.1:8000/docs`
  - `http://127.0.0.1:8000/openapi.json`

## 1. Browser App no WSL

No WSL:

```bash
git clone https://github.com/open-jarvis/OpenJarvis.git
cd OpenJarvis
./scripts/quickstart.sh
```

O `quickstart.sh` e o caminho mais seguro porque faz o setup integrado do projeto.

## 2. Validacao

Se quiser conferir que o backend subiu:

```bash
curl -i http://127.0.0.1:8000/docs
curl -i http://127.0.0.1:8000/openapi.json
```

Esperado:

- `200 OK` em `/docs`
- `200 OK` em `/openapi.json`
- `404` em `/` pode acontecer e nao indica falha

## 3. Desktop App no Windows

Depois de deixar o backend rodando no WSL, instale o app nativo do Windows:

- https://github.com/open-jarvis/OpenJarvis/releases/download/desktop-v1.0.2/OpenJarvis_1.0.1_x64-setup.exe

Abra o instalador, conclua a instalacao e depois inicie o OpenJarvis Desktop.

## 4. O que evitar

- Nao misturar install manual e `quickstart.sh` no mesmo teste.
- Nao usar `http://127.0.0.1:8000/` como teste da interface.
- Nao usar `uv sync` sozinho se depois voce quiser voltar ao fluxo manual do servidor.

## 5. Se depois voce quiser rodar manualmente

Esse e o fluxo mais seguro:

```bash
cd OpenJarvis
uv sync --extra server
uv run jarvis serve
```

## 6. Resumo curto

1. No WSL: `git clone`, `cd OpenJarvis`, `./scripts/quickstart.sh`
2. Validar com `/docs`
3. No Windows: instalar o Desktop App
4. Ignorar `404` na raiz `/`
