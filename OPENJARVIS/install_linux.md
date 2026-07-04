# OpenJarvis no Linux

Guia copy-paste para instalar o OpenJarvis no Linux, sem misturar esta parte com configuracao de Google OAuth, som, voz e ajustes do `config.toml`.

A instalacao fica neste arquivo. As configuracoes de uso ficam em [`configuracoes_openjarvis.md`](./configuracoes_openjarvis.md).

## Objetivo

Instalar o OpenJarvis em Linux, validar a CLI, subir o backend local, abrir a interface web e confirmar que o Ollama esta respondendo como engine local.

## Fontes oficiais consultadas

- Documentacao oficial do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/
- Instalacao oficial: https://open-jarvis.github.io/OpenJarvis/getting-started/installation/
- Configuracao oficial: https://open-jarvis.github.io/OpenJarvis/getting-started/configuration/
- Repositorio oficial: https://github.com/open-jarvis/OpenJarvis
- Releases oficiais: https://github.com/open-jarvis/OpenJarvis/releases
- uv: https://docs.astral.sh/uv/
- Rust: https://rustup.rs/
- Ollama: https://ollama.com/
- Node.js: https://nodejs.org/

## Ambiente testado no video

- Sistema operacional: Ubuntu Linux 24.04 LTS
- Hardware: desktop i7, 16 GB RAM, NVIDIA GTX 960 2 GB
- Terminal/shell: Bash
- Modelo local usado: Qwen via Ollama
- Pasta usada para o projeto: `~/OpenJarvis`

## Observacao sobre a instalacao

A documentacao oficial mostra dois caminhos principais para Linux:

- `./scripts/quickstart.sh`, que tenta automatizar backend, frontend, dependencias e Ollama;
- instalacao manual com `uv sync --extra desktop`, `maturin`, backend e frontend separados.

Para gravacao e troubleshooting, o metodo manual costuma ser melhor, porque deixa claro onde cada erro acontece.

## Pre-requisitos

A documentacao oficial informa estes requisitos principais:

- Python 3.10 a 3.13;
- `uv`;
- Git;
- Rust estavel;
- Node.js 18+ para a interface web;
- pelo menos uma engine de inferencia, como Ollama, vLLM, llama.cpp ou API em nuvem.

> Evite Python 3.14 por enquanto. A propria documentacao oficial avisa que Python 3.14+ ainda pode exigir ajuste por dependencia sem wheel compativel.

## Instalar dependencias no Ubuntu

```bash
sudo apt update
sudo apt install -y git curl build-essential pkg-config libssl-dev python3 python3-venv python3-pip nodejs npm
```

Confira as versoes:

```bash
python3 --version
git --version
node --version
npm --version
```

Se o Node.js do repositario do Ubuntu estiver antigo, instale pelo metodo oficial do NodeSource ou pelo metodo recomendado no site do Node.js.

## Instalar uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
uv --version
```

Se o comando `uv` nao aparecer, feche e abra o terminal.

## Instalar Rust

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
rustc --version
cargo --version
```

## Instalar Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama --version
```

Suba o servidor do Ollama em um terminal separado:

```bash
ollama serve
```

Em outro terminal, baixe um modelo leve:

```bash
ollama pull qwen3:0.6b
ollama list
```

Para maquina com pouca VRAM, comece por modelo pequeno. Depois de tudo funcionando, teste modelos maiores.

## Instalar OpenJarvis manualmente

```bash
cd ~
git clone https://github.com/open-jarvis/OpenJarvis.git
cd OpenJarvis
uv sync --extra desktop
uv run maturin develop -m rust/crates/openjarvis-python/Cargo.toml
cd frontend && npm install && cd ..
```

## Verificar a CLI

```bash
cd ~/OpenJarvis
uv run jarvis --version
uv run jarvis doctor
uv run jarvis model list
```

Se `uv run jarvis model list` nao encontrar modelo, confirme que o Ollama esta rodando e que o modelo foi baixado:

```bash
ollama list
curl http://127.0.0.1:11434/api/tags
```

## Inicializar configuracao basica

Se ainda nao existir `~/.openjarvis/config.toml`, rode:

```bash
cd ~/OpenJarvis
uv run jarvis init
```

Confira o arquivo criado:

```bash
ls -la ~/.openjarvis
nano ~/.openjarvis/config.toml
```

A configuracao detalhada fica no arquivo [`configuracoes_openjarvis.md`](./configuracoes_openjarvis.md).

## Subir backend local

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8000
```

