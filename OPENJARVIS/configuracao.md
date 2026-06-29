#OpenJarvis no Windows: servidor, Google OAuth, conectores e skills

Vamos continuar depois da instalação do OpenJarvis no Windows.

O objetivo é deixar o ambiente pronto para uso real: iniciar o Jarvis Server da forma correta, conectar Google Drive/Gmail/Calendar/Tasks via OAuth, entender os conectores e conhecer a ideia de presets, agentes e skills.

> Observação: no Windows, em alguns casos, o app do Jarvis abre, mas o Jarvis Server não inicia automaticamente. Quando isso acontece, precisamos iniciar o servidor manualmente na pasta correta do projeto.

---

## 1. Estrutura básica

No OpenJarvis, existem duas partes importantes:

- **Jarvis Server / Backend**: normalmente roda na porta `8000`.
- **Interface visual / Desktop / Web UI**: pode abrir em outra porta, como `5139`, `5173` ou similar.

Exemplo:

```text
http://127.0.0.1:8000
```

Essa porta costuma ser a API/backend, não necessariamente a interface visual.

A interface pode estar em algo como:

```text
http://127.0.0.1:5173
```

ou:

```text
http://127.0.0.1:5139
```

---

## 2. Problema comum no Windows

Às vezes o app do Jarvis abre, mas o servidor não carrega automaticamente.

Sintomas comuns:

- O botão de conexão fica em `Synchronizing...`.
- O navegador não abre automaticamente.
- O comando `uv run jarvis serve 8000` falha se for executado fora da pasta correta.
- Aparece erro parecido com:

```text
Failed to spawn: jarvis
Caused by: program not found
```

Isso geralmente acontece porque o comando foi executado fora da pasta do projeto.

---

## 3. Como descobrir a pasta correta do OpenJarvis

Abra o PowerShell e rode:

```powershell
Get-ChildItem -Path C:\Users\denis -Filter pyproject.toml -Recurse -ErrorAction SilentlyContinue
```

O arquivo `pyproject.toml` indica a raiz do projeto.

No meu caso, a pasta correta apareceu como:

```text
C:\Users\denis\OpenJarvis
```

Ou seja, a pasta certa é a que contém:

```text
pyproject.toml
README.md
src
.venv
```

Para testar:

```powershell
cd "C:\Users\denis\OpenJarvis"
dir
```

Se aparecer o `pyproject.toml`, você está na pasta certa.

---

## 4. Como iniciar o Jarvis Server manualmente

Depois de entrar na pasta correta, rode:

```powershell
cd "C:\Users\denis\OpenJarvis"
uv run jarvis serve 8000
```

Se tudo estiver certo, o servidor será iniciado na porta `8000`.

Depois disso, abra o app/interface do Jarvis normalmente.

---

## 5. Criando um atalho para iniciar o Jarvis Server

Para não precisar digitar o comando toda vez, podemos criar um arquivo `.bat`.

Crie um arquivo chamado:

```text
iniciar_jarvis_server.bat
```

Conteúdo do arquivo:

```bat
@echo off
cd /d "C:\Users\denis\OpenJarvis"
uv run jarvis serve 8000
pause
```

Agora basta dar dois cliques nesse arquivo para iniciar o Jarvis Server.

---

## 6. Criando um ícone na área de trabalho

Depois de criar o `.bat`:

1. Clique com o botão direito na área de trabalho.
2. Vá em **Novo → Atalho**.
3. Aponte para o arquivo:

```text
C:\Users\denis\OpenJarvis\iniciar_jarvis_server.bat
```

4. Nomeie como:

```text
Iniciar Jarvis Server
```

5. Se quiser, clique com o botão direito no atalho, vá em **Propriedades → Alterar ícone**.

Fluxo recomendado:

1. Clicar em **Iniciar Jarvis Server**.
2. Abrir o app/interface do OpenJarvis.
3. Fazer as conexões e testes.

---

## 7. Conectando Google Drive, Gmail, Calendar e Tasks

Segundo a documentação do OpenJarvis, um único OAuth do Google pode cobrir:

- Google Drive
- Gmail
- Google Calendar
- Google Tasks

Exemplo da documentação:

