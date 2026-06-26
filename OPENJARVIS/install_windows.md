# OpenJarvis no Windows

Passo a passo para instalar o **OpenJarvis diretamente no Windows**, sem WSL2.

> A instalacao nativa no Windows ainda e marcada como avancada pela documentacao oficial do projeto. Antes de rodar o instalador, confira os pre-requisitos.

## Pre-requisitos

- Windows 10 1809 ou superior, ou Windows 11
- Python 3.10 ate 3.13 no PATH
- Git no PATH
- Aproximadamente 5 GB livres em `%LOCALAPPDATA%`
- PowerShell
- Internet ativa

## Instalar pre-requisitos com winget

Abra o **PowerShell como Administrador** e rode:

```powershell
winget install Python.Python.3.13
winget install Git.Git
winget install Ollama.Ollama
```

Feche o PowerShell e abra novamente.

## Verificar pre-requisitos

```powershell
python --version
git --version
ollama --version
winget --version
```

O Python precisa estar entre 3.10 e 3.13.

> Evite Python 3.14 por enquanto. A documentacao oficial informa que o OpenJarvis usa Python 3.10 a 3.13 no Windows.

## Instalar o OpenJarvis

No PowerShell, rode:

```powershell
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex
```

O instalador deve:

- verificar Windows;
- verificar Python;
- verificar Git;
- instalar `uv`, se estiver ausente;
- clonar o OpenJarvis em `%LOCALAPPDATA%\OpenJarvis\src`;
- rodar `uv sync --extra desktop`.

Quando terminar, feche o PowerShell e abra novamente.

## Verificar a instalacao

```powershell
jarvis --version
jarvis doctor
```

Se `jarvis` nao for reconhecido, rode pelo caminho direto:

```powershell
& "$env:LOCALAPPDATA\OpenJarvis\bin\jarvis.cmd" doctor
```

## Baixar modelo no Ollama

```powershell
ollama pull qwen3.5:2b
ollama list
```

## Testar no terminal

```powershell
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
```

Para abrir o chat no terminal:

```powershell
jarvis chat
```

## Iniciar o servidor local

A documentacao oficial do Windows nativo manda rodar o servidor dentro da pasta do projeto:

```powershell
cd "$env:LOCALAPPDATA\OpenJarvis\src"
uv run jarvis serve
```

A API local fica em:

```text
http://127.0.0.1:8000/health
```

Deixe esse PowerShell aberto.

## Baixar o Desktop App

Pagina de releases:

```text
https://github.com/open-jarvis/OpenJarvis/releases/latest
```

Download direto Windows 64-bit:

```text
https://github.com/open-jarvis/OpenJarvis/releases/download/desktop-v1.0.2/OpenJarvis_1.0.1_x64-setup.exe
```

Instale e abra o Desktop App.

O servidor local precisa continuar rodando no PowerShell.

## Resumo rapido

```powershell
winget install Python.Python.3.13
winget install Git.Git
winget install Ollama.Ollama
```

Feche e abra o PowerShell.

```powershell
python --version
git --version
ollama --version
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex
```

Feche e abra o PowerShell novamente.

```powershell
jarvis doctor
ollama pull qwen3.5:2b
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
cd "$env:LOCALAPPDATA\OpenJarvis\src"
uv run jarvis serve
```

Depois instale o Desktop App:

```text
https://github.com/open-jarvis/OpenJarvis/releases/latest
```
