# OpenJarvis no Windows: WSL2 primeiro, Windows puro depois

Guia pratico para instalar e testar o **OpenJarvis no Windows** sem misturar os caminhos.

A ordem deste documento e proposital:

- primeiro: **instalacao pelo WSL2 + Ubuntu**;
- depois: **instalacao no Windows puro**;
- no final: **app desktop, erros comuns e resumo copy-paste**.

> Nao misture os dois caminhos no mesmo teste. Escolha WSL2 ou Windows puro, siga ate o fim, e so depois teste o outro.

## Fontes oficiais consultadas

- Repositorio oficial: https://github.com/open-jarvis/OpenJarvis
- Documentacao oficial: https://open-jarvis.github.io/OpenJarvis/
- Instalacao oficial: https://open-jarvis.github.io/OpenJarvis/getting-started/installation/
- Releases do app desktop: https://github.com/open-jarvis/OpenJarvis/releases
- Ollama: https://ollama.com
- uv: https://docs.astral.sh/uv/
- Git for Windows: https://git-scm.com/downloads/win
- Python: https://www.python.org/downloads/windows/
- Rust: https://rustup.rs/
- Node.js: https://nodejs.org/

## O que sera instalado

O OpenJarvis pode ser usado de algumas formas:

| Forma de uso | Onde aparece | Precisa do backend local? |
| --- | --- | --- |
| CLI | Terminal | Sim |
| Browser App | Navegador | Sim |
| Desktop App | Janela nativa no Windows | Sim |

O ponto mais importante:

```text
O app desktop nao substitui o backend.
```

Mesmo usando o app desktop, o backend precisa estar rodando em:

```text
http://localhost:8000
```

## Ambiente testado no video

Preencha depois do teste:

```text
Sistema operacional:
Versao do Windows:
Caminho usado: WSL2 + Ubuntu ou Windows puro
Terminal:
Python:
Node.js:
Rust:
Ollama:
Modelo usado:
Data do teste:
```

---

# Caminho 1: instalacao pelo WSL2 + Ubuntu

Este e o primeiro caminho do documento. Siga esta parte inteira se voce quiser rodar o OpenJarvis em ambiente Linux dentro do Windows.

## Quando usar WSL2

Use WSL2 se voce quer:

- ambiente mais parecido com Linux;
- menos conflito com permissao de arquivos Python;
- evitar problemas com `.venv` dentro do disco do Windows;
- seguir um fluxo bom para projetos com Python, Rust e Node.js.

## Instalar o WSL2

Abra o **PowerShell como Administrador** e rode:

```powershell
wsl --install
```

Se o Windows pedir, reinicie a maquina.

Depois abra o **Ubuntu** pelo menu iniciar e finalize a criacao do usuario e senha.

## Atualizar o Ubuntu

No terminal do Ubuntu:

```bash
sudo apt update
sudo apt upgrade -y
```

## Instalar dependencias basicas no Ubuntu

```bash
sudo apt install -y curl git build-essential ca-certificates
```

## Criar a pasta correta dentro do Linux

No WSL2, trabalhe dentro da home do Linux:

```bash
cd ~
mkdir -p projetos
cd ~/projetos
```

O caminho recomendado fica assim:

```text
~/projetos
```

Nao use este caminho para rodar projeto Python no WSL2:

```text
/mnt/c/Users/seu_usuario/OpenJarvis
```

Esse caminho aponta para o disco do Windows. Ele funciona para copiar arquivos, mas pode dar erro com `.venv`, permissao e desempenho.

## Instalar o OpenJarvis pelo script oficial no WSL2

Dentro do Ubuntu:

```bash
curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash
```

Depois feche e abra o terminal Ubuntu novamente, ou rode:

```bash
source ~/.bashrc
```

Teste:

```bash
jarvis --version
jarvis doctor
```

## Instalar o Ollama no WSL2

Se voce quer deixar tudo dentro do WSL2, instale o Ollama tambem no Ubuntu:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Inicie o Ollama:

```bash
ollama serve
```

Abra outro terminal Ubuntu e baixe um modelo pequeno para teste:

```bash
ollama pull qwen3:0.6b
ollama list
```

> Para teste didatico, evite misturar Ollama do Windows com OpenJarvis no WSL2 logo no primeiro teste. Primeiro faca tudo em um lugar so.

## Rodar o OpenJarvis no terminal pelo WSL2

