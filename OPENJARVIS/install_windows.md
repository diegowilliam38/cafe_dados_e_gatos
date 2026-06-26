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

## 1. Instalar o Browser App no WSL

No WSL:

```bash
cd /mnt/c/Users/denis
git clone https://github.com/open-jarvis/OpenJarvis.git
cd OpenJarvis
./scripts/quickstart.sh
```

O que cada comando faz:

- `cd /mnt/c/Users/denis`: entra na pasta onde o projeto sera baixado.
- `git clone https://github.com/open-jarvis/OpenJarvis.git`: baixa o codigo-fonte oficial do OpenJarvis.
- `cd OpenJarvis`: entra na pasta do projeto recem-clonado.
- `./scripts/quickstart.sh`: executa o script oficial de instalacao rapida, preparando o ambiente e subindo os servicos usados pelo OpenJarvis.

O `quickstart.sh` e o caminho mais seguro porque faz o setup integrado do projeto.

## 2. Validar se o backend esta funcionando

Se quiser conferir que o backend subiu:

```bash
curl -i http://127.0.0.1:8000/docs
curl -i http://127.0.0.1:8000/openapi.json
```

O que cada comando faz:

- `curl -i http://127.0.0.1:8000/docs`: verifica se a documentacao interativa da API esta acessivel.
- `curl -i http://127.0.0.1:8000/openapi.json`: verifica se a especificacao da API foi carregada corretamente.

Resultado esperado:

- `200 OK` em `/docs`
- `200 OK` em `/openapi.json`
- `404` em `/` pode acontecer e nao indica falha

## 3. Instalar o Desktop App no Windows

Depois de deixar o backend rodando no WSL, instale o app nativo do Windows:

- https://github.com/open-jarvis/OpenJarvis/releases/download/desktop-v1.0.2/OpenJarvis_1.0.1_x64-setup.exe

Abra o instalador, conclua a instalacao e depois inicie o OpenJarvis Desktop.

O Desktop App usa o backend local ja iniciado no WSL.

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

1. No WSL: `cd /mnt/c/Users/denis`
2. Clonar o repo: `git clone https://github.com/open-jarvis/OpenJarvis.git`
3. Entrar no projeto: `cd OpenJarvis`
4. Rodar o setup: `./scripts/quickstart.sh`
5. Validar com `/docs`
6. No Windows: instalar o Desktop App
7. Ignorar `404` na raiz `/`
