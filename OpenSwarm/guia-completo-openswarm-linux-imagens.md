# Como instalar o OpenSwarm no Linux e gerar imagens com o Image Generation Agent

Este guia mostra como instalar o **OpenSwarm** no Linux, configurar as chaves necessárias e usar o **Image Generation Agent** para gerar, editar, combinar imagens e remover fundo.

O objetivo é que outra pessoa consiga repetir o mesmo fluxo do zero, sem Docker, direto pelo terminal.

Repositório oficial:

```text
https://github.com/VRSEN/OpenSwarm
```

> Observação importante: este documento é sobre **OpenSwarm**, não sobre Docker Swarm, Hermes Agent, Open WebUI, PaperClip ou OpenClaw. Essas ferramentas não são necessárias para este fluxo.

---

## 1. O que é o OpenSwarm

O OpenSwarm é um sistema multiagente open source que roda pelo terminal.

Ele trabalha com uma equipe de agentes especializados. Em vez de um único agente tentar fazer tudo, o OpenSwarm tem agentes diferentes para tarefas diferentes, como pesquisa, documentos, apresentações, análise de dados, imagens e vídeos.

Para geração de imagens, o agente correto é o:

```text
Image Generation Agent
```

Esse agente pode:

- gerar imagem a partir de texto;
- editar imagem existente;
- combinar duas ou mais imagens;
- remover fundo de imagem, se a chave da fal.ai estiver configurada;
- salvar o resultado em uma pasta local do projeto.

---

## 2. O que este guia ensina

Este guia cobre:

- instalação do Node.js;
- instalação do Python e venv;
- instalação do OpenSwarm sem Docker;
- criação de uma pasta limpa de teste;
- configuração de API Keys;
- configuração do `.env`;
- geração de imagem com Gemini;
- edição de imagem existente;
- combinação de imagens;
- remoção de fundo;
- localização dos arquivos gerados;
- erros comuns e soluções;
- remoção completa do teste, se quiser limpar tudo depois.

---

## 3. Requisitos

Sistema recomendado:

- Ubuntu, Debian ou distribuição Linux equivalente;
- terminal com acesso a `bash`;
- usuário com permissão de `sudo`;
- conexão com a internet;
- Node.js 20 ou superior;
- npm;
- Python 3.10 ou superior;
- pacote de ambiente virtual Python (`venv`);
- pelo menos uma chave de API para o modelo principal;
- chave do Google AI Studio para geração de imagem com Gemini.

Para gerar imagem com Gemini, a chave mais importante é:

```env
GOOGLE_API_KEY=
```

Para remover fundo, também será necessária:

```env
FAL_KEY=
```

A `FAL_KEY` é opcional. Ela não é necessária para geração de imagem com Gemini.

---

## 4. Atualizar o sistema

```bash
sudo apt update && sudo apt upgrade -y
```

Instale pacotes básicos:

```bash
sudo apt install -y curl git build-essential ca-certificates python3 python3-pip python3-venv
```

Observação: durante o `apt upgrade`, o Linux pode atualizar pacotes que já existem no sistema, inclusive Docker, caso ele esteja instalado. Isso não significa que o OpenSwarm instalou Docker. Foi apenas uma atualização do sistema.

---

## 5. Verificar Node.js e npm

Verifique as versões:

```bash
node -v
npm -v
```

O recomendado é Node.js 20 ou superior.

Se o Node não estiver instalado ou estiver abaixo da versão 20, instale uma versão atual.

---

## 6. Instalar Node.js 22 LTS

```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
```

Verifique novamente:

```bash
node -v
npm -v
```

A saída esperada deve mostrar algo como:

```text
v22.x.x
```

Se aparecer Node 20 ou superior, pode continuar.

---

## 7. Verificar Python e venv

Verifique a versão do Python:

```bash
python3 --version
```

Instale o suporte a ambiente virtual:

```bash
sudo apt install -y python3-venv python3-pip
```

Se estiver usando Ubuntu 24.04 e quiser garantir o pacote específico do Python 3.12:

```bash
sudo apt install -y python3.12-venv python3-pip
```

Se o pacote `python3.12-venv` não existir na sua distribuição, use:

```bash
sudo apt install -y python3-venv python3-pip
```

---

## 8. Instalar o OpenSwarm

Instale o OpenSwarm globalmente pelo npm:

```bash
sudo npm install -g @vrsen/openswarm
```

