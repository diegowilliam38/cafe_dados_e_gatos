# Como criar um agente de pesquisa de mercado com CrewAI, Crew Studio e CrewAI Studio

## Objetivo

Este guia mostra três caminhos diferentes para criar e testar um agente de pesquisa de mercado usando o ecossistema CrewAI:

```text
1. CrewAI Open Source oficial por CLI e código
2. Crew Studio oficial dentro do CrewAI AMP
3. CrewAI Studio da comunidade rodando localmente sem Docker
```

O foco prático deste arquivo é instalar localmente o **CrewAI Studio da comunidade**, configurar o arquivo `.env`, corrigir o erro comum do Ubuntu com `python` e `venv`, conectar **Ollama** e deixar um modelo de configuração para **MiniMax como OpenAI compatible** usando placeholders seguros.

---

## 1. Diferença entre CrewAI Open Source, Crew Studio oficial e CrewAI Studio da comunidade

## CrewAI Open Source oficial

O **CrewAI Open Source** é o framework oficial em Python para criar agentes, tarefas, crews e flows usando código.

Uso principal:

```text
Criar automações com agentes usando Python, YAML, CLI e arquivos de projeto.
```

Exemplo de fluxo oficial:

```text
Instalar CrewAI
Criar projeto com CLI
Editar agents.yaml
Editar tasks.yaml
Editar crew.py
Executar a crew pelo terminal
```

Comando comum para criar um projeto:

```bash
crewai create crew "market_research_crew"
```

Esse caminho é o mais adequado quando o objetivo é versionar código, criar automações mais controladas e evoluir o projeto tecnicamente.

Referência:

```text
https://docs.crewai.com
https://github.com/crewAIInc/crewAI
```

---

## Crew Studio oficial dentro do CrewAI AMP

O **Crew Studio** oficial faz parte do **CrewAI AMP**, a plataforma oficial da CrewAI para criar, operar, monitorar e escalar automações com agentes.

Uso principal:

```text
Criar e gerenciar crews em uma interface no-code/low-code oficial dentro da plataforma CrewAI AMP.
```

Esse caminho é diferente do projeto local da comunidade chamado CrewAI Studio.

Resumo prático:

```text
Crew Studio oficial = parte do CrewAI AMP
CrewAI AMP = plataforma oficial gerenciada da CrewAI
Uso principal = criação, deploy, observabilidade e operação de crews
```

Referência:

```text
https://docs.crewai.com/en/enterprise/introduction
https://app.crewai.com
```

---

## CrewAI Studio da comunidade

O **CrewAI Studio da comunidade** é um projeto open source separado, criado pela comunidade, com interface em Streamlit para criar e executar agentes e tarefas do CrewAI de forma visual.

Repositório:

```text
https://github.com/strnad/CrewAI-Studio
```

Uso principal:

```text
Testar CrewAI localmente com interface visual, sem precisar escrever todo o projeto em código no primeiro contato.
```

Importante:

```text
CrewAI Studio da comunidade não é o Crew Studio oficial do CrewAI AMP.
```

---

## 2. O que será instalado localmente

O ambiente local deste guia usa:

```text
Ubuntu ou WSL Ubuntu
Python
venv
Git
CrewAI Studio da comunidade
Ollama local
MiniMax configurado como provedor OpenAI compatible com placeholders
```

Fluxo final:

```text
CrewAI Studio comunidade
        |
        |-- Ollama local
        |
        |-- MiniMax via endpoint OpenAI compatible
        |
        |-- Agente: Market Research Analyst
        |
        |-- Tarefa: Market Research Report
```

---

## 3. Onde rodar os comandos

Rodar os comandos no terminal do Ubuntu ou WSL Ubuntu.

```text
Sistema recomendado para este passo a passo: Ubuntu / WSL Ubuntu
Pasta de instalação: $HOME/CrewAI-Studio
Modo de instalação: virtual environment sem Docker
```

---

## 4. Atualizar pacotes do Ubuntu

```bash
sudo apt update
```

```bash
sudo apt install -y git curl python3 python3-pip python3-venv
```

