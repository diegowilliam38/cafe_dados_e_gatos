# OpenJarvis no Linux: configuração, Google OAuth, Gemini, conectores e skills

Este documento continua a configuração depois que o OpenJarvis já está instalado no Linux.

O objetivo aqui não é reinstalar tudo. A ideia é deixar o ambiente pronto para uso real: iniciar o servidor corretamente, configurar modelo local ou em nuvem, conectar Google Drive/Gmail/Calendar/Tasks via OAuth, entender onde ficam os arquivos de configuração e testar conectores, agentes e skills.

> Referências usadas nesta documentação:
>
> - Documentação oficial do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/
> - Instalação oficial do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/getting-started/installation/
> - Configuração oficial do OpenJarvis: https://open-jarvis.github.io/OpenJarvis/getting-started/configuration/
> - Google Workspace - criação de credenciais: https://developers.google.com/workspace/guides/create-credentials
> - Google Workspace - tela de consentimento OAuth: https://developers.google.com/workspace/guides/configure-oauth-consent

---

## Observação importante sobre `jarvis` e `uv run jarvis`

A documentação oficial mostra comandos usando `jarvis` direto depois da instalação do CLI.

No ambiente testado neste vídeo, o projeto estava instalado em:

```text
~/OpenJarvis
```

A pasta `.venv` existia dentro do projeto:

```text
~/OpenJarvis/.venv
```

Mesmo assim, ao rodar o comando direto:

```bash
jarvis
```

o terminal retornou:

```text
jarvis: command not found
```

Isso significa que o OpenJarvis pode estar instalado dentro do ambiente do projeto, mas o comando `jarvis` ainda não está disponível globalmente no `PATH` do sistema.

Por isso, neste guia, o caminho mais seguro para o teste é sempre entrar na pasta do projeto e executar com `uv run`:

```bash
cd ~/OpenJarvis
uv run jarvis --version
uv run jarvis doctor
```

Se o comando `jarvis` direto funcionar no seu terminal, você pode usar os comandos curtos da documentação oficial. Se não funcionar, use sempre o formato:

```bash
cd ~/OpenJarvis
uv run jarvis <comando>
```

Exemplo:

```bash
cd ~/OpenJarvis
uv run jarvis ask "Responda apenas: OpenJarvis funcionando."
```

---

## Conferir onde o OpenJarvis está instalado

Para verificar se a pasta do projeto existe:

```bash
ls -la ~ | grep OpenJarvis
```

Ou procure pela pasta:

```bash
find ~ -type d -iname "OpenJarvis" 2>/dev/null
```

Entre na pasta:

```bash
cd ~/OpenJarvis
pwd
ls -la
```

O `pwd` deve mostrar algo parecido com:

```text
/home/denise/OpenJarvis
```

Confira se o ambiente virtual existe:

```bash
ls -la .venv
```

Confira se existe executável do Jarvis dentro do ambiente:

```bash
ls .venv/bin | grep jarvis
```

Se aparecer `jarvis`, também é possível testar diretamente:

```bash
./.venv/bin/jarvis --version
./.venv/bin/jarvis doctor
```

Se `.venv` existe, mas `jarvis` não aparece dentro de `.venv/bin`, o ambiente foi criado, mas o CLI ainda não foi registrado corretamente.

---

## Instalação oficial do CLI

Segundo a documentação oficial do OpenJarvis, a instalação do CLI a partir do repositório usa este fluxo:

```bash
git clone https://github.com/open-jarvis/OpenJarvis.git
cd OpenJarvis
uv sync
uv run maturin develop -m rust/crates/openjarvis-python/Cargo.toml
```

Depois, a verificação oficial é:

```bash
jarvis --version
```

Se `jarvis --version` retornar `command not found`, use o diagnóstico abaixo.

---

## Diagnóstico quando `jarvis` dá command not found

Confirme se está na pasta certa:

```bash
cd ~/OpenJarvis
pwd
ls -la
```

