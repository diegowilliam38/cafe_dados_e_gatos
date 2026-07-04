# Instalacao Linux via Git do OpenJarvis

Este guia documenta a instalacao do OpenJarvis no Linux usando o repositorio oficial via Git.

Objetivo: instalar o OpenJarvis via Git, usar Ollama/local, configurar Google OAuth e speech local com `faster-whisper`.

Este guia nao usa MiniMax.

## Regra principal sobre porta

Nao troque a porta por padrao.

O OpenJarvis Desktop e o comando `jarvis serve` usam o mesmo servico. Se voce subir o backend manualmente e depois abrir o Desktop, o Desktop pode tentar subir/gerenciar o mesmo backend e derrubar o processo anterior.

Por isso, o padrao deste guia e:

```text
Backend/API: http://127.0.0.1:8000
Desktop: usa o mesmo backend/API em http://127.0.0.1:8000
```

A porta 8001 nao resolve esse caso se o Desktop tambem tentar subir o mesmo servico nela. O problema nao e a porta em si; e abrir dois processos tentando gerenciar o mesmo backend.

## Fontes oficiais consultadas

- Instalacao oficial do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/getting-started/installation/
- Configuracao oficial do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/getting-started/configuration/
- API Server do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/deployment/api-server/
- Releases oficiais do OpenJarvis Desktop: https://github.com/open-jarvis/OpenJarvis/releases/latest
- Google Workspace OAuth: https://developers.google.com/workspace/guides/configure-oauth-consent
- Credenciais Google Workspace: https://developers.google.com/workspace/guides/create-credentials

## Pre-requisitos

Confirme que voce tem:

```bash
python3 --version
git --version
node --version
npm --version
uv --version
rustc --version
```

A documentacao oficial pede Python 3.10+, Node.js 18+ e Rust para compilar partes do projeto.

Se o Rust nao estiver instalado, instale pelo metodo oficial:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Depois feche e abra o terminal ou rode:

```bash
source "$HOME/.cargo/env"
```

## Instalacao limpa opcional

Use esta etapa apenas se voce quer apagar uma instalacao anterior e comecar do zero.

```bash
pkill -f jarvis
pkill -f OpenJarvis

rm -rf ~/OpenJarvis
rm -rf ~/OpenJarvis_old_*

rm -rf ~/.openjarvis
rm -rf ~/.config/OpenJarvis
rm -rf ~/.local/share/OpenJarvis
rm -rf ~/.cache/OpenJarvis

rm -rf ~/.config/openjarvis
rm -rf ~/.local/share/openjarvis
rm -rf ~/.cache/openjarvis

rm -rf ~/.config/Jarvis
rm -rf ~/.local/share/Jarvis
rm -rf ~/.cache/Jarvis

rm -rf ~/.local/share/com.openjarvis.desktop
rm -rf ~/.cache/uv
rm -rf ~/.cache/gnome-software/odrs/OpenJarvis.desktop.json

rm -f ~/Downloads/OpenJarvis*.deb
rm -f ~/Downloads/openjarvis*.deb
rm -f ~/Downloads/OpenJarvis_*.AppImage
```

Confira se sobrou algo:

```bash
find ~ -iname "*openjarvis*" 2>/dev/null
```

Arquivos pessoais, como anotacoes `.md` ou `.txt`, podem aparecer no resultado. Apague apenas se tiver certeza.

## Clonar o repositorio

```bash
cd ~
git clone https://github.com/open-jarvis/OpenJarvis.git
cd ~/OpenJarvis
```

Se a pasta ja existir:

```bash
cd ~/OpenJarvis
git pull
```

## Instalar dependencias do backend e Desktop

Use o extra `desktop`, porque ele inclui dependencias necessarias para o app e para speech local.

```bash
cd ~/OpenJarvis
uv sync --extra desktop
```

Depois compile/desenvolva o modulo Rust/Python:

```bash
cd ~/OpenJarvis
uv run maturin develop -m rust/crates/openjarvis-python/Cargo.toml
```

