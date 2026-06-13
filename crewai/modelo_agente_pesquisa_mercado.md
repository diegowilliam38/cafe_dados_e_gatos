# Como instalar o CrewAI Studio da comunidade com Ollama e MiniMax

## Objetivo

Instalar o CrewAI Studio da comunidade no Ubuntu sem Docker, configurar Ollama, configurar MiniMax como provedor compatível com OpenAI e criar uma equipe com 4 agentes para produzir um manual simples sobre as 10 raças de gatos mais conhecidas.

Repositório usado:

```text
https://github.com/strnad/CrewAI-Studio
```

Equipe criada:

```text
1. Coordenador da Equipe
2. Pesquisador de Raças de Gatos
3. Redator do Manual
4. Revisor e Entregador Final
```

---

## 1. Instalar dependências no Ubuntu

```bash
sudo apt update
```

```bash
sudo apt install -y git curl python3 python3-pip python3-venv python-is-python3
```

Testar:

```bash
python --version
```

```bash
python3 --version
```

---

## 2. Baixar o CrewAI Studio

```bash
cd "$HOME"
```

```bash
git clone "https://github.com/strnad/CrewAI-Studio.git"
```

```bash
cd "$HOME/CrewAI-Studio"
```

---

## 3. Criar o arquivo .env

```bash
cp ".env_example" ".env"
```

```bash
nano ".env"
```

Colar ou ajustar:

```env
AGENTOPS_ENABLED="False"
DEFAULT_LANGUAGE="en"

OLLAMA_HOST="http://localhost:11434"
OLLAMA_MODELS="ollama/llama3.2,ollama/phi3.5"

OPENAI_API_KEY="SUA_CHAVE_MINIMAX_AQUI"
OPENAI_API_BASE="URL_BASE_OPENAI_COMPATIBLE_DA_MINIMAX_AQUI"
OPENAI_PROXY_MODELS="minimax/M3"
```

Salvar no Nano:

```text
CTRL + O
ENTER
CTRL + X
```

Não colocar chave real no GitHub.

---

## 4. Instalar o CrewAI Studio sem Docker

```bash
cd "$HOME/CrewAI-Studio"
```

```bash
chmod +x "install_venv.sh" "run_venv.sh"
```

```bash
./install_venv.sh
```

Quando perguntar sobre cache do pip, responder:

```text
n
```

Quando perguntar sobre AgentOps, para teste simples pode responder:

```text
n
```

---

## 5. Rodar o CrewAI Studio

```bash
cd "$HOME/CrewAI-Studio"
```

```bash
./run_venv.sh
```

Abrir no navegador:

```text
http://localhost:8501
```

---

## 6. Corrigir erro python: command not found

Erro:

```text
python: command not found
```

Correção:

```bash
sudo apt install -y python-is-python3
```

Testar:

```bash
python --version
```

Rodar a instalação novamente:

```bash
cd "$HOME/CrewAI-Studio"
```

```bash
./install_venv.sh
```

---

## 7. Corrigir erro Failed to create venv

Erro:

```text
Failed to create venv
```

Correção:

```bash
sudo apt install -y python3-venv python-is-python3
```

Remover o venv quebrado:

```bash
cd "$HOME/CrewAI-Studio"
```

```bash
rm -rf "venv"
```

Rodar a instalação novamente:

```bash
./install_venv.sh
```

---

## 8. Instalar e preparar o Ollama

Verificar se o Ollama já está instalado:

```bash
ollama --version
```

Se não estiver instalado:

```bash
curl -fsSL "https://ollama.com/install.sh" | sh
```

Subir o Ollama:

```bash
ollama serve
```

Se aparecer que a porta já está em uso, o Ollama já está rodando.

Em outro terminal, baixar modelos:

```bash
ollama pull "llama3.2"
```

```bash
ollama pull "phi3.5"
```

Listar modelos:

```bash
ollama list
```

Testar API local:

```bash
curl "http://localhost:11434/api/tags"
```

---

