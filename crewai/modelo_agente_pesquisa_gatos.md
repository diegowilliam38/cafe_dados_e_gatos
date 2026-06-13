# Como criar uma equipe de agentes no CrewAI

## Objetivo

Criar um projeto CrewAI com 4 agentes para gerar um manual em Markdown sobre as 10 raças de gatos mais conhecidas.

Equipe:

```text
1. Coordenador da Equipe
2. Pesquisador de Raças de Gatos
3. Redator do Manual
4. Revisor e Entregador Final
```

Fluxo:

```text
Planejar
Pesquisar
Redigir
Revisar e entregar
```

Modelos usados neste exemplo:

```text
Ollama local/cloud para agentes leves
MiniMax cloud oficial como provedor compatível com OpenAI
```

---

## 1. Instalar o uv

O CrewAI usa `uv` para criar ambiente, instalar dependências e executar o projeto.

No terminal:

```bash
curl -LsSf "https://astral.sh/uv/install.sh" | sh
```

Fechar e abrir o terminal novamente.

Conferir:

```bash
uv --version
```

---

## 2. Instalar o CrewAI

Este comando instala a ferramenta de linha de comando `crewai`.

```bash
uv tool install crewai
```

Se aparecer aviso de PATH:

```bash
uv tool update-shell
```

Fechar e abrir o terminal novamente.

Conferir instalação:

```bash
uv tool list
```

Resultado esperado:

```text
crewai
```

---

## 3. Criar o projeto

Este comando cria a estrutura inicial do projeto CrewAI.

```bash
crewai create crew manual_gatos
```

Entrar na pasta do projeto:

```bash
cd "manual_gatos"
```

---

## 4. Conferir a estrutura principal

Este passo serve para confirmar se o projeto foi criado no formato esperado.

```bash
ls
```

Estrutura esperada:

```text
manual_gatos/
├── .env
├── pyproject.toml
├── src/
│   └── manual_gatos/
│       ├── main.py
│       ├── crew.py
│       └── config/
│           ├── agents.yaml
│           └── tasks.yaml
```

---

## 5. Configurar o arquivo .env

O arquivo `.env` guarda variáveis de ambiente, chaves de API e nomes de modelos.

Não colocar código Python no `.env`.

Abrir o arquivo:

```bash
nano ".env"
```

Apagar o conteúdo atual e colar:

```env
# Modelo Ollama disponível localmente ou via Ollama Cloud
OLLAMA_BASE_URL="http://localhost:11434"
OLLAMA_MODEL_PHI="ollama/phi4-mini:latest"
OLLAMA_MODEL_GEMMA="ollama/gemma4:31b-cloud"

# MiniMax cloud oficial em endpoint compatível com OpenAI
MINIMAX_API_KEY="SUA_CHAVE_MINIMAX_AQUI"
MINIMAX_BASE_URL="https://api.minimax.io/v1"
MINIMAX_MODEL="NOME_EXATO_DO_MODELO_MINIMAX_AQUI"

# Configuração geral
CREWAI_TELEMETRY_OPT_OUT="true"
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

Importante:

```text
Substituir SUA_CHAVE_MINIMAX_AQUI pela chave real somente no ambiente local.
Substituir NOME_EXATO_DO_MODELO_MINIMAX_AQUI pelo nome correto do modelo no painel/documentação da MiniMax.
Não publicar o arquivo .env com chave real no GitHub.
```

---

## 6. Testar o Ollama antes de rodar o CrewAI

Este teste confirma se o Ollama está respondendo fora do CrewAI.

Listar modelos disponíveis:

```bash
ollama list
```

Testar um modelo local:

```bash
curl "http://localhost:11434/api/generate" -d '{
  "model": "phi4-mini:latest",
  "prompt": "Responda apenas: funcionando",
  "stream": false
}'
```

Se estiver usando outro nome no `ollama list`, trocar o valor de `"model"` pelo nome exato exibido.

Resultado esperado:

```text
funcionando
```

---

## 7. Editar os agentes

O arquivo `agents.yaml` define os agentes, seus papéis, objetivos e contexto de trabalho.

Os modelos não serão definidos aqui neste guia. Eles serão definidos diretamente no `crew.py`, para deixar claro qual agente usa Ollama e qual usa MiniMax.

Abrir o arquivo:

```bash
nano "src/manual_gatos/config/agents.yaml"
```

Apagar o conteúdo atual e colar:

```yaml
coordenador:
  role: >
    Coordenador da Equipe
  goal: >
    Organizar o trabalho da equipe e garantir que o manual final tenha estrutura clara,
    linguagem simples e foco no objetivo principal.
  backstory: >
    Você é um coordenador experiente em projetos de conteúdo educativo.
    Sua função é transformar uma ideia geral em um plano claro de execução,
    dividindo o trabalho entre pesquisa, redação e revisão.

