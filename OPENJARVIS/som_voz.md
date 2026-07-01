# OpenJarvis no Linux: som, microfone, voz e speech backend

Este documento é focado apenas na parte de som e voz do OpenJarvis no Linux.

A ideia é separar esta etapa da configuração geral. Primeiro o OpenJarvis precisa estar instalado, rodando e respondendo por texto. Depois configuramos microfone, entrada de voz, Speech-to-Text e, se necessário, TTS.

> Este material é para teste prático em Linux. A documentação oficial do OpenJarvis ainda não deixa todos os detalhes de voz em formato de passo a passo único, então este arquivo separa o que foi confirmado na documentação/código do projeto e o que precisa ser validado no ambiente real.

---

## Fontes oficiais consultadas

- Documentação oficial do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/
- Instalação oficial: https://open-jarvis.github.io/OpenJarvis/getting-started/installation/
- Configuração oficial: https://open-jarvis.github.io/OpenJarvis/getting-started/configuration/
- Repositório oficial: https://github.com/open-jarvis/OpenJarvis
- `pyproject.toml` oficial do OpenJarvis: confirma os extras `desktop`, `speech` e `speech-deepgram`.
- Interface de configurações do OpenJarvis: mostra a seção **Speech**, o toggle **Speech-to-Text** e o status **Requires Whisper, Deepgram, or another speech backend**.

---

## Ambiente testado no vídeo

Preencher durante a gravação:

```markdown
- Sistema operacional:
- Versão:
- Ambiente gráfico:
- Terminal/shell:
- Microfone usado:
- Placa de som:
- Instalação do OpenJarvis:
- Modelo usado:
- Data do teste:
```

---

## O que esta etapa configura

Esta etapa pode envolver três coisas diferentes:

| Recurso | Função |
|---|---|
| Microfone no Linux | Capturar sua voz no sistema operacional |
| Speech-to-Text / STT | Transformar sua fala em texto |
| Text-to-Speech / TTS | Transformar resposta do agente em áudio |

No OpenJarvis, a mensagem mais comum na tela de configurações é:

```text
Requires Whisper, Deepgram, or another speech backend
```

Isso significa que o backend principal pode estar funcionando, mas a parte de fala ainda não está configurada.

Resumo:

```text
OpenJarvis respondendo por texto = instalação principal funcionando.
Speech backend ausente = voz/microfone ainda não configurado.
```

---

## Verificar se o OpenJarvis está funcionando por texto

Antes de mexer em áudio, confirme que o básico funciona.

Se o comando `jarvis` está disponível globalmente:

```bash
jarvis doctor
jarvis ask "Responda apenas: OpenJarvis funcionando por texto."
```

Se você usa `uv` dentro da pasta do projeto:

```bash
cd ~/OpenJarvis
uv run jarvis doctor
uv run jarvis ask "Responda apenas: OpenJarvis funcionando por texto."
```

Se isso falhar, resolva a instalação principal antes de configurar voz.

---

## Verificar microfone no Linux

Antes de culpar o OpenJarvis, teste se o Linux está capturando áudio.

Instale ferramentas úteis de áudio:

```bash
sudo apt update
sudo apt install -y alsa-utils pulseaudio-utils pavucontrol
```

Liste dispositivos de captura:

```bash
arecord -l
```

Teste gravação curta:

```bash
arecord -d 5 -f cd teste_microfone.wav
```

Reproduza o teste:

```bash
aplay teste_microfone.wav
```

Se estiver usando PipeWire/PulseAudio, confira fontes de entrada:

```bash
pactl list short sources
```

Abra o controle gráfico de áudio:

```bash
pavucontrol
```

No `pavucontrol`, confira:

- aba **Input Devices**;
- microfone correto selecionado;
- volume de entrada;
- se o microfone não está mutado;
- se o navegador/app do OpenJarvis tem permissão de microfone.

---

## Instalar dependência de fala local com Whisper

No `pyproject.toml` oficial do OpenJarvis, o extra `speech` instala:

```text
faster-whisper>=1.0
```

Se você usa OpenJarvis a partir do repositório com `uv`, rode:

```bash
cd ~/OpenJarvis
uv sync --extra speech
```

Se você usa o extra desktop, ele também inclui `faster-whisper`:

```bash
cd ~/OpenJarvis
uv sync --extra desktop
```

Para conferir se o pacote está disponível no ambiente do projeto:

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

---

## Instalar backend Deepgram

O `pyproject.toml` oficial também mostra o extra:

```text
speech-deepgram = ["deepgram-sdk>=3.0"]
```

Para instalar:

```bash
cd ~/OpenJarvis
uv sync --extra speech-deepgram
```

Configure a chave da Deepgram como variável de ambiente:

```bash
export DEEPGRAM_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Para persistir no terminal Bash:

```bash
nano ~/.bashrc
```

Adicione:

```bash
export DEEPGRAM_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Recarregue:

```bash
source ~/.bashrc
```

Teste sem mostrar a chave:

```bash
python3 - <<'PY'
import os
print('DEEPGRAM_API_KEY configurada:', bool(os.getenv('DEEPGRAM_API_KEY')))
PY
```

> Não encontrei, na documentação oficial aberta, um passo a passo completo dizendo qual nome de backend selecionar dentro do `config.toml` para Deepgram. O extra oficial existe, mas o teste prático precisa confirmar como a versão instalada expõe essa opção.

---

## Conferir status de voz na interface

Com o servidor rodando:

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8000
```

Abra a interface do OpenJarvis.

Vá em:

```text
Settings > Speech
```

Confira:

- **Speech-to-Text** ativado;
- **Backend status**;
- se aparece `Available` ou `Not configured`;
- se o navegador/app pediu permissão de microfone.

Se aparecer:

```text
Not configured
```

ou:

```text
Requires Whisper, Deepgram, or another speech backend
```

significa que o backend de voz ainda não foi reconhecido.

---

## Testar endpoint de saúde do backend de voz

A interface do OpenJarvis consulta um status de speech no backend.

Com o servidor rodando na porta `8000`, teste:

```bash
curl http://127.0.0.1:8000/health
```

Depois tente localizar endpoints relacionados a speech na documentação aberta da API, se disponível na sua versão local:

```bash
curl http://127.0.0.1:8000/openapi.json | python3 -m json.tool | grep -i speech -n
```

Se o projeto expuser documentação automática, abra:

```text
http://127.0.0.1:8000/docs
```

Procure por termos como:

```text
speech
transcribe
audio
microphone
whisper
```

> Este ponto precisa ser validado na versão instalada, porque os endpoints podem mudar entre builds.

---

## Testar microfone no navegador

Se você usa a interface web, o navegador precisa liberar o microfone.

No Chromium/Chrome/Edge:

```text
Clique no cadeado ao lado do endereço > Site settings > Microphone > Allow
```

Endereço comum da interface:

```text
http://127.0.0.1:5173
```

ou:

```text
http://localhost:5173
```

Depois recarregue a página.

---

## Fluxo copy-paste recomendado para Linux

Este bloco é o fluxo principal para testar voz local com Whisper/faster-whisper.

```bash
sudo apt update
sudo apt install -y alsa-utils pulseaudio-utils pavucontrol

arecord -l
arecord -d 5 -f cd teste_microfone.wav
aplay teste_microfone.wav