## Instalar dependencias do frontend

```bash
cd ~/OpenJarvis/frontend
npm install
cd ~/OpenJarvis
```

## Baixar e instalar o OpenJarvis Desktop

O repositorio clonado em `~/OpenJarvis` sera usado como base local. O Desktop pode ser instalado separadamente para servir como interface visual.

Baixe o Desktop pela pagina oficial de releases:

```text
https://github.com/open-jarvis/OpenJarvis/releases/latest
```

No Ubuntu/Debian, baixe o arquivo `.deb` disponivel na release.

Exemplo usado na release desktop-v1.0.2:

```text
OpenJarvis_1.0.1_amd64.deb
```

Download direto:

```bash
cd ~/Downloads
wget https://github.com/open-jarvis/OpenJarvis/releases/download/desktop-v1.0.2/OpenJarvis_1.0.1_amd64.deb
```

Instale:

```bash
cd ~/Downloads
sudo apt install ./OpenJarvis_1.0.1_amd64.deb
```

Depois abra o OpenJarvis Desktop pelo menu de aplicativos.

## Configuracao local com Ollama

Este guia usa Ollama como fluxo local principal.

Confirme que o Ollama esta rodando:

```bash
ollama serve
```

Em outro terminal:

```bash
ollama list
```

Se precisar de um modelo pequeno para teste:

```bash
ollama pull qwen3.5:2b
```

Edite a configuracao:

```bash
mkdir -p ~/.openjarvis
nano ~/.openjarvis/config.toml
```

Use um bloco simples:

```toml
[engine]
default = "ollama"

[engine.ollama]
host = "http://127.0.0.1:11434"

[intelligence]
default_model = "qwen3.5:2b"
temperature = 0.7
max_tokens = 2048

[agent]
default_agent = "simple"
```

Teste:

```bash
cd ~/OpenJarvis
uv run jarvis ask "Responda apenas: OpenJarvis funcionando."
```

## Subir backend local no padrao