## 9. Configurar modelos no CrewAI Studio

Modelo MiniMax:

```text
OpenAI: minimax/M3
```

Modelo Ollama principal:

```text
Ollama: ollama/llama3.2
```

Modelo Ollama leve:

```text
Ollama: ollama/phi3.5
```

Para este teste, usar preferencialmente:

```text
OpenAI: minimax/M3
```

---

## 10. Criar o agente 1: Coordenador da Equipe

Criar em `Agents`.

Name:

```text
Coordenador da Equipe
```

Role:

```text
Coordenador de equipe editorial
```

Goal:

```text
Organizar o trabalho da equipe para criar um manual simples, claro e bem estruturado sobre as 10 raças de gatos mais conhecidas.
```

Backstory:

```text
Você coordena uma pequena equipe de agentes responsáveis por pesquisar, escrever, revisar e entregar um manual final.

Seu trabalho é garantir que o material tenha ordem, clareza e foco no objetivo principal.
```

Configuração:

```text
Allow delegation: desligado
Verbose: ligado
Cache: ligado
Temperature: 0.10
Max Iterations: 25
Model: OpenAI: minimax/M3
```

---

## 11. Criar o agente 2: Pesquisador de Raças de Gatos

Criar em `Agents`.

Name:

```text
Pesquisador de Raças de Gatos
```

Role:

```text
Pesquisador de conteúdo sobre raças de gatos
```

Goal:

```text
Levantar informações simples e úteis sobre as 10 raças de gatos mais conhecidas, incluindo características, comportamento e cuidados básicos.
```

Backstory:

```text
Você pesquisa informações sobre gatos e organiza os dados de forma simples para ajudar a criação de um manual educativo.

Seu trabalho é selecionar informações úteis, evitar excesso de detalhes e preparar uma base clara para o redator.
```

Configuração:

```text
Allow delegation: desligado
Verbose: ligado
Cache: ligado
Temperature: 0.10
Max Iterations: 25
Model: OpenAI: minimax/M3
```

---

## 12. Criar o agente 3: Redator do Manual

Criar em `Agents`.

Name:

```text
Redator do Manual
```

Role:

```text
Redator de manual educativo
```

Goal:

```text
Transformar as informações pesquisadas em um manual claro, organizado e fácil de entender sobre as 10 raças de gatos mais conhecidas.
```

Backstory:

```text
Você escreve textos educativos simples e bem organizados.

Seu trabalho é transformar informações brutas em um manual com linguagem acessível, boa estrutura e leitura agradável.
```

Configuração:

```text
Allow delegation: desligado
Verbose: ligado
Cache: ligado
Temperature: 0.20
Max Iterations: 25
Model: OpenAI: minimax/M3
```

---

## 13. Criar o agente 4: Revisor e Entregador Final

Criar em `Agents`.

Name:

```text
Revisor e Entregador Final
```

Role:

```text
Revisor final e organizador de entrega
```

Goal:

```text
Revisar o manual, corrigir falhas, melhorar a clareza e entregar uma versão final organizada em Markdown.
```

Backstory:

```text
Você revisa materiais educativos antes da entrega final.

Seu trabalho é verificar clareza, organização, repetição, inconsistências e qualidade geral do texto.

A entrega final deve ser limpa, objetiva e pronta para leitura.
```

Configuração:

```text
Allow delegation: desligado
Verbose: ligado
Cache: ligado
Temperature: 0.10
Max Iterations: 25
Model: OpenAI: minimax/M3
```

---

## 14. Criar a tarefa 1: Organizar o plano do manual

Criar em `Tasks`.

Name:

```text
Organizar o plano do manual
```

Description:

```text
Organize o plano de trabalho para criar um manual simples sobre as 10 raças de gatos mais conhecidas.

Defina a estrutura do manual, a ordem das seções e os critérios para selecionar informações úteis.
```

Expected output:

```text
Um plano em Markdown contendo:

1. Objetivo do manual
2. Estrutura recomendada
3. Critérios para escolher as informações
4. Lista inicial das 10 raças que devem aparecer
5. Orientações para o pesquisador, redator e revisor
```

