# OpenJarvis no Windows

Passo a passo para instalar o **OpenJarvis diretamente no Windows**, sem WSL2.

## Instalar o OpenJarvis

Abra o **PowerShell como Administrador** e rode:

```powershell
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex
```

Feche o PowerShell e abra novamente.

## Verificar a instalacao

```powershell
jarvis --version
jarvis doctor
```

## Instalar o Ollama

Baixe e instale o Ollama:

```text
https://ollama.com
```

Feche o PowerShell e abra novamente.

Verifique:

```powershell
ollama --version
```

Baixe um modelo pequeno para testar:

```powershell
ollama pull qwen3.5:2b
```

Veja os modelos instalados:

```powershell
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

```powershell
jarvis serve --port 8000
```

Deixe esse PowerShell aberto.

A API local fica em:

```text
http://localhost:8000
```

## Baixar o Desktop App

Baixe o instalador do Desktop App para Windows:

```text
https://github.com/open-jarvis/OpenJarvis/releases/download/desktop-v1.0.2/OpenJarvis_1.0.1_x64-setup.exe
```

Ou acesse a pagina de releases:

```text
https://github.com/open-jarvis/OpenJarvis/releases/latest
```

Instale e abra o Desktop App.

O servidor local precisa continuar rodando no PowerShell:

```powershell
jarvis serve --port 8000
```

## Resumo rapido

```powershell
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex
```

Feche e abra o PowerShell.

```powershell
jarvis --version
jarvis doctor
ollama pull qwen3.5:2b
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
jarvis serve --port 8000
```

Depois instale o Desktop App:

```text
https://github.com/open-jarvis/OpenJarvis/releases/download/desktop-v1.0.2/OpenJarvis_1.0.1_x64-setup.exe
```
