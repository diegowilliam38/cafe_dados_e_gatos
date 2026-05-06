# Como Instalar o OpenSwarm no Linux Sem Docker

Este guia mostra como instalar o OpenSwarm diretamente no Linux usando Node.js, sem Docker.

Repositório oficial:

https://github.com/VRSEN/OpenSwarm

---

# Requisitos

O OpenSwarm precisa de:

- Ubuntu/Linux
- Node.js 20+
- npm
- Pelo menos uma API Key de IA, como OpenAI ou Anthropic
- Opcionalmente, Ollama instalado para tentar usar modelos locais via LiteLLM

---

# 1. Atualizar o sistema

```bash
sudo apt update && sudo apt upgrade -y
```

---

# 2. Verificar Node.js e npm

```bash
node -v
npm -v
```

Se o Node for menor que 20 ou não estiver instalado, continue para o próximo passo.

---

# 3. Instalar Node.js 22 LTS

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
```

Verificar novamente:

```bash
node -v
npm -v
```

---

# 4. Instalar o OpenSwarm

Instalação global:

```bash
sudo npm install -g @vrsen/openswarm
```

---

# 5. Iniciar o OpenSwarm

```bash
openswarm
```

Na primeira execução, ele abrirá o assistente de configuração.

---

# 6. Configurar uma API Key

O OpenSwarm precisa de pelo menos uma chave de IA para funcionar com provedores em nuvem, como OpenAI ou Anthropic.

## 6.1. Como pegar uma chave da OpenAI

1. Acesse o painel da OpenAI.
2. Crie uma API Key.
3. Copie a chave.
4. No terminal Linux, rode:

```bash
export OPENAI_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Exemplo:

```bash
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxx"
```

Depois rode o OpenSwarm no mesmo terminal:

```bash
openswarm
```

Atenção: esse comando `export` vale apenas para o terminal atual. Se fechar o terminal, precisará exportar de novo.

---

## 6.2. Como pegar uma chave da Anthropic

1. Acesse o painel da Anthropic.
2. Crie uma API Key.
3. Copie a chave.
4. No terminal Linux, rode:

```bash
export ANTHROPIC_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Exemplo:

```bash
export ANTHROPIC_API_KEY="sk-ant-xxxxxxxxxxxxxxxxxxxxxxxx"
```

Depois rode o OpenSwarm no mesmo terminal:

```bash
openswarm
```

---

## 6.3. Como deixar a chave salva no Linux

Se quiser deixar a chave salva para não precisar digitar toda vez, adicione ao arquivo `~/.bashrc`.

Para OpenAI:

```bash
echo 'export OPENAI_API_KEY="COLE_SUA_CHAVE_AQUI"' >> ~/.bashrc
source ~/.bashrc
```

Para Anthropic:

```bash
echo 'export ANTHROPIC_API_KEY="COLE_SUA_CHAVE_AQUI"' >> ~/.bashrc
source ~/.bashrc
```

Depois confira se a variável foi carregada:

```bash
echo $OPENAI_API_KEY
```

ou:

```bash
echo $ANTHROPIC_API_KEY
```

Se aparecer a chave ou parte dela, está configurado.

Atenção: não compartilhe prints ou arquivos contendo sua API Key. Se a chave aparecer em vídeo ou print, revogue a chave no painel do provedor e gere outra.

---

# 7. Testar se está funcionando

Verificar se o comando existe:

```bash
which openswarm
```

Abrir ajuda:

```bash
openswarm --help
```

Iniciar:

```bash
openswarm
```

---

# 8. Como tentar usar Ollama no OpenSwarm

O README do OpenSwarm não documenta Ollama como caminho principal. Porém, o projeto usa roteamento de modelos via LiteLLM, então o caminho provável para usar Ollama é configurar o modelo local usando o padrão do LiteLLM.

## 8.1. Conferir se o Ollama está instalado

```bash
ollama --version
```

Se não estiver instalado, instale pelo comando oficial:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## 8.2. Iniciar o Ollama

Em um terminal:

```bash
ollama serve
```

Se o Ollama já estiver rodando como serviço, esse comando pode avisar que a porta já está em uso. Nesse caso, tudo bem.

---

## 8.3. Baixar um modelo local

Exemplo com Gemma:

```bash
ollama pull gemma3:4b
```

Testar o modelo:

```bash
ollama run gemma3:4b
```

---

## 8.4. Configurar o OpenSwarm para tentar usar Ollama

No terminal onde você vai rodar o OpenSwarm:

```bash
export DEFAULT_MODEL="litellm/ollama/gemma3:4b"
export OLLAMA_API_BASE="http://localhost:11434"
openswarm
```

Outra forma possível, dependendo da versão do LiteLLM/OpenSwarm:

```bash
export DEFAULT_MODEL="ollama/gemma3:4b"
export OLLAMA_API_BASE="http://localhost:11434"
openswarm
```

---

## 8.5. Observação importante sobre Ollama

O uso com Ollama pode depender da versão do OpenSwarm, do LiteLLM e da forma como o projeto carrega o modelo padrão.

Se não funcionar de primeira, teste primeiro com uma chave de OpenAI ou Anthropic para confirmar que o OpenSwarm está funcionando. Depois tente trocar para Ollama.

---

# 9. APIs opcionais

O projeto também suporta integrações extras, dependendo da configuração:

- Google
- Composio
- fal.ai
- Busca web
- Outras ferramentas externas

---

# 10. Observação Importante

Este projeto NÃO é Docker Swarm.

O nome "OpenSwarm" aqui se refere ao framework multiagente da VRSEN.

---

# 11. Método Alternativo: Clonando o Repositório

Se quiser rodar manualmente:

```bash
git clone https://github.com/VRSEN/OpenSwarm.git
cd OpenSwarm
python3 swarm.py
```

---

# 12. Método Recomendado

Para a maioria das pessoas, o mais simples é:

```bash
sudo npm install -g @vrsen/openswarm
openswarm
```

---

# Projeto Oficial

GitHub:

https://github.com/VRSEN/OpenSwarm
