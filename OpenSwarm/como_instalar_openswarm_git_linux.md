# Como Instalar o OpenSwarm pelo Git no Linux

Este guia mostra a instalação do OpenSwarm pelo Git no Linux, usando ambiente virtual Python.

Este documento foca apenas neste caminho:

```text
Git clone + Python venv + Agency Swarm + OpenSwarm
```

Não mistura instalação global via npm, Homebrew, Docker ou outro método.

---

# 1. O que é o OpenSwarm

OpenSwarm é uma base para criar “enxames” de agentes de IA: vários agentes especializados trabalhando juntos, coordenados por um projeto central.

Ele não é, por padrão, um gerador de imagens pronto nem uma interface completa como Open WebUI ou ComfyUI.

Ele funciona como uma estrutura para criar agentes, conectar ferramentas e montar fluxos multiagentes.

---

# 2. OpenSwarm precisa do Agency Swarm?

Sim.

O OpenSwarm usa o Agency Swarm como base/framework para criar e organizar agentes.

Por isso, na instalação pelo Git, não basta clonar o OpenSwarm e rodar `swarm.py`.

Também é necessário instalar o pacote:

```bash
agency-swarm
```

Esse pacote deve ser instalado dentro de um ambiente virtual Python (`.venv`), para evitar erro de sistema gerenciado pelo Ubuntu.

---

# 3. O que NÃO fazer

Não instale pacotes Python direto no sistema com:

```bash
pip3 install pacote
```

Isso pode gerar erro como:

```text
externally-managed-environment
```

Também não use:

```bash
--break-system-packages
```

E não precisa instalar Homebrew para este fluxo no Ubuntu.

O caminho correto é usar `.venv`.

---

# 4. Limpeza de tentativas anteriores

Se você já tentou instalar antes e quer começar limpo, rode:

```bash
cd ~
rm -rf ~/OpenSwarm
```

