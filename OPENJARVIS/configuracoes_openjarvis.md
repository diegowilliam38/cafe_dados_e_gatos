# Configuracoes do OpenJarvis

Guia unico para configurar o OpenJarvis depois da instalacao.

A instalacao Linux fica em [`install_linux.md`](./install_linux.md). A instalacao Windows fica em [`install_windows.md`](./install_windows.md).

## Objetivo

Centralizar a configuracao real usada nos testes:

- Ollama local como fluxo principal do Desktop;
- MiniMax Cloud como teste via CLI;
- Google OAuth para conectores Google;
- som, microfone, speech-to-text e text-to-speech.

> Resultado importante do teste: MiniMax Cloud funcionou no OpenJarvis via CLI. Na build testada do OpenJarvis Desktop, MiniMax nao aparece como provedor configuravel na interface.

Este arquivo substitui:

- `configuracao.md`;
- `som_voz.md`;
- `voz.md`.

## Fontes oficiais consultadas

- Documentacao oficial do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/
- Instalacao oficial: https://open-jarvis.github.io/OpenJarvis/getting-started/installation/
- Configuracao oficial: https://open-jarvis.github.io/OpenJarvis/getting-started/configuration/
- Tools do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/user-guide/tools/
- API Server do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/deployment/api-server/
- API de audio: https://open-jarvis.github.io/OpenJarvis/api-reference/openjarvis/tools/audio_tool/
- API de text-to-speech: https://open-jarvis.github.io/OpenJarvis/api-reference/openjarvis/tools/text_to_speech/
- Google Workspace OAuth: https://developers.google.com/workspace/guides/configure-oauth-consent
- Credenciais Google Workspace: https://developers.google.com/workspace/guides/create-credentials

## Antes de configurar

Confirme que a instalacao basica funciona.

```bash
cd ~/OpenJarvis
uv run jarvis doctor
uv run jarvis model list
uv run jarvis ask "Responda apenas: OpenJarvis funcionando."
```

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

Este e o fluxo mais seguro para o Desktop na build testada.

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
default_model = "qwen3.5:2b"
temperature = 0.7
max_tokens = 2048

[agent]
default_agent = "simple"
```

Depois teste:

```bash
cd ~/OpenJarvis
uv run jarvis ask "Explique em uma frase o que e o OpenJarvis."
```

## MiniMax Cloud: funciona via CLI

MiniMax Cloud foi validado no OpenJarvis pelo modo CLI.

Resultado observado no terminal:

```text
OpenJarvis Chat
  Engine: cloud  Model: MiniMax-M3  Agent: orchestrator
```

Isso confirma que o `~/.openjarvis/config.toml` foi lido corretamente pela CLI e que a engine cloud conseguiu selecionar o modelo MiniMax.

## MiniMax no Desktop: limitacao encontrada

Na build testada do OpenJarvis Desktop, a interface de modelos em nuvem mostrou apenas:

```text
OpenAI
Anthropic
Google
OpenRouter
```

A tela do Desktop nao exibiu:

```text
MiniMax
MINIMAX_API_KEY
```

Por isso, nesta versao, MiniMax Cloud deve ser tratado como funcionando via CLI, nao como configuracao direta pelo Desktop.

Nao coloque a URL da MiniMax no campo `API URL` do Desktop. Esse campo e para o backend local do OpenJarvis, normalmente:

```text
http://127.0.0.1:8000
```

O endpoint da MiniMax usado internamente pelo backend cloud e:

```text
https://api.minimax.io/v1
```

Mas esse endpoint nao foi exposto como opcao direta na interface do Desktop testada.

## Variavel de ambiente para MiniMax

A chave da MiniMax deve ficar fora do repositorio.

Abra o arquivo do shell:

```bash
nano ~/.bashrc
```

Adicione:

```bash
export MINIMAX_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Recarregue:

```bash
source ~/.bashrc
```

Confira sem mostrar a chave:

```bash
python3 - <<'PY'
import os
print('MINIMAX_API_KEY', 'OK' if os.getenv('MINIMAX_API_KEY') else 'NAO CONFIGURADA')
PY
```

> Nunca publique API Key em print, video, live, commit ou repositorio publico.

## Configuracao MiniMax Cloud para CLI

Edite:

```bash
nano ~/.openjarvis/config.toml
```

Use este bloco para testar MiniMax Cloud pela CLI:

