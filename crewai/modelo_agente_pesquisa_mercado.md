# Como instalar o CrewAI Studio da comunidade com Ollama e MiniMax

## Objetivo

Instalar o CrewAI Studio da comunidade no Ubuntu sem Docker, configurar Ollama, configurar MiniMax como provedor compatível com OpenAI e criar uma crew simples de pesquisa de mercado.

Repositório usado:

```text
https://github.com/strnad/CrewAI-Studio
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
OPENAI_PROXY_MODELS="minimax/NOME_DO_MODELO_MINIMAX_AQUI"
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

Quando perguntar sobre AgentOps, responder:

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

## 9. Configurar Ollama no CrewAI Studio

Na interface do CrewAI Studio, usar um dos modelos configurados no `.env`.

Modelo principal:

```text
ollama/llama3.2
```

Modelo leve:

```text
ollama/phi3.5
```

Host:

```text
http://localhost:11434
```

---

## 10. Configurar MiniMax no CrewAI Studio

No `.env`, manter os placeholders:

```env
OPENAI_API_KEY="SUA_CHAVE_MINIMAX_AQUI"
OPENAI_API_BASE="URL_BASE_OPENAI_COMPATIBLE_DA_MINIMAX_AQUI"
OPENAI_PROXY_MODELS="minimax/NOME_DO_MODELO_MINIMAX_AQUI"
```

Na interface, usar o modelo configurado em:

```text
OPENAI_PROXY_MODELS
```

Exemplo:

```text
minimax/NOME_DO_MODELO_MINIMAX_AQUI
```

Substituir os placeholders pelos dados reais da conta MiniMax somente no ambiente local.

---

## 11. Criar o agente de pesquisa de mercado

Criar um novo agente.

Name:

```text
Market Research Analyst
```

Role:

```text
Market Research Analyst
```

Goal:

```text
Research market opportunities, audience needs, competitors, risks, and practical recommendations for AI education content.
```

Backstory:

```text
You are a market research analyst specialized in artificial intelligence, digital education, audience behavior, content strategy, and competitor analysis. Your job is to transform scattered information into a clear and practical market report.
```

Model:

```text
minimax/NOME_DO_MODELO_MINIMAX_AQUI
```

Alternativa local:

```text
ollama/llama3.2
```

---

## 12. Criar a tarefa de pesquisa de mercado

Criar uma nova tarefa.

Name:

```text
Market Research Report
```

Description:

```text
Analyze the market opportunity for educational content about local AI agents, Ollama, cloud models, OpenAI-compatible providers, and multi-agent workflows.

Identify the target audience, audience pains, content opportunities, competitor angles, risks, and practical recommendations.
```

Expected output:

```text
A Markdown report with:

1. Market overview
2. Target audience
3. Audience pains
4. Content opportunities
5. Competitor angles
6. Risks and limitations
7. Practical recommendations
8. Next steps
```

Agent:

```text
Market Research Analyst
```

---

## 13. Criar a crew

Criar uma nova crew.

Name:

```text
Market Research Crew
```

Process:

```text
Sequential
```

Agent:

```text
Market Research Analyst
```

Task:

```text
Market Research Report
```

---

## 14. Executar teste

Prompt de teste:

```text
Analyze the market opportunity for a YouTube channel that teaches local AI agents, Ollama, cloud models, OpenAI-compatible providers, and multi-agent workflows to beginner and intermediate users.
```

Resultado esperado:

```text
Um relatório em Markdown com público-alvo, dores, oportunidades, riscos e recomendações práticas.
```

---

## 15. Checklist

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
Agente criado
Tarefa criada
Crew criada
Teste executado
```
