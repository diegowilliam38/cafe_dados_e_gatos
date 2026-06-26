# OpenJarvis no Windows: instalacao organizada e copy-paste

Guia pratico para instalar e testar o **OpenJarvis no Windows**, separando os caminhos que costumam confundir:

- instalacao **nativa no Windows**, usando PowerShell;
- instalacao pelo **WSL2 + Ubuntu**, usando ambiente Linux dentro do Windows;
- uso do **app desktop do Windows** conectado ao backend local;
- organizacao de pastas para evitar erro com `.venv`, permissao e arquivos em `/mnt/c`.

> Este guia foi escrito para reproducao de teste em video e para quem quer instalar em casa sem misturar comandos de Windows, Linux e WSL2.

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

## O que o OpenJarvis roda no Windows

O OpenJarvis pode ser usado de tres formas principais:

| Forma de uso | Onde roda | Para quem serve |
| --- | --- | --- |
| CLI | Terminal | Testes rapidos por comando |
| Browser App | Backend local + navegador | Interface web local |
| Desktop App | App Windows + backend local | Janela nativa no Windows |

A interface desktop **nao substitui o backend**. O app desktop abre uma janela para a interface, mas o backend local precisa estar rodando na maquina.

## Caminho recomendado para este teste

Para evitar confusao, use um destes caminhos:

| Caminho | Quando usar |
| --- | --- |
| Windows nativo | Quando quiser testar o instalador PowerShell oficial do projeto |
| WSL2 + Ubuntu | Quando quiser um ambiente mais parecido com Linux e menos conflito com ferramentas Python |
| Desktop App | Quando quiser usar a janela nativa do Windows depois que o backend estiver rodando |

Neste documento, o caminho mais didatico para video e:

```text
Windows -> WSL2/Ubuntu -> backend OpenJarvis -> navegador ou app desktop
```

Mas tambem deixo o caminho nativo Windows separado, porque ele aparece no README oficial do projeto.

## Ambiente testado no video

Preencha depois do teste:

```text
Sistema operacional: Windows 10 ou Windows 11
Ambiente usado: Windows nativo ou WSL2 + Ubuntu
Terminal: PowerShell / Windows Terminal / Ubuntu WSL2
Python:
Node.js:
Rust:
Ollama:
Modelo local usado:
Data do teste:
```

## Antes de comecar

Tenha pelo menos:

- Windows 10 ou Windows 11;
- internet funcionando;
- permissao de administrador no Windows;
- espaco livre no disco `C:`;
- Git instalado, se for clonar o repositorio;
- Ollama instalado ou pronto para instalar;
- Python 3.10 a 3.13, se for fazer instalacao manual;
- Node.js 18+, se for usar a interface web local;
- Rust, se for compilar a extensao usada pelo projeto.

> A documentacao oficial informa Python 3.10 a 3.13. Python 3.14+ ainda nao e o caminho ideal para este projeto.

## Organizacao de pastas

### Se usar Windows nativo

Use uma pasta simples, sem acento e sem espaco no caminho:

```powershell
mkdir C:\Projetos
cd C:\Projetos
```

Se for clonar o projeto:

```powershell
cd C:\Projetos
git clone https://github.com/open-jarvis/OpenJarvis.git
cd OpenJarvis
```

### Se usar WSL2 + Ubuntu

No WSL2, trabalhe dentro da home do Linux:

```bash
cd ~
mkdir -p projetos
cd ~/projetos
```

Clone ou rode o projeto dentro de:

```text
~/projetos/OpenJarvis
```

Evite rodar o ambiente Python dentro de:

```text
/mnt/c/Users/seu_usuario/OpenJarvis
```

O WSL2 acessa o disco do Windows por `/mnt/c`, mas ambientes Python com `.venv` podem dar problema de permissao, lentidao ou travamento quando ficam ali.

## Instalacao nativa no Windows

A pagina inicial do README oficial mostra o instalador nativo Windows com PowerShell.

Abra o **PowerShell como Administrador** e rode:

```powershell
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex
```

Depois feche e abra o terminal novamente.

Teste:

```powershell
jarvis --version
jarvis doctor
```

Para iniciar uma conversa simples:

```powershell
jarvis chat
```

Para fazer uma pergunta pelo terminal:

```powershell
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
```

Para subir o servidor local:

```powershell
jarvis serve --port 8000
```

Depois abra no navegador:

```text
http://localhost:8000
```

## Instalacao no Windows usando WSL2 + Ubuntu

Este caminho usa Linux dentro do Windows. Ele costuma ser mais previsivel para projetos Python, Rust e Node.

### Instalar o WSL2

Abra o **PowerShell como Administrador**:

```powershell
wsl --install
```

Reinicie o Windows se ele pedir.

Abra o **Ubuntu** pelo menu iniciar e finalize a criacao do usuario e senha.

### Atualizar o Ubuntu

No terminal do Ubuntu:

```bash
sudo apt update
sudo apt upgrade -y
```

