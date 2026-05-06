# Como instalar o OpenSwarm completo pelo Git no Linux e testar geração de imagens

Este guia mostra como instalar o **OpenSwarm completo no Linux usando o repositório oficial do GitHub**, configurar o ambiente Python, configurar chaves de API, abrir a interface pelo terminal e verificar se o **Image Generation Agent** está disponível para gerar imagens.

O foco aqui é o caminho **full**, ou seja: clonar o repositório completo, instalar dependências e rodar o projeto com:

```bash
python swarm.py
```

Este guia também documenta uma descoberta importante feita no teste prático: a instalação rápida via npm pode abrir um projeto inicial com apenas agentes de exemplo. Nesse caso, o OpenSwarm funciona, mas não gera imagens diretamente.

---

## 1. O que é o OpenSwarm

O OpenSwarm é um sistema multiagente open source que roda pelo terminal.

Ele trabalha com agentes especializados para diferentes tarefas, como:

- assistência geral;
- pesquisa;
- criação de documentos;
- criação de apresentações;
- análise de dados;
- geração de imagens;
- geração de vídeos;
- automações e integrações.

Para imagens, o agente correto é o:

```text
Image Generation Agent
```

Esse agente pode gerar e editar imagens usando modelos como:

```text
gemini-2.5-flash-image
gemini-3-pro-image-preview
gpt-image-1.5
```

Dependendo da configuração, também pode usar recursos da fal.ai, como remoção de fundo.

---

## 2. Ponto mais importante antes de começar

Instalar o OpenSwarm e abrir a interface **não significa automaticamente** que todos os agentes especializados estarão carregados no projeto atual.

No teste prático, a instalação rápida abriu um projeto chamado `ExampleAgency` com apenas:

```text
ExampleAgent
ExampleAgent2
```

Esses agentes não geram imagens diretamente.

Eles podem responder em texto e criar prompts, mas não salvam arquivos de imagem.

Quando o projeto está nesse estado, ao pedir uma imagem, o agente pode responder algo parecido com:

```text
I can't generate the image directly in this chat because there isn't a dedicated image generation tool available here.
```

Isso significa que o problema não é necessariamente sua chave do Google. O problema é que o swarm atual não tem o agente/ferramenta de imagem carregado.

Por isso, este guia usa o caminho completo pelo GitHub.

---

## 3. Quando usar instalação npm e quando usar instalação full pelo Git

### Instalação rápida via npm

A instalação rápida é:

```bash
sudo npm install -g @vrsen/openswarm
openswarm
```

Ela é útil para abrir a interface e criar um projeto inicial.

Mas, no teste prático, esse caminho abriu apenas agentes de exemplo.

### Instalação full pelo Git

A instalação full é:

```bash
git clone https://github.com/VRSEN/OpenSwarm.git
cd OpenSwarm
python swarm.py
```

Este é o caminho usado neste documento para tentar carregar o projeto completo e testar os agentes especializados.

---

## 4. Requisitos

Sistema recomendado:

- Ubuntu, Debian ou distribuição Linux equivalente;
- terminal com acesso a `bash`;
- usuário com permissão de `sudo`;
- conexão com a internet;
- Git;
- Python 3.10 ou superior;
- pacote `python3-venv`;
- pip;
- Node.js 20 ou superior;
- npm;
- chave de API para o modelo principal;
- chave do Google AI Studio para geração de imagem com Gemini;
- opcionalmente, chave da fal.ai para remoção de fundo.

---

## 5. Atualizar o sistema

```bash
sudo apt update && sudo apt upgrade -y
```

Instale pacotes básicos:

```bash
sudo apt install -y git curl build-essential ca-certificates python3 python3-pip python3-venv
```

Se estiver usando Ubuntu com Python 3.12 e aparecer erro de ambiente virtual, instale também:

```bash
sudo apt install -y python3.12 python3.12-venv python3-pip
```

Verifique o Python:

```bash
python3 --version
```

Verifique o pip:

```bash
python3 -m pip --version
```