pesquisador:
  role: >
    Pesquisador de Raças de Gatos
  goal: >
    Levantar informações confiáveis e organizadas sobre as 10 raças de gatos mais conhecidas.
  backstory: >
    Você é especialista em pesquisa e organização de informações.
    Seu trabalho é reunir dados claros sobre origem, aparência, comportamento
    e curiosidades de raças de gatos.

redator:
  role: >
    Redator do Manual
  goal: >
    Transformar a pesquisa em um manual didático, simples e bem estruturado.
  backstory: >
    Você escreve materiais educativos com linguagem acessível.
    Seu foco é explicar bem, sem enrolação, usando seções curtas e leitura fácil.

revisor:
  role: >
    Revisor e Entregador Final
  goal: >
    Revisar o manual, melhorar clareza, corrigir repetições e entregar a versão final em Markdown.
  backstory: >
    Você é especialista em revisão editorial.
    Seu trabalho é garantir que o material final esteja claro, organizado,
    coerente e pronto para ser publicado.
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

---

## 8. Editar as tarefas

O arquivo `tasks.yaml` define o que cada agente deve fazer.

Cada tarefa aponta para um agente. As tarefas seguintes podem receber o contexto das tarefas anteriores.

Abrir o arquivo:

```bash
nano "src/manual_gatos/config/tasks.yaml"
```

Apagar o conteúdo atual e colar:

```yaml
planejamento_task:
  description: >
    Crie um plano simples para um manual sobre as 10 raças de gatos mais conhecidas.
    Defina a estrutura do manual, a ordem das seções e os critérios para apresentar cada raça.
  expected_output: >
    Um plano em Markdown com título, introdução, lista das 10 raças e estrutura sugerida
    para cada raça.
  agent: coordenador

pesquisa_task:
  description: >
    Pesquise e organize informações sobre as 10 raças de gatos mais conhecidas.
    Para cada raça, inclua origem, aparência, comportamento, nível de energia
    e uma curiosidade.
  expected_output: >
    Uma pesquisa organizada em Markdown, com uma seção para cada raça.
  agent: pesquisador
  context:
    - planejamento_task

redacao_task:
  description: >
    Escreva um manual didático em português usando a pesquisa recebida.
    O manual deve ser claro, leve e organizado.
    Use linguagem simples para pessoas que gostam de gatos, mas não são especialistas.
  expected_output: >
    Um manual completo em Markdown com introdução, 10 seções de raças e conclusão.
  agent: redator
  context:
    - pesquisa_task

revisao_task:
  description: >
    Revise o manual final.
    Melhore clareza, fluidez, organização e consistência.
    Remova repetições desnecessárias.
    Entregue a versão final pronta para publicação.
  expected_output: >
    Um arquivo final em Markdown chamado manual_racas_gatos.md.
  agent: revisor
  context:
    - redacao_task
  output_file: "output/manual_racas_gatos.md"
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

---

## 9. Editar o arquivo da equipe

O arquivo `crew.py` monta a equipe.

Aqui ficam os modelos. Neste exemplo:

```text
Coordenador: MiniMax cloud
Pesquisador: Ollama Phi
Redator: MiniMax cloud
Revisor: Ollama Gemma
```

Abrir o arquivo:

```bash
nano "src/manual_gatos/crew.py"
```

Apagar o conteúdo atual e colar:

```python
import os