```bash
jarvis init --preset morning-digest-mac
jarvis connect gdrive          # one OAuth covers Gmail / Calendar / Tasks
jarvis digest --fresh          # generate and play your first briefing
```

Na prática, isso significa que a autenticação feita para o Google Drive também pode ser usada para outros serviços Google, dependendo dos escopos/permissões configurados.

---

## 8. Configuração no Google Cloud

Para usar os conectores Google, precisamos criar credenciais OAuth.

Passo a passo:

1. Acesse o Google Cloud Console.
2. Crie ou selecione um projeto.
3. Vá em **APIs e serviços → Biblioteca**.
4. Ative as APIs necessárias:
   - Google Drive API
   - Gmail API
   - Google Calendar API
   - Google Tasks API, se for usar Tasks
5. Vá em **APIs e serviços → Tela de consentimento OAuth**.
6. Configure como app externo em modo de teste.
7. Adicione seu próprio Gmail em **Usuários de teste**.
8. Vá em **APIs e serviços → Credenciais**.
9. Clique em **Criar credenciais → ID do cliente OAuth**.
10. Escolha **Aplicativo para computador / Desktop App**.
11. Copie o `Client ID` e o `Client Secret`.

Importante: não mostrar o `Client Secret` em vídeo, print ou live.

---

## 9. O que acontece depois do Client ID e Client Secret

O `Client ID` e o `Client Secret` não bastam sozinhos.

Depois de preencher as credenciais, o OpenJarvis precisa abrir o navegador para você autorizar sua conta Google.

Após a autorização, o OpenJarvis recebe tokens, como:

- `access_token`
- `refresh_token`

Esses tokens são salvos localmente, geralmente em:

```text
~/.openjarvis/connectors/
```

No Windows, isso pode aparecer como:

```text
C:\Users\denis\.openjarvis\connectors
```

---

## 10. Se ficar preso em Synchronizing

Se o conector ficar preso em `Synchronizing...`, verifique:

1. O Jarvis Server está rodando?
2. Você iniciou o servidor dentro da pasta correta?
3. A API do Google Drive/Gmail/Calendar foi ativada no Google Cloud?
4. Seu Gmail está cadastrado como usuário de teste?
5. A credencial criada é do tipo **Desktop App**?
6. O navegador abriu para autorizar o Google?
7. O token foi salvo em `.openjarvis/connectors`?

Também pode ajudar fechar o app, parar o servidor e iniciar novamente:

```powershell
cd "C:\Users\denis\OpenJarvis"
uv run jarvis serve 8000
```

---

## 11. Backend status e fala/voz

Na tela de status do backend, o OpenJarvis pode mostrar uma mensagem parecida com:

```text
Backend status
Requires Whisper, Deepgram, or another speech backend
```

Isso significa que a parte de fala/transcrição precisa de um backend de áudio. Pode ser:

- Whisper
- Deepgram
- outro backend compatível

No meu caso, o Whisper funciona na minha máquina, mas ele não veio instalado por padrão junto com o OpenJarvis. Ou seja: se eu quiser usar recursos de voz, preciso instalar e configurar o Whisper separadamente.

Importante para explicar no vídeo:

- O OpenJarvis pode abrir e funcionar mesmo sem o backend de voz.
- A mensagem não significa necessariamente que o Jarvis Server está quebrado.
- Ela indica que falta configurar o componente de áudio/fala.
- Para quem não vai usar voz no início, dá para deixar essa parte para depois.

Resumo:

```text
Jarvis Server rodando = backend principal funcionando
Whisper/Deepgram ausente = recurso de fala ainda não configurado
```

---

## 12. Presets do OpenJarvis

O OpenJarvis tem presets prontos para alguns fluxos.

Exemplo:

```bash
jarvis init --preset morning-digest-mac
```

O preset `morning-digest` cria um resumo matinal usando fontes como e-mail, calendário, notícias e outros dados.

Depois de conectar os serviços:

```bash
jarvis digest --fresh
```

---

## 13. Skills no OpenJarvis

Skills são capacidades extras que ensinam os agentes a usar ferramentas e executar tarefas específicas.

Exemplos:

```bash
jarvis skill install hermes:arxiv
jarvis skill sync hermes --category research
```

