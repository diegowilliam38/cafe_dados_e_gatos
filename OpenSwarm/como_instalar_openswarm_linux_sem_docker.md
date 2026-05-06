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


# 18. Como adicionar um gerador de imagens

Durante o teste, o OpenSwarm subiu com o agente padrão:

```text
ExampleAgent
```

Esse agente padrão não gerou imagem diretamente. Ele apenas transformou o pedido da imagem em um prompt pronto para ser usado em outro gerador de imagens.

Exemplo do comportamento observado:

```text
Usuário pede: crie uma imagem de um gato em uma xícara com o texto Café com Dados e Gatos

OpenSwarm responde: Aqui vai um prompt pronto para gerar essa imagem em um gerador de imagens.
```

Ou seja, até esse ponto, o fluxo foi:

```text
Pedido de imagem -> OpenSwarm melhora o prompt -> usuário copia o prompt -> cola em uma IA de imagem
```

Para o OpenSwarm gerar imagem diretamente, é necessário conectar uma ferramenta/provedor de imagem ao agente.

---

## 18.1. O que a documentação do OpenSwarm menciona

No repositório oficial, o OpenSwarm menciona suporte a recursos de imagem/vídeo usando chaves opcionais.

No `.env.example`, aparece:

```bash
# Google AI / Gemini — used for image generation, editing, and composition
# (Gemini 2.5 Flash Image, Gemini 3 Pro Image)
GOOGLE_API_KEY=
```

Também aparece:

```bash
# fal.ai — used for video generation, editing, and background removal
FAL_KEY=
```

Então, pela documentação do projeto, as chaves importantes para recursos visuais são:

```bash
GOOGLE_API_KEY
FAL_KEY
```

Atenção: no teste feito, o menu de autenticação principal mostrou apenas:

```text
OpenAI
Anthropic
```

Isso não significa que o projeto não tenha suporte a Google. Significa apenas que, no starter project testado, o Google/Gemini não apareceu como opção direta no menu de autenticação principal.

---

## 18.2. Configurar chave Google/Gemini

O método mais simples e recomendado para testes rápidos é configurar a chave diretamente no terminal Linux ANTES de abrir o OpenSwarm.

Método rápido:

```bash
export GOOGLE_API_KEY="SUA_CHAVE_GOOGLE_AI_STUDIO_AQUI"
openswarm
```

Exemplo:

```bash
export GOOGLE_API_KEY="AIzaxxxxxxxxxxxxxxxx"
openswarm
```

Importante:

- O comando `export` vale apenas para o terminal atual.
- Se fechar o terminal, precisará executar novamente.
- Esse foi o método mais simples usado durante o teste.

---

### Como verificar se a chave carregou

```bash
echo $GOOGLE_API_KEY
```

Se aparecer a chave, a variável foi carregada corretamente.

---

### Como deixar salvo permanentemente no Linux

Se quiser deixar salvo para não precisar digitar toda vez:

```bash
echo 'export GOOGLE_API_KEY="SUA_CHAVE_GOOGLE_AI_STUDIO_AQUI"' >> ~/.bashrc
source ~/.bashrc
```

Depois confira novamente:

```bash
echo $GOOGLE_API_KEY
```

---

### Método alternativo usando `.env`

Também é possível colocar a chave no arquivo `.env` do projeto, se ele existir.

Entre na pasta do projeto:

```bash
cd ~/cafe_com_dados_e_gatos
```

Abra o arquivo:

```bash
nano .env
```

Adicione:

```bash
GOOGLE_API_KEY="SUA_CHAVE_GOOGLE_AI_STUDIO_AQUI"
GEMINI_API_KEY="SUA_CHAVE_GOOGLE_AI_STUDIO_AQUI"
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

Observação importante:

Durante o teste prático, o OpenSwarm NÃO pediu a chave Google/Gemini no assistente inicial.

O wizard pediu apenas:

```text
OpenAI
Anthropic
```

Isso acontece porque os recursos de imagem são opcionais no starter project testado.

---

## 18.3. Configurar chave fal.ai

Para usar fal.ai, configure:

```bash
export FAL_KEY="SUA_CHAVE_FAL_AQUI"
```

Se quiser deixar salva no Linux:

```bash
echo 'export FAL_KEY="SUA_CHAVE_FAL_AQUI"' >> ~/.bashrc
source ~/.bashrc
```

Verifique:

```bash
echo $FAL_KEY
```

Ou coloque no `.env` do projeto, se ele existir:

```bash
cd ~/cafe_com_dados_e_gatos
nano .env
```

Adicione:

```bash
FAL_KEY="SUA_CHAVE_FAL_AQUI"
```

Salve com:

```text
Ctrl + O
Enter
Ctrl + X
```

Depois rode:

```bash
openswarm
```

---

## 18.4. Procurar se o starter criou arquivos de imagem

Saia da interface com:

```bash
Ctrl + C
```

Entre na pasta do projeto:

```bash
cd ~/cafe_com_dados_e_gatos
```

Procure arquivos relacionados a imagem, Google, Gemini ou fal.ai:

```bash
find . -maxdepth 4 -type f | grep -Ei "env|agent|tool|config|image|fal|gemini|google"
```

Se quiser listar todos os arquivos do projeto:

```bash
find . -maxdepth 4 -type f
```

---

## 18.5. Diagnóstico importante

Só colocar a chave no `.env` ou no terminal pode não ser suficiente.

No teste, o projeto criado veio com:

```text
ExampleAgent
```

E esse agente se comportou como gerador de prompt, não como gerador de imagem.

Se, ao pedir uma imagem, o OpenSwarm responder apenas com algo parecido com:

```text
Aqui vai um prompt pronto para gerar essa imagem em um gerador de imagens
```

então ele ainda não está gerando imagem.

Ele está funcionando apenas como:

```text
Gerador de prompt de imagem
```

Para virar um gerador de imagem real, precisa de três coisas:

```text
API de imagem + ferramenta configurada + agente usando essa ferramenta
```

---

## 18.6. Conclusão prática do teste

O suporte a Google/Gemini aparece na documentação do OpenSwarm por meio da variável:

```bash
GOOGLE_API_KEY
```

Mas, no teste prático, o starter project não mostrou Google no menu e não gerou imagem automaticamente.

Portanto, o caminho correto é:

1. Instalar o OpenSwarm.
2. Criar o starter project.
3. Configurar `GOOGLE_API_KEY` ou `FAL_KEY`.
4. Verificar se existe ferramenta/agente de imagem no projeto.
5. Se não existir, editar o agente ou criar um agente/ferramenta de imagem.
6. Testar novamente o pedido de imagem.

Enquanto essa ferramenta não estiver conectada ao agente, o OpenSwarm continuará apenas criando prompts para imagem.

---
