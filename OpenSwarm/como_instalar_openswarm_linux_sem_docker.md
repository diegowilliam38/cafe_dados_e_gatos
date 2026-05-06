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
- Pelo menos uma API Key de IA

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

# 6. Configurar API Key

O OpenSwarm precisa de pelo menos uma chave de IA.

Exemplos:

## OpenAI

```bash
export OPENAI_API_KEY="SUA_CHAVE"
```

## Anthropic

```bash
export ANTHROPIC_API_KEY="SUA_CHAVE"
```

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

# APIs opcionais

O projeto também suporta integrações extras:

- Google
- Composio
- fal.ai
- Busca web
- Outras ferramentas externas

---

# Observação Importante

Este projeto NÃO é Docker Swarm.

O nome "OpenSwarm" aqui se refere ao framework multiagente da VRSEN.

---

# Método Alternativo: Clonando o Repositório

Se quiser rodar manualmente:

```bash
git clone https://github.com/VRSEN/OpenSwarm.git
cd OpenSwarm
python3 swarm.py
```

---

# Método Recomendado

Para a maioria das pessoas, o mais simples é:

```bash
sudo npm install -g @vrsen/openswarm
openswarm
```

---

# Projeto Oficial

GitHub:

https://github.com/VRSEN/OpenSwarm