---

## 6. Instalar ou verificar Node.js

Verifique se o Node.js já está instalado:

```bash
node -v
npm -v
```

O recomendado é Node.js 20 ou superior.

Se o Node.js não existir ou estiver antigo, instale o Node.js 22:

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
```

Confira novamente:

```bash
node -v
npm -v
```

---

## 7. Clonar o repositório completo do OpenSwarm

Entre na home:

```bash
cd ~
```

Clone o repositório oficial:

```bash
git clone https://github.com/VRSEN/OpenSwarm.git
```

Entre na pasta:

```bash
cd ~/OpenSwarm
```

Confira os arquivos:

```bash
ls -la
```

Procure o arquivo principal:

```bash
find . -maxdepth 2 -type f | sort
```

O arquivo importante para este guia é:

```text
swarm.py
```

---

## 8. Criar ambiente virtual Python

Dentro da pasta `~/OpenSwarm`, crie o ambiente virtual:

```bash
python3 -m venv .venv
```

Ative o ambiente:

```bash
source .venv/bin/activate
```

Quando o ambiente estiver ativo, o terminal normalmente mostra algo como:

```text
(.venv)
```

Atualize o pip:

```bash
python -m pip install --upgrade pip
```

---

## 9. Instalar dependências Python

Ainda dentro de `~/OpenSwarm` e com o `.venv` ativo, instale as dependências:

```bash
pip install -r requirements.txt
```

Se o arquivo `requirements.txt` não existir, liste os arquivos para verificar a estrutura atual do projeto:

```bash
find . -maxdepth 3 -type f | sort
```

Se houver outro arquivo de dependências, como `pyproject.toml`, `requirements-dev.txt` ou similar, consulte o README do projeto para a forma atual de instalação.

---

## 10. Criar e configurar o arquivo `.env`

Dentro da pasta do repositório:

```bash
cd ~/OpenSwarm
```

Se existir `.env.example`, copie:

```bash
cp .env.example .env
```

Abra o arquivo:

```bash
nano .env
```

Configuração mínima para usar Gemini como provedor principal e liberar imagem com Google:

```env
GOOGLE_API_KEY="COLE_SUA_CHAVE_GOOGLE_AI_STUDIO_AQUI"
DEFAULT_MODEL="litellm/gemini/gemini-3-flash"
```

Se for usar OpenAI como modelo principal e Google só para imagem:

```env
OPENAI_API_KEY="COLE_SUA_CHAVE_OPENAI_AQUI"
GOOGLE_API_KEY="COLE_SUA_CHAVE_GOOGLE_AI_STUDIO_AQUI"
DEFAULT_MODEL="gpt-5.2"
```

Se for usar Anthropic como modelo principal e Google só para imagem:

```env
ANTHROPIC_API_KEY="COLE_SUA_CHAVE_ANTHROPIC_AQUI"
GOOGLE_API_KEY="COLE_SUA_CHAVE_GOOGLE_AI_STUDIO_AQUI"
```

Se for usar recursos da fal.ai, como remoção de fundo:

```env
FAL_KEY="COLE_SUA_CHAVE_FAL_AQUI"
```

Salve no nano:

```text
Ctrl+O
Enter
Ctrl+X
```

---

## 11. Cuidados importantes com o `.env`

Formato correto:

```env
GOOGLE_API_KEY="sua_chave_aqui"
```

Também pode funcionar sem aspas:

```env
GOOGLE_API_KEY=sua_chave_aqui
```

Formato errado por causa dos espaços:

```env
GOOGLE_API_KEY = "sua_chave_aqui"
```

Formato errado dentro do `.env`:

```env
export GOOGLE_API_KEY="sua_chave_aqui"
```

Dentro do `.env`, não use `export`.

Verifique se a chave ficou salva:

```bash
cat .env | grep GOOGLE_API_KEY
```

Verifique se não existem duas linhas com a mesma chave:

```bash
grep GOOGLE_API_KEY .env
```

Se aparecer mais de uma, deixe apenas uma.

---

## 12. Nunca publique o `.env`

Antes de colocar o projeto no GitHub, confira se o `.env` está no `.gitignore`:

```bash
cat .gitignore | grep .env
```

Se não aparecer nada, adicione:

```bash
echo ".env" >> .gitignore
```

Nunca publique chaves como:

```text
GOOGLE_API_KEY
OPENAI_API_KEY
ANTHROPIC_API_KEY
FAL_KEY
COMPOSIO_API_KEY
SEARCH_API_KEY
```

Se uma chave aparecer em vídeo, print ou commit público:

1. revogue a chave no painel do provedor;
2. gere uma chave nova;
3. atualize o `.env`;
4. não reutilize a chave exposta.

---

## 13. Rodar o OpenSwarm completo

Entre no repositório:

```bash
cd ~/OpenSwarm
```

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

Rode o projeto completo:

```bash
python swarm.py
```

Esse é o comando principal da instalação full pelo Git.

---

## 14. Entendendo a interface do OpenSwarm

A interface abre no terminal.

Ela aceita prompts em linguagem natural, mas também possui comandos internos.

A caixa onde você digita mensagens **não é o terminal Linux**.

Se você digitar comandos Linux dentro da interface, o agente vai interpretar como conversa.

Para voltar ao terminal Linux:

```text
Ctrl+C
```

Se não sair na primeira vez, pressione `Ctrl+C` novamente.

---

## 15. Comando interno para listar agentes

Dentro da interface do OpenSwarm, digite:

```text
/agents
```

Esse comando lista os agentes disponíveis no swarm atual.

Se aparecer apenas:

```text
ExampleAgent
ExampleAgent2
```

então o swarm atual ainda é básico e não tem agente de imagem carregado.

Se aparecer algo como:

```text
Image Generation Agent
ImageAgent
ImageGenerationAgent
```

selecione esse agente para gerar imagens.

Também pode aparecer indicação visual como:

```text
tab agents
```

A tecla `Tab` abre ou alterna a seleção de agentes na interface, mas ela só mostra agentes que já existem no swarm atual.

---

## 16. Diagnóstico: verificar se o projeto tem ferramenta de imagem

Saia da interface:

```text
Ctrl+C
```

No terminal Linux, rode:

```bash
cd ~/OpenSwarm
```

Procure arquivos relacionados a imagem:

```bash
grep -R "GenerateImages\|EditImages\|CombineImages\|RemoveBackground\|Image Generation\|gemini-2.5-flash-image" -n . 2>/dev/null
```

Você também pode procurar por nomes de arquivos:

```bash
find . -maxdepth 8 -type f 2>/dev/null | grep -Ei "GenerateImages|EditImages|CombineImages|RemoveBackground|image_generation|image.*agent|gemini-2.5-flash-image"
```

Se aparecerem arquivos como:

```text
GenerateImages.py
EditImages.py
CombineImages.py
RemoveBackground.py
image_generation_agent
```

isso indica que o repositório possui arquivos de agente/ferramenta de imagem.

Se nada aparecer, a versão atual clonada pode ter mudado de estrutura ou não trazer esses arquivos da forma esperada.

---

## 17. Gerar uma imagem simples

Com o projeto rodando via:

```bash
python swarm.py
```

e com o agente de imagem selecionado em `/agents`, envie:

```text
Generate one image with gemini-2.5-flash-image.