Agent:

```text
Coordenador da Equipe
```

---

## 15. Criar a tarefa 2: Pesquisar as 10 raças de gatos

Criar em `Tasks`.

Name:

```text
Pesquisar as 10 raças de gatos
```

Description:

```text
Pesquise e organize informações sobre as 10 raças de gatos mais conhecidas.

Para cada raça, levante:

1. Nome da raça
2. Origem resumida
3. Características físicas
4. Personalidade
5. Cuidados básicos
6. Perfil de tutor mais indicado
```

Expected output:

```text
Material de pesquisa em Markdown com 10 raças de gatos, cada uma contendo origem resumida, características físicas, personalidade, cuidados básicos e perfil de tutor indicado.
```

Agent:

```text
Pesquisador de Raças de Gatos
```

Context from sync tasks:

```text
Organizar o plano do manual
```

---

## 16. Criar a tarefa 3: Redigir o manual

Criar em `Tasks`.

Name:

```text
Redigir o manual
```

Description:

```text
Use o plano e o material de pesquisa para escrever um manual simples sobre as 10 raças de gatos mais conhecidas.

O texto deve ser claro, organizado e fácil de entender.
```

Expected output:

```text
Um manual em Markdown contendo:

1. Título
2. Introdução curta
3. Lista das 10 raças de gatos
4. Uma seção para cada raça
5. Comparação simples entre perfis de gatos
6. Conclusão curta
```

Agent:

```text
Redator do Manual
```

Context from sync tasks:

```text
Organizar o plano do manual
Pesquisar as 10 raças de gatos
```

---

## 17. Criar a tarefa 4: Revisar e entregar o manual final

Criar em `Tasks`.

Name:

```text
Revisar e entregar o manual final
```

Description:

```text
Revise o manual produzido pela tarefa anterior.

Corrija problemas de clareza, organização, repetição e inconsistência.

Entregue a versão final em Markdown.
```

Expected output:

```text
Manual final em Markdown contendo:

1. Título
2. Introdução
3. As 10 raças de gatos mais conhecidas
4. Características principais de cada raça
5. Cuidados básicos
6. Para quem cada raça pode ser indicada
7. Conclusão final
```

Agent:

```text
Revisor e Entregador Final
```

Context from sync tasks:

```text
Redigir o manual
```

---

## 18. Criar a crew

Criar em `Crews`.

Name:

```text
Equipe Manual de Raças de Gatos
```

Process:

```text
Sequential
```

Agents:

```text
Coordenador da Equipe
Pesquisador de Raças de Gatos
Redator do Manual
Revisor e Entregador Final
```

Tasks:

```text
Organizar o plano do manual
Pesquisar as 10 raças de gatos
Redigir o manual
Revisar e entregar o manual final
```

Configuração da crew:

```text
Manager LLM: None
Manager Agent: None
Verbose: ligado
Memory: desligado
Cache: ligado
Planning: desligado
Planning LLM: None
```

---

## 19. Executar no Kickoff

Ir em `Kickoff` e executar a crew.

Prompt de teste:

```text
Crie um manual simples, claro e organizado com as 10 raças de gatos mais conhecidas.

O manual deve explicar as principais características de cada raça, personalidade, cuidados básicos e para quem cada raça pode ser indicada.
```

Resultado esperado:

```text
Um manual final em Markdown sobre as 10 raças de gatos mais conhecidas.
```

---

## 20. Checklist

```text
Python instalado
python-is-python3 instalado
python3-venv instalado
CrewAI Studio clonado
.env criado
Ollama configurado
MiniMax configurado com placeholders
install_venv.sh executado
run_venv.sh executado
Interface aberta em http://localhost:8501
4 agentes criados
4 tarefas criadas
Crew criada com processo Sequential
Memory desligado
Planning desligado
Cache ligado
Verbose ligado
Teste executado no Kickoff
Resultado conferido em Results
```
