# OpenJarvis: configuração de voz, transcrição e TTS

Este documento reúne apenas a parte de voz do OpenJarvis: transcrição de áudio para texto, geração de voz a partir de texto e instalação de backends locais.

> Referências usadas:
>
> - Tools do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/user-guide/tools/
> - API `audio_transcribe`: https://open-jarvis.github.io/OpenJarvis/api-reference/openjarvis/tools/audio_tool/
> - API `text_to_speech`: https://open-jarvis.github.io/OpenJarvis/api-reference/openjarvis/tools/text_to_speech/
> - Código oficial do OpenJarvis: `src/openjarvis/tools/audio_tool.py`, `src/openjarvis/tools/text_to_speech.py`, `src/openjarvis/speech/faster_whisper.py`, `src/openjarvis/speech/kokoro_tts.py`

---

## 1. Como a parte de voz é dividida

No OpenJarvis, a parte de voz aparece separada em dois tipos principais de ferramenta:

```text
audio_transcribe = áudio para texto
text_to_speech  = texto para áudio
```

A ferramenta `audio_transcribe` recebe um arquivo de áudio e devolve texto transcrito.

A ferramenta `text_to_speech` recebe texto e gera um arquivo de áudio com voz sintetizada.

---

## 2. Transcrição de áudio com `audio_transcribe`

A ferramenta de transcrição é chamada:

```text
audio_transcribe
```

Ela aceita arquivos nos formatos:

```text
.mp3
.wav
.m4a
.ogg
.flac
.webm
```

O limite definido no código é de 25 MB por arquivo.

Parâmetros principais:

| Parâmetro | Obrigatório | Descrição |
|---|---:|---|
| `file_path` | Sim | Caminho do arquivo de áudio |
| `language` | Não | Código do idioma, como `pt`, `en`, `es` |
| `provider` | Não | Provedor de transcrição |

No código atual, o provider padrão é:

```text
openai
```

A ferramenta também aceita o valor `local`, mas no arquivo `audio_tool.py` o provider local ainda retorna:

```text
Local transcription provider is not yet implemented.
```

Ou seja: existe infraestrutura local de speech-to-text no projeto, mas a ferramenta `audio_transcribe`, do jeito que está no código atual, usa OpenAI Whisper como caminho direto.

---

## 3. Transcrição via OpenAI Whisper

Para usar transcrição via OpenAI, é necessário ter a variável de ambiente:

```bash
export OPENAI_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Para persistir no Linux:

```bash
nano ~/.bashrc
```

Adicione ao final:

```bash
export OPENAI_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Recarregue:

```bash
source ~/.bashrc
```

Teste se a variável existe sem revelar a chave:

```bash
python3 - <<'PY'
import os
print('OPENAI_API_KEY configurada:', bool(os.getenv('OPENAI_API_KEY')))
PY
```

Também é necessário ter o pacote `openai` instalado no ambiente usado pelo OpenJarvis.

Dentro da pasta do OpenJarvis:

```bash
cd ~/OpenJarvis
uv sync
```

Se o erro disser que o pacote `openai` não está instalado, instale ou sincronize os extras usados no projeto conforme a documentação da versão instalada.

---

## 4. Speech-to-text local com Faster-Whisper

O projeto tem backend local registrado como:

```text
faster-whisper
```

Ele usa Faster-Whisper/CTranslate2 para transcrição local.

No código, quando `faster-whisper` não está instalado, a mensagem sugerida é:

```bash
uv sync --extra desktop
```

Então o caminho recomendado para instalar os componentes locais de desktop/voz é:

```bash
cd ~/OpenJarvis
uv sync --extra desktop
```

Depois confira se o ambiente continua funcionando:

```bash
uv run jarvis doctor
```

Importante: mesmo com o backend `faster-whisper` existindo no projeto, a ferramenta `audio_transcribe` atual ainda pode não usar `provider="local"` diretamente, porque o próprio código da ferramenta retorna que o provider local ainda não foi implementado nessa chamada.

---

## 5. Texto para voz com `text_to_speech`

A ferramenta de TTS é chamada:

```text
text_to_speech
```

Ela converte texto em áudio e retorna o caminho do arquivo gerado.

Parâmetros principais:

| Parâmetro | Obrigatório | Descrição |
|---|---:|---|
| `text` | Sim | Texto que será convertido em voz |
| `voice_id` | Não | Voz usada pelo backend |
| `backend` | Não | Backend de TTS |
| `output_dir` | Não | Pasta onde o áudio será salvo |
| `speed` | Não | Velocidade da fala |