Product name: cafe_com_dados_e_gatos
File name: teste_gato_cafe
Aspect ratio: 1:1
Number of variants: 1

Prompt:
A cute black cat drinking coffee beside a laptop, cozy AI studio, modern avatar style, high quality, no text.
```

Se funcionar, o agente deve informar o caminho da imagem gerada.

O caminho pode ser parecido com:

```text
mnt/cafe_com_dados_e_gatos/generated_images/teste_gato_cafe.png
```

---

## 18. Encontrar a imagem gerada

Se o agente informou o caminho, abra a pasta indicada.

Se você não encontrou o arquivo, procure pelo nome:

```bash
find ~/ -iname "*teste_gato_cafe*" 2>/dev/null
```

Ou procure qualquer pasta de imagens geradas:

```bash
find ~/ -path "*generated_images*" -type f 2>/dev/null
```

Para abrir a pasta no Ubuntu:

```bash
xdg-open CAMINHO_DA_PASTA
```

Exemplo:

```bash
xdg-open ~/OpenSwarm/mnt/cafe_com_dados_e_gatos/generated_images
```

---

## 19. Prompt para thumbnail 16:9

Use este prompt quando quiser capa de vídeo do YouTube:

```text
Generate one YouTube thumbnail image with gemini-2.5-flash-image.