from crewai import Agent, Crew, LLM, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class ManualGatosCrew:
    """Equipe para criar um manual sobre raças de gatos."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def ollama_phi(self) -> LLM:
        """Modelo leve via Ollama para tarefas simples."""
        return LLM(
            model=os.getenv("OLLAMA_MODEL_PHI", "ollama/phi4-mini:latest"),
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
            temperature=0.2,
        )

    def ollama_gemma(self) -> LLM:
        """Modelo Gemma via Ollama local ou cloud."""
        return LLM(
            model=os.getenv("OLLAMA_MODEL_GEMMA", "ollama/gemma4:31b-cloud"),
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
            temperature=0.2,
        )

    def minimax_cloud(self) -> LLM:
        """Modelo MiniMax cloud oficial usando endpoint compatível com OpenAI."""
        return LLM(
            model=f"openai/{os.getenv('MINIMAX_MODEL', 'NOME_EXATO_DO_MODELO_MINIMAX_AQUI')}",
            api_key=os.getenv("MINIMAX_API_KEY"),
            base_url=os.getenv("MINIMAX_BASE_URL", "https://api.minimax.io/v1"),
            temperature=0.2,
        )

    @agent
    def coordenador(self) -> Agent:
        return Agent(
            config=self.agents_config["coordenador"],
            llm=self.minimax_cloud(),
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def pesquisador(self) -> Agent:
        return Agent(
            config=self.agents_config["pesquisador"],
            llm=self.ollama_phi(),
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def redator(self) -> Agent:
        return Agent(
            config=self.agents_config["redator"],
            llm=self.minimax_cloud(),
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def revisor(self) -> Agent:
        return Agent(
            config=self.agents_config["revisor"],
            llm=self.ollama_gemma(),
            verbose=True,
            allow_delegation=False,
        )

    @task
    def planejamento_task(self) -> Task:
        return Task(
            config=self.tasks_config["planejamento_task"],
        )

    @task
    def pesquisa_task(self) -> Task:
        return Task(
            config=self.tasks_config["pesquisa_task"],
        )

    @task
    def redacao_task(self) -> Task:
        return Task(
            config=self.tasks_config["redacao_task"],
        )

    @task
    def revisao_task(self) -> Task:
        return Task(
            config=self.tasks_config["revisao_task"],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

---

## 10. Alternativa: rodar tudo só com Ollama

Use esta opção se quiser testar sem MiniMax primeiro.

No arquivo `crew.py`, trocar estes dois trechos:

```python
llm=self.minimax_cloud(),
```

por:

```python
llm=self.ollama_phi(),
```

Assim, todos os agentes rodam pelo Ollama.

---

## 11. Conferir o arquivo main.py

O arquivo `main.py` é o ponto de entrada do projeto.

Ele define o comando que será executado quando rodar:

```bash
crewai run
```

Abrir o arquivo:

```bash
nano "src/manual_gatos/main.py"
```

Verificar se ele importa a classe correta do arquivo `crew.py`.

Apagar o conteúdo atual e colar:

```python
#!/usr/bin/env python
import sys

from manual_gatos.crew import ManualGatosCrew


def run():
    """
    Executa a equipe.
    """
    inputs = {
        "tema": "Manual com as 10 raças de gatos mais conhecidas"
    }
    ManualGatosCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Treina a equipe por um número de iterações.
    """
    inputs = {
        "tema": "Manual com as 10 raças de gatos mais conhecidas"
    }
    try:
        ManualGatosCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"Erro ao treinar a equipe: {e}")


def replay():
    """
    Repete a execução a partir de uma tarefa específica.
    """
    try:
        ManualGatosCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"Erro ao repetir a execução: {e}")


def test():
    """
    Testa a execução da equipe.
    """
    inputs = {
        "tema": "Manual com as 10 raças de gatos mais conhecidas"
    }
    try:
        ManualGatosCrew().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"Erro ao testar a equipe: {e}")
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

---

## 12. Criar a pasta de saída

A tarefa final vai salvar o arquivo `manual_racas_gatos.md` dentro da pasta `output`.

Criar a pasta:

```bash
mkdir -p "output"
```

---

