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
- Python 3.12
- Pacote `python3.12-venv`
- Pelo menos uma API Key de IA, como OpenAI ou Anthropic

---

# 1. Atualizar o sistema

```bash
sudo apt update && sudo apt upgrade -y
```

Observação: durante o `apt upgrade`, o Linux pode atualizar pacotes que já existem no sistema, inclusive Docker. Isso não significa que o OpenSwarm instalou ou criou Docker. Foi apenas uma atualização do sistema.

---

# 2. Verificar Node.js e npm

```bash
node -v
npm -v
```

O OpenSwarm precisa de Node.js 20 ou superior.

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

# 4. Verificar Python

O OpenSwarm cria um projeto baseado em Agency Swarm e usa um ambiente virtual Python (`.venv`).

Verifique a versão do Python:

```bash
python3 --version
```

No teste feito em Ubuntu, o sistema detectou:

```bash
Python 3.12
```

Se o Python 3.12 já estiver instalado, siga para o próximo passo.

---

# 5. Instalar Python 3.12 e venv

Em algumas instalações do Ubuntu, o Python já vem instalado, mas o pacote para criar ambiente virtual não vem.

Instale os pacotes necessários:

```bash
sudo apt install -y python3.12 python3.12-venv python3-pip
```

Se aparecer erro dizendo que `python3.12-venv` não está disponível, tente:

```bash
sudo apt update
sudo apt install -y python3-venv python3-pip
```

Verifique novamente:

```bash
python3 --version
```

---

# 6. Instalar o OpenSwarm

Instalação global:

```bash
sudo npm install -g @vrsen/openswarm
```

Se aparecer algo como:

```bash
added 110 packages
```

significa que a instalação global foi concluída.

---

# 7. Criar uma pasta limpa para o projeto

```bash
cd ~
mkdir -p ~/openswarm-teste
cd ~/openswarm-teste
```

---

# 8. Iniciar o OpenSwarm

```bash
openswarm
```

Na primeira execução, ele abrirá o assistente de configuração.

Quando perguntar como começar, escolha:

```text
Create a new starter project
```

Quando perguntar se deseja criar um `.venv`, escolha:

```text
Yes
```

Se aparecer erro parecido com:

```text
The virtual environment was not created successfully because ensurepip is not available.
On Debian/Ubuntu systems, you need to install the python3.12-venv package.
```

corrija com:

```bash
sudo apt install -y python3.12-venv
```

Depois volte para a pasta do projeto e rode novamente:

```bash
cd ~/openswarm-teste
openswarm
```

---

# 9. Configurar uma API Key

O OpenSwarm precisa de pelo menos uma chave de IA para funcionar com provedores em nuvem, como OpenAI ou Anthropic.

## 9.1. Como configurar chave da OpenAI

No terminal Linux, rode:

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

## 9.2. Como configurar chave da Anthropic

No terminal Linux, rode:

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

## 9.3. Como deixar a chave salva no Linux

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

Atenção: não compartilhe prints ou arquivos contendo sua API Key. Se a chave aparecer em vídeo ou print, revogue a chave no painel do provedor e gere outra.

---

# 10. Testar se está funcionando

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

Se a interface abrir com o logo `AGENTSWARM` e aparecer uma caixa `Ask anything...`, o ambiente subiu corretamente.

---


# 11. Erro comum: servidor local indisponível

Se aparecer algo como:

```text
http://127.0.0.1:8000 Unavailable
http://127.0.0.1:8080 Unavailable
```

significa que a interface está tentando conectar a um servidor local que não está rodando.

Nesse caso, volte e escolha:

```text
Create a new starter project
```

em vez de:

```text
Connect to an existing agency
```

---

# 12. Como remover completamente o teste

Para remover o OpenSwarm e apagar as configurações criadas no teste:

```bash
cd ~
sudo npm uninstall -g @vrsen/openswarm
```

Apagar projetos criados:

```bash
rm -rf ~/cafe_com_dados_e_gatos
rm -rf ~/openswarm-teste
```

Apagar possíveis configurações/cache:

```bash
rm -rf ~/.config/agent-swarm
rm -rf ~/.local/share/agent-swarm
rm -rf ~/.cache/agent-swarm
rm -rf ~/.agent-swarm
rm -rf ~/.agency-swarm
rm -rf ~/.openswarm
```

Procurar sobras:

```bash
find ~ -maxdepth 3 -iname "*openswarm*" -o -iname "*agent-swarm*" -o -iname "*agency-swarm*"
```

Se aparecer alguma pasta que você reconhece como sobra do teste, apague com cuidado usando:

