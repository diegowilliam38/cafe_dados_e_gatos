# Instalacao Linux via Git do OpenJarvis

Este guia documenta a instalacao do OpenJarvis no Linux usando o repositorio oficial via Git.

O objetivo aqui e usar o projeto clonado como backend real do OpenJarvis e, se quiser usar o Desktop, apontar a interface para esse backend local.

Este arquivo cobre apenas:

- instalacao via Git;
- backend local;
- Desktop apontando para o backend do Git;
- Google OAuth;
- voz e speech-to-text local.

Este arquivo nao cobre MiniMax.

## Fontes oficiais consultadas

- Instalacao oficial do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/getting-started/installation/
- Configuracao oficial do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/getting-started/configuration/
- API Server do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/deployment/api-server/
- Google Workspace OAuth: https://developers.google.com/workspace/guides/configure-oauth-consent
- Credenciais Google Workspace: https://developers.google.com/workspace/guides/create-credentials

## Ideia deste metodo

Na instalacao via Desktop, pode acontecer de a interface abrir um backend proprio que nao enxerga as dependencias instaladas no projeto clonado.

Neste metodo, usamos o backend do proprio repositorio clonado:

```text
~/OpenJarvis
```

E subimos a API local manualmente em uma porta separada, por exemplo:

```text
http://127.0.0.1:8001
```

Depois, no OpenJarvis Desktop, apontamos o campo `API URL` para essa porta.

Assim:

```text
Desktop visual  ->  http://127.0.0.1:8001
Backend real    ->  ~/OpenJarvis via uv run jarvis serve
Speech local    ->  faster-whisper instalado no projeto clonado
```

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

## Subir backend local em porta separada

Para evitar conflito com o Desktop na porta 8000, suba o backend do projeto na porta 8001:

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8001
```

Deixe este terminal aberto.

Em outro terminal, teste:

```bash
curl http://127.0.0.1:8001/health
```

Resultado esperado:

```json
{"status":"ok"}
```

## Apontar o Desktop para o backend do Git

Abra o OpenJarvis Desktop.

Va em:

```text
Settings > Connection > API URL
```

Troque para:

```text
http://127.0.0.1:8001
```

A ideia e usar o Desktop apenas como interface visual, enquanto o backend real fica rodando pelo projeto clonado em `~/OpenJarvis`.

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

Com o backend rodando na porta 8001:

```bash
curl http://127.0.0.1:8001/v1/speech/health
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
lsof -i :8001
```

Para matar processo na porta 8001:

```bash
fuser -k 8001/tcp
```

Depois suba novamente:

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8001
```

## Fluxo recomendado para gravacao

Terminal 1:

```bash
ollama serve
```

Terminal 2:

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8001
```

Desktop:

```text
Settings > Connection > API URL = http://127.0.0.1:8001
```

Teste:

```bash
curl http://127.0.0.1:8001/health
curl http://127.0.0.1:8001/v1/speech/health
```

## O que este metodo resolve

Este metodo evita depender do backend embutido que o Desktop pode abrir sozinho na porta 8000.

Em vez disso, voce controla o backend do projeto clonado, com as dependencias instaladas no ambiente correto.

## Regra de ouro

- Backend real: `~/OpenJarvis`.
- Porta recomendada para este metodo: `8001`.
- Desktop: apenas interface visual apontando para `http://127.0.0.1:8001`.
- OAuth JSON, tokens e API keys nunca devem ir para o GitHub.
- Este guia nao usa MiniMax.
