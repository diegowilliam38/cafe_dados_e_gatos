# Configuracoes do OpenJarvis

Guia unico para configurar o OpenJarvis depois da instalacao.

Use este documento para organizar `config.toml`, engines, modelos, variaveis de ambiente, Google OAuth, conectores, som, microfone, speech-to-text e text-to-speech.

A instalacao Linux fica em [`install_linux.md`](./install_linux.md). A instalacao Windows fica em [`install_windows.md`](./install_windows.md).

## Objetivo

Centralizar a configuracao real do OpenJarvis sem espalhar informacao em varios arquivos soltos.

Este arquivo substitui:

- `configuracao.md`;
- `som_voz.md`;
- `voz.md`.

## Fontes oficiais consultadas

- Documentacao oficial do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/
- Instalacao oficial: https://open-jarvis.github.io/OpenJarvis/getting-started/installation/
- Configuracao oficial: https://open-jarvis.github.io/OpenJarvis/getting-started/configuration/
- Tools do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/user-guide/tools/
- API de audio: https://open-jarvis.github.io/OpenJarvis/api-reference/openjarvis/tools/audio_tool/
- API de text-to-speech: https://open-jarvis.github.io/OpenJarvis/api-reference/openjarvis/tools/text_to_speech/
- Google Workspace OAuth: https://developers.google.com/workspace/guides/configure-oauth-consent
- Credenciais Google Workspace: https://developers.google.com/workspace/guides/create-credentials

## Antes de configurar

Confirme que a instalacao basica funciona.

No Linux:

```bash
cd ~/OpenJarvis
uv run jarvis doctor
uv run jarvis model list
uv run jarvis ask "Responda apenas: OpenJarvis funcionando."
```

No Windows, use o guia [`install_windows.md`](./install_windows.md).

## Onde ficam os arquivos principais

No Linux:

```text
~/.openjarvis/
~/.openjarvis/config.toml
~/.openjarvis/connectors/
~/.openjarvis/skills/
~/.openjarvis/memory.db
~/.openjarvis/traces.db
~/.openjarvis/telemetry.db
```

Para conferir:

```bash
ls -la ~/.openjarvis
```

Para abrir a configuracao:

```bash
nano ~/.openjarvis/config.toml
```

Se quiser confirmar o caminho pelo proprio OpenJarvis:

```bash
cd ~/OpenJarvis
uv run jarvis config path
```

## Backup antes de mexer

Antes de editar configuracao, faca backup:

```bash
cp ~/.openjarvis/config.toml ~/.openjarvis/config.toml.bak
```

Para restaurar:

```bash
cp ~/.openjarvis/config.toml.bak ~/.openjarvis/config.toml
```

## Inicializar ou regenerar configuracao

Se o arquivo ainda nao existir:

```bash
cd ~/OpenJarvis
uv run jarvis init
```

Se voce ja tem configuracao funcionando, nao rode `init --force` sem backup.

## Configuracao com Ollama local

Confirme que o Ollama esta rodando:

```bash
ollama serve
```

Em outro terminal:

```bash
ollama list
curl http://127.0.0.1:11434/api/tags
```

Exemplo de configuracao local no `~/.openjarvis/config.toml`:

```toml
[engine]
default = "ollama"

[engine.ollama]
host = "http://127.0.0.1:11434"

[intelligence]
default_model = "qwen3:0.6b"
temperature = 0.7
max_tokens = 2048

[agent]
default_agent = "orchestrator"
max_turns = 10
context_from_memory = true
```

A linha do host precisa estar ativa, sem `#`:

```toml
host = "http://127.0.0.1:11434"
```

Nao deixe assim:

```toml
# host = "http://127.0.0.1:11434"
```

Depois teste:

```bash
cd ~/OpenJarvis
uv run jarvis ask "Explique em uma frase o que e o OpenJarvis."
```

## Variaveis de ambiente para APIs

A documentacao oficial lista variaveis para engines em nuvem e ferramentas.

Abra o arquivo do shell:

```bash
nano ~/.bashrc
```

Adicione somente as chaves que voce realmente usa:

```bash
export OPENAI_API_KEY="COLE_SUA_CHAVE_AQUI"
export ANTHROPIC_API_KEY="COLE_SUA_CHAVE_AQUI"
export GOOGLE_API_KEY="COLE_SUA_CHAVE_AQUI"
export MINIMAX_API_KEY="COLE_SUA_CHAVE_AQUI"
export TAVILY_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Recarregue:

```bash
source ~/.bashrc
```

Confira sem mostrar os valores:

```bash
python3 - <<'PY'
import os
for key in ['OPENAI_API_KEY','ANTHROPIC_API_KEY','GOOGLE_API_KEY','MINIMAX_API_KEY','TAVILY_API_KEY']:
    print(key, 'OK' if os.getenv(key) else 'NAO CONFIGURADA')