```bash
rm -rf CAMINHO_DA_PASTA
```


---

# 13. APIs opcionais

O projeto também suporta integrações extras, dependendo da configuração:

- Google
- Composio
- fal.ai
- Busca web
- Outras ferramentas externas

---

# 14. Observação importante

Este projeto NÃO é Docker Swarm.

O nome "OpenSwarm" aqui se refere ao framework multiagente da VRSEN.

---

# 15. Método alternativo: clonando o repositório

Se quiser rodar manualmente:

```bash
git clone https://github.com/VRSEN/OpenSwarm.git
cd OpenSwarm
python3 swarm.py
```

---

# 16. Método recomendado

Para a maioria das pessoas, o mais simples é:

```bash
sudo npm install -g @vrsen/openswarm
openswarm
```

---

---

# 17. Como adicionar um gerador de imagens

Durante o teste, o OpenSwarm subiu com o agente padrão:

```text
ExampleAgent
```

Esse agente padrão não gera imagem diretamente. Ele apenas transforma o pedido do usuário em um prompt pronto para ser usado em outro gerador de imagens.

Exemplo do comportamento observado:

```text
Usuário pede: crie uma imagem de um gato em uma xícara com o texto Café com Dados e Gatos

OpenSwarm responde: Aqui vai um prompt pronto para gerar essa imagem em um gerador de imagens.
```

Ou seja: até esse ponto, o fluxo é:

```text
Pedido de imagem -> OpenSwarm melhora o prompt -> usuário copia o prompt -> cola em uma IA de imagem
```

Para o OpenSwarm gerar a imagem diretamente, é necessário conectar uma ferramenta/provedor de imagem.

O projeto menciona suporte a agentes/ferramentas de imagem como:

- fal.ai
- Google/Gemini Image
- Gemini 2.5 Flash Image
- Gemini 3 Pro Image
- Outras ferramentas externas compatíveis com Agency Swarm

---

## 17.1. Verificar arquivos criados pelo projeto

Saia da interface com:

```bash
Ctrl + C
```

Entre na pasta do projeto:

```bash
cd ~/cafe_com_dados_e_gatos
```

Liste os arquivos relacionados a configuração, agentes e ferramentas:

```bash
find . -maxdepth 4 -type f | grep -Ei "env|agent|tool|config|image|fal|gemini|google"
```

Se quiser listar todos os arquivos do projeto:

```bash
find . -maxdepth 4 -type f
```

---

## 17.2. Configurar chave da fal.ai

Se o projeto tiver um arquivo `.env`, abra:

```bash
nano .env
```

Adicione a chave da fal.ai:

```bash
FAL_KEY="SUA_CHAVE_FAL_AQUI"
```

Salve com:

```text
Ctrl + O
Enter
Ctrl + X
```

Depois rode novamente:

```bash
openswarm
```

---

## 17.3. Configurar chave do Google/Gemini

Se for usar Google/Gemini Image, abra o `.env`:

```bash
nano .env
```

Adicione:

```bash
GOOGLE_API_KEY="SUA_CHAVE_GOOGLE_AQUI"
GEMINI_API_KEY="SUA_CHAVE_GOOGLE_AQUI"
```

Salve com:

```text
Ctrl + O
Enter
Ctrl + X
```

Depois rode novamente:

```bash
openswarm
```

---

## 17.4. Observação importante

Só colocar a chave no `.env` pode não ser suficiente.

Se o projeto criado pelo OpenSwarm veio apenas com o `ExampleAgent`, ele pode continuar apenas criando prompts, mesmo com as chaves configuradas.

Nesse caso, será necessário editar os arquivos do agente e adicionar uma ferramenta/agente de geração de imagens.

Para descobrir qual arquivo editar, rode:

```bash
cd ~/cafe_com_dados_e_gatos
find . -maxdepth 4 -type f
```

Depois procure arquivos relacionados a:

```text
agent
tools
agency
config
```

A partir desses arquivos, é possível adicionar uma ferramenta de imagem ao agente.

---

## 17.5. Diagnóstico rápido

Se ao pedir uma imagem o OpenSwarm responder apenas com um texto como:

```text
Aqui vai um prompt pronto para gerar essa imagem em um gerador de imagens
```

então ele ainda não está gerando imagem.

Ele está apenas funcionando como:

```text
Gerador de prompt de imagem
```

Para virar um gerador de imagem real, precisa de:

```text
API de imagem + ferramenta configurada + agente usando essa ferramenta
```

# Projeto oficial

GitHub:

https://github.com/VRSEN/OpenSwarm