Se preferir evitar `sudo`, configure o npm global no seu usuário antes. Para a maioria dos testes simples em Ubuntu, o comando com `sudo` costuma ser o mais direto.

Verifique se o comando existe:

```bash
which openswarm
```

Teste a ajuda:

```bash
openswarm --help
```

---

## 9. Criar uma pasta limpa para o projeto

Crie uma pasta de teste:

```bash
cd ~
mkdir -p ~/openswarm-teste
cd ~/openswarm-teste
```

Essa pasta ajuda a manter o teste organizado e facilita encontrar os arquivos gerados depois.

---

## 10. Iniciar o OpenSwarm pela primeira vez

Dentro da pasta de teste, rode:

```bash
openswarm
```

Na primeira execução, o OpenSwarm pode abrir um assistente de configuração.

Atenção: se o seu objetivo é usar os agentes completos do OpenSwarm, incluindo o **Image Generation Agent**, não escolha um fluxo que crie apenas um agente mínimo de exemplo, caso essa opção apareça.

Se você escolheu um projeto básico e só apareceu algo como:

```text
ExampleAgent
```

então esse projeto pode apenas responder texto ou melhorar prompts, sem chamar o agente real de imagem. Nesse caso, use o fluxo completo do OpenSwarm ou clone o repositório oficial, como mostrado mais abaixo.

---

## 11. Chaves de API necessárias

O OpenSwarm precisa de pelo menos um provedor principal de modelo para o agente orquestrador responder.

Exemplos:

```env
OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GOOGLE_API_KEY=
```

Para geração de imagem com Gemini, configure:

```env
GOOGLE_API_KEY=
```

Para remoção de fundo, configure também:

```env
FAL_KEY=
```

Resumo prático:

| Recurso | Chave necessária |
|---|---|
| Usar Gemini como modelo principal | `GOOGLE_API_KEY` |
| Gerar imagem com Gemini | `GOOGLE_API_KEY` |
| Editar imagem com Gemini | `GOOGLE_API_KEY` |
| Combinar imagens com Gemini | `GOOGLE_API_KEY` |
| Remover fundo | `FAL_KEY` |
| Usar OpenAI como modelo principal ou imagem OpenAI | `OPENAI_API_KEY` |
| Usar Anthropic como modelo principal | `ANTHROPIC_API_KEY` |

---

## 12. Criar ou editar o arquivo `.env`

Dentro da pasta onde você está rodando o OpenSwarm, veja se existe um `.env`:

```bash
ls -la
```

Se já existir, abra:

```bash
nano .env
```

Se não existir, crie:

```bash
nano .env
```

Configuração mínima usando Gemini como modelo principal e Gemini para imagens:

```env
GOOGLE_API_KEY="COLE_SUA_CHAVE_DO_GOOGLE_AI_STUDIO_AQUI"
DEFAULT_MODEL="litellm/gemini/gemini-3-flash"
```

Se também quiser remover fundo:

```env
FAL_KEY="COLE_SUA_CHAVE_DA_FAL_AQUI"
```

Exemplo completo com Gemini:

```env
GOOGLE_API_KEY="COLE_SUA_CHAVE_DO_GOOGLE_AI_STUDIO_AQUI"
DEFAULT_MODEL="litellm/gemini/gemini-3-flash"
FAL_KEY="COLE_SUA_CHAVE_DA_FAL_AQUI"
```

Se quiser usar OpenAI como modelo principal, mas Gemini para imagens:

```env
OPENAI_API_KEY="COLE_SUA_CHAVE_OPENAI_AQUI"
GOOGLE_API_KEY="COLE_SUA_CHAVE_GOOGLE_AI_STUDIO_AQUI"
DEFAULT_MODEL="gpt-5.2"
```

Nesse caso:

- o agente principal usa OpenAI;
- o Image Generation Agent ainda consegue usar Gemini por causa da `GOOGLE_API_KEY`.

---

## 13. Formato correto do `.env`

Correto:

```env
GOOGLE_API_KEY="sua_chave_aqui"
```

Também funciona:

```env
GOOGLE_API_KEY=sua_chave_aqui
```

Errado:

```env
GOOGLE_API_KEY = "sua_chave_aqui"
```

Errado:

```env
export GOOGLE_API_KEY="sua_chave_aqui"
```

Errado:

```env
GOOGLE_API_KEY=""
```

Regras importantes:

- não coloque espaço antes ou depois do `=`;
- não coloque `export` dentro do `.env`;
- não deixe a chave vazia;
- não duplique a mesma variável com valores diferentes;
- não suba o `.env` para o GitHub.