### Instalar dependencias basicas

```bash
sudo apt install -y curl git build-essential ca-certificates
```

### Criar pasta de trabalho

```bash
cd ~
mkdir -p projetos
cd ~/projetos
```

### Instalar pelo script oficial Linux/macOS/WSL2

```bash
curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash
```

Feche e abra o terminal Ubuntu novamente, ou recarregue o shell:

```bash
source ~/.bashrc
```

Teste:

```bash
jarvis --version
jarvis doctor
```

## Instalacao manual pelo codigo-fonte no WSL2

Use esta opcao se quiser clonar o projeto e controlar cada etapa.

```bash
cd ~/projetos
git clone https://github.com/open-jarvis/OpenJarvis.git
cd OpenJarvis
```

Instale o `uv`, se ainda nao existir:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
uv --version
```

Instale Rust, se ainda nao existir:

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

Instale dependencias do frontend:

```bash
cd frontend
npm install
cd ..
```

## Backend de inferencia: Ollama

O OpenJarvis precisa de pelo menos um backend de inferencia. O caminho mais simples para comecar e o Ollama.

### No Windows nativo

Instale pelo site oficial:

```text
https://ollama.com
```

Depois teste no PowerShell:

```powershell
ollama --version
ollama pull qwen3:0.6b
ollama list
```

### No WSL2 + Ubuntu

Se for usar Ollama dentro do WSL2:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama serve
```

Em outro terminal Ubuntu:

```bash
ollama pull qwen3:0.6b
ollama list
```

> Se voce ja usa Ollama no Windows, ele pode estar rodando fora do WSL2. Para um teste simples, escolha um lado: Windows nativo ou WSL2. Misturar os dois pode confundir portas, modelos e servicos.

## Como iniciar o OpenJarvis

### CLI simples

```bash
jarvis ask "O que e o OpenJarvis?"
```

```bash
jarvis chat
```

### Servidor local

```bash
jarvis serve --port 8000
```

Depois abra:

```text
http://localhost:8000
```

### Frontend web local pelo codigo-fonte

Se voce instalou manualmente pelo repositorio e quer rodar o frontend separado:

Terminal 1, dentro da pasta do projeto:

```bash
cd ~/projetos/OpenJarvis
uv run jarvis serve --port 8000
```

Terminal 2:

```bash
cd ~/projetos/OpenJarvis/frontend
npm run dev
```

Depois abra:

```text
http://localhost:5173
```

## Como usar o app desktop do Windows

O app desktop e uma janela nativa para a interface do OpenJarvis. A documentacao oficial informa que ele se conecta automaticamente ao backend local em:

```text
http://localhost:8000
```

Primeiro, suba o backend:

```bash
jarvis serve --port 8000
```

Depois baixe o instalador do Windows na pagina oficial de releases:

```text
https://github.com/open-jarvis/OpenJarvis/releases
```

Procure pelo arquivo Windows 64-bit, por exemplo:

```text
OpenJarvis-setup.exe
```

Instale e abra o app.

Se o app nao conectar, confira se o backend ainda esta rodando e se a porta e `8000`.

## Comandos uteis

Ver versao:

```bash
jarvis --version
```

Diagnostico:

```bash
jarvis doctor
```

Listar modelos detectados:

```bash
jarvis model list
```

Pergunta simples:

```bash
jarvis ask "What is the capital of France?"
```

Pergunta com agente e ferramenta:

```bash
jarvis ask --agent orchestrator --tools calculator "What is 137 * 42?"
```

Servidor local:

```bash
jarvis serve --port 8000
```

Chat no terminal:

```bash
jarvis chat
```

## Como parar

Se o `jarvis serve` estiver rodando no terminal, pressione:

```text
Ctrl + C
```

Se o frontend estiver rodando com `npm run dev`, pressione tambem:

```text
Ctrl + C
```

Para parar o Ollama no terminal Linux, use:

```text
Ctrl + C
```

## Como atualizar

### Instalacao por script

Rode novamente o instalador oficial do caminho usado.

Windows nativo:

```powershell
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex
```

WSL2/Linux:

```bash
curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash
```

### Instalacao por clone do repositorio

Dentro da pasta do projeto:

```bash
cd ~/projetos/OpenJarvis
git pull
uv sync --extra desktop
uv run maturin develop -m rust/crates/openjarvis-python/Cargo.toml
```

Se usa frontend:

```bash
cd frontend
npm install
cd ..
```

## Como remover um checkout manual

Se voce clonou o projeto dentro do WSL2:

```bash
cd ~
rm -rf ~/projetos/OpenJarvis
```

Se quer apagar uma `.venv` antiga:

```bash
cd ~/projetos/OpenJarvis
rm -rf .venv
```

> Nao apague pastas do sistema sem conferir o caminho atual com `pwd`.

## Erros comuns e ajustes

### PowerShell tentou abrir `quickstart.sh` como aplicativo

**O que aconteceu:**

