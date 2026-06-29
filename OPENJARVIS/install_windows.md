# OpenJarvis no Windows

Passo a passo para instalar o **OpenJarvis diretamente no Windows**, sem WSL2.

> A instalacao nativa no Windows ainda e marcada como avancada pela documentacao oficial do projeto. Antes de rodar o instalador, confira os pre-requisitos e valide se o Python esta corretamente acessivel pelo terminal.

## Fluxo geral

A ordem recomendada e:

1. instalar os pre-requisitos;
2. verificar Python, `python3` e PATH;
3. corrigir aliases da Microsoft Store, se necessario;
4. instalar o OpenJarvis;
5. inicializar e configurar o `config.toml`;
6. baixar um modelo no Ollama;
7. testar no terminal;
8. iniciar o servidor local/backend;
9. subir a interface web/frontend, se quiser usar pelo navegador;
10. instalar o Desktop App, se quiser usar o app.

## Resumo rapido

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
winget install Python.Python.3.12
winget install Git.Git
winget install OpenJS.NodeJS.LTS
irm https://ollama.com/install.ps1 | iex
```

Feche e abra o PowerShell.

```powershell
python --version
python3 --version
py -3.12 --version
where.exe python
where.exe python3
git --version
ollama --version
uv --version
node --version
npm --version
```

Se `python3` chamar a Microsoft Store, corrija os aliases do Windows:

```powershell
start ms-settings:apps-advanced-app-settings
```

Depois instale:

```powershell
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex
```

Feche e abra o PowerShell novamente.

```powershell
jarvis init
notepad $HOME\.openjarvis\config.toml
jarvis doctor
ollama pull qwen3.5:0.8b
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
cd "$env:LOCALAPPDATA\OpenJarvis\src"
uv run jarvis serve
```

Em outro PowerShell, para abrir a interface web:

```powershell
cd "$env:LOCALAPPDATA\OpenJarvis\src\frontend"
npm install
npm run dev
```

Depois instale o Desktop App:

```text
https://github.com/open-jarvis/OpenJarvis/releases/latest
```

## Pre-requisitos

- Windows 10 1809 ou superior, ou Windows 11
- Python 3.10 a 3.13
- Git no PATH
- uv
- Ollama instalado
- Node.js e npm, caso queira subir a interface web/frontend pelo navegador
- Aproximadamente 5 GB livres em `%LOCALAPPDATA%`
- PowerShell
- Internet ativa

> Nos testes em Windows, o instalador do OpenJarvis pode chamar `python3.exe`. Mesmo com Python instalado, o Windows pode apontar `python3.exe` para o alias da Microsoft Store. Por isso, a verificacao do Python e importante antes de instalar.

## Instalar pre-requisitos com winget

Abra o **PowerShell como Administrador** e rode:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
winget install Python.Python.3.12
winget install Git.Git
winget install OpenJS.NodeJS.LTS
irm https://ollama.com/install.ps1 | iex
```

Feche o PowerShell e abra novamente.

## Verificar Python, python3 e PATH

Rode:

```powershell
python --version
python3 --version
py -3.12 --version
py -0p
where.exe python
where.exe python3
```

O esperado e que `python --version` e `python3 --version` mostrem Python 3.12.x, ou outra versao entre 3.10 e 3.13.

Exemplo esperado:

```text
Python 3.12.10
```

Se `py -3.12 --version` funciona, mas `python` ou `python3` mostram a mensagem da Microsoft Store, o Python esta instalado, mas o alias do Windows esta atrapalhando.

Mensagem comum do erro:

```text
Python nao foi encontrado; executar sem argumentos para instalar do Microsoft Store ou desabilitar este atalho em Configuracoes > Aplicativos > Configuracoes avancadas do aplicativo > Aliases de execucao do aplicativo.
```

## Corrigir alias do Python da Microsoft Store

Abra a tela de aliases do Windows:

```powershell
start ms-settings:apps-advanced-app-settings
```

Em **Aliases de execucao do aplicativo**, desative os aliases da Microsoft Store/App Installer para:

```text
python.exe
python3.exe
```

Feche o PowerShell e abra novamente.

Teste outra vez:

```powershell
python --version
python3 --version
where.exe python
where.exe python3
```

## Colocar Python 3.12 no PATH, se necessario

Se `py -3.12 --version` funciona, mas `python --version` nao funciona, adicione o Python 3.12 ao PATH do usuario:

```powershell
$pythonDir = "C:\Users\denis\AppData\Local\Programs\Python\Python312"
$scriptsDir = "$pythonDir\Scripts"

[Environment]::SetEnvironmentVariable(
  "Path",
  [Environment]::GetEnvironmentVariable("Path", "User") + ";$pythonDir;$scriptsDir",
  "User"
)
```

Feche o PowerShell e abra novamente.

Teste:

```powershell
python --version
where.exe python
```

## Criar `python3.exe`, se necessario

Se `python --version` funciona, mas `python3 --version` ainda chama a Microsoft Store, crie uma copia do executavel como `python3.exe`:

```powershell
Copy-Item "C:\Users\denis\AppData\Local\Programs\Python\Python312\python.exe" "C:\Users\denis\AppData\Local\Programs\Python\Python312\python3.exe"
```

Feche o PowerShell e abra novamente.

Teste:

```powershell
where.exe python3
python3 --version
```

O caminho correto deve aparecer antes do caminho da Microsoft Store:

```text
C:\Users\denis\AppData\Local\Programs\Python\Python312\python3.exe
C:\Users\denis\AppData\Local\Microsoft\WindowsApps\python3.exe
```

Se `python3 --version` mostrar Python 3.12.x, pode continuar.

## Verificar pre-requisitos

```powershell
python --version
python3 --version
git --version
ollama --version
winget --version
uv --version
node --version
npm --version
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

## Inicializar configuracao

Se o `jarvis doctor` mostrar que nao existe arquivo de configuracao:

```text
Config file Not found at C:\Users\denis\.openjarvis\config.toml
Run `jarvis init` to generate a config file.
```

Rode:

```powershell
jarvis init
```

Se a configuracao ja existir, ele mostrara:

```text
Config already exists at C:\Users\denis\.openjarvis\config.toml
Use --force to overwrite.
```

Nesse caso, nao precisa rodar de novo, a menos que queira sobrescrever tudo.

## Configurar Ollama no OpenJarvis

Abra o arquivo de configuracao:

```powershell
notepad $HOME\.openjarvis\config.toml
```

Para usar Ollama local com um modelo leve, deixe assim:

```toml
# OpenJarvis configuration

[engine]
default = "ollama"

[engine.ollama]
host = "http://127.0.0.1:11434"

[intelligence]
default_model = "qwen3.5:0.8b"

[agent]
default_agent = "simple"

[tools]
enabled = [
  "code_interpreter",
  "web_search",
  "file_read",
  "shell_exec",
]
```

Importante: a linha do `host` nao pode estar comentada. Ou seja, nao deixe assim:

```toml
# host = "http://localhost:11434"
```

Ela precisa ficar ativa, sem `#`:

```toml
host = "http://127.0.0.1:11434"
```

Se essa linha ficar comentada, pode aparecer erro como:

```text
httpx.UnsupportedProtocol: Request URL is missing an 'http://' or 'https://' protocol.
```

## Baixar modelo no Ollama

Para maquina com pouca VRAM, como uma GTX 960 de 2 GB, prefira um modelo pequeno:

```powershell
ollama pull qwen3.5:0.8b
ollama list
```

Opcionalmente, para testar um pouco mais de capacidade:

```powershell
ollama pull qwen3.5:2b
ollama list
```

Teste o modelo diretamente no Ollama:

```powershell
ollama run qwen3.5:0.8b
```

Se o modelo responder no Ollama, mas o OpenJarvis falhar, o problema provavelmente esta no `config.toml` ou na comunicacao com o endpoint do Ollama.

## Testar se o Ollama esta acessivel

```powershell
ollama ps
Invoke-WebRequest http://127.0.0.1:11434/api/tags
```

Se o Ollama nao estiver ativo, abra outra janela do PowerShell e rode:

```powershell
ollama serve
```

Deixe essa janela aberta.

## Testar no terminal

```powershell
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
```

Para abrir o chat no terminal:

```powershell
jarvis chat
```

Se aparecer:

```text
No inference engine available.
```

Confira:

```powershell
notepad $HOME\.openjarvis\config.toml
ollama list
ollama ps
Invoke-WebRequest http://127.0.0.1:11434/api/tags
jarvis doctor
```

## Iniciar o servidor local/backend

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

> Importante: no Windows nativo, `uv run jarvis serve` sobe apenas o backend/API. Ele nao abre automaticamente a interface no navegador. No Linux/WSL, o quickstart pode subir tudo junto, mas no Windows nativo a API e o frontend podem precisar ser iniciados separadamente.