Também é possível usar uma skill diretamente com um agente:

```bash
jarvis ask "Use the code-explainer skill to explain this Python code: for i in range(5): print(i*2)"
```

O OpenJarvis pode importar skills de fontes como:

- Hermes Agent
- OpenClaw
- Repositórios do GitHub

---

## 14. Comandos avançados de skills

A documentação também mostra comandos para otimização e benchmark:

```bash
jarvis optimize skills --policy dspy
```

```bash
jarvis bench skills --max-samples 5 --seeds 42
```

Esses comandos são mais avançados e podem ficar para testes posteriores.

---

## 15. Agentes internos do OpenJarvis

O OpenJarvis vem com agentes internos para diferentes tipos de tarefa:

| Agente | Tipo | Função |
|---|---|---|
| `morning_digest` | Agendado | Resumo diário com e-mail, calendário, notícias e áudio |
| `deep_research` | Sob demanda | Pesquisa aprofundada com citações |
| `monitor_operative` | Contínuo | Monitoramento com memória e recuperação |
| `orchestrator` | Sob demanda | Raciocínio multi-turno com seleção automática de ferramentas |
| `native_react` | Sob demanda | Agente no estilo ReAct |
| `operative` | Contínuo | Agente autônomo persistente |
| `native_openhands` | Sob demanda | Agente de código que gera e executa Python |
| `simple` | Sob demanda | Chat simples, sem ferramentas |

Nem todo agente serve para tudo. Alguns são para tarefas rápidas, outros para automação, pesquisa ou execução de código.

---

## 16. Sugestão de roteiro do vídeo

### Abertura

No vídeo anterior, instalamos o OpenJarvis no Windows. Hoje vamos configurar a parte que ficou pendente: iniciar corretamente o Jarvis Server, conectar os serviços Google e entender presets, agentes e skills.

### Parte 1 — Explicar o problema

Mostrar que o app pode abrir sem o servidor estar rodando corretamente.

Explicar:

- Porta `8000` é backend/API.
- Interface visual pode estar em outra porta.
- O comando precisa ser executado dentro da pasta correta.

### Parte 2 — Descobrir a pasta correta

Mostrar o comando:

```powershell
Get-ChildItem -Path C:\Users\denis -Filter pyproject.toml -Recurse -ErrorAction SilentlyContinue
```

Explicar que a pasta correta é:

```text
C:\Users\denis\OpenJarvis
```

### Parte 3 — Criar atalho do servidor

Criar o arquivo:

```text
iniciar_jarvis_server.bat
```

Com o conteúdo:

```bat
@echo off
cd /d "C:\Users\denis\OpenJarvis"
uv run jarvis serve 8000
pause
```

### Parte 4 — Google OAuth

Mostrar no Google Cloud:

- Ativar APIs.
- Configurar tela de consentimento.
- Adicionar usuário de teste.
- Criar OAuth Desktop App.
- Copiar Client ID e Client Secret.
- Autorizar a conta Google.

### Parte 5 — Testar conector

Testar conexão com Drive/Gmail/Calendar.

Explicar que o token deve ser salvo em:

```text
C:\Users\denis\.openjarvis\connectors
```

### Parte 6 — Backend status e voz

Mostrar a mensagem:

```text
Requires Whisper, Deepgram, or another speech backend
```

Explicar que o Whisper funciona na minha máquina, mas não veio instalado por padrão. Então, para recursos de fala, será necessário instalar/configurar o Whisper ou usar outro backend, como Deepgram.

### Parte 7 — Skills e agentes

Mostrar rapidamente:

```bash
jarvis skill install hermes:arxiv
```

E explicar a diferença entre agentes como `simple`, `orchestrator`, `deep_research` e `native_openhands`.

---

## 17. Fechamento

Neste vídeo, configuramos o OpenJarvis para deixar de ser apenas uma instalação e começar a funcionar como um agente conectado a ferramentas reais.

No próximo vídeo, podemos testar um fluxo prático, como:

- Ler arquivos do Google Drive.
- Consultar e-mails.
- Criar eventos no Calendar.
- Gerar um resumo matinal.
- Usar skills em tarefas reais.
- Comparar modelos como MiniMax, Ollama ou outros provedores.
