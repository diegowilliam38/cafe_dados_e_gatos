# Como instalar o LocalAI e testar Whisper + Piper

## 1. Objetivo

Rodar o LocalAI localmente, sem depender de API externa, e testar duas funções de voz:

- Whisper: áudio para texto.
- Piper: texto para áudio.

O foco deste teste é CPU-only, ou seja, sem GPU dedicada.

## 2. Requisitos

- Linux ou WSL2 com Docker instalado.
- Docker funcionando.
- Internet para baixar imagens e modelos.
- Espaço em disco para modelos.

## 3. Criar a pasta do teste

```bash
mkdir -p ~/localai-teste/models
cd ~/localai-teste
```

## 4. Criar o docker-compose.yml

```bash
cat > docker-compose.yml <<'EOF_DOCKER'
services:
  localai:
    image: localai/localai:latest
    container_name: local-ai
    ports:
      - "8080:8080"
    volumes:
      - ./models:/models
    environment:
      - DEBUG=true
    restart: unless-stopped
EOF_DOCKER
```

## 5. Subir o LocalAI

```bash
docker compose up -d
```

## 6. Ver os logs

```bash
docker logs -f local-ai
```

Quando terminar de iniciar, o LocalAI deve ficar disponível em:

```text
http://localhost:8080
```

## 7. Testar se a API está respondendo

```bash
curl http://localhost:8080/readyz
```

```bash
curl http://localhost:8080/v1/models
```

## 8. Abrir a interface web

No navegador:

```text
http://localhost:8080
```

Na aba de modelos, instalar um modelo de transcrição e um modelo de TTS se estiverem disponíveis pela galeria.

Observação: os nomes dos modelos podem mudar. O próprio LocalAI avisa na documentação que nomes como `whisper-1` e `tts-1` são exemplos e devem ser trocados pelo nome real do modelo instalado.

## 9. Teste do Whisper: áudio para texto

Baixar um áudio de exemplo:

```bash
wget --quiet --show-progress -O gb1.ogg https://upload.wikimedia.org/wikipedia/commons/1/1f/George_W_Bush_Columbia_FINAL.ogg
```

Enviar para o endpoint de transcrição:

```bash
curl http://localhost:8080/v1/audio/transcriptions \
  -H "Content-Type: multipart/form-data" \
  -F file="@$PWD/gb1.ogg" \
  -F model="whisper-1"
```

Se der erro de modelo não encontrado, listar os modelos disponíveis:

```bash
curl http://localhost:8080/v1/models
```

Depois repetir o comando trocando `whisper-1` pelo nome real do modelo instalado.

## 10. Teste do Piper: texto para voz

Baixar voz brasileira simples do Piper:

```bash
cd ~/localai-teste/models
wget -O pt_BR-edresson-low.onnx "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/pt/pt_BR/edresson/low/pt_BR-edresson-low.onnx?download=true"
wget -O pt_BR-edresson-low.onnx.json "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/pt/pt_BR/edresson/low/pt_BR-edresson-low.onnx.json?download=true"
cd ~/localai-teste
```

Testar TTS com endpoint `/tts`:

```bash
curl http://localhost:8080/tts \
  -H "Content-Type: application/json" \
  -d '{
    "model": "pt_BR-edresson-low.onnx",
    "backend": "piper",
    "input": "Olá, eu sou o Robô Frank falando localmente com Piper e LocalAI."
  }' \
  --output frank-piper.wav
```

Tocar o áudio no Linux:

```bash
aplay frank-piper.wav
```

Se estiver no WSL e o áudio não tocar pelo terminal, copie o arquivo para o Windows e abra com o player:

```bash
explorer.exe .
```

## 11. Teste do endpoint OpenAI-compatible de TTS

```bash
curl http://localhost:8080/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1",
    "input": "Teste de voz local usando endpoint compatível com OpenAI.",
    "voice": "alloy"
  }' \
  --output speech.mp3
```

Se der erro de modelo não encontrado, use o teste com `/tts` e Piper manual da etapa anterior.

## 12. Parar o LocalAI

```bash
cd ~/localai-teste
docker compose down
```

## 13. Remover tudo do teste

Atenção: este comando apaga a pasta do teste e os modelos baixados.

```bash
cd ~
docker compose -f ~/localai-teste/docker-compose.yml down 2>/dev/null || true
docker rm -f local-ai 2>/dev/null || true
rm -rf ~/localai-teste
```

## 14. Fala curta para o vídeo

```text
O LocalAI não precisa ser o cérebro principal do Robô Frank. No meu caso, com hardware mais limitado, faz mais sentido usar ele como uma peça auxiliar: transcrição com Whisper, voz com Piper e talvez embeddings ou modelos pequenos. O raciocínio pesado pode continuar em outro modelo, mas a parte de voz pode ficar local, privada e sem API paga.
```

## 15. Fontes oficiais

- https://github.com/mudler/LocalAI
- https://localai.io/installation/
- https://localai.io/features/audio-to-text/
- https://localai.io/features/text-to-audio/
- https://localai.io/models/