Teste em outro terminal:

```bash
curl http://127.0.0.1:8000/health
```

O backend/API local fica em:

```text
http://127.0.0.1:8000
```

## Subir interface web

Em outro terminal:

```bash
cd ~/OpenJarvis/frontend
npm run dev -- --host 127.0.0.1 --port 5173
```

Abra no navegador:

```text
http://127.0.0.1:5173
```

## Instalar app desktop no Linux

O app desktop e opcional. O backend continua rodando localmente pela porta `8000`.

Baixe pela pagina oficial de releases:

```text
https://github.com/open-jarvis/OpenJarvis/releases/latest
```

A documentacao oficial lista pacotes Linux em formato DEB, RPM e AppImage.

## Teste rapido

Com Ollama e backend rodando:

```bash
cd ~/OpenJarvis
uv run jarvis ask "Responda em uma frase: OpenJarvis funcionando no Linux."
```

Para abrir chat no terminal:

```bash
cd ~/OpenJarvis
uv run jarvis chat
```

## Como parar

Pare backend, frontend e Ollama com `Ctrl+C` nos terminais onde eles estao rodando.

Para conferir processos:

```bash
ps aux | grep -E 'jarvis|ollama|vite' | grep -v grep
```

## Como remover instalacao local

Use somente se quiser limpar o ambiente e reinstalar do zero.

```bash
rm -rf ~/OpenJarvis
rm -rf ~/.openjarvis
```

Se quiser manter configuracoes, memoria e conectores, nao apague `~/.openjarvis`.

## Erros encontrados e ajustes necessarios

### `maturin` precisa de Rust

**O que aconteceu:**

A instalacao manual chama:

```bash
uv run maturin develop -m rust/crates/openjarvis-python/Cargo.toml
```

Sem Rust instalado, essa etapa falha.

**Correcao usada:**

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

### Backend e frontend sao processos separados

**O que aconteceu:**

O backend sobe na porta `8000`, mas a interface web precisa ser iniciada separadamente dentro da pasta `frontend`.

**Correcao usada:**

Terminal do backend:

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8000
```

Terminal do frontend:

```bash
cd ~/OpenJarvis/frontend
npm run dev -- --host 127.0.0.1 --port 5173
```

### Ollama precisa estar rodando

**O que aconteceu:**

Se o Ollama nao estiver ativo, o OpenJarvis pode nao listar modelos ou falhar ao responder.

**Correcao usada:**

```bash
ollama serve
ollama pull qwen3:0.6b
ollama list
```

### Maquina com pouca VRAM

**O que aconteceu:**

Modelos maiores podem ficar lentos ou nao carregar bem em GPU antiga com pouca VRAM.

**Correcao usada:**

Comecar com modelo pequeno:

```bash
ollama pull qwen3:0.6b
```

Depois testar modelos maiores apenas quando a instalacao basica estiver funcionando.

## O que fica neste arquivo

- instalacao Linux;
- validacao da CLI;
- backend;
- frontend;
- desktop app;
- remocao e troubleshooting basico.

## O que nao fica neste arquivo

- Google OAuth;
- chaves de API;
- configuracao de engine/modelo;
- Gmail, Drive, Calendar, Contacts e Tasks;
- som, microfone, speech-to-text e text-to-speech.

Esses pontos ficam em [`configuracoes_openjarvis.md`](./configuracoes_openjarvis.md).
