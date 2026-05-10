# Como instalar o LocalAI no Windows com WSL2 + Docker e testar o Phi-2

## 1. Objetivo

Rodar o LocalAI no Windows usando WSL2 + Docker Desktop e validar a instalação usando um modelo local leve.

Neste guia vamos usar:

- Phi-2 GGUF
- CPU-only
- Docker
- WSL2

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

## 11. Criar o arquivo de configuração do modelo

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

## 14. Testar chat/completions

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

## 15. Abrir a interface web no navegador

No Windows:

```text
http://localhost:8080
```

## 16. Parar o LocalAI

```bash
cd ~/localai-teste
docker compose down
```

## 17. Remover tudo do teste

Atenção: este comando apaga a pasta do teste e os modelos baixados.

```bash
cd ~
docker compose -f ~/localai-teste/docker-compose.yml down 2>/dev/null || true
docker rm -f local-ai 2>/dev/null || true
rm -rf ~/localai-teste
```

## 18. Fala curta para o vídeo

```text
Neste teste eu estou usando Windows com WSL2 e Docker Desktop. O LocalAI roda em container, mas os comandos são executados dentro do Ubuntu/WSL. Para validar a instalação, estou usando um modelo pequeno e leve, o Phi-2. A ideia aqui não é competir com modelos gigantes na nuvem, mas mostrar que hoje já existe IA local funcionando em hardware comum e até sem GPU dedicada.
```

## 19. Observação importante para o vídeo

```text
Instalar o LocalAI não instala automaticamente modelos. Primeiro o servidor sobe. Depois você baixa e configura os modelos que quer usar. Se chamar um modelo antes de instalar ou configurar, o LocalAI responde que o modelo não foi encontrado. Isso é normal.
```

## 20. Fontes oficiais

- https://github.com/mudler/LocalAI
- https://localai.io/installation/
- https://localai.io/models/
- https://localai.io/getting-started/models/