Use a porta padrao 8000.

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8000
```

Deixe este terminal aberto somente se voce for testar o backend manualmente.

Em outro terminal, teste:

```bash
curl http://127.0.0.1:8000/health
```

Resultado esperado:

```json
{"status":"ok"}
```

## Importante sobre Desktop e backend

Se o backend manual ja estiver rodando na porta 8000 e voce abrir o Desktop, o Desktop pode tentar subir o mesmo servico e derrubar o processo anterior.

Fluxo recomendado:

1. Para testar backend/API, use `uv run jarvis serve --host 127.0.0.1 --port 8000`.
2. Para usar o Desktop, feche o backend manual antes ou deixe o Desktop gerenciar o backend.
3. No Desktop, mantenha a API URL no padrao:

```text
http://127.0.0.1:8000
```

Nao mude para 8001 por padrao.

## Google OAuth

Google OAuth nao e a mesma coisa que `GOOGLE_API_KEY`.

Neste guia, OAuth e usado para autorizar conectores como Drive, Gmail, Calendar, Contacts e Tasks.

### Criar projeto no Google Cloud

Acesse o Google Cloud Console e crie um projeto para o OpenJarvis.

Depois configure a tela de consentimento OAuth:

```text
https://console.cloud.google.com/apis/credentials/consent
```

Para uso pessoal/teste, mantenha o app em modo de teste e adicione sua propria conta Google como usuaria de teste.

### Criar credencial OAuth

Crie uma credencial OAuth Client ID:

```text
APIs & Services > Credentials > Create Credentials > OAuth client ID
```

Baixe o arquivo JSON de credenciais e guarde fora do repositorio publico.

Sugestao local:

```bash
mkdir -p ~/.openjarvis/credentials
mv ~/Downloads/client_secret*.json ~/.openjarvis/credentials/google_client_secret.json
chmod 600 ~/.openjarvis/credentials/google_client_secret.json
```

### Ativar APIs Google

Ative apenas o que voce vai testar:

```text
Google Drive API
Gmail API
Google Calendar API
People API / Contacts
Google Tasks API
```

### Conectar pelo OpenJarvis

A documentacao do OpenJarvis mostra o fluxo com `jarvis connect` para conectores.

Exemplo:

```bash
cd ~/OpenJarvis
uv run jarvis connect gdrive
```

Depois teste outros conectores, se estiverem disponiveis na sua versao:

```bash
cd ~/OpenJarvis
uv run jarvis connect gmail
uv run jarvis connect gcalendar
uv run jarvis connect gcontacts
uv run jarvis connect google_tasks
```

Se algum nome nao existir, liste os comandos disponiveis:

```bash
cd ~/OpenJarvis
uv run jarvis --help
uv run jarvis connect --help
```

Os tokens normalmente ficam em:

```bash
ls -la ~/.openjarvis/connectors
```

Nunca suba estes arquivos para o GitHub.

## Voz e speech-to-text local

Este guia usa `faster-whisper` para speech-to-text local.

O extra `desktop` deve instalar o `faster-whisper`:

```bash
cd ~/OpenJarvis
uv sync --extra desktop
```

Confirme:

```bash
cd ~/OpenJarvis
uv run python - <<'PY'
import importlib.util
print('faster_whisper instalado:', importlib.util.find_spec('faster_whisper') is not None)
PY
```

Resultado esperado:

```text
faster_whisper instalado: True
```

Edite a configuracao:

```bash
nano ~/.openjarvis/config.toml
```

Adicione:

```toml
[speech]
backend = "faster-whisper"
model = "tiny"
device = "auto"
compute_type = "int8"
language = "pt"
```

Para melhor qualidade, depois de validar com `tiny`, voce pode testar:

```toml
[speech]
backend = "faster-whisper"
model = "base"
device = "auto"
compute_type = "int8"
language = "pt"
```

## Testar microfone

Se o microfone ja funciona no sistema, nao troque o dispositivo manualmente.

Teste a captura padrao:

```bash
arecord -d 5 teste_microfone.wav
aplay teste_microfone.wav
```

Se gravou sua voz, o Linux esta capturando audio corretamente.

## Testar speech no backend local

Com o backend rodando na porta 8000:

```bash
curl http://127.0.0.1:8000/v1/speech/health
```

Resultado esperado:

```json
{"available":true,"backend":"faster-whisper"}
```

Se retornar `available: false`, leia o campo `reason`.

Exemplo de erro comum:

```json
{"available":false,"backend":"faster-whisper","reason":"faster-whisper is not installed. Install with: uv sync --extra desktop"}
```

Nesse caso, rode dentro do projeto:

```bash
cd ~/OpenJarvis
uv sync --extra desktop
```

Depois reinicie o backend.

## Reiniciar backend limpo

Se uma porta ficar presa:

```bash
lsof -i :8000
```

Para matar processo na porta 8000:

```bash
fuser -k 8000/tcp
```

Depois suba novamente:

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8000
```

## Fluxo recomendado para gravacao

Terminal 1:

```bash
ollama serve
```

Terminal 2, apenas se for testar backend manual:

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8000
```

Desktop:

```text
API URL = http://127.0.0.1:8000
```

Teste:

```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/v1/speech/health
```

## O que este metodo resolve

Este metodo documenta a instalacao limpa via Git, com configuracao local do Ollama, Google OAuth e speech local.

Ele nao tenta resolver conflito usando outra porta, porque o Desktop pode subir o mesmo servico de qualquer forma.

## Regra de ouro

- Porta padrao: `8000`.
- Nao trocar para `8001` por padrao.
- Se o Desktop derrubar o `serve`, nao e bug da porta: e conflito de gerenciamento do mesmo backend.
- Para usar Desktop, deixe o Desktop gerenciar o backend ou feche o `serve` manual antes de abrir.
- OAuth JSON, tokens e API keys nunca devem ir para o GitHub.
- Este guia nao usa MiniMax.