## Subir a interface web/frontend no navegador

Se voce quiser usar a interface web pelo navegador, abra **outro PowerShell** e rode:

```powershell
cd "$env:LOCALAPPDATA\OpenJarvis\src\frontend"
npm install
npm run dev
```

Se voce clonou o repositorio manualmente em `C:\Users\denis\OpenJarvis`, use:

```powershell
cd C:\Users\denis\OpenJarvis\frontend
npm install
npm run dev
```

O frontend normalmente fica em:

```text
http://localhost:5173
```

Se aparecer o erro:

```text
'vite' nao e reconhecido como um comando interno ou externo, um programa operavel ou um arquivo em lotes.
```

rode primeiro:

```powershell
npm install
```

Depois tente novamente:

```powershell
npm run dev
```

Resumo:

```text
Backend/API: http://127.0.0.1:8000
Frontend/Web UI: http://localhost:5173
```

## Baixar o Desktop App

Pagina de releases:

```text
https://github.com/open-jarvis/OpenJarvis/releases/latest
```

Download direto Windows 64-bit:

```text
https://github.com/open-jarvis/OpenJarvis/releases/download/desktop-edge/OpenJarvis_1.0.1_x64-setup.exe
```

Instale e abra o Desktop App.

O servidor local precisa continuar rodando no PowerShell.

## Criar um atalho para iniciar o Jarvis Server

Se voce nao quiser digitar o caminho toda vez, crie um arquivo chamado:

```text
iniciar_jarvis_server.bat
```

Conteudo para instalacao oficial em `%LOCALAPPDATA%`:

```bat
@echo off
cd /d "%LOCALAPPDATA%\OpenJarvis\src"
uv run jarvis serve
pause
```

Conteudo para repositorio clonado manualmente em `C:\Users\denis\OpenJarvis`:

```bat
@echo off
cd /d "C:\Users\denis\OpenJarvis"
uv run jarvis serve
pause
```

Para descobrir a pasta certa, procure o arquivo `pyproject.toml`:

```powershell
Get-ChildItem -Path C:\Users\denis -Filter pyproject.toml -Recurse -ErrorAction SilentlyContinue
```

A pasta correta e aquela onde aparece o `pyproject.toml` do OpenJarvis, por exemplo:

```text
C:\Users\denis\OpenJarvis\pyproject.toml
```

Nesse caso, a pasta do projeto e:

```text
C:\Users\denis\OpenJarvis
```

## Atualizar o OpenJarvis

O `jarvis doctor` pode mostrar algo assim:

```text
A new version of OpenJarvis is available
Update: cd C:\Users\denis\AppData\Local\OpenJarvis\src && git pull && uv sync
Or run: jarvis self-update
```

Se estiver usando PowerShell antigo, ele pode nao aceitar `&&` e mostrar erro como:

```text
O token '&&' nao e um separador de instrucoes valido nesta versao.
```

Nesse caso, rode os comandos linha por linha:

```powershell
cd C:\Users\denis\AppData\Local\OpenJarvis\src
git pull
uv sync
```

Ou use `;` no lugar de `&&`:

```powershell
cd C:\Users\denis\AppData\Local\OpenJarvis\src; git pull; uv sync
```

Tambem e possivel tentar:

```powershell
jarvis self-update
```

Se ele perguntar:

```text
Run the upgrade command now? [Y/n]:
```

Digite `Y` e pressione Enter **enquanto a pergunta estiver aparecendo**. Se digitar `Y` depois que o comando ja terminou, o PowerShell tentara executar `Y` como se fosse um comando e mostrara erro.

## Remover e reinstalar o OpenJarvis

Se a instalacao ficar quebrada ou parcial, remova apenas o OpenJarvis. Isso nao apaga os modelos do Ollama.

```powershell
taskkill /IM jarvis.exe /F
taskkill /IM python.exe /F
Remove-Item -Recurse -Force "$env:LOCALAPPDATA\OpenJarvis"
Remove-Item -Recurse -Force "$env:USERPROFILE\.openjarvis"
```

Pode aparecer erro dizendo que algum processo nao foi encontrado. Tudo bem.

Feche o PowerShell e abra novamente.

Teste se o comando saiu do sistema:

```powershell
where.exe jarvis
jarvis
```

O esperado e o Windows dizer que `jarvis` nao foi reconhecido.

Depois instale novamente:

```powershell
irm https://open-jarvis.github.io/OpenJarvis/install.ps1 | iex
```
