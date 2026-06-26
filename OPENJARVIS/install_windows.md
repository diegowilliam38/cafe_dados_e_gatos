# OpenJarvis no Windows: WSL2 + browser + Desktop App

Guia pratico para instalar e testar o **OpenJarvis no Windows** usando o fluxo hibrido:

```text
WSL2 + Ubuntu -> API/backend do OpenJarvis -> frontend no browser do Windows -> Desktop App no Windows
```

Este fluxo e bom para video porque separa bem as partes:

- o **backend/API** roda dentro do WSL2/Ubuntu na porta `8000`;
- o **frontend web** roda separado, pela pasta `frontend`, na porta `5173`;
- o **browser do Windows** abre a interface em `http://localhost:5173`;
- o **Desktop App** e baixado depois, pelo GitHub Releases;
- o Desktop App tambem depende do backend/API funcionando.

> Ponto importante: `jarvis serve` sobe apenas a API em `8000`. Ele nao sobe a tela web do browser. Para usar no navegador, rode tambem o frontend com `npm run dev`.

## Fontes oficiais consultadas

- Repositorio oficial: https://github.com/open-jarvis/OpenJarvis
- Documentacao oficial: https://open-jarvis.github.io/OpenJarvis/
- Instalacao oficial: https://open-jarvis.github.io/OpenJarvis/getting-started/install/
- Releases do Desktop App: https://github.com/open-jarvis/OpenJarvis/releases/latest
- Ollama: https://ollama.com
- uv: https://docs.astral.sh/uv/

## O que sera testado

| Forma de uso | Onde aparece | Porta | Precisa do backend? |
| --- | --- | --- | --- |
| Terminal | Ubuntu/WSL2 | nao usa browser | Sim |
| REST API server | Ubuntu/WSL2 | `8000` | Sim |
| Browser | Navegador do Windows | `5173` | Sim |
| Desktop App | Aplicativo instalado no Windows | app | Sim |

O ponto principal:

```text
http://localhost:8000 = REST API server / backend
http://localhost:5173 = interface web/browser
```

Se abrir `http://localhost:8000` e aparecer `404 Not Found`, isso nao significa que esta quebrado. A API pode estar viva mesmo assim. A interface visual fica no `5173`.

## Checklist do `jarvis doctor`

Depois da instalacao, rode:

```bash
jarvis doctor
```

O objetivo nao e zerar todos os warnings. Alguns itens sao opcionais ou nao fazem sentido no Windows/WSL. O foco para este video e deixar funcionando:

| Item no doctor | Vale instalar agora? | Para que serve | Comando principal |
| --- | --- | --- | --- |
| `Engine: ollama` | Sim | Motor local para rodar modelo | Instalador oficial ja costuma preparar |
| `Models: ollama` | Sim | Modelo local usado pelo Jarvis | `ollama pull qwen3.5:2b` ou outro modelo |
| `Optional: REST API server` | Sim | Backend/API usado pelo browser e Desktop App | `uv sync --extra server` |
| `Speech backend` | Sim | Voz/transcricao com faster-whisper | `uv sync --extra desktop` |
| `Node.js` | Sim | Frontend web, ClaudeCodeAgent e WhatsApp/Baileys | instalar Node 22+ |
| `Security profile` | Sim | Perfil de seguranca local | adicionar `security.profile = "personal"` no config |
| `Rust extension` | Sim, se falhar | Melhor desempenho/extensao Rust | scripts sugeridos pelo doctor |
| `NVIDIA energy monitoring` | Opcional | Monitoramento de energia da GPU NVIDIA | ja pode aparecer instalado |
| `ColBERT memory backend` | Depois | Memoria semantica mais avancada | instalar depois, se for usar memoria |
| `SFT/GRPO training` | Nao agora | Treinamento/fine-tuning | nao precisa para teste |
| `AMD energy monitoring` | Nao agora | Monitoramento AMD | nao precisa se nao for AMD |
| `Apple Silicon energy monitoring` | Nao | Recurso de Mac Apple Silicon | nao serve para Windows/WSL |

## Instalar os itens que valem a pena

Execute estes comandos dentro da pasta real do projeto:

```bash
cd ~/.openjarvis/src
uv sync --extra server --extra desktop
```

Isso instala dois pontos importantes:

```text
REST API server
Speech backend / faster-whisper
```

Depois instale o Node.js 22+:

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
node -v
npm -v
```

Para configurar o perfil de seguranca, abra o arquivo:

```bash
nano ~/.openjarvis/config.toml
```

Adicione ou ajuste esta linha:

```toml
security.profile = "personal"
```

Salve com `Ctrl + O`, confirme com `Enter` e saia com `Ctrl + X`.

Depois rode novamente:

```bash
jarvis doctor
```

Se o doctor ainda mostrar warnings em coisas como `ColBERT`, `AMD energy monitoring`, `Apple Silicon energy monitoring` ou `SFT/GRPO training`, tudo bem. Esses nao sao obrigatorios para testar browser e Desktop App.

## Onde o instalador oficial coloca os arquivos

Pela instalacao oficial, o OpenJarvis fica assim:

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

significa que voce rodou `uv sync` na pasta errada.

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
Backend/API: OpenJarvis no WSL2
Frontend web: browser do Windows
Desktop App: Windows
Modelo usado: qwen3.5:2b / outro
Data do teste:
```