Product name: cafe_com_dados_e_gatos
File name: thumbnail_agentes_ia
Aspect ratio: 16:9
Number of variants: 1

Prompt:
Create a colorful YouTube thumbnail background for a video about AI agents. Include a cute black cat, a laptop, glowing data panels, a coffee cup, and a futuristic but cozy desk setup. High contrast, expressive composition, no text.
```

---

## 20. Prompt para avatar 1:1

```text
Generate one image with gemini-2.5-flash-image.

Product name: cafe_com_dados_e_gatos
File name: avatar_robo_frank
Aspect ratio: 1:1
Number of variants: 1

Prompt:
Create a friendly robot avatar for a Brazilian YouTube channel about AI and Data Science. The robot should look approachable, intelligent and slightly futuristic, with a cozy coffee-and-cats visual identity. Clean modern style, high quality, soft lighting, no text.
```

---

## 21. Editar uma imagem existente

Primeiro descubra o caminho absoluto da imagem:

```bash
realpath ~/Downloads/minha-imagem.png
```

Depois, dentro do OpenSwarm com o agente de imagem selecionado:

```text
Edit this image with gemini-2.5-flash-image.

Input image: /home/SEU_USUARIO/Downloads/minha-imagem.png
Product name: cafe_com_dados_e_gatos
Output file name: imagem_editada
Aspect ratio: 1:1
Number of variants: 1

Edit prompt:
Transform this image into a polished YouTube avatar style. Keep the main character recognizable. Improve lighting, colors and composition. Do not add text.
```

---

## 22. Combinar duas ou mais imagens

Use este fluxo para usar uma imagem como referência e outra como personagem, logo ou elemento visual.

```text
Combine these images with gemini-2.5-flash-image.

Product name: cafe_com_dados_e_gatos
Output file name: capa_com_avatar
Aspect ratio: 16:9
Number of variants: 1

Images:
1. /home/SEU_USUARIO/Downloads/capa-antiga.png
2. /home/SEU_USUARIO/Downloads/avatar-gato.png

Instruction:
Create a polished YouTube thumbnail using the first image as the composition reference and the second image as the character/avatar reference. Keep the avatar visible, improve lighting, make the image colorful and high contrast, no extra text.
```

---

## 23. Remover fundo

A remoção de fundo pode exigir chave da fal.ai.

No `.env`:

```env
FAL_KEY="COLE_SUA_CHAVE_FAL_AQUI"
```

Depois, dentro do OpenSwarm:

```text
Remove the background from this image.

