# Como instalar o LocalAI no Windows com WSL2 + Docker e testar Phi-2 e TTS

## 1. Objetivo

Rodar o LocalAI no Windows usando WSL2 + Docker Desktop e validar a instalação usando:

- Phi-2 GGUF: modelo local leve para texto.
- vits-ljs-sherpa: modelo TTS leve para texto em voz.
- qwen3-tts-cpp: modelo TTS mais avançado para texto em voz.
- CPU-only.
- Docker.
- WSL2.

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

A interface web também pode ser usada para procurar, baixar e gerenciar modelos.

## 10. Baixar modelo local Phi-2

Este é o teste mais simples para confirmar que o LocalAI está respondendo como servidor local de IA.

Baixar o modelo Phi-2 em formato GGUF:

```bash
cd ~/localai-teste/models
wget -O phi-2.Q4_K_M.gguf \
https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf
```

## 11. Criar o arquivo de configuração do modelo Phi-2

```bash
cat > ~/localai-teste/models/phi-2.yaml <<'EOF_PHI'
name: phi-2
parameters:
  model: phi-2.Q4_K_M.gguf
  temperature: 0.7
context_size: 2048
threads: 4
backend: llama-cpp
EOF_PHI
```

## 12. Reiniciar o LocalAI

```bash
cd ~/localai-teste
docker compose restart
```

## 13. Conferir se o modelo apareceu

```bash
curl http://localhost:8080/v1/models
```

O modelo esperado deve aparecer como:

```text
phi-2
```

## 14. Testar chat/completions com Phi-2

```bash
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi-2",
    "messages": [
      {
        "role": "user",
        "content": "Explique em português o que é um servidor local de IA em 3 frases simples."
      }
    ],
    "temperature": 0.7
  }'
```

## 15. Instalar modelos TTS pela galeria

Na interface web do LocalAI:

```text
http://localhost:8080
```

Clique no filtro:

```text
TTS
```

Instale estes dois modelos pela galeria:

```text
vits-ljs-sherpa
```

```text
qwen3-tts-cpp
```

Depois confira se eles aparecem na API:

```bash
curl http://localhost:8080/v1/models
```

Use exatamente o nome que aparecer na lista.

## 16. Testar TTS com vits-ljs-sherpa

```bash
cd ~/localai-teste
curl http://localhost:8080/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{
    "model": "vits-ljs-sherpa",
    "input": "Hello, this is a local voice test running inside LocalAI."
  }' \
  --output voz-vits.mp3
```

Abrir a pasta no Windows:

```bash
explorer.exe .
```

Depois abra o arquivo:

```text
voz-vits.mp3
```

## 17. Testar TTS com qwen3-tts-cpp

```bash
cd ~/localai-teste
curl http://localhost:8080/v1/audio/speech \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-tts-cpp",
    "input": "Olá, eu sou o Robô Frank falando pelo LocalAI em um teste local de texto para voz."
  }' \
  --output voz-qwen3.mp3
```

Abrir a pasta no Windows:

```bash
explorer.exe .
```

Depois abra o arquivo:

```text
voz-qwen3.mp3
```

## 18. Se o TTS der erro

Liste os modelos instalados:

```bash
curl http://localhost:8080/v1/models
```

Se o nome estiver diferente, troque no comando.

Exemplo:

```text
qwen3-tts-cpp
```

pode aparecer com outro nome dependendo da versão da galeria.

## 19. Parar o LocalAI

```bash
cd ~/localai-teste
docker compose down
```

## 20. Remover tudo do teste

Atenção: este comando apaga a pasta do teste e os modelos baixados.

```bash
cd ~
docker compose -f ~/localai-teste/docker-compose.yml down 2>/dev/null || true
docker rm -f local-ai 2>/dev/null || true
rm -rf ~/localai-teste
```

## 21. Fala curta para o vídeo

```text
Neste teste eu estou usando Windows com WSL2 e Docker Desktop. O LocalAI roda em container, mas os comandos são executados dentro do Ubuntu/WSL. Primeiro eu valido o servidor com um modelo pequeno de texto, o Phi-2. Depois eu testo dois modelos de voz pela própria galeria do LocalAI: um TTS mais simples, o vits-ljs-sherpa, e outro mais avançado, o qwen3-tts-cpp. A ideia não é competir com modelos gigantes na nuvem, mas mostrar que hoje já existe IA local multimodal funcionando em hardware comum e até sem GPU dedicada.
```

## 22. Observação importante para o vídeo

```text
Instalar o LocalAI não instala automaticamente modelos. Primeiro o servidor sobe. Depois você baixa e configura os modelos que quer usar. Se chamar um modelo antes de instalar ou configurar, o LocalAI responde que o modelo não foi encontrado. Isso é normal.
```

## 23. Fontes oficiais

- https://github.com/mudler/LocalAI
- https://localai.io/installation/
- https://localai.io/models/
- https://localai.io/getting-started/models/
- https://localai.io/features/text-to-audio/
