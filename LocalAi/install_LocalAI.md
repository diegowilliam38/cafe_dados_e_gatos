# Como instalar e remover o LocalAI no Windows com WSL2 + Docker

## 1. Objetivo

Instalar o LocalAI no Windows usando WSL2 + Docker Desktop.

Este guia contém apenas:

- preparação do ambiente
- instalação do LocalAI
- verificação básica
- acesso pela interface web
- parada do container
- remoção completa do teste

## 2. Ambiente usado

Este guia é para:

- Windows 10 ou Windows 11
- WSL2 instalado
- Ubuntu instalado dentro do WSL2
- Docker Desktop instalado no Windows
- integração do Docker Desktop com WSL2 ativada

Todos os comandos abaixo devem ser executados dentro do Ubuntu/WSL, não no PowerShell.

## 3. Conferir se o Docker está funcionando no WSL

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

## 4. Criar a pasta do LocalAI

```bash
mkdir -p ~/localai-teste/models
cd ~/localai-teste
```

## 5. Criar o arquivo docker-compose.yml

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

Para sair dos logs sem parar o container:

```text
CTRL + C
```

## 8. Testar se o LocalAI está respondendo

```bash
curl http://localhost:8080/readyz
```

Também é possível listar os modelos instalados:

```bash
curl http://localhost:8080/v1/models
```

Se vier vazio, é normal. Isso significa que o servidor subiu, mas ainda não há modelos instalados.

## 9. Abrir a interface web no Windows

No navegador do Windows, acesse:

```text
http://localhost:8080
```

## 10. Parar o LocalAI

```bash
cd ~/localai-teste
docker compose down
```

## 11. Subir novamente depois

```bash
cd ~/localai-teste
docker compose up -d
```

## 12. Remover tudo do teste

Atenção: este comando apaga o container e a pasta do teste, incluindo modelos baixados dentro de `~/localai-teste/models`.

```bash
cd ~
docker compose -f ~/localai-teste/docker-compose.yml down 2>/dev/null || true
docker rm -f local-ai 2>/dev/null || true
rm -rf ~/localai-teste
```

## 13. Limpeza opcional do Docker

Atenção: este comando remove imagens, containers parados, cache e recursos Docker não utilizados.

Use apenas se quiser limpar o ambiente de teste.

```bash
docker system prune -a
```

## 14. Fontes oficiais

- https://github.com/mudler/LocalAI
- https://localai.io/installation/
- https://localai.io/models/