```toml
# OpenJarvis configuration
# MiniMax Cloud via CLI
# Endpoint usado internamente pelo backend cloud:
# https://api.minimax.io/v1

[engine]
default = "cloud"

[intelligence]
default_model = "MiniMax-M3"
fallback_model = "MiniMax-M2.7"
preferred_engine = "cloud"
provider = "minimax"
temperature = 0.7
max_tokens = 2048

[agent]
default_agent = "orchestrator"
max_turns = 10
context_from_memory = true

[tools]
enabled = ["code_interpreter", "web_search", "file_read", "shell_exec"]
```

Teste:

```bash
jarvis
```

Resultado esperado:

```text
OpenJarvis Chat
  Engine: cloud  Model: MiniMax-M3  Agent: orchestrator
```

Depois envie uma mensagem:

```text
Responda apenas: MiniMax-M3 funcionando no OpenJarvis CLI.
```

Se o M3 nao estiver liberado ou o nome do modelo nao for aceito na sua conta, volte temporariamente para:

```toml
[intelligence]
default_model = "MiniMax-M2.7"
fallback_model = "MiniMax-M2.7-highspeed"
preferred_engine = "cloud"
provider = "minimax"
temperature = 0.7
max_tokens = 2048
```

## REST API Server do OpenJarvis

O servidor REST do OpenJarvis e opcional. Ele sobe uma API local compativel com OpenAI.

Instale o extra do servidor:

```bash
cd ~/OpenJarvis
uv sync --extra server
```

Suba localmente:

```bash
uv run jarvis serve --host 127.0.0.1 --port 8000
```

Teste:

```bash
curl http://127.0.0.1:8000/health
```

Resultado esperado:

```json
{"status":"ok"}
```

Importante: abrir o Desktop pode usar o fluxo proprio da interface. Na build testada, o Desktop continuou preso ao fluxo visual de Ollama/OpenAI/Anthropic/Google/OpenRouter e nao herdou MiniMax como provedor direto.

## Google OAuth para Drive, Gmail, Calendar, Contacts e Tasks

Google OAuth nao e a mesma coisa que `GOOGLE_API_KEY`.

Neste guia:

- `MINIMAX_API_KEY` e chave de API para MiniMax;
- Google OAuth e login/autorizacao para acessar Drive, Gmail, Calendar, Contacts e Tasks;
- `GOOGLE_API_KEY` nao faz parte do fluxo principal.

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

Os tokens normalmente ficam na pasta de conectores:

```bash
ls -la ~/.openjarvis/connectors
```

Nunca suba estes arquivos para o GitHub.

## Configurar som e microfone no Linux

Como o microfone ja funciona no sistema, nao troque o dispositivo manualmente.

Para validar rapidamente a captura padrao, grave 5 segundos:

```bash
arecord -d 5 teste_microfone.wav
```

Reproduza:

```bash
aplay teste_microfone.wav
```

Se gravou sua voz, o Linux ja esta capturando audio corretamente.

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

Esta parte nao faz parte do fluxo principal deste guia.

Use somente se voce decidir testar OpenAI para transcricao.

Nesse caso, a ferramenta de transcricao por OpenAI depende de:

```bash
export OPENAI_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Nao configure essa variavel se voce nao for usar OpenAI.

## Text-to-speech local com Kokoro

O backend local de TTS citado no codigo do OpenJarvis e `kokoro`.

Instale dentro do ambiente do projeto apenas se for testar TTS local:

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
ollama pull qwen3.5:2b
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
default_model = "qwen3.5:2b"
temperature = 0.7
max_tokens = 2048

[agent]
default_agent = "simple"

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
```

OpenJarvis:

```bash
cd ~/OpenJarvis
uv run jarvis --version
uv run jarvis doctor
uv run jarvis model list
jarvis
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
arecord -d 5 teste_microfone.wav
aplay teste_microfone.wav
```

## O que ficou pendente

- Confirmar em cada versao do OpenJarvis quais nomes de conectores Google estao disponiveis no `jarvis connect --help`.
- Confirmar se a interface web da versao instalada ja reconhece automaticamente o backend local `faster-whisper`.
- Confirmar quais vozes Kokoro estao disponiveis na versao instalada.
- Confirmar se uma build futura do OpenJarvis Desktop passara a expor MiniMax diretamente na tela de Cloud Models / API Keys.

## Regra de ouro

- Instalacao fica em `install_linux.md` ou `install_windows.md`.
- Configuracao fica neste arquivo.
- MiniMax Cloud, nesta build testada, fica documentado como funcionando via CLI.
- Desktop, nesta build testada, segue limitado ao fluxo local/Ollama e aos provedores exibidos na propria interface.
- No fluxo principal, nao configure chaves que voce nao vai usar.
- Google OAuth nao e `GOOGLE_API_KEY`.
- Nunca colocar tokens, OAuth JSON, API keys ou arquivos de `~/.openjarvis/connectors/` no repositorio.