Backends citados no código:

```text
cartesia
kokoro
openai_tts
```

O código também aceita o alias:

```text
openai -> openai_tts
```

Se `output_dir` não for informado, o OpenJarvis cria uma pasta temporária e salva o áudio com nome parecido com:

```text
digest.mp3
```

ou outro formato retornado pelo backend.

---

## 6. TTS local com Kokoro

O backend local Kokoro aparece registrado como:

```text
kokoro
```

Segundo o código, ele é um backend open-source local de text-to-speech.

Para instalar:

```bash
cd ~/OpenJarvis
uv pip install kokoro
```

Se o ambiente não aceitar `uv pip`, use:

```bash
pip install kokoro
```

Vozes listadas no código:

```text
af_heart
af_bella
am_adam
am_michael
```

Exemplo conceitual de uso da ferramenta:

```text
Use a ferramenta text_to_speech para converter o texto "OpenJarvis funcionando com voz local" usando backend kokoro e voz af_heart.
```

---

## 7. Testes básicos

### 7.1 Testar backend e instalação geral

```bash
cd ~/OpenJarvis
uv run jarvis doctor
```

### 7.2 Testar variável da OpenAI

```bash
python3 - <<'PY'
import os
print('OPENAI_API_KEY configurada:', bool(os.getenv('OPENAI_API_KEY')))
PY
```

### 7.3 Testar se o Kokoro importa

```bash
python3 - <<'PY'
try:
    import kokoro
    print('kokoro instalado: OK')
except Exception as e:
    print('kokoro não disponível:', e)
PY
```

### 7.4 Testar se Faster-Whisper importa

```bash
python3 - <<'PY'
try:
    import faster_whisper
    print('faster-whisper instalado: OK')
except Exception as e:
    print('faster-whisper não disponível:', e)
PY
```

Se estiver usando o ambiente do OpenJarvis com `uv`, rode os testes com:

```bash
cd ~/OpenJarvis
uv run python - <<'PY'
try:
    import faster_whisper
    print('faster-whisper instalado: OK')
except Exception as e:
    print('faster-whisper não disponível:', e)

try:
    import kokoro
    print('kokoro instalado: OK')
except Exception as e:
    print('kokoro não disponível:', e)
PY
```

---

## 8. Observações importantes

1. `audio_transcribe` via OpenAI Whisper depende de `OPENAI_API_KEY`.
2. A ferramenta `audio_transcribe` tem limite de 25 MB por arquivo.
3. O provider `local` da ferramenta `audio_transcribe` aparece no schema, mas no código atual retorna que ainda não está implementado.
4. O backend local `faster-whisper` existe no projeto, mas pode não estar ligado diretamente ao provider `local` da ferramenta `audio_transcribe`.
5. `text_to_speech` usa backends registrados no `TTSRegistry`.
6. Kokoro é o caminho local open-source de TTS presente no código.
7. Para recursos locais de voz, o extra `desktop` é o caminho mais provável indicado pelo próprio código do Faster-Whisper.

---

## 9. Comandos principais

Instalar extras de desktop/voz:

```bash
cd ~/OpenJarvis
uv sync --extra desktop
```

Instalar Kokoro:

```bash
cd ~/OpenJarvis
uv pip install kokoro
```

Configurar OpenAI Whisper:

```bash
export OPENAI_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Testar instalação:

```bash
cd ~/OpenJarvis
uv run jarvis doctor
```

Testar imports locais:

```bash
cd ~/OpenJarvis
uv run python - <<'PY'
for pkg in ['faster_whisper', 'kokoro']:
    try:
        __import__(pkg)
        print(pkg, 'OK')
    except Exception as e:
        print(pkg, 'erro:', e)
PY
```

---

## 10. Conclusão técnica

A parte de voz do OpenJarvis existe em camadas:

```text
Transcrição cloud: audio_transcribe + OpenAI Whisper
Transcrição local: backend faster-whisper
TTS cloud/local: text_to_speech + backends registrados
TTS local: Kokoro
```

Para começar com menos erro, use primeiro OpenAI Whisper para transcrição e depois teste Kokoro para TTS local.

Para uma configuração totalmente local, instale o extra `desktop`, teste `faster-whisper` e `kokoro`, e confirme se a versão atual do OpenJarvis já conecta esses backends às ferramentas usadas na interface.