---

# Instalacao hibrida: WSL2 + browser + Desktop App

## 1. Instalar o WSL2

Abra o **PowerShell como Administrador** e rode:

```powershell
wsl --install
```

Se o Windows pedir, reinicie a maquina.

Depois abra o **Ubuntu** pelo menu iniciar e finalize a criacao do usuario e senha.

## 2. Atualizar o Ubuntu

No terminal do Ubuntu:

```bash
sudo apt update
sudo apt upgrade -y
```

## 3. Instalar dependencias basicas

```bash
sudo apt install -y curl git build-essential ca-certificates
```

## 4. Instalar Node.js

O frontend do OpenJarvis usa Node. O `package.json` pede Node `>=20`, mas o `jarvis doctor` pode recomendar Node 22+ para alguns recursos, como ClaudeCodeAgent e WhatsApp/Baileys.

Primeiro veja sua versao:

```bash
node -v
npm -v
```

Se nao tiver Node, ou se a versao for antiga, instale Node 22 pelo NodeSource:

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
node -v
npm -v
```

## 5. Criar pasta de trabalho no WSL2

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

## 6. Instalar o OpenJarvis pelo instalador oficial

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

## 7. Testar o OpenJarvis no terminal

Teste rapido:

```bash
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
```

Para abrir o chat no terminal:

```bash
jarvis
```

ou:

```bash
jarvis chat
```

Para sair do chat:

```text
/quit
```

ou aperte `Ctrl + C`.

---

# Modo browser: REST API server em 8000 + frontend em 5173

Para usar no browser do Windows, voce precisa de **dois terminais WSL2 abertos**.

## Terminal 1: subir a REST API/backend

```bash
cd ~/.openjarvis/src
uv sync --extra server --extra desktop
uv run jarvis serve --port 8000
```

Deixe esse terminal aberto.

Resultado esperado:

```text
Starting OpenJarvis API server
URL: http://127.0.0.1:8000
Uvicorn running on http://127.0.0.1:8000
```

Se abrir `http://localhost:8000` no browser e aparecer `404 Not Found`, tudo bem. Essa porta e a API, nao a interface visual.

## Terminal 2: subir o frontend web

Abra outro terminal Ubuntu/WSL2 e rode:

```bash
cd ~/.openjarvis/src/frontend
npm install
npm run dev -- --host 0.0.0.0
```

Resultado esperado:

```text
Local:   http://localhost:5173/
Network: http://0.0.0.0:5173/
```

Agora sim abra no browser do Windows:

```text
http://localhost:5173
```

Este e o endereco da interface web.

## Resumo do modo browser

Terminal 1:

```bash
cd ~/.openjarvis/src
uv run jarvis serve --port 8000
```

Terminal 2:

```bash
cd ~/.openjarvis/src/frontend
npm run dev -- --host 0.0.0.0
```

Browser do Windows:

```text
http://localhost:5173
```

---

# Desktop App no Windows

Depois que a REST API estiver funcionando, baixe o Desktop App pela pagina oficial de releases:

```text
https://github.com/open-jarvis/OpenJarvis/releases/latest
```

Na pagina de releases, procure o instalador do Windows. O nome pode variar conforme a versao, mas deve ser algo como:

```text
OpenJarvis-setup.exe
```

ou outro arquivo `.exe` / `.msi` listado nos assets da release.

Instale e abra o Desktop App no Windows.

> O Desktop App precisa que a API/backend continue rodando no terminal WSL2. Se voce fechar o `jarvis serve`, o app pode nao conectar.

## Fluxo correto para usar o Desktop App

Terminal WSL2:

```bash
cd ~/.openjarvis/src
uv run jarvis serve --port 8000
```

Windows:

```text
1. Abra o Desktop App instalado no Windows.
2. Se ele pedir backend/API, use http://localhost:8000.
3. Mantenha o terminal WSL2 aberto enquanto usa o app.
```

---

# Voz, microfone e speech

O `jarvis doctor` pode mostrar:

```text
Speech backend: faster-whisper unavailable
```

Para instalar o suporte de voz/speech:

```bash
cd ~/.openjarvis/src
uv sync --extra desktop
jarvis doctor
```

Se aparecer:

```text
Speech: faster-whisper
```

entao o backend de fala foi instalado.

> Observacao: no WSL2, microfone e audio podem depender do navegador, do Windows e da forma como o projeto implementa STT/TTS. Primeiro faca texto e browser funcionarem. Depois teste voz.

---

# Erros comuns no fluxo hibrido

## `localhost:5173` nao abre

