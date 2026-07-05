# Instalacao Linux via Git do OpenJarvis

Guia basico para instalar o OpenJarvis no Linux usando o repositorio oficial via Git.

Este guia cobre:

- instalacao via Git;
- backend local na porta padrao `8000`;
- configuracao local com Ollama;
- Google OAuth;
- skills do Hermes Agent e OpenClaw;
- speech local com `faster-whisper`;
- voz local com `kokoro`;
- correcoes comuns.

Este guia nao usa MiniMax.

## Fontes oficiais

- Instalacao: https://open-jarvis.github.io/OpenJarvis/getting-started/installation/
- Configuracao: https://open-jarvis.github.io/OpenJarvis/getting-started/configuration/
- API Server: https://open-jarvis.github.io/OpenJarvis/deployment/api-server/
- Tools: https://open-jarvis.github.io/OpenJarvis/user-guide/tools/
- Skills: https://open-jarvis.github.io/OpenJarvis/user-guide/skills/
- Faster Whisper: https://open-jarvis.github.io/OpenJarvis/api-reference/openjarvis/speech/faster_whisper/
- Releases Desktop: https://github.com/open-jarvis/OpenJarvis/releases/latest
- Google OAuth: https://developers.google.com/workspace/guides/configure-oauth-consent
- Credenciais Google: https://developers.google.com/workspace/guides/create-credentials

## 1. Pre-requisitos

Confira se ja tem as ferramentas principais:

```bash
python3 --version
git --version
node --version
npm --version
uv --version
rustc --version
```

Se nao tiver Rust:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

## 2. Clonar o repositorio

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

## 3. Instalar dependencias

```bash
cd ~/OpenJarvis
uv sync --extra desktop
uv run maturin develop -m rust/crates/openjarvis-python/Cargo.toml
```

Frontend:

```bash
cd ~/OpenJarvis/frontend
npm install
cd ~/OpenJarvis
```

## 4. Instalar o Desktop

Baixe o `.deb` na pagina oficial de releases:

```text
https://github.com/open-jarvis/OpenJarvis/releases/latest
```

Exemplo:

```bash
cd ~/Downloads
wget https://github.com/open-jarvis/OpenJarvis/releases/download/desktop-v1.0.2/OpenJarvis_1.0.1_amd64.deb
sudo apt install ./OpenJarvis_1.0.1_amd64.deb
```

Depois abra o OpenJarvis Desktop pelo menu de aplicativos.

## 5. Configurar Ollama

Confirme que o Ollama esta rodando:

```bash
ollama serve
```

Em outro terminal:

```bash
ollama list
```

Baixe um modelo pequeno para teste, se precisar:

```bash
ollama pull qwen3.5:2b
```

Crie/edite a configuracao:

```bash
mkdir -p ~/.openjarvis
nano ~/.openjarvis/config.toml
```

Configuracao basica:

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

## 6. Backend local e Desktop

A porta padrao do backend local e `8000`:

```text
http://127.0.0.1:8000
```

Nao troque para `8001` por padrao.

Para usar o Desktop, abra o OpenJarvis Desktop normalmente. Em algumas versoes, o Desktop gerencia o backend automaticamente. Evite rodar dois backends ao mesmo tempo.

## 7. Google OAuth

OAuth e usado para autorizar conectores como Drive, Gmail, Calendar, Contacts e Tasks.

Crie um projeto no Google Cloud e configure a tela de consentimento:

```text
https://console.cloud.google.com/apis/credentials/consent
```

Para uso pessoal/teste, mantenha o app em modo de teste e adicione sua propria conta Google como usuaria de teste.

Crie uma credencial OAuth Client ID do tipo `App para computador` / `Desktop app`:

```text
APIs & Services > Credentials > Create Credentials > OAuth client ID
```

Baixe o JSON e guarde uma copia. Depois copie para o caminho usado pelo OpenJarvis:

```bash
mkdir -p ~/.openjarvis/credentials
cp ~/Downloads/client_secret*.json ~/.openjarvis/credentials/google_client_secret.json
chmod 600 ~/.openjarvis/credentials/google_client_secret.json
```

Use `cp`, nao `mv`, para manter o arquivo original em Downloads.

Ative apenas as APIs que for usar:

```text
Google Drive API
Gmail API
Google Calendar API
People API / Contacts
Google Tasks API
```

Conecte pelo OpenJarvis:

```bash
cd ~/OpenJarvis
uv run jarvis connect gdrive
uv run jarvis connect gmail
uv run jarvis connect gcalendar
uv run jarvis connect gcontacts
uv run jarvis connect google_tasks
```