---

## 5. Corrigir o erro python: command not found

## Erro encontrado

```text
python: command not found
```

## Causa provável

Em muitas instalações do Ubuntu, o comando disponível é `python3`, mas o script `install_venv.sh` do CrewAI Studio da comunidade chama:

```bash
python -m venv venv
```

Se o comando `python` não existir, a criação do ambiente virtual falha.

## Correção

Instalar o pacote que cria o alias `python` apontando para `python3`:

```bash
sudo apt install -y python-is-python3
```

Testar:

```bash
python --version
```

```bash
python3 --version
```

Resultado esperado:

```text
Os dois comandos devem mostrar uma versão do Python 3.
```

---

## 6. Corrigir o erro Failed to create venv

## Erro encontrado

```text
Failed to create venv
```

## Causa provável

O pacote `python3-venv` não está instalado, ou o comando `python` não está disponível no Ubuntu.

## Correção

```bash
sudo apt install -y python3-venv python-is-python3
```

Testar criação de venv fora do projeto:

```bash
cd "$HOME"
```

```bash
python -m venv "teste_venv"
```

```bash
source "teste_venv/bin/activate"
```

```bash
python --version
```

```bash
deactivate
```

Remover o ambiente de teste:

```bash
rm -rf "$HOME/teste_venv"
```

---

## 7. Baixar o CrewAI Studio da comunidade

```bash
cd "$HOME"
```

```bash
git clone "https://github.com/strnad/CrewAI-Studio.git"
```

```bash
cd "$HOME/CrewAI-Studio"
```

Conferir arquivos principais:

```bash
ls
```

Arquivos esperados:

```text
install_venv.sh
run_venv.sh
.env_example
requirements.txt
app/
```

---

## 8. Criar o arquivo .env antes de rodar

O repositório fornece um arquivo de exemplo chamado `.env_example`.

Criar o `.env` a partir dele:

```bash
cd "$HOME/CrewAI-Studio"
```

```bash
cp ".env_example" ".env"
```

Abrir para edição:

```bash
nano ".env"
```

---

## 9. Modelo de .env para Ollama e MiniMax

Usar este modelo como base e ajustar os valores conforme o ambiente.

```env
# =========================================================
# CrewAI Studio comunidade - configuração local
# =========================================================

# Interface
DEFAULT_LANGUAGE="en"

# AgentOps
AGENTOPS_ENABLED="False"

# =========================================================
# Ollama local
# =========================================================

OLLAMA_HOST="http://localhost:11434"
OLLAMA_MODELS="ollama/llama3.2,ollama/phi3.5,ollama/qwen2.5:7b"

# =========================================================
# OpenAI compatible genérico
# Pode ser usado para MiniMax, proxy OpenAI compatible
# ou outro provedor compatível com a API da OpenAI.
# =========================================================

OPENAI_API_KEY="SUA_CHAVE_MINIMAX_AQUI"
OPENAI_API_BASE="URL_BASE_OPENAI_COMPATIBLE_DA_MINIMAX_AQUI"
OPENAI_PROXY_MODELS="minimax/NOME_DO_MODELO_MINIMAX_AQUI"

# =========================================================
# Outros provedores opcionais
# Preencher somente se for usar.
# =========================================================

# GROQ_API_KEY="SUA_CHAVE_GROQ_AQUI"
# ANTHROPIC_API_KEY="SUA_CHAVE_ANTHROPIC_AQUI"
# XAI_API_KEY="SUA_CHAVE_XAI_AQUI"
# LMSTUDIO_API_BASE="http://localhost:1234/v1"
# SERPER_API_KEY="SUA_CHAVE_SERPER_AQUI"
# SCRAPFLY_API_KEY="SUA_CHAVE_SCRAPFLY_AQUI"
```

Salvar no Nano:

```text
CTRL + O
ENTER
CTRL + X
```

Importante:

```text
Nunca colocar chave real em repositório público.
Nunca gravar a tela mostrando chave real.
Usar placeholders em documentação pública.
```

---

## 10. Instalar o CrewAI Studio da comunidade sem Docker