Causa mais comum: o frontend nao esta rodando.

Correcao:

```bash
cd ~/.openjarvis/src/frontend
npm install
npm run dev -- --host 0.0.0.0
```

Depois abra:

```text
http://localhost:5173
```

## `localhost:8000` mostra 404 Not Found

Isso e normal se voce abriu a raiz da API no navegador.

A porta `8000` e o backend/API. A interface visual fica em:

```text
http://localhost:5173
```

## `jarvis serve` abre so a REST API

Isso e esperado.

```bash
jarvis serve
```

ou:

```bash
uv run jarvis serve --port 8000
```

sobe apenas a REST API.

Para browser, suba tambem o frontend:

```bash
cd ~/.openjarvis/src/frontend
npm run dev -- --host 0.0.0.0
```

## `jarvis` abre chat no terminal

Isso e esperado tambem.

```bash
jarvis
```

abre o chat no terminal, nao a interface web.

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

Se o comando global `jarvis serve` continuar reclamando, use:

```bash
cd ~/.openjarvis/src
uv run jarvis serve --port 8000
```

## `Optional: REST API server Not installed`

Se o `jarvis doctor` mostrar:

```text
Optional: REST API server    Not installed (openjarvis)
```

instale o extra do servidor:

```bash
cd ~/.openjarvis/src
uv sync --extra server
jarvis doctor
```

Depois suba a API:

```bash
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
~/.openjarvis
~/projetos
/mnt/c/Users/seu_usuario/OpenJarvis
```

Correcao:

```bash
cd ~/.openjarvis/src
uv sync --extra server
```

## Erro de permissao em `.venv` dentro de `/mnt/c`

Erro comum:

```text
Acesso negado
failed to remove file ... .venv ...
```

Causa comum: projeto rodando dentro do disco do Windows:

```text
/mnt/c/Users/...
```

Correcao: use a instalacao oficial em:

```text
~/.openjarvis/src
```

ou clone o projeto dentro da home do Linux:

```text
~/projetos
```

## Node.js nao encontrado

Erro:

```text
Node.js Not found
```

Correcao:

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
node -v
npm -v
```

## Security profile nao configurado

Se o doctor mostrar:

```text
No security profile set
Recommended: add security.profile = 'personal' to config.toml
```

abra o config:

```bash
nano ~/.openjarvis/config.toml
```

adicione:

```toml
security.profile = "personal"
```

salve e rode:

```bash
jarvis doctor
```

## Rust extension failed

Se o `jarvis doctor` mostrar:

```text
Rust extension: failed
```

rode o comando sugerido pelo proprio doctor, normalmente algo assim:

```bash
~/.openjarvis/.scripts/install-rust.sh
~/.openjarvis/.scripts/build-extension.sh
```

Depois confira:

```bash
jarvis doctor
```

## Porta 8000 ocupada

Teste outra porta:

```bash
cd ~/.openjarvis/src
uv run jarvis serve --port 8010
```

Depois a API ficara em:

```text
http://localhost:8010
```

> Para o Desktop App, prefira usar a porta padrao `8000`, quando possivel.

---

# Resumo copy-paste do fluxo completo

PowerShell como Administrador:

```powershell
wsl --install
```

Ubuntu/WSL2:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y curl git build-essential ca-certificates
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
cd ~
mkdir -p projetos
cd ~/projetos
curl -fsSL https://open-jarvis.github.io/OpenJarvis/install.sh | bash
source ~/.bashrc
jarvis --version
jarvis doctor
jarvis ask "Explique o que e o OpenJarvis em poucas palavras."
```

Preparar componentes principais:

```bash
cd ~/.openjarvis/src
uv sync --extra server --extra desktop
```

Preparar REST API/backend:

```bash
cd ~/.openjarvis/src
uv run jarvis serve --port 8000
```

Em outro terminal, preparar frontend/browser:

```bash
cd ~/.openjarvis/src/frontend
npm install
npm run dev -- --host 0.0.0.0
```

Abrir no browser do Windows:

```text
http://localhost:5173
```

Baixar Desktop App:

```text
https://github.com/open-jarvis/OpenJarvis/releases/latest
```

---

# Veredito pratico

Para o video, o fluxo mais claro e:

```text
1. Instalar no WSL2.
2. Rodar jarvis doctor.
3. Instalar REST API server com uv sync --extra server.
4. Instalar speech/faster-whisper com uv sync --extra desktop.
5. Instalar Node.js 22+.
6. Configurar security.profile = "personal".
7. Testar no terminal com jarvis ask.
8. Subir a REST API com uv run jarvis serve --port 8000.
9. Subir o frontend em outro terminal com npm run dev.
10. Abrir http://localhost:5173 no browser do Windows.
11. Depois baixar e testar o Desktop App.
```

Nao misture com instalacao Windows pura neste video. O modo hibrido ja cobre o que interessa: backend no WSL2, interface no browser e aplicativo desktop no Windows.