Se algum comando nao existir:

```bash
uv run jarvis --help
uv run jarvis connect --help
```

Nunca envie credenciais, tokens ou API keys para o GitHub.

## 8. Skills do Hermes Agent e OpenClaw

Skills sao pacotes reutilizaveis de instrucoes e ferramentas para os agentes. Elas nao sao a mesma coisa que conectores Google nem configuracao de personalidade.

Listar skills instaladas:

```bash
cd ~/OpenJarvis
uv run jarvis skill list
```

Instalar uma skill do Hermes Agent:

```bash
cd ~/OpenJarvis
uv run jarvis skill install hermes:apple-notes
```

Instalar por categoria do Hermes Agent:

```bash
cd ~/OpenJarvis
uv run jarvis skill sync hermes --category research
uv run jarvis skill sync hermes --category coding
```

Instalar todas as skills disponiveis do Hermes Agent:

```bash
cd ~/OpenJarvis
uv run jarvis skill sync hermes
```

OpenClaw aparece na documentacao oficial como fonte de skills, mas o repositorio padrao pode nao estar disponivel em algumas instalacoes. Se retornar `repository not found`, ignore o OpenClaw e use Hermes/GitHub.

Sincronizar OpenClaw por busca, se a fonte estiver disponivel:

```bash
cd ~/OpenJarvis
uv run jarvis skill sync openclaw --search "web3|crypto"
```

Instalar skill de qualquer repositorio GitHub:

```bash
cd ~/OpenJarvis
uv run jarvis skill install github:user/repo/path/to/skill --url https://github.com/user/repo
```

Ver detalhes de uma skill:

```bash
cd ~/OpenJarvis
uv run jarvis skill info nome-da-skill
```

Rodar uma skill diretamente:

```bash
cd ~/OpenJarvis
uv run jarvis skill run nome-da-skill
```

Tambem e possivel configurar auto-sync no `~/.openjarvis/config.toml`:

```toml
[skills]
enabled = true
auto_sync = true

[[skills.sources]]
source = "hermes"
filter = { category = ["research", "coding", "productivity"] }
auto_update = true
```

## 9. Testar no Desktop via Tauri

Para testar o Desktop Linux pelo codigo-fonte, pode ser necessario instalar dependencias nativas:

```bash
sudo apt update
sudo apt install -y \
  build-essential \
  pkg-config \
  libglib2.0-dev \
  libgtk-3-dev \
  libwebkit2gtk-4.1-dev \
  libayatana-appindicator3-dev \
  librsvg2-dev \
  patchelf
```

Depois rode:

```bash
cd ~/OpenJarvis/frontend
npm run tauri dev
```

Esse comando sobe o frontend de desenvolvimento e abre o Desktop Tauri.

Se o navegador funciona, mas o Desktop retorna `Microphone access denied`, o problema tende a estar na permissao de microfone do runtime grafico, e nao no `faster-whisper`.

## 10. Speech local com faster-whisper

Para usar transcricao de voz local, sem custo por token, configure o OpenJarvis com `faster-whisper`.

Instale o pacote diretamente no projeto clonado pelo Git:

```bash
cd ~/OpenJarvis
uv add faster-whisper
```

Confira se ficou disponivel no ambiente do projeto:

```bash
cd ~/OpenJarvis
uv run python -c "import faster_whisper; print('ok')"
```

Resultado esperado:

```text
ok
```

Edite o arquivo `~/.openjarvis/config.toml` e adicione:

```toml
[speech]
backend = "faster-whisper"
model = "tiny"
device = "cpu"
compute_type = "int8"
language = "pt"
```

Significado da configuracao:

- `backend = "faster-whisper"`: ativa o backend local de speech-to-text.
- `model = "tiny"`: usa um modelo leve e rapido para testes.
- `device = "cpu"`: forca execucao na CPU.
- `compute_type = "int8"`: reduz uso de memoria e funciona bem em CPU.
- `language = "pt"`: forca transcricao em portugues.

Verifique se o backend esta ativo:

```bash
curl http://127.0.0.1:8000/v1/speech/health
```

Resultado esperado:

```json
{"available":true,"backend":"faster-whisper"}
```

Teste o microfone no Linux:

```bash
arecord -d 5 teste_microfone.wav
aplay teste_microfone.wav
```

Se gravou sua voz, o Linux esta capturando audio corretamente.

## 11. Voz local com kokoro

