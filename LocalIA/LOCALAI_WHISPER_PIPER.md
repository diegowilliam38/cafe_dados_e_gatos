# Como instalar o LocalAI no Windows com WSL2 + Docker e testar 3 modelos

## 1. Objetivo

Rodar o LocalAI no Windows usando WSL2 + Docker Desktop e validar a instalação usando 3 modelos instalados pela galeria:

- dolphin3.0-llama3.2-1b: modelo LLM leve para texto.
- moonshine-tiny: modelo STT para áudio em texto.
- vibevoice-cpp: modelo TTS para texto em voz.

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

Se `/v1/models` vier vazio, isso é normal em uma instalação nova. O LocalAI subiu, mas ainda não tem modelos instalados.

## 9. Abrir a interface web no Windows

No navegador do Windows, acesse:

```text
http://localhost:8080
```

A interface web será usada para instalar os modelos pela galeria.

## 10. Instalar os 3 modelos pela galeria

Na interface web do LocalAI, abra a Model Gallery.

Instale estes 3 modelos:

```text
dolphin3.0-llama3.2-1b
```

```text
moonshine-tiny
```

```text
vibevoice-cpp
```

Depois confira se os modelos aparecem na API:

```bash
curl http://localhost:8080/v1/models
```

O retorno esperado deve conter algo parecido com:

```text
dolphin3.0-llama3.2-1b
moonshine-tiny
vibevoice-cpp
```

Use sempre exatamente o nome que aparecer em `/v1/models`.

## 11. Testar o modelo LLM dolphin3.0-llama3.2-1b

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "dolphin3.0-llama3.2-1b",
    "messages": [
      {
        "role": "user",
        "content": "Explique em português o que é um servidor local de IA em 3 frases simples."
      }
    ],
    "temperature": 0.7
  }'
```

## 12. Baixar áudio de exemplo para testar STT

O modelo `moonshine-tiny` transforma áudio em texto.

Baixar um áudio de exemplo dentro do Ubuntu/WSL:

```bash
cd ~/localai-teste
wget --quiet --show-progress -O gb1.ogg https://upload.wikimedia.org/wikipedia/commons/1/1f/George_W_Bush_Columbia_FINAL.ogg
```

## 13. Testar STT com moonshine-tiny

```bash
curl http://localhost:8080/v1/audio/transcriptions \
  -H "Content-Type: multipart/form-data" \
  -F file="@$PWD/gb1.ogg" \
  -F model="moonshine-tiny"
```

Se der erro de modelo não encontrado, confira o nome exato:

```bash
curl http://localhost:8080/v1/models
```

Depois repita o comando trocando `moonshine-tiny` pelo nome real listado.

## 14. Testar TTS com vibevoice-cpp

O modelo `vibevoice-cpp` transforma texto em voz.

```bash
cd ~/localai-teste
curl http://localhost:8080/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{
    "model": "vibevoice-cpp",
    "input": "Olá, eu sou o Robô Frank falando localmente pelo LocalAI."
  }' \
  --output voz-vibevoice.mp3
```

## 15. Abrir o áudio gerado no Windows

Como o comando está rodando no WSL, o jeito mais simples é abrir a pasta atual no Windows Explorer:

```bash
explorer.exe .
```

Depois abra o arquivo:

```text
voz-vibevoice.mp3
```

## 16. Se algum teste der erro

Liste os modelos instalados:

```bash
curl http://localhost:8080/v1/models
```

Use exatamente o nome que aparecer no campo `id`.

Exemplo:

```text
dolphin3.0-llama3.2-1b
moonshine-tiny
vibevoice-cpp
```

Se o nome estiver diferente, troque no comando.

## 17. Parar o LocalAI

```bash
cd ~/localai-teste
docker compose down
```

## 18. Remover tudo do teste

Atenção: este comando apaga a pasta do teste e os modelos baixados.

```bash
cd ~
docker compose -f ~/localai-teste/docker-compose.yml down 2>/dev/null || true
docker rm -f local-ai 2>/dev/null || true
rm -rf ~/localai-teste
```

## 19. Fala curta para o vídeo

```text
Neste teste eu estou usando Windows com WSL2 e Docker Desktop. O LocalAI roda em container, mas os comandos são executados dentro do Ubuntu/WSL. Primeiro eu instalo um modelo pequeno de texto, o dolphin3.0-llama3.2-1b. Depois testo áudio para texto com moonshine-tiny e texto para voz com vibevoice-cpp. A ideia não é competir com modelos gigantes na nuvem, mas mostrar que hoje já existe IA local multimodal funcionando em hardware comum e até sem GPU dedicada.
```

## 20. Observação importante para o vídeo

```text
Instalar o LocalAI não instala automaticamente modelos. Primeiro o servidor sobe. Depois você baixa e configura os modelos que quer usar. Se chamar um modelo antes de instalar ou configurar, o LocalAI responde que o modelo não foi encontrado. Isso é normal.
```

## 21. Fontes oficiais

- https://github.com/mudler/LocalAI
- https://localai.io/installation/
- https://localai.io/models/
- https://localai.io/getting-started/models/
- https://localai.io/features/audio-to-text/
- https://localai.io/features/text-to-audio/