## 13. Instalar dependências do projeto

O comando `crewai install` instala as dependências declaradas no projeto, usando o ambiente gerenciado pelo `uv`.

Ele deve ser rodado dentro da raiz do projeto, onde está o arquivo `pyproject.toml`.

Na raiz do projeto:

```bash
crewai install
```

Por que este passo fica depois da edição dos arquivos:

```text
Porque primeiro o projeto é criado e configurado.
Depois o ambiente do projeto é preparado para executar a equipe.
Se o projeto usar LiteLLM, Ollama ou outros provedores, as dependências precisam estar instaladas antes do crewai run.
```

Se for usar Ollama, MiniMax ou outro provedor via LiteLLM, adicionar suporte a LiteLLM:

```bash
uv add "crewai[litellm]"
```

Depois rodar novamente:

```bash
crewai install
```

---

## 14. Rodar a equipe

Executar a crew:

```bash
crewai run
```

---

## 15. Conferir o resultado

Conferir se o arquivo foi gerado:

```bash
ls "output"
```

Abrir o arquivo gerado:

```bash
cat "output/manual_racas_gatos.md"
```

Resultado esperado:

```text
manual_racas_gatos.md
```

---

## 16. Erro: comando crewai não encontrado

Erro:

```text
crewai: command not found
```

Correção:

```bash
uv tool update-shell
```

Fechar e abrir o terminal novamente.

Testar:

```bash
crewai --help
```

---

## 17. Erro: chave da MiniMax não configurada

Erro possível:

```text
MINIMAX_API_KEY não configurada
```

Correção:

```bash
nano ".env"
```

Conferir se existe:

```env
MINIMAX_API_KEY="SUA_CHAVE_MINIMAX_AQUI"
MINIMAX_BASE_URL="https://api.minimax.io/v1"
MINIMAX_MODEL="NOME_EXATO_DO_MODELO_MINIMAX_AQUI"
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

---

## 18. Erro: modelo MiniMax não encontrado

Erro possível:

```text
model not found
```

Causa provável:

```text
O nome do modelo MiniMax no .env não é o nome aceito pela API.
```

Correção:

```bash
nano ".env"
```

Corrigir:

```env
MINIMAX_MODEL="NOME_EXATO_DO_MODELO_MINIMAX_AQUI"
```

Usar o nome exato informado pela documentação ou painel da MiniMax.

---

## 19. Erro: Ollama não responde

Testar o Ollama:

```bash
curl "http://localhost:11434/api/tags"
```

Se não responder, subir o Ollama:

```bash
ollama serve
```

---

## 20. Erro: modelo Ollama não encontrado

Listar modelos:

```bash
ollama list
```

Corrigir o `.env` com o nome real do modelo instalado.

Exemplo:

```env
OLLAMA_MODEL_PHI="ollama/phi4-mini:latest"
```

No teste direto via `curl`, o nome usado não tem o prefixo `ollama/`:

```bash
curl "http://localhost:11434/api/generate" -d '{
  "model": "phi4-mini:latest",
  "prompt": "teste",
  "stream": false
}'
```

No CrewAI, o modelo usa prefixo `ollama/`:

```text
ollama/phi4-mini:latest
```

---

## 21. Como remover o projeto

Entrar na pasta onde o projeto foi criado:

```bash
cd "$HOME"
```

Remover a pasta do projeto:

```bash
rm -rf "manual_gatos"
```

Conferir:

```bash
ls "$HOME" | grep "manual_gatos"
```

Se não aparecer nada, a pasta foi removida.

---

## 22. Como remover o CrewAI instalado por uv tool

Listar ferramentas instaladas:

```bash
uv tool list
```

Remover o CrewAI:

```bash
uv tool uninstall crewai
```

Conferir:

```bash
uv tool list
```

---

## 23. Como remover cache opcional

Aviso: este passo remove caches locais usados pelo `uv`. Não é obrigatório.

```bash
uv cache clean
```

---

## 24. Fontes usadas

```text
CrewAI Installation:
https://docs.crewai.com/en/installation

CrewAI LLMs:
https://docs.crewai.com/en/concepts/llms
```