PY
```

> Nunca publique API Key em print, video, live, commit ou repositorio publico.

## Google Gemini como modelo

Google Gemini via API Key e diferente de Google OAuth.

- `GOOGLE_API_KEY`: chave para usar Gemini como modelo.
- Google OAuth: login/autorizacao para Gmail, Drive, Calendar, Contacts e Tasks.

Para instalar extra de Gemini:

```bash
cd ~/OpenJarvis
uv sync --extra inference-google
```

Configure a variavel:

```bash
export GOOGLE_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Para persistir:

```bash
nano ~/.bashrc
```

Adicione:

```bash
export GOOGLE_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Recarregue:

```bash
source ~/.bashrc
```

## OpenAI, Anthropic, MiniMax e Tavily

Para OpenAI e Anthropic:

```bash
cd ~/OpenJarvis
uv sync --extra inference-cloud
```

Para cloud + Google:

```bash
cd ~/OpenJarvis
uv sync --extra inference-cloud --extra inference-google
```

Variaveis:

```bash
export OPENAI_API_KEY="COLE_SUA_CHAVE_AQUI"
export ANTHROPIC_API_KEY="COLE_SUA_CHAVE_AQUI"
export MINIMAX_API_KEY="COLE_SUA_CHAVE_AQUI"
export TAVILY_API_KEY="COLE_SUA_CHAVE_AQUI"
```

## Google OAuth para Drive, Gmail, Calendar, Contacts e Tasks

Esta parte conecta a sua conta Google ao OpenJarvis.

Ela nao e a mesma coisa que `GOOGLE_API_KEY`.

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

Use o tipo recomendado pela documentacao do conector/fluxo local da sua versao do OpenJarvis.

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

Depois teste outros conectores, se disponiveis na sua versao:

```bash
cd ~/OpenJarvis
uv run jarvis connect gmail
uv run jarvis connect gcalendar
uv run jarvis connect gcontacts
uv run jarvis connect google_tasks
```

Se algum nome nao existir, liste conectores/comandos disponiveis:

```bash
cd ~/OpenJarvis
uv run jarvis --help
uv run jarvis connect --help
```

### Onde ficam tokens Google

Os tokens normalmente ficam na pasta de conectores:

```bash
ls -la ~/.openjarvis/connectors
```

Nunca suba estes arquivos para o GitHub.

## Configurar som e microfone no Linux

Antes de culpar o OpenJarvis, confirme que o Linux reconhece o microfone.

Instale ferramentas de audio:

```bash
sudo apt update
sudo apt install -y alsa-utils pulseaudio-utils pavucontrol
```

Liste dispositivos de captura:

```bash
arecord -l
```

Grave 5 segundos:

```bash
arecord -d 5 -f cd teste_microfone.wav
```

Reproduza:

```bash
aplay teste_microfone.wav
```

Se nao gravar, abra o controle de audio:

```bash
pavucontrol
```

Confira:

- microfone correto;
- volume de entrada;
- se nao esta mutado;
- permissao de microfone no navegador;
- se a interface esta apontando para a API correta.

## Configurar speech-to-text local com Faster-Whisper

O `config.toml` usa TOML, nao YAML.

Nao use isto:

```yaml
speech:
  stt:
    backend: faster-whisper
```

Use a secao `[speech]`:

```toml
[speech]
backend = "faster-whisper"
model = "base"
device = "auto"
compute_type = "int8"
language = ""
```

Para maquina fraca, teste `tiny`:

```toml
[speech]
backend = "faster-whisper"
model = "tiny"
device = "auto"
compute_type = "int8"
language = ""
```

Para instalar extras de voz/desktop:

```bash
cd ~/OpenJarvis
uv sync --extra desktop
```

Teste se `faster_whisper` esta disponivel:

```bash
cd ~/OpenJarvis
uv run python - <<'PY'
import importlib.util
print('faster_whisper instalado:', importlib.util.find_spec('faster_whisper') is not None)
PY
```

Reinicie o servidor:

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8000
```

No log, procure:

```text
Speech: faster-whisper
```

Se aparecer, o backend de voz foi carregado.

## Testar API local

Com o servidor rodando:

```bash
curl http://127.0.0.1:8000/health
```

Para procurar endpoints relacionados a speech na sua versao:

```bash
curl http://127.0.0.1:8000/openapi.json | python3 -m json.tool | grep -i speech -n
```