Pergunta simples:

```bash
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
```

Chat no terminal:

```bash
jarvis chat
```

## Subir o servidor local pelo WSL2

```bash
jarvis serve --port 8000
```

Depois abra no navegador do Windows:

```text
http://localhost:8000
```

## Se `jarvis serve` falhar no WSL2

Em algumas instalacoes, o modo servidor pode precisar das dependencias extras do servidor.

Tente:

```bash
cd ~/.openjarvis/src
uv sync --extra server
uv run jarvis serve --port 8000
```

Se o comando `uv` nao existir:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
cd ~/.openjarvis/src
uv sync --extra server
uv run jarvis serve --port 8000
```

## Instalacao manual pelo codigo-fonte no WSL2

Use esta parte somente se voce quiser clonar o repositorio e rodar o projeto manualmente.

```bash
cd ~/projetos
git clone https://github.com/open-jarvis/OpenJarvis.git
cd OpenJarvis
```

Instale o `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
uv --version
```

Instale o Rust:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env
rustc --version
```

Sincronize as dependencias:

```bash
uv sync --extra desktop
```

Compile/registre a extensao Rust usada pelo projeto:

```bash
uv run maturin develop -m rust/crates/openjarvis-python/Cargo.toml
```

Instale as dependencias do frontend:

```bash
cd frontend
npm install
cd ..
```

Suba o backend:

```bash
uv run jarvis serve --port 8000
```

Em outro terminal Ubuntu, suba o frontend:

```bash
cd ~/projetos/OpenJarvis/frontend
npm run dev
```

Abra no navegador:

```text
http://localhost:5173
```

## Resumo copy-paste do caminho WSL2

PowerShell como Administrador:

```powershell
wsl --install
```