O arquivo `.sh` foi executado no Windows/PowerShell.

**Por que acontece:**

Scripts `.sh` sao scripts de shell Linux/macOS. No Windows puro, eles podem abrir uma janela perguntando qual aplicativo deve executar o arquivo.

**Correcao:**

Use o instalador nativo Windows:

```powershell
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex
```

Ou execute o script Linux dentro do Ubuntu/WSL2:

```bash
curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash
```

### WSL diz que nao ha distribuicao instalada

**O que aconteceu:**

O Windows tem WSL, mas ainda nao tem Ubuntu configurado.

**Correcao:**

```powershell
wsl --install
```

Para listar distribuicoes disponiveis:

```powershell
wsl --list --online
```

Para instalar Ubuntu explicitamente:

```powershell
wsl --install -d Ubuntu
```

### Erro de permissao ou travamento em `.venv` dentro de `/mnt/c`

**Exemplo:**

```text
failed to remove file 'C:\Users\seu_usuario\OpenJarvis\.venv\lib64': Acesso negado
```

**Por que acontece:**

O projeto foi rodado dentro do disco do Windows pelo caminho `/mnt/c/...`.

**Correcao:**

Copie ou clone o projeto para dentro da home do Linux:

```bash
cd ~
mkdir -p projetos
cd ~/projetos
git clone https://github.com/open-jarvis/OpenJarvis.git
cd OpenJarvis
uv sync --extra desktop
```

Se voce ja copiou uma pasta antiga:

```bash
cd ~/projetos/OpenJarvis
rm -rf .venv
uv sync --extra desktop
```

### `jarvis serve` nao sobe

**Possivel causa:**

Dependencias do servidor nao foram instaladas.

**Correcao no clone manual:**

```bash
cd ~/projetos/OpenJarvis
uv sync --extra server
uv run jarvis serve --port 8000
```

**Correcao se instalou por script e existe uma pasta fonte em `~/.openjarvis/src`:**

```bash
cd ~/.openjarvis/src
uv sync --extra server
uv run jarvis serve --port 8000
```

Se `uv` nao existir:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
```

### `ollama` nao encontrado

**Correcao no Windows:**

Instale pelo site oficial:

```text
https://ollama.com
```

Feche e abra o terminal novamente.

**Correcao no WSL2:**

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Porta 8000 ocupada

**O que aconteceu:**

Outro processo ja esta usando a porta `8000`.

**Teste outra porta:**

```bash
jarvis serve --port 8010
```

Depois abra:

```text
http://localhost:8010
```

### Python 3.14 ou superior dando problema

A documentacao oficial indica Python 3.10 a 3.13.

Confira a versao:

```bash
python --version
```

Se estiver usando Python 3.14+, instale Python 3.13 ou use um ambiente com Python 3.10 a 3.13.

## Resumo copy-paste: Windows nativo

PowerShell como Administrador:

```powershell
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex
```

Novo terminal:

```powershell
jarvis --version
jarvis doctor
jarvis chat
```

Servidor:

```powershell
jarvis serve --port 8000
```

Abra:

```text
http://localhost:8000
```

## Resumo copy-paste: WSL2 + Ubuntu

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

Rodar:

```bash
jarvis chat
```

Servidor:

```bash
jarvis serve --port 8000
```

Abra no Windows:

```text
http://localhost:8000
```

## Resumo copy-paste: clone manual no WSL2

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y curl git build-essential ca-certificates
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source ~/.cargo/env
cd ~
mkdir -p projetos
cd ~/projetos
git clone https://github.com/open-jarvis/OpenJarvis.git
cd OpenJarvis
uv sync --extra desktop
uv run maturin develop -m rust/crates/openjarvis-python/Cargo.toml
cd frontend
npm install
cd ..
uv run jarvis serve --port 8000
```

Em outro terminal:

```bash
cd ~/projetos/OpenJarvis/frontend
npm run dev
```

Abra:

```text
http://localhost:5173
```

## O que ficou pendente validar no teste real

- Se o instalador nativo Windows instala todos os requisitos sem ajuste manual.
- Se o `jarvis serve` sobe direto depois do instalador nativo.
- Se o app desktop Windows conecta automaticamente ao backend em WSL2 ou somente ao backend nativo Windows.
- Se o Ollama do Windows e detectado corretamente quando o OpenJarvis roda dentro do WSL2.

## Veredito pratico

Para video didatico, o melhor e nao misturar tudo ao mesmo tempo.

Use um caminho por vez:

```text
Windows nativo -> instalador PowerShell -> jarvis serve
```

ou:

```text
WSL2 + Ubuntu -> install.sh -> jarvis serve -> navegador/app desktop
```

Se der erro com `.venv`, permissao ou arquivos travando, mova o projeto para dentro da home do Linux:

```text
~/projetos/OpenJarvis
```

E evite rodar o projeto em:

```text
/mnt/c/Users/seu_usuario/OpenJarvis
```