Confirme se o `uv` está instalado:

```bash
uv --version
```

Confirme se o ambiente virtual existe:

```bash
ls -la .venv
```

Tente rodar pelo `uv`:

```bash
uv run jarvis --version
uv run jarvis doctor
```

Se ainda falhar, rode novamente a etapa que registra o pacote Python/Rust no ambiente:

```bash
cd ~/OpenJarvis
uv run maturin develop -m rust/crates/openjarvis-python/Cargo.toml
```

Depois teste:

```bash
uv run jarvis --version
uv run jarvis doctor
```

Se funcionar com `uv run`, mas não funcionar com `jarvis` direto, o problema é apenas o comando global não estar no `PATH`.

---

## Estrutura básica do OpenJarvis

No uso diário, existem três partes importantes:

- **CLI do Jarvis**: comandos como `jarvis ask`, `jarvis chat`, `jarvis doctor`, `jarvis connect`.
- **Jarvis Server / Backend**: servidor local, normalmente na porta `8000`.
- **Interface web ou desktop**: pode abrir em outra porta, como `5173`, `5139` ou outra porta local.

A porta `8000` costuma ser o backend/API:

```text
http://127.0.0.1:8000
```

A interface visual pode aparecer em algo como:

```text
http://127.0.0.1:5173
```

---

## Onde ficam os arquivos principais

No Linux, o OpenJarvis usa a pasta local do usuário para guardar configurações, memória, skills, traces e conectores.

Caminhos importantes:

```text
~/.openjarvis/
~/.openjarvis/config.toml
~/.openjarvis/connectors/
~/.openjarvis/skills/
~/.openjarvis/memory.db
~/.openjarvis/traces.db
~/.openjarvis/telemetry.db
```

Para listar:

```bash
ls -la ~/.openjarvis
```

Para ver conectores autenticados:

```bash
ls -la ~/.openjarvis/connectors
```

Para abrir a configuração no Nano:

```bash
nano ~/.openjarvis/config.toml
```

Se usa VS Code:

```bash
code ~/.openjarvis/config.toml
```

---

## Gerar ou regenerar configuração

Se ainda não existir configuração, rode um preset inicial.

Caminho seguro usando `uv`:

```bash
cd ~/OpenJarvis
uv run jarvis init --preset chat-simple
```

Para resumo matinal no Linux:

```bash
cd ~/OpenJarvis
uv run jarvis init --preset morning-digest-linux
```

> Atenção: regenerar configuração pode alterar escolhas anteriores de engine, agente, modelo e ferramentas. Se você já ajustou o `config.toml`, faça backup antes.

Backup simples:

```bash
cp ~/.openjarvis/config.toml ~/.openjarvis/config.toml.bak
```

---

## Iniciar o Jarvis Server no Linux

Para iniciar o backend local:

```bash
cd ~/OpenJarvis
uv run jarvis serve --port 8000
```

Se quiser restringir o servidor apenas ao próprio computador:

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8000
```

A documentação oficial informa que a seção `[server]` do `config.toml` controla host, porta, agente e modelo do servidor.

Exemplo:

```toml
[server]
host = "127.0.0.1"
port = 8000
agent = "orchestrator"
model = ""
workers = 1
```

Quando `model = ""`, o OpenJarvis usa o modelo padrão definido na seção de inteligência ou o primeiro modelo disponível.

---

## Configurar engine local com Ollama

Se você quer usar modelo local com Ollama, confirme que o Ollama está rodando:

```bash
ollama serve
```

Em outro terminal, liste os modelos:

```bash
ollama list
```

Baixe um modelo leve para teste:

```bash
ollama pull qwen3:0.6b
```

Teste pelo Jarvis:

```bash
cd ~/OpenJarvis
uv run jarvis model list
```

Exemplo de configuração local no `~/.openjarvis/config.toml`:

```toml
[engine]
default = "ollama"

[engine.ollama]
host = "http://localhost:11434"

