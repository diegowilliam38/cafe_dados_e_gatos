# Como instalar o Claw3D com Hermes

## 1. Limpar instalação anterior

Parar qualquer terminal que esteja rodando Claw3D ou Hermes Adapter:

```text
Ctrl + C
```

Remover instalação antiga:

```bash
cd ~
rm -rf "claw3d"
```

Limpar cache do npm:

```bash
npm cache clean --force
```

## 2. Clonar o repositório oficial

```bash
git clone "https://github.com/iamlukethedev/Claw3D.git" "claw3d"
```

## 3. Entrar na pasta

```bash
cd "claw3d"
```

## 4. Garantir instalação limpa

Remover dependências e lockfile antigos, caso existam:

```bash
rm -rf "node_modules" "package-lock.json"
```

## 5. Instalar dependências

```bash
npm install
```

## 6. Conferir versão do Next

```bash
npm list next
```

O esperado no repositório atual é algo próximo de:

```text
next@16.1.7
```

Se aparecer:

```text
next@9.3.3
```

a instalação ainda está pegando dependência antiga ou cache errado.

## 7. Criar o arquivo de ambiente

```bash
cp ".env.example" ".env"
```

## 8. Configurar o arquivo .env para Hermes

Abrir o arquivo:

```bash
nano ".env"
```

Confirmar ou adicionar estas variáveis:

```env
NEXT_PUBLIC_GATEWAY_URL=ws://localhost:18789
HERMES_API_URL=http://localhost:8642
HERMES_ADAPTER_PORT=18789
HERMES_MODEL=hermes
HERMES_AGENT_NAME=Hermes
```

Salvar:

```text
Ctrl + O
Enter
Ctrl + X
```

## 9. Não renomear next.config.ts

No repositório atual, o arquivo:

```text
next.config.ts
```

deve permanecer assim.

Não fazer:

```bash
mv "next.config.ts" "next.config.js"
```

Esse erro aconteceu quando o projeto instalou uma versão antiga do Next.

Com Next 16, o `next.config.ts` é compatível.

## 10. Confirmar que o Hermes está rodando

No ambiente atual, o Hermes Agent Office aparece em:

```text
http://localhost:3100/office
```

O Claw3D usa o Hermes como runtime dos agentes.

## 11. Rodar o Hermes Adapter

Abrir um terminal e rodar:

```bash
cd ~/claw3d
npm run hermes-adapter
```

Esse terminal deve ficar aberto.

O adapter cria a ponte WebSocket entre Claw3D e Hermes.

Endereço esperado:

```text
ws://localhost:18789
```

Se aparecer algo como:

```text
Port 18789 in use
```

provavelmente já existe outro adapter ou gateway rodando nessa porta.

## 12. Rodar o Claw3D Studio

Abrir outro terminal e rodar:

```bash
cd ~/claw3d
npm run dev
```

Depois abrir no navegador:

```text
http://localhost:3000
```

## 13. Conectar no Claw3D

Na tela de conexão do Claw3D, usar:

```text
Backend: Hermes backend
Gateway URL: ws://localhost:18789
```

## 14. Entender a arquitetura

```text
Hermes = motor dos agentes
Hermes Adapter = ponte entre Hermes e Claw3D
Claw3D Studio = interface visual em 3D
Office = empresa de agentes
Jane = agente de escrita
Turing = agente de codificação
```

## 15. Fluxo recomendado

```text
1. Iniciar Hermes
2. Iniciar Hermes Adapter
3. Iniciar Claw3D Studio
4. Conectar em ws://localhost:18789
5. Criar a empresa Office
6. Criar ou revisar os agentes Jane e Turing
7. Testar chat, perfis e Kanban
```

## 16. O que não fazer

Não rodar:

```bash
npm audit fix --force
```

Esse comando pode instalar versões novas demais e quebrar o projeto.

Não renomear:

```text
next.config.ts
```

Não tentar corrigir dependência antiga manualmente antes de verificar:

```bash
npm list next
```

## 17. Observações

O Claw3D não substitui o Hermes.

Ele funciona como uma camada visual para ver, organizar e interagir com agentes que rodam no runtime conectado.

O marketplace de skills pode ser explorado depois. Para o início, focar em:

```text
Company
Office
Profiles
Chat
Kanban
Jane
Turing
```
