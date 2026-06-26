# OpenJarvis no Windows: modo hibrido com WSL2, browser e Desktop App

Guia pratico para instalar e testar o **OpenJarvis no Windows** usando o fluxo hibrido:

```text
WSL2 + Ubuntu -> backend do OpenJarvis -> browser no Windows -> Desktop App no Windows
```

Este e o fluxo mais didatico para o video, porque separa bem as partes:

- o **backend** roda dentro do WSL2/Ubuntu;
- o **browser** abre no Windows em `http://localhost:8000`;
- o **Desktop App** e baixado e instalado no Windows;
- o Desktop App tambem precisa que o backend esteja rodando.

> Nao rode `uv sync --extra server` em qualquer pasta. Ele precisa ser executado dentro da pasta do projeto, onde existe o arquivo `pyproject.toml`.

## Fontes oficiais consultadas

- Repositorio oficial: https://github.com/open-jarvis/OpenJarvis
- Documentacao oficial: https://open-jarvis.github.io/OpenJarvis/
- Instalacao oficial: https://open-jarvis.github.io/OpenJarvis/getting-started/installation/
- Releases do Desktop App: https://github.com/open-jarvis/OpenJarvis/releases/latest
- Ollama: https://ollama.com
- uv: https://docs.astral.sh/uv/

## O que sera testado

Neste guia vamos testar tres formas de uso:

| Forma de uso | Onde aparece | Precisa do backend? |
| --- | --- | --- |
| Terminal | Ubuntu/WSL2 | Sim |
| Browser | Navegador do Windows | Sim |
| Desktop App | Aplicativo instalado no Windows | Sim |

O ponto principal:

```text
O Desktop App nao substitui o backend.
```

Antes de abrir o browser ou o Desktop App, o backend precisa estar rodando em:

```text
http://localhost:8000
```

## Onde o instalador oficial coloca os arquivos

Pela documentacao oficial, o instalador Linux/WSL2 faz o seguinte:

| Item | Local |
| --- | --- |
| Codigo-fonte do OpenJarvis | `~/.openjarvis/src/` |
| Ambiente Python/venv | `~/.openjarvis/.venv/` |
| Comando `jarvis` | `~/.local/bin/jarvis` |
| Configuracao | `~/.openjarvis/config.toml` |

Por isso, se aparecer este erro:

```text
No pyproject.toml found in current directory or any parent directory
```

significa que voce rodou `uv sync --extra server` na pasta errada.

O comando precisa ser rodado aqui:

```bash
cd ~/.openjarvis/src
```

## Ambiente testado no video

Preencha depois do teste:

```text
Sistema operacional: Windows
Ambiente: WSL2 + Ubuntu
Terminal: Ubuntu no Windows Terminal
Backend: OpenJarvis no WSL2
Interface: browser do Windows e Desktop App do Windows
Modelo usado:
Data do teste:
```

---

# Instalacao hibrida: WSL2 + browser + Desktop App

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

## Instalar dependencias basicas

```bash
sudo apt install -y curl git build-essential ca-certificates
```

## Criar pasta de trabalho no WSL2

```bash
cd ~
mkdir -p projetos
cd ~/projetos
```

Use a home do Linux para seus testes:

```text
~/projetos
```

Evite rodar projeto Python no WSL2 dentro de:

```text
/mnt/c/Users/seu_usuario/...
```

Esse caminho aponta para o disco do Windows e pode gerar erro de permissao, lentidao ou problema com `.venv`.

## Instalar o OpenJarvis pelo instalador oficial

Dentro do Ubuntu/WSL2:

```bash
curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash
```

Depois recarregue o terminal:

```bash
source ~/.bashrc
```

Teste se o comando `jarvis` ficou disponivel:

```bash
jarvis --version
jarvis doctor
```

## Testar o OpenJarvis no terminal

```bash
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
```

Para abrir o chat no terminal:

```bash
jarvis chat
```

## Preparar o modo browser/server

Para abrir o OpenJarvis no navegador, precisa instalar o extra do servidor.

Entre na pasta real do projeto:

```bash
cd ~/.openjarvis/src
```

Instale as dependencias do servidor:

```bash
uv sync --extra server
```

Agora suba o backend:

```bash
uv run jarvis serve --port 8000
```

Deixe esse terminal aberto.

## Abrir no browser do Windows

Com o backend rodando no WSL2, abra no navegador do Windows:

```text
http://localhost:8000
```

Se abrir, o modo browser esta funcionando.

## Baixar o Desktop App do Windows

Depois que o backend estiver funcionando no browser, baixe o Desktop App pela pagina oficial de releases:

```text
https://github.com/open-jarvis/OpenJarvis/releases/latest
```

Na pagina de releases, procure o instalador do Windows. O nome pode variar conforme a versao, mas deve ser algo como:

```text
OpenJarvis-setup.exe
```

ou outro arquivo `.exe` / `.msi` listado nos assets da release.

Baixe, instale e abra o Desktop App.

> O Desktop App precisa que o backend continue rodando no terminal WSL2. Se voce fechar o `jarvis serve`, o app pode nao conectar.

## Fluxo correto para usar o Desktop App

Terminal WSL2:

```bash
cd ~/.openjarvis/src
uv run jarvis serve --port 8000
```

Windows:

```text
1. Abra o browser em http://localhost:8000 para confirmar que o backend esta ativo.
2. Abra o Desktop App instalado no Windows.
3. Mantenha o terminal WSL2 aberto enquanto usa o app.
```

---

# Erros comuns no fluxo hibrido

## `jarvis serve --port` sem numero da porta

Se voce rodar:

```bash
jarvis serve --port
```

vai aparecer:

```text
Error: Option '--port' requires an argument.
```

O correto e passar o numero da porta:

```bash
jarvis serve --port 8000
```

## `Server dependencies not installed`

Erro:

```text
Server dependencies not installed.
Install the server extra:
uv sync --extra server
```

Correcao:

```bash
cd ~/.openjarvis/src
uv sync --extra server
uv run jarvis serve --port 8000
```

## `No pyproject.toml found`

Erro:

```text
No pyproject.toml found in current directory or any parent directory
```

Isso acontece quando voce roda:

```bash
uv sync --extra server
```

em uma pasta qualquer, por exemplo:

```text
~/projetos
```

Correcao:

```bash
cd ~/.openjarvis/src
uv sync --extra server
```

## `which` nao instalado

Se voce tentar:

```bash
which jarvis
```

e aparecer que `which` nao foi encontrado, instale:

```bash
sudo apt install -y debianutils
```

Depois rode:

```bash
which jarvis
```

Alternativa sem instalar nada:

```bash
command -v jarvis
```

## Ver onde esta o comando `jarvis`

```bash
command -v jarvis
```

Normalmente o resultado sera:

```text
/home/seu_usuario/.local/bin/jarvis
```

Esse e apenas o atalho do comando. A pasta do projeto fica em:

```text
~/.openjarvis/src
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

## Desktop App nao conecta

Confira primeiro se o backend esta rodando.

No navegador do Windows, abra:

```text
http://localhost:8000
```

Se o browser nao abrir, o Desktop App tambem nao vai conectar.

Volte ao terminal WSL2 e rode:

```bash
cd ~/.openjarvis/src
uv run jarvis serve --port 8000
```

## Porta 8000 ocupada

Teste outra porta:

```bash
cd ~/.openjarvis/src
uv run jarvis serve --port 8010
```

Depois abra:

```text
http://localhost:8010
```

> Se mudar a porta, o Desktop App pode continuar tentando conectar na porta padrao `8000`. Para o Desktop App, prefira usar `8000` quando possivel.

---

# Resumo copy-paste do fluxo hibrido

PowerShell como Administrador:

```powershell
wsl --install
```

Ubuntu/WSL2:

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
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
```

Preparar browser e Desktop App:

```bash
cd ~/.openjarvis/src
uv sync --extra server
uv run jarvis serve --port 8000
```

Abrir no browser do Windows:

```text
http://localhost:8000
```

Baixar Desktop App:

```text
https://github.com/open-jarvis/OpenJarvis/releases/latest
```

---

# Veredito pratico

Para o video, o fluxo mais claro e:

```text
Instalar no WSL2
Testar no terminal
Entrar em ~/.openjarvis/src
Rodar uv sync --extra server
Subir uv run jarvis serve --port 8000
Abrir http://localhost:8000 no browser do Windows
Baixar o Desktop App no GitHub Releases
Abrir o Desktop App com o backend ainda rodando
```

Nao misture com instalacao Windows pura neste video. O modo hibrido ja cobre o que interessa: backend no WSL2, interface no browser e aplicativo desktop no Windows.