[intelligence]
default_model = "qwen3:0.6b"
temperature = 0.7
max_tokens = 2048

[agent]
default_agent = "orchestrator"
max_turns = 10
context_from_memory = true
```

Teste:

```bash
cd ~/OpenJarvis
uv run jarvis ask "Explique em uma frase o que é o OpenJarvis."
```

---

## Configurar Google Gemini como modelo

Aqui existem duas coisas diferentes:

- **Google Gemini via API Key**: usado como modelo de linguagem.
- **Google Workspace via OAuth**: usado para Drive, Gmail, Calendar, Contacts e Tasks.

Para usar Gemini como modelo, a documentação oficial do OpenJarvis indica o extra `inference-google` e a variável `GOOGLE_API_KEY`.

Dentro da pasta do OpenJarvis:

```bash
cd ~/OpenJarvis
uv sync --extra inference-google
```

Depois, exporte a chave da API do Google:

```bash
export GOOGLE_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Para não precisar exportar toda vez, adicione no final do `~/.bashrc`:

```bash
nano ~/.bashrc
```

Adicione:

```bash
export GOOGLE_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Recarregue:

```bash
source ~/.bashrc
```

Teste sem revelar a chave:

```bash
python3 - <<'PY'
import os
print('GOOGLE_API_KEY configurada:', bool(os.getenv('GOOGLE_API_KEY')))
PY
```

> Importante: não grave vídeo mostrando a chave. Não coloque API Key em repositório público.

---

## Configurar OpenAI, Anthropic, MiniMax e Tavily

A documentação oficial lista variáveis de ambiente para provedores em nuvem.

```bash
export OPENAI_API_KEY="COLE_SUA_CHAVE_AQUI"
export ANTHROPIC_API_KEY="COLE_SUA_CHAVE_AQUI"
export GOOGLE_API_KEY="COLE_SUA_CHAVE_AQUI"
export MINIMAX_API_KEY="COLE_SUA_CHAVE_AQUI"
export TAVILY_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Para OpenAI e Anthropic, instale o extra de cloud inference:

```bash
cd ~/OpenJarvis
uv sync --extra inference-cloud
```

Para Google Gemini:

```bash
cd ~/OpenJarvis
uv sync --extra inference-google
```

Para instalar os dois:

```bash
cd ~/OpenJarvis
uv sync --extra inference-cloud --extra inference-google
```

No Linux, uma forma simples de persistir as chaves é colocar no `~/.bashrc`:

```bash
nano ~/.bashrc
```

Exemplo:

```bash
export OPENAI_API_KEY="COLE_SUA_CHAVE_AQUI"
export ANTHROPIC_API_KEY="COLE_SUA_CHAVE_AQUI"
export GOOGLE_API_KEY="COLE_SUA_CHAVE_AQUI"
export MINIMAX_API_KEY="COLE_SUA_CHAVE_AQUI"
export TAVILY_API_KEY="COLE_SUA_CHAVE_AQUI"
```

Recarregue:

```bash
source ~/.bashrc
```

Confira sem mostrar os valores:

```bash
python3 - <<'PY'
import os
for key in ['OPENAI_API_KEY','ANTHROPIC_API_KEY','GOOGLE_API_KEY','MINIMAX_API_KEY','TAVILY_API_KEY']:
    print(key, 'OK' if os.getenv(key) else 'NAO CONFIGURADA')
PY
```

---

## Google Workspace OAuth: Drive, Gmail, Calendar, Contacts e Tasks

Esta parte é para conectar serviços da sua conta Google.

O fluxo básico recomendado no teste é:

```bash
cd ~/OpenJarvis
uv run jarvis init --preset morning-digest-linux
uv run jarvis connect gdrive
uv run jarvis digest --fresh
```

Na prática:

- `uv run jarvis connect gdrive` inicia a autenticação OAuth.
- O navegador abre para autorizar sua conta Google.
- Depois da autorização, os tokens são salvos localmente.
- Os conectores Google passam a usar esses tokens.