Salve no nano:

```text
Ctrl + O
Enter
Ctrl + X
```

---

## 14. Segurança: proteger suas chaves

Antes de subir qualquer projeto para o GitHub, confira se `.env` está no `.gitignore`:

```bash
cat .gitignore 2>/dev/null | grep '^.env$'
```

Se não aparecer nada, adicione:

```bash
echo ".env" >> .gitignore
```

Nunca publique sua chave de API.

Se publicou uma chave sem querer:

1. revogue a chave no painel do provedor;
2. crie uma chave nova;
3. atualize o `.env` local;
4. não reutilize a chave exposta.

---

## 15. Iniciar novamente o OpenSwarm

Depois de configurar o `.env`, rode:

```bash
openswarm
```

Se a interface abrir no terminal com uma caixa de entrada para você digitar o pedido, o OpenSwarm está rodando.

---

## 16. Como chamar o agente certo para gerar imagem

Para gerar imagem de verdade, peça explicitamente o agente correto:

```text
Use the Image Generation Agent to generate one image with gemini-2.5-flash-image.
```

Evite pedir apenas:

```text
Crie uma imagem.
```

O pedido curto pode fazer o agente principal apenas escrever um prompt, em vez de chamar a ferramenta de imagem.

---

## 17. Gerar uma imagem simples

Com o OpenSwarm aberto, envie:

```text
Use the Image Generation Agent to generate one image with gemini-2.5-flash-image.

Product name: cafe_dados_gatos
File name: teste_gato_cafe
Aspect ratio: 1:1
Number of variants: 1

Prompt:
A cute black cat drinking coffee beside a laptop, cozy studio lighting, modern YouTube avatar style, high quality, no text.
```

A imagem deve ser salva em uma pasta parecida com:

```text
mnt/cafe_dados_gatos/generated_images/teste_gato_cafe.png
```

Se forem geradas variantes, os nomes podem receber sufixos como:

```text
teste_gato_cafe_1.png
teste_gato_cafe_2.png
teste_gato_cafe_3.png
teste_gato_cafe_4.png
```

---

## 18. Prompt pronto para testar no vídeo

```text
Use the Image Generation Agent to generate one image with gemini-2.5-flash-image.

Product name: cafe_dados_gatos
File name: robo_frank_teste
Aspect ratio: 1:1
Number of variants: 1

Prompt:
Create a friendly robot avatar for a Brazilian YouTube channel about AI and Data Science. The robot should look approachable, intelligent and slightly futuristic, with a cozy coffee-and-cats visual identity. Use a clean modern style, high quality, soft lighting, no text, simple background.
```

Depois procure o arquivo:

```bash
find ~/ -iname "*robo_frank_teste*" 2>/dev/null
```

---

## 19. Gerar thumbnail 16:9 para YouTube

Para capa de vídeo do YouTube, use `16:9`.

```text
Use the Image Generation Agent to generate one YouTube thumbnail image with gemini-2.5-flash-image.

Product name: cafe_dados_gatos
File name: thumbnail_ia_gatos
Aspect ratio: 16:9
Number of variants: 1

Prompt:
Create a colorful YouTube thumbnail background for a video about AI agents. Include a cute black cat, a laptop, glowing data panels, a coffee cup, and a futuristic but cozy desk setup. High contrast, expressive composition, no text.
```

Caminho esperado:

```text
mnt/cafe_dados_gatos/generated_images/thumbnail_ia_gatos.png
```

---

## 20. Gerar imagem vertical para Shorts, Reels ou TikTok

Use `9:16`.

```text
Use the Image Generation Agent to generate one vertical image with gemini-2.5-flash-image.

Product name: cafe_dados_gatos
File name: short_ai_agents_vertical
Aspect ratio: 9:16
Number of variants: 1

Prompt:
Create a vertical visual for a short video about AI agents. Show a cute black cat beside a glowing robot assistant, coffee cup, data panels, cozy studio, high quality, no text.
```

---

## 21. Editar uma imagem existente

Para editar uma imagem, primeiro descubra o caminho absoluto dela.

Exemplo:

```bash
realpath ~/Downloads/minha-imagem.png
```

Depois, dentro do OpenSwarm, peça:

```text
Use the Image Generation Agent to edit this image with gemini-2.5-flash-image.

Input image: /home/SEU_USUARIO/Downloads/minha-imagem.png
Product name: cafe_dados_gatos
Output file name: imagem_editada
Aspect ratio: 1:1
Number of variants: 1

Edit prompt:
Transform this image into a polished YouTube avatar style. Keep the main character recognizable. Improve lighting, colors and composition. Do not add text.
```

Resultado esperado:

```text
mnt/cafe_dados_gatos/generated_images/imagem_editada.png
```

---

## 22. Combinar duas ou mais imagens

Use esse fluxo quando quiser juntar elementos de imagens diferentes.

Exemplos:

- usar uma capa antiga como referência;
- inserir um avatar em uma thumbnail;
- juntar personagem, cenário e logo;
- criar uma nova imagem a partir de referências visuais.

Prompt:

```text
Use the Image Generation Agent to combine these images with gemini-2.5-flash-image.

Product name: cafe_dados_gatos
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

## 23. Remover fundo de imagem

A remoção de fundo usa fal.ai. Para isso, o `.env` precisa ter:

```env
FAL_KEY="COLE_SUA_CHAVE_DA_FAL_AQUI"
```

Depois peça:

```text
Use the Image Generation Agent to remove the background from this image.

Product name: cafe_dados_gatos
Input image: /home/SEU_USUARIO/Downloads/avatar.png
Output file name: avatar_sem_fundo
```

Resultado esperado:

```text
mnt/cafe_dados_gatos/generated_images/avatar_sem_fundo.png
```

Se você não configurou `FAL_KEY`, esse recurso deve falhar. Isso não impede geração, edição ou combinação de imagem com Gemini.

---

## 24. Modelos de imagem disponíveis

O Image Generation Agent trabalha com estes modelos:

```text
gemini-2.5-flash-image
gemini-3-pro-image-preview
gpt-image-1.5
```

### gemini-2.5-flash-image

Use como padrão.

Bom para:

- gerar imagem rápido;
- testar variações;
- criar avatar;
- criar capa simples;
- editar imagem com instruções diretas.

### gemini-3-pro-image-preview

Use quando precisar de mais precisão.

Bom para:

- composições complexas;
- imagem com muitas regras;
- identidade visual mais rígida;
- edição com mais detalhes;
- tentativa de correção quando o Gemini Flash não acertar.

### gpt-image-1.5

Use quando quiser testar especificamente imagem com OpenAI.

Observação: esse caminho depende da `OPENAI_API_KEY` e da disponibilidade do modelo na sua conta.

---

## 25. Proporções aceitas

Proporções aceitas pelo Image Generation Agent:

```text
1:1
2:3
3:2
3:4
4:3
4:5
5:4
9:16
16:9
21:9
```

Sugestões práticas:

```text
1:1    avatar, foto de perfil, post quadrado
16:9   thumbnail do YouTube
9:16   Shorts, Reels, TikTok
4:5    post vertical para Instagram
3:2    imagem horizontal simples
21:9   banner bem largo
```

Atenção: `gpt-image-1.5` pode ter menos proporções disponíveis dentro do agente. Se quiser usar várias proporções, o caminho mais simples é usar Gemini.

---

## 26. Como encontrar a imagem gerada

Normalmente o OpenSwarm informa o caminho final no terminal.

Se você não encontrar, procure assim:

```bash
find ~/ -path "*generated_images*" -type f 2>/dev/null
```

Para procurar pelo nome específico:

```bash
find ~/ -iname "*teste_gato_cafe*" 2>/dev/null
```

Para encontrar a pasta:

```bash
find ~/ -type d -path "*generated_images*" 2>/dev/null
```

Para abrir a pasta no gerenciador de arquivos do Ubuntu, entre na pasta correta e rode:

```bash
xdg-open mnt/cafe_dados_gatos/generated_images
```

Se esse caminho não existir no diretório atual, use o `find` para localizar a pasta correta.

---

## 27. Como saber se está gerando imagem de verdade

Funcionou quando o OpenSwarm:

- chama o **Image Generation Agent**;
- informa que gerou uma imagem;
- mostra um caminho de arquivo local;
- salva um `.png`, `.jpg` ou arquivo de imagem dentro de `generated_images`.

Não funcionou ainda se ele apenas responder algo como:

```text
Aqui está um prompt para você usar em um gerador de imagens...
```

Nesse caso, ele está apenas criando prompt, não gerando a imagem.

Solução:

1. confira se a `GOOGLE_API_KEY` está configurada;
2. chame explicitamente o `Image Generation Agent`;
3. use o modelo `gemini-2.5-flash-image`;
4. confira se você não criou apenas um projeto mínimo com `ExampleAgent`;
5. use o método alternativo de clonar o repositório oficial, se necessário.

---

## 28. Diagnóstico rápido

Confira Node e npm:

```bash
node -v
npm -v
```

Confira OpenSwarm:

```bash
which openswarm
openswarm --help
```

Confira o `.env`:

```bash
grep -E "GOOGLE_API_KEY|DEFAULT_MODEL|FAL_KEY|OPENAI_API_KEY|ANTHROPIC_API_KEY" .env
```

Atenção: esse comando pode mostrar parte das chaves no terminal. Não grave vídeo ou tire print mostrando suas chaves reais.

Para conferir sem exibir o valor inteiro:

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('.env')
if not p.exists():
    print('Arquivo .env não encontrado')
else:
    for line in p.read_text().splitlines():
        if '=' in line and not line.strip().startswith('#'):
            k, v = line.split('=', 1)
            if k.strip() in {'GOOGLE_API_KEY', 'DEFAULT_MODEL', 'FAL_KEY', 'OPENAI_API_KEY', 'ANTHROPIC_API_KEY'}:
                v = v.strip().strip('"').strip("'")
                status = 'preenchida' if v else 'vazia'
                print(f'{k.strip()}: {status}')
PY
```