O script oficial do repositório para instalação com venv é:

```bash
./install_venv.sh
```

Antes de rodar, garantir permissão de execução:

```bash
cd "$HOME/CrewAI-Studio"
```

```bash
chmod +x "install_venv.sh" "run_venv.sh"
```

Rodar a instalação:

```bash
./install_venv.sh
```

Durante a instalação, o script pode perguntar se deve usar cache do pip.

Para uma instalação limpa, responder:

```text
n
```

Se perguntar sobre instalar AgentOps e o objetivo for apenas teste local simples, responder:

```text
n
```

Resultado esperado:

```text
Installation completed successfully. Do not forget to update the .env file with your credentials. Then run run_venv.sh to start the app.
```

---

## 11. Rodar o CrewAI Studio da comunidade

```bash
cd "$HOME/CrewAI-Studio"
```

```bash
./run_venv.sh
```

Acessar no navegador:

```text
http://localhost:8501
```

Se estiver no WSL e o navegador estiver no Windows, acessar:

```text
http://localhost:8501
```

---

## 12. Preparar o Ollama

Verificar se o Ollama está instalado:

```bash
ollama --version
```

Se o Ollama não estiver instalado, instalar pelo método oficial do projeto Ollama:

```bash
curl -fsSL "https://ollama.com/install.sh" | sh
```

Verificar novamente:

```bash
ollama --version
```

---

## 13. Subir o servidor do Ollama

```bash
ollama serve
```

Se aparecer mensagem de porta em uso, o Ollama provavelmente já está rodando.

Em outro terminal, testar:

```bash
curl "http://localhost:11434/api/tags"
```

Resultado esperado:

```text
Uma resposta JSON com a lista de modelos instalados, ou uma lista vazia se nenhum modelo tiver sido baixado ainda.
```

---

## 14. Baixar modelos no Ollama

Modelo leve para máquina mais simples:

```bash
ollama pull "phi3.5"
```

Modelo intermediário para testes gerais:

```bash
ollama pull "llama3.2"
```

Modelo alternativo:

```bash
ollama pull "qwen2.5:7b"
```

Listar modelos instalados:

```bash
ollama list
```

---

## 15. Configurar Ollama no CrewAI Studio da comunidade

Na interface do CrewAI Studio, usar os dados do `.env`.

Configuração prática:

```text
Provider: Ollama
Host: http://localhost:11434
Model: ollama/llama3.2
```

Ou:

```text
Provider: Ollama
Host: http://localhost:11434
Model: ollama/phi3.5
```

Se a interface aceitar apenas o nome sem prefixo, usar:

```text
llama3.2
```

Ou:

```text
phi3.5
```

---

## 16. Configurar MiniMax como OpenAI compatible

A configuração do MiniMax depende do endpoint OpenAI compatible disponível na conta ou documentação atual da MiniMax.

Usar placeholders no `.env`:

```env
OPENAI_API_KEY="SUA_CHAVE_MINIMAX_AQUI"
OPENAI_API_BASE="URL_BASE_OPENAI_COMPATIBLE_DA_MINIMAX_AQUI"
OPENAI_PROXY_MODELS="minimax/NOME_DO_MODELO_MINIMAX_AQUI"
```

Na interface, quando houver opção de provedor compatível com OpenAI, usar:

```text
Provider: OpenAI compatible / Custom OpenAI compatible
API key: SUA_CHAVE_MINIMAX_AQUI
Base URL: URL_BASE_OPENAI_COMPATIBLE_DA_MINIMAX_AQUI
Model: minimax/NOME_DO_MODELO_MINIMAX_AQUI
```

Exemplo com placeholders:

```text
Provider: Custom OpenAI Compatible
Connection name: MiniMax
API key: SUA_CHAVE_MINIMAX_AQUI
Base URL: URL_BASE_OPENAI_COMPATIBLE_DA_MINIMAX_AQUI
Model: NOME_DO_MODELO_MINIMAX_AQUI
```

Importante:

