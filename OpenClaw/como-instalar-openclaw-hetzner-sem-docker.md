# Como instalar o OpenClaw na Hetzner

Instalação do OpenClaw em uma VPS Linux Ubuntu da Hetzner, sem Docker, usando o instalador oficial do OpenClaw e o comando `openclaw onboard`.

## Base oficial usada

- Instalação Linux/macOS/WSL2: `https://docs.openclaw.ai/install`
- Onboarding CLI: `https://docs.openclaw.ai/start/wizard`
- Atualização: `https://docs.openclaw.ai/install/updating`
- Releases: `https://github.com/openclaw/openclaw/releases/latest`

## O que este guia faz

- Atualiza a VPS Ubuntu.
- Instala dependências básicas.
- Instala o OpenClaw pelo instalador oficial.
- Roda o `openclaw onboard`.
- Mostra como obter o caminho de acesso da interface web.
- Mostra os comandos básicos para verificar a instalação.

## O que este guia não faz

- Não usa Docker.
- Não clona o repositório manualmente.
- Não cria serviço `systemd` manual.
- Não força instalação de daemon.
- Não assume que existe tela `Advanced` no onboard.
- Não assume que o dashboard abre sempre na mesma porta.

## 1. Acessar a VPS

No computador local:

```bash
ssh "root@IP_DA_VPS"
```

## 2. Atualizar o Ubuntu

Na VPS:

```bash
apt update
apt upgrade -y
```

## 3. Instalar dependências básicas

```bash
apt install -y curl git ca-certificates nano unzip build-essential
```

## 4. Baixar o instalador oficial do OpenClaw

```bash
curl -fsSL "https://openclaw.ai/install.sh" -o "install-openclaw.sh"
```

## 5. Executar o instalador

```bash
bash "install-openclaw.sh"
```

## 6. Recarregar o terminal se o comando não aparecer

Se o comando `openclaw` não for encontrado depois da instalação:

```bash
source "$HOME/.bashrc"
```

Teste novamente:

```bash
openclaw --version
```

## 7. Conferir a instalação

```bash
openclaw --version
```

```bash
openclaw --help
```

## 8. Rodar o onboard

```bash
openclaw onboard
```

Siga as perguntas que aparecerem na tela.

No teste feito para este guia, não apareceu uma etapa obrigatória chamada `Advanced` e também não foi necessário instalar daemon manualmente.

## 9. Obter o caminho de acesso da interface web

Depois do onboard, use este comando para ver o endereço de acesso da interface:

```bash
openclaw dashboard --no-open
```

Esse comando é útil em VPS, porque o servidor normalmente não tem navegador gráfico.

Se o OpenClaw mostrar uma URL com token, copie a URL completa exibida no terminal.

Se precisar ver o token separadamente:

```bash
openclaw config get gateway.auth.token
```

## 10. Acessar pelo navegador

Se o OpenClaw mostrar uma URL pública em `https`, copie e cole essa URL no navegador.

Se ele mostrar apenas um endereço local, use o caminho indicado pelo próprio comando:

```bash
openclaw dashboard --no-open
```

## 11. Conferir comandos disponíveis

```bash
openclaw --help
```

Se quiser conferir comandos relacionados a configuração:

```bash
openclaw configure --help
```

Se quiser conferir comandos relacionados ao Gateway:

```bash
openclaw gateway --help
```

## 12. Verificar status depois do onboard

Use os comandos disponíveis no seu ambiente:

```bash
openclaw doctor
```

```bash
openclaw gateway status
```

Se algum comando não existir na sua versão, confira a lista atual:

```bash
openclaw --help
```

## 13. Atualizar o OpenClaw

```bash
openclaw update
```

Depois da atualização:

```bash
openclaw --version
openclaw doctor
```

Se algum comando de atualização não existir na sua versão:

```bash
openclaw --help
```

## 14. Ver a versão mais recente publicada

```bash
npm view openclaw version
```

## 15. Comandos principais

```bash
openclaw --version
openclaw --help
openclaw onboard
openclaw dashboard --no-open
openclaw config get gateway.auth.token
openclaw configure --help
openclaw gateway --help
openclaw doctor
openclaw gateway status
openclaw update
```

## Resultado esperado

Ao final, a VPS deve ter:

```text
OpenClaw instalado sem Docker.
CLI openclaw funcionando.
Onboarding executado.
Caminho de acesso da interface web disponível no terminal.
Comandos básicos disponíveis no terminal.
```

## Observação importante

A interface e as opções do `openclaw onboard` podem mudar entre versões.

Por isso, este guia registra o fluxo real usado na instalação: instalar pelo script oficial, rodar `openclaw onboard`, obter o caminho com `openclaw dashboard --no-open` e seguir as opções que aparecem na tela.
