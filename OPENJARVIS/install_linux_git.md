# Instalacao Linux via Git do OpenJarvis

Guia basico para instalar o OpenJarvis no Linux usando o repositorio oficial via Git.

Este guia cobre:

- instalacao via Git;
- backend local na porta padrao `8000`;
- configuracao local com Ollama;
- Google OAuth;
- speech local com `faster-whisper`;
- correcoes comuns.

Este guia nao usa MiniMax.

## Fontes oficiais

- Instalacao: https://open-jarvis.github.io/OpenJarvis/getting-started/installation/
- Configuracao: https://open-jarvis.github.io/OpenJarvis/getting-started/configuration/
- API Server: https://open-jarvis.github.io/OpenJarvis/deployment/api-server/
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

## 6. Subir backend local

Use a porta padrao `8000`.

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8000
```

Teste em outro terminal:

```bash
curl http://127.0.0.1:8000/health
```

Resultado esperado:

```json
{"status":"ok"}
```

## 7. Desktop e porta

Padrao:

```text
http://127.0.0.1:8000
```

Nao troque para `8001` por padrao.

Se o Desktop derrubar o `jarvis serve`, provavelmente os dois estao tentando iniciar/gerenciar o mesmo backend. Nesse caso, feche o `serve` manual antes de abrir o Desktop ou deixe apenas um processo ativo.

## 8. Google OAuth

OAuth e usado para autorizar conectores como Drive, Gmail, Calendar, Contacts e Tasks.

Crie um projeto no Google Cloud e configure a tela de consentimento:

```text
https://console.cloud.google.com/apis/credentials/consent
```

Para uso pessoal/teste, mantenha o app em modo de teste e adicione sua propria conta Google como usuaria de teste.

Crie uma credencial OAuth Client ID:

```text
APIs & Services > Credentials > Create Credentials > OAuth client ID
```

Baixe o JSON e guarde localmente:

```bash
mkdir -p ~/.openjarvis/credentials
mv ~/Downloads/client_secret*.json ~/.openjarvis/credentials/google_client_secret.json
chmod 600 ~/.openjarvis/credentials/google_client_secret.json
```

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

## 9. Speech local com faster-whisper

O extra `desktop` deve instalar o `faster-whisper`.

Confira:

```bash
cd ~/OpenJarvis
uv run python - <<'PY'
import importlib.util
print('faster_whisper instalado:', importlib.util.find_spec('faster_whisper') is not None)
PY
```

Adicione ao `~/.openjarvis/config.toml`:

```toml
[speech]
backend = "faster-whisper"
model = "tiny"
device = "auto"
compute_type = "int8"
language = "pt"
```

Teste o microfone:

```bash
arecord -d 5 teste_microfone.wav
aplay teste_microfone.wav
```

Teste o endpoint de speech:

```bash
curl http://127.0.0.1:8000/v1/speech/health
```

Resultado esperado:

```json
{"available":true,"backend":"faster-whisper"}
```

## Correcoes comuns

### Porta 8000 presa

Ver processo usando a porta:

```bash
lsof -i :8000
```

Matar processo na porta:

```bash
fuser -k 8000/tcp
```

Subir de novo:

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8000
```

### Desktop derruba o backend manual

Nao rode dois backends ao mesmo tempo.

Use um destes fluxos:

```text
Fluxo A: backend manual aberto + teste via curl
Fluxo B: Desktop aberto gerenciando o backend
```

Evite abrir o Desktop depois de ja ter iniciado manualmente o `jarvis serve`, se a versao do Desktop tentar iniciar o mesmo servico.

### Modelo vazio ou configuracao antiga

Se aparecer erro como modelo vazio, configuracao antiga ou provider errado, renomeie a configuracao local:

```bash
mv ~/.openjarvis ~/.openjarvis_old_$(date +%Y%m%d_%H%M%S) 2>/dev/null
mkdir -p ~/.openjarvis
nano ~/.openjarvis/config.toml
```

Depois recrie apenas o bloco necessario do Ollama.

### Limpeza completa para reinstalar

Use apenas se quiser apagar a instalacao anterior.

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
rm -rf ~/.local/share/com.openjarvis.desktop
rm -rf ~/.cache/uv
rm -rf ~/.cache/gnome-software/odrs/OpenJarvis.desktop.json
rm -f ~/Downloads/OpenJarvis*.deb
rm -f ~/Downloads/openjarvis*.deb
rm -f ~/Downloads/OpenJarvis_*.AppImage
```

Conferir:

```bash
find ~ -iname "*openjarvis*" 2>/dev/null
```

Apague manualmente apenas arquivos pessoais se tiver certeza.