Ubuntu:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y curl git build-essential ca-certificates
cd ~
mkdir -p projetos
cd ~/projetos
curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash
source ~/.bashrc
jarvis --version
jarvis doctor
```

Teste no terminal:

```bash
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
jarvis chat
```

Servidor local:

```bash
jarvis serve --port 8000
```

Abrir no Windows:

```text
http://localhost:8000
```

---

# Caminho 2: instalacao no Windows puro

Agora comeca o segundo caminho. Use esta parte se voce quer instalar e rodar o OpenJarvis diretamente no Windows, sem WSL2.

## Quando usar Windows puro

Use Windows puro se voce quer:

- testar o instalador PowerShell oficial;
- usar tudo direto no PowerShell;
- evitar abrir Ubuntu/WSL2;
- testar o app desktop com backend tambem rodando no Windows.

## Criar pasta de trabalho no Windows

Use uma pasta simples, sem acento e sem espaco no caminho:

```powershell
mkdir C:\Projetos
cd C:\Projetos
```

## Instalar o OpenJarvis pelo instalador oficial Windows

Abra o **PowerShell como Administrador**:

```powershell
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex
```

Feche e abra o PowerShell novamente.

Teste:

```powershell
jarvis --version
jarvis doctor
```

## Instalar o Ollama no Windows

Baixe e instale pelo site oficial:

```text
https://ollama.com
```

Depois feche e abra o PowerShell novamente.

Teste:

```powershell
ollama --version
ollama pull qwen3:0.6b
ollama list
```

## Rodar o OpenJarvis no terminal pelo Windows puro

Pergunta simples:

```powershell
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
```

Chat no terminal:

```powershell
jarvis chat
```

## Subir o servidor local pelo Windows puro

```powershell
jarvis serve --port 8000
```

Depois abra no navegador:

```text
http://localhost:8000
```

## Clone manual no Windows puro

Use esta parte somente se voce quiser clonar o projeto no Windows.

Instale antes:

- Git for Windows;
- Python 3.10 a 3.13;
- Node.js 18+;
- Rust;
- uv.

Depois:

```powershell
cd C:\Projetos
git clone https://github.com/open-jarvis/OpenJarvis.git
cd OpenJarvis
```

Instale o `uv`, se ainda nao existir:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Feche e abra o PowerShell novamente.

Sincronize as dependencias:

```powershell
uv sync --extra desktop
```

Compile/registre a extensao Rust:

```powershell
uv run maturin develop -m rust/crates/openjarvis-python/Cargo.toml
```

Instale o frontend:

```powershell
cd frontend
npm install
cd ..
```

Suba o backend:

```powershell
uv run jarvis serve --port 8000
```

Em outro PowerShell, suba o frontend:

```powershell
cd C:\Projetos\OpenJarvis\frontend
npm run dev
```

Abra:

```text
http://localhost:5173
```

## Resumo copy-paste do caminho Windows puro

PowerShell como Administrador:

```powershell
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex
```

Novo PowerShell:

```powershell
jarvis --version
jarvis doctor
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
jarvis chat
```

Servidor local:

```powershell
jarvis serve --port 8000
```

Abrir no navegador:

```text
http://localhost:8000
```

---

# App desktop do Windows

Use esta parte depois que voce ja tiver escolhido um caminho e conseguido subir o backend.

O app desktop conecta no backend local:

```text
http://localhost:8000
```

Primeiro suba o backend pelo caminho escolhido.

WSL2:

```bash
jarvis serve --port 8000
```

Windows puro:

```powershell
jarvis serve --port 8000
```

Depois baixe o instalador na pagina oficial de releases:

```text
https://github.com/open-jarvis/OpenJarvis/releases
```

Procure pelo instalador Windows, por exemplo:

```text
OpenJarvis-setup.exe
```

Instale e abra o app.

Se nao conectar, confira se o backend esta rodando e se a porta usada e `8000`.

---

# Erros comuns

## `quickstart.sh` abriu uma janela pedindo aplicativo

Isso acontece quando um script `.sh` foi executado no PowerShell do Windows.

Script `.sh` e para Linux/macOS/WSL2, nao para PowerShell.

No Windows puro, use:

```powershell
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex
```

No WSL2/Ubuntu, use:

```bash
curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash
```

## WSL diz que nao ha distribuicao instalada

Instale o Ubuntu:

```powershell
wsl --install -d Ubuntu
```

Ou liste as distribuicoes disponiveis:

```powershell
wsl --list --online
```

## Erro de permissao na `.venv` dentro de `/mnt/c`

Exemplo:

```text
failed to remove file 'C:\Users\seu_usuario\OpenJarvis\.venv\lib64': Acesso negado
```

Corrija movendo o projeto para dentro da home do Linux:

```bash
cd ~
mkdir -p projetos
cd ~/projetos
git clone https://github.com/open-jarvis/OpenJarvis.git
cd OpenJarvis
uv sync --extra desktop
```

Se ja existir uma `.venv` antiga:

```bash
cd ~/projetos/OpenJarvis
rm -rf .venv
uv sync --extra desktop
```

## `jarvis serve` nao sobe

No WSL2, tente:

```bash
cd ~/.openjarvis/src
uv sync --extra server
uv run jarvis serve --port 8000
```

No Windows puro com clone manual, tente:

```powershell
cd C:\Projetos\OpenJarvis
uv sync --extra server
uv run jarvis serve --port 8000
```

## `ollama` nao encontrado

No Windows, instale pelo site oficial:

```text
https://ollama.com
```

No WSL2:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Depois feche e abra o terminal novamente.

## Porta 8000 ocupada

Teste outra porta:

WSL2:

```bash
jarvis serve --port 8010
```

Windows puro:

```powershell
jarvis serve --port 8010
```

Depois abra:

```text
http://localhost:8010
```

## Python 3.14 ou superior dando problema

A documentacao oficial indica Python 3.10 a 3.13.

Confira:

WSL2:

```bash
python --version
```

Windows puro:

```powershell
python --version
```

Se estiver usando Python 3.14+, instale Python 3.13 ou use um ambiente com Python 3.10 a 3.13.

---

# Veredito pratico

Para video e para quem esta instalando junto, o melhor e seguir um caminho por vez.

Primeiro caminho:

```text
WSL2 + Ubuntu -> install.sh -> jarvis serve -> navegador ou app desktop
```

Segundo caminho:

```text
Windows puro -> install.ps1 -> jarvis serve -> navegador ou app desktop
```

Se o objetivo for reduzir chance de erro com ambiente Python, comece pelo WSL2.

Se o objetivo for testar o instalador oficial do Windows, use Windows puro.

O que nao recomendo no primeiro teste:

```text
instalar parte no Windows, parte no WSL2, Ollama em um lado e OpenJarvis no outro, tudo ao mesmo tempo
```

Isso ate pode funcionar, mas confunde a gravacao e dificulta explicar para quem esta seguindo o tutorial.