cd ~/OpenJarvis
uv sync --extra speech
uv run python - <<'PY'
import importlib.util
print('faster_whisper instalado:', importlib.util.find_spec('faster_whisper') is not None)
PY
uv run jarvis serve --host 127.0.0.1 --port 8000
```

Depois abra a interface e confira:

```text
Settings > Speech > Backend status
```

---

## Fluxo alternativo com Deepgram

Use este caminho se quiser testar STT em nuvem com Deepgram.

```bash
cd ~/OpenJarvis
uv sync --extra speech-deepgram
export DEEPGRAM_API_KEY="COLE_SUA_CHAVE_AQUI"
python3 - <<'PY'
import os
print('DEEPGRAM_API_KEY configurada:', bool(os.getenv('DEEPGRAM_API_KEY')))
PY
uv run jarvis serve --host 127.0.0.1 --port 8000
```

Depois abra:

```text
Settings > Speech
```

> Ponto pendente: confirmar na prática se a versão instalada detecta Deepgram automaticamente ou se exige ajuste adicional no `config.toml`.

---

## Possíveis problemas e correções

### Microfone não aparece no Linux

**O que verificar:**

```bash
arecord -l
pactl list short sources
```

**Correção provável:**

Abrir o controle de áudio:

```bash
pavucontrol
```

Selecionar o dispositivo correto em **Input Devices**.

---

### Microfone grava mudo

**O que verificar:**

```bash
alsamixer
```

No `alsamixer`:

- pressione `F4` para captura;
- veja se o microfone está mutado;
- aumente o volume de captura.

---

### Interface mostra `Not configured`

**O que aconteceu:**

O OpenJarvis está rodando, mas não encontrou backend de fala.

**Correção para Whisper local:**

```bash
cd ~/OpenJarvis
uv sync --extra speech
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

---

### Navegador não pede microfone

**O que verificar:**

No navegador:

```text
Site settings > Microphone > Allow
```

Depois recarregue a página.

---

### Deepgram instalado, mas não funciona

**O que verificar:**

```bash
python3 - <<'PY'
import os
print('DEEPGRAM_API_KEY configurada:', bool(os.getenv('DEEPGRAM_API_KEY')))
PY
```

Se aparecer `False`, configure a variável:

```bash
export DEEPGRAM_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Se ainda assim não funcionar, registrar no teste:

```text
O extra speech-deepgram existe oficialmente, mas a versão testada não detectou automaticamente o backend sem configuração adicional.
```

---

## O que mostrar no vídeo

### Abertura

```text
Neste vídeo eu não vou reinstalar o OpenJarvis. Ele já está rodando. Agora eu vou separar uma parte que costuma confundir bastante: som, microfone e voz. Uma coisa é o Jarvis responder por texto. Outra coisa é ele conseguir ouvir sua voz e transformar áudio em texto.
```

### Explicação curta

```text
Quando aparece a mensagem Requires Whisper, Deepgram, or another speech backend, não significa necessariamente que o OpenJarvis quebrou. Significa que o backend principal está funcionando, mas a parte de fala ainda precisa de um motor de speech-to-text.
```

### Demonstração

Mostrar:

```bash
arecord -l
arecord -d 5 -f cd teste_microfone.wav
aplay teste_microfone.wav
```

Depois:

```bash
cd ~/OpenJarvis
uv sync --extra speech
uv run jarvis serve --host 127.0.0.1 --port 8000
```

E conferir na interface:

```text
Settings > Speech
```

### Fechamento

```text
Então o raciocínio é: primeiro o Linux precisa enxergar o microfone. Depois o OpenJarvis precisa ter um backend de fala, como Whisper ou Deepgram. Só depois faz sentido testar voz dentro da interface.
```

---

## O que ficou pendente

- Confirmar, na instalação real, se `uv sync --extra speech` é suficiente para o status aparecer como `Available`.
- Confirmar se Deepgram é detectado automaticamente ou se precisa de configuração adicional no `config.toml`.
- Confirmar se a versão atual expõe endpoints específicos de speech em `/docs` ou `/openapi.json`.
- Testar TTS separadamente, porque a parte visível da interface consultada fala principalmente de **Speech-to-Text**.

---

## Resumo final

Para áudio funcionar, siga esta ordem:

```text
Linux reconhece o microfone
↓
OpenJarvis responde por texto
↓
Backend de fala instalado: Whisper/faster-whisper ou Deepgram
↓
Servidor reiniciado
↓
Permissão de microfone liberada no navegador/app
↓
Settings > Speech mostra backend disponível
```