O `kokoro` e um backend local de text-to-speech (TTS). Ele permite que o OpenJarvis gere fala sem usar API paga.

Instale as dependencias no diretorio do projeto:

```bash
cd ~/OpenJarvis
uv pip install kokoro soundfile numpy
```

O backend local de fala fica em:

```text
src/openjarvis/speech/kokoro_tts.py
```

Ele e registrado com o nome:

```text
kokoro
```

Teste uma voz:

```bash
cd ~/OpenJarvis
uv run python - <<'PY'
from openjarvis.speech.kokoro_tts import KokoroTTSBackend

tts = KokoroTTSBackend()
result = tts.synthesize(
    "Ola. Este e um teste de voz local do OpenJarvis.",
    voice_id="af_heart",
    speed=1.0,
    output_format="wav",
)

with open("/tmp/openjarvis_kokoro.wav", "wb") as f:
    f.write(result.audio)

print("/tmp/openjarvis_kokoro.wav")
PY
```

Ouça o audio gerado:

```bash
xdg-open /tmp/openjarvis_kokoro.wav
```

Vozes disponiveis no backend atual:

- `af_heart`
- `af_bella`
- `am_adam`
- `am_michael`

Teste outra voz:

```bash
cd ~/OpenJarvis
uv run python - <<'PY'
from openjarvis.speech.kokoro_tts import KokoroTTSBackend

tts = KokoroTTSBackend()
result = tts.synthesize(
    "Este e outro teste de voz local com Kokoro.",
    voice_id="am_michael",
    speed=1.0,
    output_format="wav",
)

with open("/tmp/openjarvis_kokoro_michael.wav", "wb") as f:
    f.write(result.audio)

print("/tmp/openjarvis_kokoro_michael.wav")
PY
```

Se aparecer erro de pacote ausente, rode novamente:

```bash
cd ~/OpenJarvis
uv pip install kokoro soundfile numpy
```

Resumo:

- `faster-whisper`: audio para texto.
- `kokoro`: texto para audio.

Ou seja:

- para ouvir sua voz no OpenJarvis: `faster-whisper`.
- para o OpenJarvis responder falando: `kokoro`.

## 12. Testar no navegador

Com o backend rodando:

```bash
cd ~/OpenJarvis/frontend
npm run dev
```

Abra no navegador:

```text
http://localhost:5173
```

Ative Speech-to-Text nas configuracoes e teste o microfone.

Se o navegador funcionar, o backend de transcricao esta correto.

## Correcoes comuns

### Erro de CUDA no faster-whisper

Se surgir a mensagem abaixo, ainda pode haver processo antigo tentando usar CUDA:

```text
Library libcublas.so.12 is not found or cannot be loaded
```

Encerre os processos do OpenJarvis e suba novamente:

```bash
pkill -f "jarvis serve"
pkill -f "openjarvis-desktop"
pkill -f "vite"

cd ~/OpenJarvis
uv run jarvis serve --port 8000
```

### Porta 8000 presa

Ver processo usando a porta:

```bash
lsof -i :8000
```

Matar processo na porta:

```bash
fuser -k 8000/tcp
```

### Desktop derruba o backend manual

Nao rode dois backends ao mesmo tempo.

Use um destes fluxos:

```text
Fluxo A: backend manual aberto para testes via API/curl
Fluxo B: Desktop aberto gerenciando o backend
```

Para uso normal do Desktop, prefira abrir apenas o Desktop.

### faster-whisper nao aparece habilitado no Desktop

Siga a secao `Speech local com faster-whisper`: instale pelo projeto Git com `uv add faster-whisper`, confira o import e abra novamente o Desktop.

### OAuth usando cliente antigo

Se o OAuth continuar usando um Client ID antigo, remova os conectores/tokens locais e tente novamente:

```bash
rm -rf ~/.openjarvis/connectors
rm -rf ~/.openjarvis/tokens
rm -rf ~/.openjarvis/oauth*
rm -rf ~/.openjarvis/auth*
```

Confira se o JSON atual esta no caminho correto:

```bash
grep client_id ~/.openjarvis/credentials/google_client_secret.json
```

### Modelo vazio ou configuracao antiga

Se aparecer erro como modelo vazio, configuracao antiga ou provider errado, renomeie a configuracao local:

```bash
mv ~/.openjarvis ~/.openjarvis_old_$(date +%Y%m%d_%H%M%S) 2>/dev/null
mkdir -p ~/.openjarvis
nano ~/.openjarvis/config.toml
```

Depois recrie apenas o bloco necessario do Ollama.
