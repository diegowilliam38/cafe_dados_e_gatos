# Como criar uma equipe de agentes no CrewAI

## 1. Instalar o CrewAI

No terminal:

```bash
uv tool install crewai
```

Se aparecer aviso de PATH:

```bash
uv tool update-shell
```

Feche e abra o terminal novamente.

Conferir instalação:

```bash
uv tool list
```

## 2. Criar o projeto

```bash
crewai create crew manual_gatos
```

Entrar na pasta:

```bash
cd "manual_gatos"
```

## 3. Estrutura principal

Arquivos principais:

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

## 4. Configurar variáveis de ambiente

Editar o arquivo `.env`:

```env
OPENAI_API_KEY="SUA_CHAVE_AQUI"
OPENAI_MODEL_NAME="gpt-4o-mini"
```

## 5. Editar os agentes

Arquivo:

```text
src/manual_gatos/config/agents.yaml
```

Conteúdo:

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

## 6. Editar as tarefas

Arquivo:

```text
src/manual_gatos/config/tasks.yaml
```

Conteúdo:

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

## 7. Editar o arquivo da equipe

Arquivo:

```text
src/manual_gatos/crew.py
```

Conteúdo:

```python
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class ManualGatosCrew:
    """Equipe para criar um manual sobre raças de gatos."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def coordenador(self) -> Agent:
        return Agent(
            config=self.agents_config["coordenador"],
            verbose=True,
        )

    @agent
    def pesquisador(self) -> Agent:
        return Agent(
            config=self.agents_config["pesquisador"],
            verbose=True,
        )

    @agent
    def redator(self) -> Agent:
        return Agent(
            config=self.agents_config["redator"],
            verbose=True,
        )

    @agent
    def revisor(self) -> Agent:
        return Agent(
            config=self.agents_config["revisor"],
            verbose=True,
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

## 8. Instalar dependências do projeto

Na raiz do projeto:

```bash
crewai install
```

## 9. Rodar a equipe

```bash
crewai run
```

## 10. Conferir o resultado

Abrir o arquivo gerado:

```bash
cat "output/manual_racas_gatos.md"
```

Ou abrir a pasta:

```bash
ls "output"
```

Resultado esperado:

```text
manual_racas_gatos.md
```

## 11. O que mostrar no vídeo

Mostrar a criação do projeto:

```bash
crewai create crew manual_gatos
```

Mostrar os arquivos principais:

```bash
ls
ls "src/manual_gatos/config"
```

Mostrar os agentes:

```bash
cat "src/manual_gatos/config/agents.yaml"
```

Mostrar as tarefas:

```bash
cat "src/manual_gatos/config/tasks.yaml"
```

Rodar a equipe:

```bash
crewai run
```

Mostrar o resultado:

```bash
cat "output/manual_racas_gatos.md"
```

## 12. Resumo da lógica

```text
Agente = papel dentro da equipe
Tarefa = trabalho que será executado
Crew = equipe completa
Process sequential = uma tarefa depois da outra
output_file = arquivo final gerado
```