---

## Criar credenciais OAuth no Google Cloud

Para o OAuth funcionar, você precisa criar credenciais no Google Cloud.

Acesse:

```text
https://console.cloud.google.com/
```

Crie um projeto ou selecione um projeto existente.

Sugestão de nome:

```text
OpenJarvis Local
```

No Google Cloud Console, vá em:

```text
APIs e serviços > Biblioteca
```

Ative as APIs que pretende usar:

- Google Drive API
- Gmail API
- Google Calendar API
- Google Tasks API
- People API, se for usar contatos

Depois configure a tela de consentimento OAuth:

```text
Google Auth Platform > Branding / OAuth consent screen
```

Configure como app externo em modo de teste, se for apenas para uso pessoal.

Preencha o mínimo necessário:

- Nome do app: `OpenJarvis Local`
- E-mail de suporte: seu próprio e-mail
- E-mail do desenvolvedor: seu próprio e-mail

Depois, adicione seu Gmail como usuário de teste.

> Se o app ficar em modo de teste e seu e-mail não estiver como usuário de teste, a autorização pode falhar.

Crie o OAuth Client ID:

```text
Google Auth Platform > Clients > Create Client
```

Escolha:

```text
Application type > Desktop app
```

Nome sugerido:

```text
OpenJarvis Linux
```

Guarde:

- Client ID
- Client Secret

> Não mostre o Client Secret em vídeo, print, live ou GitHub.

---

## Rodar o OAuth no OpenJarvis

Com o projeto configurado no Google Cloud e o OpenJarvis rodando, execute:

```bash
cd ~/OpenJarvis
uv run jarvis connect gdrive
```

O esperado:

- O OpenJarvis inicia o fluxo OAuth.
- O navegador abre.
- Você escolhe sua conta Google.
- Você aceita os escopos/permissões.
- O OpenJarvis salva os tokens em `~/.openjarvis/connectors/`.

Depois, confira:

```bash
ls -la ~/.openjarvis/connectors
```

Você deve ver arquivos `.json`, possivelmente algo como:

```text
google.json
gdrive.json
gmail.json
gcalendar.json
google_tasks.json
```

Os nomes podem variar conforme a versão, mas a pasta correta é:

```text
~/.openjarvis/connectors/
```

---

## Testar Google depois da autenticação

Depois do `connect gdrive`, teste o digest:

```bash
cd ~/OpenJarvis
uv run jarvis digest --fresh
```

Você também pode testar uma pergunta simples usando agente com ferramentas, se seu preset já habilitou conectores:

```bash
cd ~/OpenJarvis
uv run jarvis ask --agent orchestrator "Verifique se meus conectores Google estão disponíveis e responda quais parecem configurados."
```

Se o comando informar falta de credenciais, rode novamente:

```bash
cd ~/OpenJarvis
uv run jarvis connect gdrive
```

---

## Se o Google OAuth falhar

Verifique estes pontos:

- Você ativou as APIs corretas no Google Cloud?
- O app está com tela de consentimento configurada?
- Seu e-mail foi adicionado como usuário de teste?
- O tipo de credencial é **Desktop app**?
- Você está rodando o comando no mesmo usuário Linux que executa o OpenJarvis?
- A pasta `~/.openjarvis/connectors/` existe?
- O navegador abriu durante o fluxo OAuth?
- Você autorizou todos os escopos solicitados?

Para ver se existem tokens:

```bash
ls -la ~/.openjarvis/connectors
```

Para limpar tokens e refazer a autenticação, mova a pasta antiga para backup:

```bash
mv ~/.openjarvis/connectors ~/.openjarvis/connectors_bak
mkdir -p ~/.openjarvis/connectors
```

Depois rode novamente:

```bash
cd ~/OpenJarvis
uv run jarvis connect gdrive
```