```text
Confirmar a URL base e o nome exato do modelo na documentação atual da MiniMax ou no painel da conta.
Não usar chave real em documentação pública.
Não commitar o arquivo .env com credenciais reais.
```

---

## 17. Criar o agente Market Research Analyst

Na interface do CrewAI Studio, criar um novo agente.

## Nome do agente

```text
Market Research Analyst
```

## Role

```text
Market Research Analyst
```

## Goal

```text
Gather and synthesize market insights from reliable sources to support strategic content and product decisions.
```

## Backstory

```text
You are an experienced market research analyst specialized in technology, artificial intelligence, digital education, audience behavior, and competitive analysis. Your work is to transform scattered information into clear, practical, and decision-oriented insights.
```

## Modelo sugerido

Para análise mais estruturada:

```text
MiniMax via OpenAI compatible
```

Para teste local e econômico:

```text
Ollama
```

## Configuração simples para primeiro teste

```text
Memory: off
Tools: none
Delegation: off
Verbose: on
```

---

## 18. Criar a tarefa Market Research Report

Criar uma nova tarefa para o agente.

## Nome da tarefa

```text
Market Research Report
```

## Description

```text
Analyze the market opportunity for educational content about local AI agents, Ollama, cloud models, OpenAI compatible providers, and multi-agent workflows.

Identify the target audience, main interests, pain points, content opportunities, risks, limitations, and practical recommendations.
```

## Expected output

```text
A structured Markdown report with the following sections:

1. Market overview
2. Target audience
3. Audience pains and interests
4. Content opportunities
5. Competitive angles
6. Risks and limitations
7. Practical recommendations
8. Suggested next steps
```

## Agent

```text
Market Research Analyst
```

---

## 19. Criar a crew Market Research Crew

Criar uma crew com um agente e uma tarefa.

## Nome da crew

```text
Market Research Crew
```

## Agente

```text
Market Research Analyst
```

## Tarefa

```text
Market Research Report
```

## Processo

```text
Sequential
```

## Modelo para primeiro teste

Para validar custo zero/local:

```text
Ollama
```

Para testar melhor qualidade de análise:

```text
MiniMax via OpenAI compatible
```

---

## 20. Executar o teste inicial

Prompt de teste:

```text
Analyze the market opportunity for a YouTube channel that teaches local AI agents, Ollama, cloud models, OpenAI compatible providers, and multi-agent workflows to beginner and intermediate users.
```

Resultado esperado:

```text
Um relatório em Markdown com visão de mercado, público-alvo, dores, oportunidades, riscos e recomendações práticas.
```

---

## 21. Testar se o problema é o modelo ou o CrewAI Studio

Se a execução falhar com MiniMax, testar com Ollama.

Se funcionar com Ollama, o problema provavelmente está em:

```text
API key
Base URL
Nome do modelo
Compatibilidade do endpoint
Limite da conta
Formato esperado pelo provedor
```

Se falhar também com Ollama, verificar:

```text
Ollama está rodando?
Modelo foi baixado?
OLLAMA_HOST está correto no .env?
CrewAI Studio foi reiniciado depois de editar o .env?
```

---

## 22. Comandos úteis de manutenção

Entrar na pasta do projeto:

```bash
cd "$HOME/CrewAI-Studio"
```

Rodar novamente:

```bash
./run_venv.sh
```

Editar `.env`:

```bash
nano ".env"
```

Ativar venv manualmente:

```bash
source "venv/bin/activate"
```

Atualizar dependências dentro do venv:

```bash
pip install -r "requirements.txt" --upgrade
```

Sair do venv:

```bash
deactivate
```

Ver modelos do Ollama:

```bash
ollama list
```

Testar API local do Ollama:

```bash
curl "http://localhost:11434/api/tags"
```

---

## 23. Reinstalar o venv se a instalação quebrar

Aviso:

```text
Este passo remove apenas o ambiente virtual local do CrewAI Studio.
Não remove o repositório, o .env nem os arquivos principais do projeto.
```

```bash
cd "$HOME/CrewAI-Studio"
```

```bash
rm -rf "venv"
```

```bash
./install_venv.sh
```

```bash
./run_venv.sh
```