Se instalou Homebrew apenas por causa deste teste e quiser remover:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"
```

Depois remova possíveis sobras:

```bash
rm -rf ~/.linuxbrew
sudo rm -rf /home/linuxbrew
```

Atenção: só remova Homebrew se você não usa ele para outros projetos.

---

# 5. Instalar dependências do sistema

Atualize o sistema:

```bash
sudo apt update
```

Instale Git, Python, venv e pip:

```bash
sudo apt install -y git python3 python3-venv python3-pip
```

Confira:

```bash
git --version
python3 --version
```

---

# 6. Clonar o OpenSwarm

Entre na pasta home:

```bash
cd ~
```

Clone o repositório:

```bash
git clone https://github.com/VRSEN/OpenSwarm.git
```

Entre na pasta:

```bash
cd OpenSwarm
```

---

# 7. Criar ambiente virtual Python

Dentro da pasta `~/OpenSwarm`, crie o `.venv`:

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

---

# 8. Atualizar pip dentro do venv

Com o `.venv` ativo, rode:

```bash
python -m pip install --upgrade pip
```

---

# 9. Instalar Agency Swarm e dependências principais

Ainda com o `.venv` ativo, instale:

```bash
pip install -U agency-swarm python-dotenv openai anthropic
```

Esses pacotes cobrem:

- `agency-swarm`: base/framework de agentes
- `python-dotenv`: leitura de arquivo `.env`
- `openai`: integração com OpenAI
- `anthropic`: integração com Anthropic/Claude

---

# 10. Configurar API Key

O projeto precisa de pelo menos uma chave de IA para funcionar.

Escolha uma das opções.

---

## 10.1. OpenAI

No terminal, com o `.venv` ativo:

```bash
export OPENAI_API_KEY="SUA_CHAVE_OPENAI_AQUI"
```

Verifique:

```bash
echo $OPENAI_API_KEY
```

---

## 10.2. Anthropic

No terminal, com o `.venv` ativo:

```bash
export ANTHROPIC_API_KEY="SUA_CHAVE_ANTHROPIC_AQUI"
```

Verifique:

```bash
echo $ANTHROPIC_API_KEY
```

---

## 10.3. Google/Gemini para imagem

Se quiser testar recursos com Google/Gemini:

```bash
export GOOGLE_API_KEY="SUA_CHAVE_GOOGLE_AI_STUDIO_AQUI"
```

Verifique:

```bash
echo $GOOGLE_API_KEY
```

Observação: a chave Google/Gemini sozinha não garante que o agente padrão vai gerar imagem. O agente precisa ter uma ferramenta de imagem conectada.

---

# 11. Rodar o OpenSwarm pelo Git

Com o `.venv` ativo e dentro da pasta:

```bash
cd ~/OpenSwarm
```

Rode:

```bash
python3 swarm.py
```

Se o comando `python` não existir, use sempre:

```bash
python3 swarm.py
```

---

# 12. Se aparecer erro de módulo faltando

Se aparecer erro como:

```text
ModuleNotFoundError: No module named 'dotenv'
```

Instale dentro do `.venv`:

```bash
pip install python-dotenv
```

Depois rode novamente:

```bash
python3 swarm.py
```

Se aparecer outro módulo faltando, por exemplo:

```text
ModuleNotFoundError: No module named 'NOME_DO_MODULO'
```

Instale assim:

```bash
pip install NOME_DO_MODULO
```

E rode de novo:

```bash
python3 swarm.py
```

Importante: não saia do `.venv`.

---

# 13. Como saber se estou dentro do venv

Rode:

```bash
which python
```

Deve aparecer algo parecido com:

```text
/home/denise/OpenSwarm/.venv/bin/python
```

Rode também:

```bash
which pip
```

Deve aparecer:

```text
/home/denise/OpenSwarm/.venv/bin/pip
```

Se aparecer `/usr/bin/python` ou `/usr/bin/pip`, você não está usando o `.venv`.

Ative de novo:

```bash
cd ~/OpenSwarm
source .venv/bin/activate
```

---

# 14. Criar arquivo `.env` opcional

Se quiser salvar as chaves dentro do projeto, crie um `.env`:

```bash
cd ~/OpenSwarm
nano .env
```

Exemplo:

```env
OPENAI_API_KEY="SUA_CHAVE_OPENAI_AQUI"
ANTHROPIC_API_KEY="SUA_CHAVE_ANTHROPIC_AQUI"
GOOGLE_API_KEY="SUA_CHAVE_GOOGLE_AI_STUDIO_AQUI"
```

Salve:

```text
Ctrl + O
Enter
Ctrl + X
```

Atenção: nunca envie `.env` para o GitHub.

---

# 15. Adicionar `.env` ao `.gitignore`

Para evitar vazar chaves:

```bash
echo ".env" >> .gitignore
```

Também é bom ignorar o ambiente virtual:

```bash
echo ".venv/" >> .gitignore
```

---

# 16. Fluxo completo resumido

Use este bloco se quiser fazer tudo do zero:

```bash
cd ~
rm -rf ~/OpenSwarm
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip
git clone https://github.com/VRSEN/OpenSwarm.git
cd OpenSwarm
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -U agency-swarm python-dotenv openai anthropic
export OPENAI_API_KEY="SUA_CHAVE_OPENAI_AQUI"
python3 swarm.py
```

Para Anthropic, troque a linha da chave por:

```bash
export ANTHROPIC_API_KEY="SUA_CHAVE_ANTHROPIC_AQUI"
```

Para Google/Gemini, adicione:

```bash
export GOOGLE_API_KEY="SUA_CHAVE_GOOGLE_AI_STUDIO_AQUI"
```

---

# 17. Sobre geração de imagem

No teste prático, o agente padrão gerou apenas prompt de imagem, não a imagem final.

Isso significa que:

```text
OpenSwarm funcionando não significa geração de imagem ativada.
```

Para gerar imagem de verdade, é necessário:

```text
API de imagem + ferramenta configurada + agente usando essa ferramenta
```

Exemplos de ferramentas/provedores possíveis:

- Google/Gemini Image
- fal.ai
- ComfyUI
- OpenAI Images
- Stability API

Mas isso já é uma etapa de customização do swarm, não apenas instalação básica pelo Git.

---

# 18. Comandos para remover tudo desta instalação

Para remover apenas esta instalação pelo Git:

```bash
cd ~
rm -rf ~/OpenSwarm
```

Se quiser limpar cache do pip:

```bash
rm -rf ~/.cache/pip
```

Isso não remove Python, Git, Node, Docker, Ollama nem outros programas do sistema.

---

# 19. Conclusão

Para a instalação pelo Git funcionar corretamente no Linux, o caminho seguro é:

```text
clonar OpenSwarm
criar .venv
ativar .venv
instalar agency-swarm e dependências
configurar API key
rodar python3 swarm.py
```

O ponto mais importante é:

```text
não instalar dependências Python fora do ambiente virtual
```