Tambem pode abrir:

```text
http://127.0.0.1:8000/docs
```

Procure por:

```text
speech
transcribe
audio
whisper
```

## Se a interface mostra `Not configured`

Primeiro olhe o terminal do backend.

Se o terminal mostra:

```text
Speech: faster-whisper
```

entao o backend local foi reconhecido.

Nesse caso, verifique:

- permissao de microfone no navegador;
- se a interface esta usando `http://127.0.0.1:8000` como API;
- se o frontend foi recarregado depois de reiniciar o backend;
- se existem endpoints de speech na versao atual;
- se a versao instalada ainda nao conectou a interface ao backend local de speech.

No Chrome, Chromium ou Edge:

```text
Clique no cadeado ao lado do endereco > Site settings > Microphone > Allow
```

Depois recarregue a interface.

## Transcricao via OpenAI Whisper

A ferramenta de transcricao por OpenAI depende de:

```bash
export OPENAI_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Teste sem revelar a chave:

```bash
python3 - <<'PY'
import os
print('OPENAI_API_KEY configurada:', bool(os.getenv('OPENAI_API_KEY')))
PY
```

Se faltar pacote, sincronize o ambiente:

```bash
cd ~/OpenJarvis
uv sync --extra inference-cloud
```

## Text-to-speech local com Kokoro

O backend local de TTS citado no codigo do OpenJarvis e `kokoro`.

Instale dentro do ambiente do projeto:

```bash
cd ~/OpenJarvis
uv pip install kokoro
```

Teste import:

```bash
cd ~/OpenJarvis
uv run python - <<'PY'
try:
    import kokoro
    print('kokoro instalado: OK')
except Exception as e:
    print('kokoro nao disponivel:', e)
PY
```

Backends de TTS citados no material anterior:

```text
cartesia
kokoro
openai_tts
```

Alias comum:

```text
openai -> openai_tts
```

## Corrigir aviso `croniter not installed`

Se aparecer:

```text
WARNING openjarvis.agents.scheduler: croniter not installed, treating cron as 3600s interval
```

isso nao impede a voz de funcionar.

Se quiser remover o aviso:

```bash
cd ~/OpenJarvis
uv add croniter
uv run jarvis serve --host 127.0.0.1 --port 8000
```

## Bloco copy-paste de configuracao local basica

```bash
cd ~/OpenJarvis

# Ollama em outro terminal
ollama serve

# Modelo pequeno para teste
ollama pull qwen3:0.6b
ollama list

# Backup da configuracao
cp ~/.openjarvis/config.toml ~/.openjarvis/config.toml.bak

# Abrir config
nano ~/.openjarvis/config.toml
```

Cole ou ajuste:

```toml
[engine]
default = "ollama"

[engine.ollama]
host = "http://127.0.0.1:11434"

[intelligence]
default_model = "qwen3:0.6b"
temperature = 0.7
max_tokens = 2048

[agent]
default_agent = "orchestrator"
max_turns = 10
context_from_memory = true

[speech]
backend = "faster-whisper"
model = "base"
device = "auto"
compute_type = "int8"
language = ""
```

Depois rode:

```bash
cd ~/OpenJarvis
uv sync --extra desktop
uv run jarvis doctor
uv run jarvis model list
uv run jarvis ask "Responda apenas: configuracao funcionando."
uv run jarvis serve --host 127.0.0.1 --port 8000
```

## Checklist para gravacao

Antes de gravar:

```bash
python3 --version
uv --version
rustc --version
node --version
npm --version
ollama --version
```

OpenJarvis:

```bash
cd ~/OpenJarvis
uv run jarvis --version
uv run jarvis doctor
uv run jarvis model list
```

Ollama:

```bash
ollama list
curl http://127.0.0.1:11434/api/tags
```

Backend:

```bash
curl http://127.0.0.1:8000/health
```

Audio:

```bash
arecord -l
arecord -d 5 -f cd teste_microfone.wav
aplay teste_microfone.wav
```

## O que ficou pendente

- Confirmar em cada versao do OpenJarvis quais nomes de conectores Google estao disponiveis no `jarvis connect --help`.
- Confirmar se a interface web da versao instalada ja reconhece automaticamente o backend local `faster-whisper`.
- Confirmar quais vozes Kokoro estao disponiveis na versao instalada.

## Regra de ouro

- Instalacao fica em `install_linux.md` ou `install_windows.md`.
- Configuracao fica neste arquivo.
- Nunca colocar tokens, OAuth JSON, API keys ou arquivos de `~/.openjarvis/connectors/` no repositorio.
