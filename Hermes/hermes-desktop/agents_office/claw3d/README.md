# Como instalar o Claw3D com Hermes

## 1. Clonar o repositório

```bash
git clone "https://github.com/iamlukethedev/Claw3D.git" "claw3d"
```

## 2. Entrar na pasta

```bash
cd "claw3d"
```

## 3. Instalar dependências

```bash
npm install
```

## 4. Criar o arquivo de ambiente

```bash
cp ".env.example" ".env"
```

## 5. Confirmar que o Hermes está rodando

No ambiente atual, o Hermes Agent Office aparece em:

```text
http://localhost:3100/office
```

O Claw3D usa o Hermes como runtime dos agentes.

## 6. Rodar o Hermes Adapter

Abra um terminal e rode:

```bash
cd "claw3d"
npm run hermes-adapter
```

O adapter cria a ponte WebSocket entre Claw3D e Hermes.

Endereço esperado:

```text
ws://localhost:18789
```

## 7. Rodar o Claw3D Studio

Abra outro terminal e rode:

```bash
cd "claw3d"
npm run dev
```

Depois abra no navegador:

```text
http://localhost:3000
```

## 8. Conectar no Claw3D

Na tela de conexão do Claw3D, usar:

```text
Backend: Hermes backend
Gateway URL: ws://localhost:18789
```

## 9. Entender a arquitetura

```text
Hermes = motor dos agentes
Hermes Adapter = ponte entre Hermes e Claw3D
Claw3D Studio = interface visual em 3D
Office = empresa de agentes
Jane = agente de escrita
Turing = agente de codificação
```

## 10. Fluxo recomendado

```text
1. Iniciar Hermes
2. Iniciar Hermes Adapter
3. Iniciar Claw3D Studio
4. Conectar em ws://localhost:18789
5. Criar a empresa Office
6. Criar ou revisar os agentes Jane e Turing
7. Testar chat, perfis e Kanban
```

## 11. Observações

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