---

## 29. Erros comuns e soluções

### Erro: `GOOGLE_API_KEY is not set`

O OpenSwarm não encontrou a chave do Google.

Confira se o `.env` existe na pasta onde você está rodando:

```bash
ls -la
```

Confira a linha:

```bash
grep GOOGLE_API_KEY .env
```

Ela deve estar assim:

```env
GOOGLE_API_KEY="sua_chave_aqui"
```

---

### Erro: chave com espaço

Errado:

```env
GOOGLE_API_KEY = "sua_chave"
```

Certo:

```env
GOOGLE_API_KEY="sua_chave"
```

---

### Erro: colocou `export` dentro do `.env`

Errado:

```env
export GOOGLE_API_KEY="sua_chave"
```

Certo:

```env
GOOGLE_API_KEY="sua_chave"
```

---

### Erro: existem duas linhas `GOOGLE_API_KEY`

Confira:

```bash
grep GOOGLE_API_KEY .env
```

Se aparecer duas vezes, deixe apenas uma linha preenchida.

---

### Erro: `FAL_KEY is not set`

Esse erro só importa se você pediu remoção de fundo ou recurso da fal.ai.

Para gerar imagem com Gemini, você não precisa de `FAL_KEY`.

---

### Erro: `ensurepip is not available`

Instale o pacote de venv:

```bash
sudo apt install -y python3-venv python3-pip
```

No Ubuntu 24.04, se necessário:

```bash
sudo apt install -y python3.12-venv python3-pip
```

Depois rode novamente:

```bash
openswarm
```

---

### Erro: servidor local indisponível

Se aparecer algo como:

```text
http://127.0.0.1:8000 Unavailable
http://127.0.0.1:8080 Unavailable
```

provavelmente você tentou conectar em uma agência/servidor local que não está rodando.

Para teste inicial, use um projeto novo/local ou o fluxo padrão do OpenSwarm.

---

### O OpenSwarm só cria prompt, mas não gera imagem

Isso costuma acontecer quando:

- o agente de imagem não foi chamado;
- a chave do Google não está configurada;
- o projeto inicial criado tem apenas `ExampleAgent`;
- o pedido foi genérico demais.

Peça assim:

```text
Use the Image Generation Agent to generate one image with gemini-2.5-flash-image.
```

---

## 30. Método alternativo: clonar o repositório oficial

Se a instalação global não trouxer o fluxo completo que você precisa, clone o repositório oficial.

```bash
cd ~
git clone https://github.com/VRSEN/OpenSwarm.git
cd OpenSwarm
```

Crie o `.env`:

```bash
cp .env.example .env
nano .env
```

Configure:

```env
GOOGLE_API_KEY="COLE_SUA_CHAVE_DO_GOOGLE_AI_STUDIO_AQUI"
DEFAULT_MODEL="litellm/gemini/gemini-3-flash"
```

Se quiser remoção de fundo:

```env
FAL_KEY="COLE_SUA_CHAVE_DA_FAL_AQUI"
```

Rode:

```bash
python3 swarm.py
```

