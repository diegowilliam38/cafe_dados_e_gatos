# OpenJarvis no Linux: som, microfone, voz e speech backend

Este guia organiza apenas a parte de áudio e voz do OpenJarvis no Linux.

Objetivo: fazer o OpenJarvis reconhecer o microfone e usar Speech-to-Text local com `faster-whisper`, sem API paga.

---

## 1. Referências oficiais verificadas

- Documentação oficial de configuração: https://open-jarvis.github.io/OpenJarvis/getting-started/configuration/
- Documentação oficial de instalação: https://open-jarvis.github.io/OpenJarvis/getting-started/installation/
- Código oficial de descoberta de speech: `src/openjarvis/speech/_discovery.py`
- Código oficial de configuração: `src/openjarvis/core/config.py`
- Código oficial do Faster-Whisper: `src/openjarvis/speech/faster_whisper.py`

Pontos confirmados:

- O arquivo de configuração padrão fica em:

```bash
~/.openjarvis/config.toml
```

- Também é possível confirmar o caminho real com:

```bash
jarvis config path
```

- A seção correta para voz no `config.toml` é:

```toml
[speech]
```

- Os campos oficiais da seção `[speech]` são:

```toml
backend = "auto"
model = "base"
language = ""
device = "auto"
compute_type = "float16"
```

- Backends oficiais detectados automaticamente:

```text
faster-whisper
openai
deepgram
```

---

## 2. Importante: erro anterior corrigido

Não use YAML no `config.toml`.

Errado para `config.toml`:

```yaml
speech:
  stt:
    backend: faster-whisper
```

Isso dá erro porque `config.toml` usa sintaxe TOML, não YAML.

Correto para `config.toml`:

```toml
[speech]
backend = "faster-whisper"
model = "base"
device = "auto"
compute_type = "int8"
language = ""
```

---

## 3. Arquivo que deve ser editado

O arquivo padrão é:

```bash
~/.openjarvis/config.toml
```

Para abrir no terminal:

```bash
nano ~/.openjarvis/config.toml
```

Ou, antes, confirme o caminho real:

```bash
jarvis config path
```

Se você usa variável de ambiente como `OPENJARVIS_HOME`, o caminho pode mudar. Por isso, o comando `jarvis config path` é o mais seguro.

---

## 4. Configuração recomendada para Faster-Whisper local

Cole ou ajuste este bloco no `~/.openjarvis/config.toml`:

```toml
[speech]
backend = "faster-whisper"
model = "base"
device = "auto"
compute_type = "int8"
language = ""
```

Explicação rápida:

| Campo | Valor | Função |
|---|---|---|
| `backend` | `faster-whisper` | força o backend local |
| `model` | `base` | modelo Whisper local inicial |
| `device` | `auto` | deixa o OpenJarvis escolher CPU/GPU |
| `compute_type` | `int8` | mais leve para máquinas comuns |
| `language` | `""` | deixa detectar idioma automaticamente |

Se quiser tentar melhor qualidade e a máquina aguentar:

```toml
[speech]
backend = "faster-whisper"
model = "small"
device = "auto"
compute_type = "int8"
language = ""
```

Se ficar pesado:

```toml
[speech]
backend = "faster-whisper"
model = "tiny"
device = "auto"
compute_type = "int8"
language = ""
```

---

## 5. Alternativa sem editar o arquivo manualmente

Também dá para tentar configurar pelo próprio CLI:

```bash
jarvis config set speech.backend faster-whisper
jarvis config set speech.model base
jarvis config set speech.device auto
jarvis config set speech.compute_type int8
jarvis config set speech.language ""
```

Depois confira:

```bash
cat ~/.openjarvis/config.toml | grep -A 10 '\[speech\]'
```

---

## 6. Instalar ou confirmar Faster-Whisper

Se ainda não instalou os extras de voz/desktop:

```bash
cd ~/OpenJarvis
uv sync --extra desktop
```

Ou apenas o extra de speech:

```bash
cd ~/OpenJarvis
uv sync --extra speech
```

Teste se o pacote está disponível dentro do ambiente do OpenJarvis:

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

## 7. Rodar o servidor

