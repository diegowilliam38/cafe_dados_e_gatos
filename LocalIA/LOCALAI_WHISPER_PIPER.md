# Como instalar o LocalAI no Windows com WSL2 + Docker e testar Whisper + Piper

## 1. Objetivo

Rodar o LocalAI no Windows usando WSL2 + Docker Desktop e testar duas funções de voz:

- Whisper: áudio para texto.
- Piper: texto para áudio.

O foco deste teste é CPU-only, ou seja, sem GPU dedicada.

## 2. Ambiente deste guia

Este guia é para:

- Windows 10 ou Windows 11.
- WSL2 instalado.
- Ubuntu instalado dentro do WSL2.
- Docker Desktop instalado no Windows.
- Integração do Docker Desktop com WSL2 ativada.

Todos os comandos deste guia devem ser executados dentro do Ubuntu/WSL, não no PowerShell.

## 3. Conferir se o Docker está funcionando no WSL

Dentro do Ubuntu/WSL, rode:

```bash
docker --version
```

```bash
docker compose version
```

```bash
docker run hello-world
```

Se o `hello-world` funcionar, o Docker Desktop está integrado ao WSL corretamente.

## 4. Criar a pasta do teste

```bash
mkdir -p ~/localai-teste/models
cd ~/localai-teste
```

## 5. Criar o docker-compose.yml

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

## 6. Subir o LocalAI

```bash
docker compose up -d
```

## 7. Ver os logs

```bash
docker logs -f local-ai
```

Quando terminar de iniciar, o LocalAI deve ficar disponível em:

```text
http://localhost:8080
```

## 8. Testar se a API está respondendo

```bash
curl http://localhost:8080/readyz
```

```bash
curl http://localhost:8080/v1/models
```

## 9. Abrir a interface web no Windows

No navegador do Windows, acesse:

```text
http://localhost:8080
```

Na aba de modelos, instalar um modelo de transcrição e um modelo de TTS se estiverem disponíveis pela galeria.

Observação: os nomes dos modelos podem mudar. O próprio LocalAI avisa na documentação que nomes como `whisper-1` e `tts-1` são exemplos e devem ser trocados pelo nome real do modelo instalado.

## 10. Teste do Whisper: áudio para texto

Baixar um áudio de exemplo dentro do Ubuntu/WSL:

```bash
cd ~/localai-teste
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

## 11. Teste do Piper: texto para voz

Baixar uma voz brasileira simples do Piper dentro da pasta de modelos:

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

## 12. Abrir o áudio gerado no Windows

Como o comando está rodando no WSL, o jeito mais simples é abrir a pasta atual no Windows Explorer:

```bash
explorer.exe .
```

Depois abra o arquivo:

```text
frank-piper.wav
```

## 13. Teste do endpoint OpenAI-compatible de TTS

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

Para abrir o arquivo gerado no Windows:

```bash
explorer.exe .
```

## 14. Parar o LocalAI

```bash
cd ~/localai-teste
docker compose down
```

## 15. Remover tudo do teste

Atenção: este comando apaga a pasta do teste e os modelos baixados.

```bash
cd ~
docker compose -f ~/localai-teste/docker-compose.yml down 2>/dev/null || true
docker rm -f local-ai 2>/dev/null || true
rm -rf ~/localai-teste
```

## 16. Fala curta para o vídeo

```text
Neste teste eu estou usando Windows com WSL2 e Docker Desktop. O LocalAI roda em container, mas os comandos são executados dentro do Ubuntu/WSL. A ideia não é transformar o LocalAI no cérebro principal do Robô Frank. No meu caso, com hardware mais limitado, faz mais sentido usar ele como uma peça auxiliar: transcrição com Whisper, voz com Piper e talvez embeddings ou modelos pequenos. O raciocínio pesado pode continuar em outro modelo, mas a parte de voz pode ficar local, privada e sem API paga.
```

## 17. Fontes oficiais

- https://github.com/mudler/LocalAI
- https://localai.io/installation/
- https://localai.io/features/audio-to-text/
- https://localai.io/features/text-to-audio/
- https://localai.io/models/