Se faltar dependência Python, crie um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
python3 swarm.py
```

Use esse método quando quiser ter acesso direto aos arquivos do projeto, agentes e ferramentas.

---

## 31. Verificar se os arquivos do Image Generation Agent existem

No repositório clonado, rode:

```bash
find . -maxdepth 3 -type d | grep image_generation_agent
```

E:

```bash
find image_generation_agent -maxdepth 3 -type f
```

Você deve ver arquivos relacionados a:

```text
GenerateImages.py
EditImages.py
CombineImages.py
RemoveBackground.py
instructions.md
```

Se esses arquivos existem, o agente de imagem está presente no projeto.

---

## 32. Remover completamente o teste

Para remover a instalação global:

```bash
sudo npm uninstall -g @vrsen/openswarm
```

Apagar pasta de teste:

```bash
rm -rf ~/openswarm-teste
```

Se você clonou o repositório:

```bash
rm -rf ~/OpenSwarm
```

Apagar possíveis caches ou configurações locais:

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

Apague manualmente apenas o que você reconhecer como sobra do teste.

---

## 33. Checklist rápido de instalação

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl git build-essential ca-certificates python3 python3-pip python3-venv
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
node -v
npm -v
sudo npm install -g @vrsen/openswarm
cd ~
mkdir -p ~/openswarm-teste
cd ~/openswarm-teste
nano .env
openswarm
```

Conteúdo mínimo do `.env`:

```env
GOOGLE_API_KEY="COLE_SUA_CHAVE_DO_GOOGLE_AI_STUDIO_AQUI"
DEFAULT_MODEL="litellm/gemini/gemini-3-flash"
```

---

## 34. Checklist rápido de imagem

Dentro do OpenSwarm, cole:

```text
Use the Image Generation Agent to generate one image with gemini-2.5-flash-image.

Product name: cafe_dados_gatos
File name: teste_final
Aspect ratio: 1:1
Number of variants: 1

Prompt:
A cute black cat with glasses drinking coffee beside a laptop, cozy AI studio, modern avatar style, high quality, no text.
```

Depois procure:

```bash
find ~/ -iname "*teste_final*" 2>/dev/null
```

Funcionou quando:

- o `openswarm` abre;
- o `.env` tem `GOOGLE_API_KEY` preenchida;
- o pedido chama explicitamente o `Image Generation Agent`;
- o modelo usado é `gemini-2.5-flash-image` ou outro modelo de imagem válido;
- a imagem aparece dentro de uma pasta `generated_images`.

---

## 35. Prompt curto para usar sempre

Para imagem quadrada:

```text
Use the Image Generation Agent to generate one image with gemini-2.5-flash-image.

Product name: cafe_dados_gatos
File name: NOME_DO_ARQUIVO
Aspect ratio: 1:1
Number of variants: 1

Prompt:
DESCREVA_A_IMAGEM_AQUI. High quality, no text.
```

Para thumbnail:

```text
Use the Image Generation Agent to generate one image with gemini-2.5-flash-image.

Product name: cafe_dados_gatos
File name: NOME_DA_THUMB
Aspect ratio: 16:9
Number of variants: 1

Prompt:
DESCREVA_A_THUMB_AQUI. YouTube thumbnail style, high contrast, no text.
```

Para imagem vertical:

```text
Use the Image Generation Agent to generate one image with gemini-2.5-flash-image.

Product name: cafe_dados_gatos
File name: NOME_VERTICAL
Aspect ratio: 9:16
Number of variants: 1

Prompt:
DESCREVA_A_IMAGEM_VERTICAL_AQUI. Vertical composition, high quality, no text.
```

---

## 36. Resumo final

Para instalar:

```bash
sudo npm install -g @vrsen/openswarm
```

Para rodar:

```bash
openswarm
```

Para gerar imagem, configure no `.env`:

```env
GOOGLE_API_KEY="SUA_CHAVE_GOOGLE_AI_STUDIO"
DEFAULT_MODEL="litellm/gemini/gemini-3-flash"
```

Depois peça explicitamente:

```text
Use the Image Generation Agent to generate one image with gemini-2.5-flash-image.
```

A imagem deve ser salva em uma pasta parecida com:

```text
mnt/NOME_DO_PROJETO/generated_images/
```

Se o OpenSwarm apenas escrever um prompt, ele ainda não gerou a imagem. Nesse caso, confira a chave `GOOGLE_API_KEY`, chame explicitamente o `Image Generation Agent` e verifique se o projeto carregado tem o agente de imagem disponível.
