# Como instalar o CrewAI Studio da comunidade com Ollama e MiniMax

## Objetivo

Instalar o CrewAI Studio da comunidade no Ubuntu sem Docker, configurar Ollama, configurar MiniMax como provedor compatível com OpenAI e criar uma crew simples com dois agentes:

```text
1. Analista de Pesquisa de Mercado
2. Avaliador do Relatório
```

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

Quando perguntar sobre AgentOps:

```text
n
```

Para este teste, AgentOps não é obrigatório.

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

Host:

```text
http://localhost:11434
```

Modelo principal:

```text
ollama/llama3.2
```

Modelo leve:

```text
ollama/phi3.5
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

## 11. Criar o agente 1: Analista de Pesquisa de Mercado

Criar um novo agente em `Agents`.

Name:

```text
Analista de Pesquisa de Mercado
```

Role:

```text
Analista de Pesquisa de Mercado
```

Goal:

```text
Pesquisar oportunidades de mercado, necessidades do público, concorrentes, riscos e recomendações práticas para conteúdos, produtos e serviços relacionados à inteligência artificial.
```

Backstory:

```text
Você é um analista especializado em inteligência artificial, educação tecnológica, comportamento de audiência e análise de mercado.

Seu trabalho é transformar informações dispersas em relatórios claros, objetivos e acionáveis para apoiar a tomada de decisão.
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

## 12. Criar o agente 2: Avaliador do Relatório

Criar outro agente em `Agents`.

Name:

```text
Avaliador do Relatório
```

Role:

```text
Avaliador crítico de relatório de pesquisa de mercado
```

Goal:

```text
Avaliar a qualidade do relatório produzido, encontrar falhas, apontar lacunas, verificar clareza e sugerir melhorias práticas.
```

Backstory:

```text
Você é um avaliador crítico especializado em revisar relatórios estratégicos.

Seu trabalho é verificar se o relatório tem clareza, coerência, profundidade suficiente, recomendações úteis e riscos bem explicados.

Você não deve reescrever tudo. Você deve avaliar o resultado, apontar problemas e sugerir melhorias objetivas.
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

## 13. Criar a tarefa 1: Relatório de Pesquisa de Mercado

Criar uma nova tarefa em `Tasks`.

Name:

```text
Relatório de Pesquisa de Mercado
```

Description:

```text
Analise as oportunidades de mercado para conteúdos sobre agentes de IA, Ollama, modelos locais, modelos em nuvem, provedores compatíveis com OpenAI e fluxos multiagentes.

Identifique público-alvo, dores do público, interesses, oportunidades de conteúdo, ângulos de concorrência, riscos e recomendações práticas.
```

Expected output:

```text
Um relatório em Markdown contendo:

1. Visão geral do mercado
2. Público-alvo
3. Principais dores do público
4. Oportunidades de conteúdo
5. Ângulos de concorrência
6. Riscos e limitações
7. Recomendações práticas
8. Próximos passos
```

Agent:

```text
Analista de Pesquisa de Mercado
```

---

## 14. Criar a tarefa 2: Avaliação do Relatório

Criar outra tarefa em `Tasks`.

Name:

```text
Avaliação do Relatório
```

Description:

```text
Avalie o relatório de pesquisa de mercado produzido pela tarefa anterior.

Verifique se o relatório está claro, útil, coerente e completo.

Aponte falhas, lacunas, pontos fracos, exageros, riscos não explicados e melhorias necessárias.
```

Expected output:

```text
Uma avaliação em Markdown contendo:

1. Resumo da qualidade geral do relatório
2. Pontos fortes
3. Pontos fracos
4. Lacunas encontradas
5. Recomendações de melhoria
6. Versão final resumida das principais recomendações
```

Agent:

```text
Avaliador do Relatório
```

---

## 15. Criar a crew

Criar uma nova crew em `Crews`.

Name:

```text
Equipe de Pesquisa de Mercado
```

Process:

```text
Sequential
```

Agents:

```text
Analista de Pesquisa de Mercado
Avaliador do Relatório
```

Tasks:

```text
Relatório de Pesquisa de Mercado
Avaliação do Relatório
```

Ordem das tarefas:

```text
1. Relatório de Pesquisa de Mercado
2. Avaliação do Relatório
```

---

## 16. Executar teste

Ir em `Kickoff` e executar a crew.

Prompt de teste:

```text
Analise a oportunidade de mercado para um canal no YouTube que ensina agentes de IA locais, Ollama, modelos em nuvem, provedores compatíveis com OpenAI e fluxos multiagentes para pessoas iniciantes e intermediárias.
```

Resultado esperado:

```text
1. Um relatório de pesquisa de mercado
2. Uma avaliação crítica do relatório
```

---

## 17. Checklist

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
Agente Analista de Pesquisa de Mercado criado
Agente Avaliador do Relatório criado
Tarefa Relatório de Pesquisa de Mercado criada
Tarefa Avaliação do Relatório criada
Crew criada com processo Sequential
Teste executado no Kickoff
Resultado conferido em Results
```