Product name: cafe_com_dados_e_gatos
Input image: /home/SEU_USUARIO/Downloads/avatar.png
Output file name: avatar_sem_fundo
```

Se não houver `FAL_KEY`, esse recurso pode falhar. Isso não impede geração ou edição de imagem com Gemini.

---

## 24. Modelos de imagem citados no projeto

Modelos citados para imagem:

```text
gemini-2.5-flash-image
gemini-3-pro-image-preview
gpt-image-1.5
```

Uso sugerido:

```text
gemini-2.5-flash-image
```

Use como padrão para testes rápidos.

```text
gemini-3-pro-image-preview
```

Use quando precisar de mais precisão ou composições mais complexas.

```text
gpt-image-1.5
```

Use se for configurar OpenAI para imagem.

---

## 25. Proporções úteis

```text
1:1
```

Avatar, foto de perfil, post quadrado.

```text
16:9
```

Thumbnail do YouTube.

```text
9:16
```

Shorts, Reels, TikTok.

```text
4:5
```

Post vertical para Instagram.

```text
21:9
```

Banner largo.

---

## 26. Erro: abriu, mas só mostra ExampleAgent

Se `/agents` mostrar apenas:

```text
ExampleAgent
ExampleAgent2
```

então o swarm atual não carregou o agente de imagem.

Nesse caso, o comportamento esperado é:

```text
O OpenSwarm responde em texto.
O OpenSwarm pode criar prompts.
O OpenSwarm não gera arquivos de imagem diretamente nesse swarm.
```

A correção é testar o projeto completo pelo Git e verificar se o agente de imagem aparece:

```bash
cd ~/OpenSwarm
source .venv/bin/activate
python swarm.py
```

Dentro da interface:

```text
/agents
```

---

## 27. Erro: `agentswarm: comando não encontrado`

No teste prático, o comando disponível foi:

```bash
openswarm
```

Então, se você tentar:

```bash
agentswarm agent --help
```

e receber:

```text
agentswarm: comando não encontrado
```

use:

```bash
openswarm --help
```

A seleção de agentes não é feita por `agentswarm agent` no terminal Linux. Ela é feita dentro da interface com:

```text
/agents
```

---

## 28. Erro: digitei comando Linux dentro do chat

Se você digitar:

```bash
openswarm --help
```

ou qualquer comando Linux dentro da caixa de conversa, o agente vai responder como se fosse uma mensagem.

Para rodar comandos Linux:

1. saia da interface com `Ctrl+C`;
2. volte ao terminal normal;
3. rode o comando.

---

## 29. Checklist da instalação full

```bash
cd ~
git clone https://github.com/VRSEN/OpenSwarm.git
cd OpenSwarm
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
nano .env
python swarm.py
```

Dentro da interface:

```text
/agents
```

Verifique se aparece agente de imagem.

Depois teste:

```text
Generate one image with gemini-2.5-flash-image.

Product name: cafe_com_dados_e_gatos
File name: teste
Aspect ratio: 1:1
Number of variants: 1

Prompt:
A cute black cat drinking coffee beside a laptop, cozy studio lighting, high quality, no text.
```

Procure o arquivo:

```bash
find ~/ -iname "*teste*" -path "*generated_images*" 2>/dev/null
```

---

## 30. Como remover a instalação full

Para apagar o clone do Git:

```bash
rm -rf ~/OpenSwarm
```

Para remover o pacote global, se você também instalou via npm:

```bash
sudo npm uninstall -g @vrsen/openswarm
```

Para procurar sobras:

```bash
find ~ -maxdepth 3 -iname "*openswarm*" -o -iname "*agent-swarm*" -o -iname "*agency-swarm*"
```

Apague apenas pastas que você reconhece como parte do teste.

---

## 31. Resumo final

Para o caminho completo pelo Git:

```bash
cd ~
git clone https://github.com/VRSEN/OpenSwarm.git
cd OpenSwarm
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
nano .env
python swarm.py
```

No `.env`, configure:

```env
GOOGLE_API_KEY="SUA_CHAVE_GOOGLE_AI_STUDIO"
DEFAULT_MODEL="litellm/gemini/gemini-3-flash"
```

Dentro da interface:

```text
/agents
```

Se aparecer o agente de imagem, selecione e teste:

```text
Generate one image with gemini-2.5-flash-image.

Product name: cafe_com_dados_e_gatos
File name: teste_gato_cafe
Aspect ratio: 1:1
Number of variants: 1

Prompt:
A cute black cat drinking coffee beside a laptop, cozy studio lighting, modern YouTube avatar style, high quality, no text.
```

Se `/agents` mostrar apenas `ExampleAgent` e `ExampleAgent2`, o projeto atual não está com o agente de imagem carregado. Nesse estado, ele cria prompt, mas não gera imagem diretamente.
