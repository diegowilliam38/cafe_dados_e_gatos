# Instalação do OpenSwarm pelo Git no Linux

Este passo a passo instala o OpenSwarm da VRSEN diretamente pelo repositório Git, usando ambiente virtual Python (`.venv`), sem Docker, sem Homebrew, sem instalação global via npm e sem `--break-system-packages`.

## 1. Limpar instalação anterior do repositório

```bash
cd ~
rm -rf ~/OpenSwarm
```

## 2. Instalar dependências básicas do sistema

```bash
sudo apt update
sudo apt install -y git python3.12 python3.12-venv python3-pip
```

## 3. Clonar o repositório oficial

```bash
git clone https://github.com/VRSEN/OpenSwarm.git
cd OpenSwarm
```

## 4. Criar o ambiente virtual Python

```bash
python3.12 -m venv .venv
```

## 5. Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

## 6. Atualizar ferramentas internas do Python

```bash
python -m pip install --upgrade pip setuptools wheel
```

## 7. Instalar o OpenSwarm e as dependências do projeto

```bash
python -m pip install -e .
```

## 8. Instalar suporte do Playwright para recursos de navegação/exportação

```bash
python -m playwright install --with-deps chromium
```

## 9. Criar o arquivo de configuração `.env`

```bash
cp .env.example .env
nano .env
```

## 10. Preencher as chaves mínimas no `.env`

Preencha pelo menos uma chave de provedor principal:

```env
OPENAI_API_KEY=sua_chave_openai_aqui
ANTHROPIC_API_KEY=sua_chave_anthropic_aqui
```

Depois defina o modelo padrão que será usado pelos agentes:

```env
DEFAULT_MODEL=gpt-5.5
```

Para recursos de imagem, vídeo, pesquisa e integrações, preencha também as chaves opcionais que você for usar:

```env
GOOGLE_API_KEY=sua_chave_google_aqui
FAL_KEY=sua_chave_fal_aqui
SEARCH_API_KEY=sua_chave_searchapi_aqui
COMPOSIO_API_KEY=sua_chave_composio_aqui
COMPOSIO_USER_ID=seu_user_id_composio_aqui
PEXELS_API_KEY=sua_chave_pexels_aqui
PIXABAY_API_KEY=sua_chave_pixabay_aqui
UNSPLASH_ACCESS_KEY=sua_chave_unsplash_aqui
```

Salvar no nano:

```text
CTRL + O
ENTER
CTRL + X
```

## 11. Rodar o OpenSwarm

Ainda dentro da pasta `~/OpenSwarm` e com o `.venv` ativo:

```bash
python swarm.py
```

## 12. Comandos básicos dentro do terminal do OpenSwarm

Listar agentes disponíveis:

```text
/agents
```

Referenciar arquivos locais no prompt:

```text
@caminho/do/arquivo
```

Exemplo de pedido inicial:

```text
Create a complete investor pitch for OpenSwarm with research, charts, slides, an executive summary, and a one-page document.
```

## 13. Como iniciar novamente depois

Quando quiser abrir o OpenSwarm em outro dia:

```bash
cd ~/OpenSwarm
source .venv/bin/activate
python swarm.py
```

## 14. Como atualizar o repositório depois

```bash
cd ~/OpenSwarm
source .venv/bin/activate
git pull
python -m pip install -e .
python swarm.py
```