Depois de ajustar o `config.toml`, reinicie o servidor:

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8000
```

No log, procure esta linha:

```text
Speech: faster-whisper
```

Se aparecer, o backend local de fala foi reconhecido pelo OpenJarvis.

Exemplo real:

```text
Energy: nvidia (polling)
Speech: faster-whisper
WARNING openjarvis.agents.scheduler: croniter not installed, treating cron as 3600s interval
Scheduler: active
Starting OpenJarvis API server
Engine: ollama
Model:  qwen3.5:2b
Agent:  orchestrator
URL:    http://127.0.0.1:8000
Uvicorn running on http://127.0.0.1:8000
```

Interpretação:

```text
Speech: faster-whisper = backend de voz carregado corretamente.
Uvicorn running = API do OpenJarvis subiu corretamente.
croniter not installed = aviso do scheduler, não é erro de voz.
```

---

## 8. Corrigir aviso `croniter not installed`

Esse aviso não impede a voz de funcionar:

```text
WARNING openjarvis.agents.scheduler: croniter not installed, treating cron as 3600s interval
```

Se quiser remover o aviso:

```bash
cd ~/OpenJarvis
uv add croniter
```

Depois reinicie:

```bash
uv run jarvis serve --host 127.0.0.1 --port 8000
```

---

## 9. Testar microfone no Linux antes da interface

Antes de culpar o OpenJarvis, confirme que o Linux grava áudio.

Instale ferramentas úteis:

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

Se não gravar, abra:

```bash
pavucontrol
```

Confira em **Input Devices**:

- microfone correto;
- volume de entrada;
- se não está mutado;
- se o navegador/app tem permissão de microfone.

---

## 10. Testar status da API

Com o servidor rodando em `127.0.0.1:8000`:

```bash
curl http://127.0.0.1:8000/health
```

Para procurar endpoints relacionados a speech na sua versão local:

```bash
curl http://127.0.0.1:8000/openapi.json | python3 -m json.tool | grep -i speech -n
```

Também pode abrir:

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

---

## 11. Se a interface mostra `Not configured`

Primeiro olhe o terminal.

Se o terminal mostra:

```text
Speech: faster-whisper
```

então o backend foi carregado pelo servidor.

Nesse caso, o problema provavelmente não é mais a instalação do Faster-Whisper. Verifique:

1. Permissão de microfone no navegador.
2. Se a interface está falando com a API certa em `http://127.0.0.1:8000`.
3. Se a interface foi recarregada depois de reiniciar o backend.
4. Se existe endpoint de speech na versão atual.

No navegador Chromium/Chrome/Edge:

```text
Clique no cadeado ao lado do endereço > Site settings > Microphone > Allow
```

Depois recarregue a interface.

---

## 12. Fluxo copy-paste completo

```bash
# 1. Entrar na pasta do projeto
cd ~/OpenJarvis

# 2. Instalar extras de desktop/speech
uv sync --extra desktop

# 3. Confirmar pacote local
uv run python - <<'PY'
import importlib.util
print('faster_whisper instalado:', importlib.util.find_spec('faster_whisper') is not None)
PY

# 4. Confirmar caminho do config
jarvis config path

# 5. Editar config
nano ~/.openjarvis/config.toml
```

Dentro do `config.toml`, colocar:

```toml
[speech]
backend = "faster-whisper"
model = "base"
device = "auto"
compute_type = "int8"
language = ""
```

Depois rodar:

```bash
uv run jarvis serve --host 127.0.0.1 --port 8000
```

Resultado esperado no log:

```text
Speech: faster-whisper
```

---

## 13. Roteiro curto para o vídeo

```text
A primeira coisa importante: o arquivo correto é ~/.openjarvis/config.toml. E ele usa TOML, não YAML. Então a configuração de voz não entra como speech: stt: backend. Ela entra como uma seção [speech].
```

```text
No meu caso, o backend local é o faster-whisper. Quando eu rodo jarvis serve e aparece Speech: faster-whisper no terminal, isso quer dizer que o OpenJarvis reconheceu o backend local de fala.
```

```text
Se mesmo assim a interface mostrar Not configured, eu não reinstalo o faster-whisper. Eu passo a verificar permissão de microfone, se a interface está apontando para a API correta e se os endpoints de speech aparecem no openapi.json.
```

---

## 14. Resumo final

O caminho correto é:

```text
Arquivo: ~/.openjarvis/config.toml
Seção: [speech]
Backend local: backend = "faster-whisper"
Log esperado: Speech: faster-whisper
```

Configuração principal:

```toml
[speech]
backend = "faster-whisper"
model = "base"
device = "auto"
compute_type = "int8"
language = ""
```