> Atenção: o comando acima não apaga sua conta Google. Ele apenas tira do caminho os tokens locais do OpenJarvis para forçar uma nova autenticação.

---

## Configurar memória local

A documentação oficial informa que o backend padrão de memória é SQLite, sem dependências extras.

Exemplo no `~/.openjarvis/config.toml`:

```toml
[tools.storage]
default_backend = "sqlite"
db_path = "~/.openjarvis/memory.db"
context_top_k = 5
context_min_score = 0.1
context_max_tokens = 2048
chunk_size = 512
chunk_overlap = 64
```

Para conferir se o banco existe:

```bash
ls -lh ~/.openjarvis/memory.db
```

Se quiser usar FAISS:

```bash
cd ~/OpenJarvis
uv sync --extra memory-faiss
```

Depois ajuste:

```toml
[tools.storage]
default_backend = "faiss"
```

Para começar, SQLite é suficiente.

---

## Configurar MCP

O OpenJarvis tem seção própria para MCP:

```toml
[tools.mcp]
enabled = true
servers = ""
```

Depois você pode adicionar servidores externos quando for testar ferramentas específicas.

---

## Skills no OpenJarvis

Skills são capacidades extras que ensinam os agentes a usar ferramentas e executar tarefas específicas.

Exemplos:

```bash
cd ~/OpenJarvis
uv run jarvis skill install hermes:arxiv
uv run jarvis skill sync hermes --category research
```

Também é possível chamar uma skill diretamente:

```bash
cd ~/OpenJarvis
uv run jarvis ask "Use the code-explainer skill to explain this Python code: for i in range(5): print(i*2)"
```

Configuração típica no `config.toml`:

```toml
[skills]
enabled = true
skills_dir = "~/.openjarvis/skills/"
active = "*"
auto_discover = true
auto_sync = false
max_depth = 5
sandbox_dangerous = true
```

Para listar a pasta:

```bash
ls -la ~/.openjarvis/skills
```

---

## Agentes internos do OpenJarvis

O OpenJarvis vem com agentes internos para tipos diferentes de tarefa.

| Agente | Tipo | Uso principal |
|---|---|---|
| `simple` | Sob demanda | Chat simples, sem ferramentas |
| `orchestrator` | Sob demanda | Raciocínio multi-turno com seleção de ferramentas |
| `native_react` | Sob demanda | Loop ReAct: pensamento, ação e observação |
| `native_openhands` | Sob demanda | Agente de código que executa Python |
| `deep_research` | Sob demanda | Pesquisa aprofundada com citações |
| `morning_digest` | Agendado | Resumo diário com e-mail, calendário, notícias e áudio |
| `monitor_operative` | Contínuo | Monitoramento com memória e recuperação |
| `operative` | Contínuo | Agente autônomo persistente |

Exemplo de pergunta com agente específico:

```bash
cd ~/OpenJarvis
uv run jarvis ask --agent simple "Explique o que é um conector em uma frase."
```

Exemplo com orquestrador:

```bash
cd ~/OpenJarvis
uv run jarvis ask --agent orchestrator "Liste três formas de testar se o Google Drive está conectado."
```

---

## Voz, Whisper e Deepgram

Se aparecer mensagem parecida com:

```text
Requires Whisper, Deepgram, or another speech backend
```

isso não significa necessariamente que o Jarvis Server está quebrado.

Significa que o backend principal pode estar funcionando, mas a parte de voz/transcrição ainda precisa ser configurada.

Resumo para vídeo:

```text
Jarvis Server rodando = backend principal funcionando.
Whisper/Deepgram ausente = recurso de fala ainda não configurado.
```

Para começar, teste primeiro texto e conectores. Voz fica para uma etapa separada.

---

## Comandos úteis de diagnóstico

Verificar instalação:

```bash
cd ~/OpenJarvis
uv run jarvis doctor
```

Listar modelos:

```bash
cd ~/OpenJarvis
uv run jarvis model list
```

Abrir chat no terminal:

```bash
cd ~/OpenJarvis
uv run jarvis chat
```

Pergunta simples:

```bash
cd ~/OpenJarvis
uv run jarvis ask "O OpenJarvis está respondendo?"
```

Subir servidor:

```bash
cd ~/OpenJarvis
uv run jarvis serve --host 127.0.0.1 --port 8000
```

Conectar Google:

```bash
cd ~/OpenJarvis
uv run jarvis connect gdrive
```

Gerar resumo matinal:

```bash
cd ~/OpenJarvis
uv run jarvis digest --fresh
```

---

## Fluxo recomendado para gravar o vídeo

### Mostrar que o projeto existe

```bash
cd ~/OpenJarvis
pwd
ls -la
ls -la .venv
```

Fala sugerida:

```text
Aqui tem uma pegadinha importante: a pasta existe, o ambiente virtual existe, mas isso não significa que o comando jarvis esteja disponível globalmente no terminal.
```

### Mostrar o erro do comando global

```bash
jarvis
which jarvis
whereis jarvis
```

Fala sugerida:

```text
Quando aparece command not found, o problema não é necessariamente que o OpenJarvis não foi instalado. Pode ser apenas que o comando não está no PATH do sistema.
```

### Usar o caminho seguro

```bash
cd ~/OpenJarvis
uv run jarvis --version
uv run jarvis doctor
```

Fala sugerida:

```text
Por isso, neste teste, eu vou usar o caminho mais seguro: entrar na pasta do projeto e rodar os comandos com uv run.
```

### Mostrar onde ficam as configurações

```bash
ls -la ~/.openjarvis
nano ~/.openjarvis/config.toml
```

### Conferir modelo

```bash
ollama list
cd ~/OpenJarvis
uv run jarvis model list
```

### Conectar Google

```bash
cd ~/OpenJarvis
uv run jarvis connect gdrive
ls -la ~/.openjarvis/connectors
```

### Testar uso real

```bash
cd ~/OpenJarvis
uv run jarvis digest --fresh
```

ou:

```bash
cd ~/OpenJarvis
uv run jarvis ask --agent orchestrator "Verifique quais conectores parecem disponíveis."
```

---

## Erros encontrados e ajustes necessários

### `jarvis: command not found`

**O que aconteceu:**

O projeto `~/OpenJarvis` existia e a pasta `.venv` também existia, mas o comando direto `jarvis` não foi encontrado pelo terminal.

**Onde apareceu:**

```bash
jarvis
```

Retorno:

```text
jarvis: command not found
```

**Diagnóstico usado:**

```bash
which jarvis
whereis jarvis
cd ~/OpenJarvis
ls -la
ls -la .venv
```

**Correção usada no guia:**

Rodar os comandos dentro da pasta do projeto usando `uv run`:

```bash
cd ~/OpenJarvis
uv run jarvis doctor
```

**Observação:**

Na documentação oficial, a verificação aparece como `jarvis --version` depois da instalação do CLI. No ambiente testado, o caminho seguro foi usar `uv run jarvis`, porque o comando global não estava disponível.

---

## Resumo final

Fluxo principal no Linux usando o caminho seguro:

```bash
cd ~/OpenJarvis
uv run jarvis --version
uv run jarvis doctor
uv run jarvis init --preset morning-digest-linux
uv run jarvis connect gdrive
uv run jarvis digest --fresh
```

Arquivos importantes:

```text
~/.openjarvis/config.toml
~/.openjarvis/connectors/
~/.openjarvis/skills/
~/.openjarvis/memory.db
```

Variáveis importantes:

```bash
OPENAI_API_KEY
ANTHROPIC_API_KEY
GOOGLE_API_KEY
MINIMAX_API_KEY
TAVILY_API_KEY
```

Diferença essencial:

```text
GOOGLE_API_KEY = Gemini/modelo.
Google OAuth = Drive/Gmail/Calendar/Contacts/Tasks.
```
