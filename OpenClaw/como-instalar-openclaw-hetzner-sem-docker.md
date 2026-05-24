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
- Mostra como obter o caminho HTTPS de acesso com Tailscale Serve.
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

## 9. Conferir se o Gateway está respondendo localmente

```bash
openclaw gateway status
```

Se o Gateway estiver usando a porta `18789`, o serviço local estará neste endereço:

```text
http://127.0.0.1:18789
```

## 10. Gerar o acesso HTTPS com Tailscale Serve

Na VPS, rode:

```bash
tailscale serve --https=18789 http://127.0.0.1:18789
```

O Tailscale vai mostrar uma saída parecida com esta:

```text
Available within your tailnet:

https://NOME-DA-MAQUINA.NOME-DA-TAILNET.ts.net:18789/
|-- proxy http://127.0.0.1:18789
```

Copie a URL `https` exibida no terminal e abra no navegador.

Exemplo de formato:

```text
https://NOME-DA-MAQUINA.NOME-DA-TAILNET.ts.net:18789/
```

## 11. Conferir o acesso HTTPS ativo

```bash
tailscale serve status
```

## 12. Remover o acesso HTTPS se precisar

Use apenas se quiser desligar o compartilhamento HTTPS criado pelo Tailscale Serve.

```bash
tailscale serve reset
```

## 13. Obter o caminho da interface pelo OpenClaw

Também é possível pedir para o OpenClaw mostrar o endereço da interface:

```bash
openclaw dashboard --no-open
```

Esse comando é útil em VPS, porque o servidor normalmente não tem navegador gráfico.

Se o OpenClaw mostrar uma URL com token, copie a URL completa exibida no terminal.

Se precisar ver o token separadamente:

```bash
openclaw config get gateway.auth.token
```

## 14. Conferir comandos disponíveis

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

## 15. Verificar status depois do onboard

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

## 16. Atualizar o OpenClaw

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

## 17. Ver a versão mais recente publicada

```bash
npm view openclaw version
```

## 18. Comandos principais

```bash
openclaw --version
openclaw --help
openclaw onboard
openclaw gateway status
tailscale serve --https=18789 http://127.0.0.1:18789
tailscale serve status
tailscale serve reset
openclaw dashboard --no-open
openclaw config get gateway.auth.token
openclaw configure --help
openclaw gateway --help
openclaw doctor
openclaw update
```

## Resultado esperado

Ao final, a VPS deve ter:

```text
OpenClaw instalado sem Docker.
CLI openclaw funcionando.
Onboarding executado.
Gateway respondendo localmente.
Acesso HTTPS gerado com Tailscale Serve.
Comandos básicos disponíveis no terminal.
```

## Observação importante

A interface e as opções do `openclaw onboard` podem mudar entre versões.

Por isso, este guia registra o fluxo real usado na instalação: instalar pelo script oficial, rodar `openclaw onboard`, expor o acesso com `tailscale serve --https=18789 http://127.0.0.1:18789` e seguir as opções que aparecem na tela.