---

## 24. Quando usar CrewAI Open Source por código

Usar o CrewAI Open Source oficial quando o objetivo for:

```text
Criar automações versionadas
Editar agentes em YAML
Editar tarefas em YAML
Controlar o fluxo em Python
Usar GitHub como base do projeto
Criar ferramentas customizadas
Evoluir para produção com mais controle
```

Comandos base:

```bash
uv pip install "crewai[tools]"
```

```bash
crewai create crew "market_research_crew"
```

Estrutura esperada do projeto:

```text
market_research_crew/
├── .env
├── pyproject.toml
├── README.md
└── src/
    └── market_research_crew/
        ├── main.py
        ├── crew.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml
```

---

## 25. Exemplo de agente em agents.yaml

```yaml
market_research_analyst:
  role: >
    Market Research Analyst
  goal: >
    Gather and synthesize market insights from reliable sources to support strategic content and product decisions.
  backstory: >
    You are an experienced market research analyst specialized in technology, artificial intelligence, digital education, audience behavior, and competitive analysis. Your work is to transform scattered information into clear, practical, and decision-oriented insights.
```

---

## 26. Exemplo de tarefa em tasks.yaml

```yaml
market_research_report:
  description: >
    Analyze the market opportunity for educational content about local AI agents, Ollama, cloud models, OpenAI compatible providers, and multi-agent workflows.

    Identify the target audience, main interests, pain points, content opportunities, risks, limitations, and practical recommendations.
  expected_output: >
    A structured Markdown report with market overview, target audience, pains and interests, content opportunities, competitive angles, risks, limitations, recommendations, and next steps.
  agent: market_research_analyst
  output_file: market_research_report.md
```

---

## 27. Comparação final: CrewAI, OpenClaw e Hermes

## CrewAI

```text
Foco principal: criação de agentes, tarefas, crews e flows.
Ponto forte: framework Python maduro para automações multiagente.
Melhor uso: criar crews com papéis definidos, tarefas estruturadas e execução programável.
Interface visual: Crew Studio oficial no AMP ou CrewAI Studio da comunidade.
```

## OpenClaw

```text
Foco principal: automação governada com agentes, permissões, memória, ferramentas e regras operacionais.
Ponto forte: estrutura de governança e controle de execução.
Melhor uso: automações locais ou híbridas com preocupação maior com segurança, permissões, rastreabilidade e controle humano.
Interface visual: depende do fluxo montado; o foco é mais arquitetura operacional do que GUI pronta.
```

## Hermes

```text
Foco principal: orquestração, coordenação de agentes e integração com modelos e fluxos operacionais.
Ponto forte: atuar como camada de organização entre modelos, agentes, comandos e interfaces.
Melhor uso: projetos em que o agente precisa operar como assistente/orquestrador conectado a ferramentas e canais.
Interface visual: pode variar conforme o setup usado no projeto.
```

## Escolha prática

```text
Usar CrewAI quando o objetivo for estudar e construir crews com agentes e tarefas bem definidos.
Usar CrewAI Studio da comunidade quando o objetivo for testar CrewAI visualmente em ambiente local.
Usar Crew Studio oficial quando o objetivo for usar a plataforma oficial CrewAI AMP.
Usar OpenClaw quando o objetivo for automação com governança, permissões e controle operacional.
Usar Hermes quando o objetivo for orquestração prática de agentes, modelos e canais dentro de um projeto maior.
```

---

## 28. Checklist final

```text
Ubuntu atualizado
Git instalado
Python instalado
python-is-python3 instalado
python3-venv instalado
CrewAI Studio clonado
.env criado a partir do .env_example
.env editado com placeholders seguros
venv criado com install_venv.sh
CrewAI Studio iniciado com run_venv.sh
Interface acessada em http://localhost:8501
Ollama instalado
Ollama rodando em http://localhost:11434
Modelo Ollama baixado
MiniMax configurado como OpenAI compatible com placeholders
Agente Market Research Analyst criado
Tarefa Market Research Report criada
Crew Market Research Crew criada
Teste inicial executado
```
