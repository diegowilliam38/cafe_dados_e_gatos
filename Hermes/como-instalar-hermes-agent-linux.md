# Como instalar o Hermes Agent no Linux sem Docker

Este guia mostra como instalar o Hermes Agent diretamente no Linux, habilitar o servidor de API local e configurar o Hermes para iniciar automaticamente quando o Linux ligar.

O objetivo deste documento é deixar o Hermes pronto para ser usado por outras interfaces locais, como o Open WebUI, sem explicar a configuração do Open WebUI aqui.

> Observação: o Hermes Agent evolui rapidamente. Antes de usar em produção, confira a documentação oficial do projeto e revise os comandos conforme a versão atual.

---

## 1. Requisitos

Sistema recomendado:

- Ubuntu 22.04, Ubuntu 24.04, Debian ou distribuição equivalente.
- Terminal com acesso a `bash`.
- Usuário com permissão de `sudo`.
- Conexão com a internet.
- Um provedor de modelo compatível com o Hermes.

Exemplos de provedores possíveis:

- Nous Portal.
- OpenRouter.
- OpenAI.
- Anthropic.
- MiniMax.
- Ollama.
- NVIDIA NIM.
- Outro endpoint compatível com a API da OpenAI.

O Hermes Agent precisa de um modelo com janela de contexto grande. Para fluxos multi-etapas, recomenda-se usar modelos com pelo menos 64K tokens de contexto.

---

## 2. Atualizar o sistema

```bash
sudo apt update
sudo apt upgrade -y
```

Instale pacotes básicos:

```bash
sudo apt install -y curl git build-essential ca-certificates openssl
```

---

## 3. Instalar o Hermes Agent

Execute o instalador oficial:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Recarregue o shell:

```bash
source ~/.bashrc
```

Se estiver usando Zsh:

```bash
source ~/.zshrc
```

Verifique se o comando ficou disponível:

```bash
hermes --version
```

Se o comando não for encontrado, feche e abra o terminal novamente.

---

## 4. Configurar o modelo do Hermes

Rode o assistente de configuração:

```bash
hermes model
```

Escolha o provedor desejado e informe os dados pedidos pelo assistente.

Exemplos comuns:

- Provedor OpenAI-compatible: URL base, nome do modelo e chave de API.
- Ollama: URL local do Ollama e nome do modelo.
- NVIDIA NIM: URL base, chave de API e nome do modelo.
- OpenRouter: chave `OPENROUTER_API_KEY` e nome do modelo.

Depois da configuração, teste o Hermes no terminal:

```bash
hermes
```

Envie uma mensagem simples:

```text
Olá, confirme que o Hermes está funcionando.
```

Para sair, use `Ctrl+C` ou o comando de saída indicado no terminal.

---

## 5. Verificar diagnóstico do Hermes

Rode:

```bash
hermes doctor
```

Se houver erro de modelo, autenticação ou configuração, rode novamente:

```bash
hermes model
```

Ou:

```bash
hermes setup
```

Comandos úteis:

```bash
hermes sessions list
hermes --continue
hermes gateway status
```

---

## 6. Habilitar o servidor de API do Hermes

Para que outra interface local consiga enxergar o Hermes, o servidor de API precisa estar habilitado.

Abra o arquivo de ambiente do Hermes:

```bash
nano ~/.hermes/.env
```

Adicione ou ajuste estas linhas:

```env
API_SERVER_ENABLED=true
API_SERVER_KEY=troque-esta-chave-por-uma-chave-forte
API_SERVER_HOST=127.0.0.1
API_SERVER_PORT=8642
```

Gere uma chave forte:

```bash
openssl rand -hex 32
```

Copie o resultado e use em `API_SERVER_KEY`.

Exemplo:

```env
API_SERVER_ENABLED=true
API_SERVER_KEY=cole_a_chave_gerada_aqui
API_SERVER_HOST=127.0.0.1
API_SERVER_PORT=8642
```

Salve o arquivo.

No `nano`:

```text
Ctrl+O
Enter
Ctrl+X
```

> Segurança: mantenha `API_SERVER_HOST=127.0.0.1` para uso local. Isso evita expor o Hermes diretamente na rede.

---

## 7. Iniciar o gateway manualmente

Rode:

```bash
hermes gateway
```

Se estiver funcionando, o terminal deve indicar que o servidor está ativo em algo semelhante a:

```text
http://127.0.0.1:8642
```

Esse terminal precisa continuar aberto enquanto o gateway estiver sendo usado.

---

## 8. Testar o servidor de API

Em outro terminal, teste a saúde do servidor:

```bash
curl http://127.0.0.1:8642/health
```

Resposta esperada:

```json
{"status":"ok"}
```

Teste a listagem de modelos:

```bash
curl http://127.0.0.1:8642/v1/models \
  -H "Authorization: Bearer SUA_CHAVE_FORTE"
```

Troque `SUA_CHAVE_FORTE` pelo valor configurado em `API_SERVER_KEY`.

A resposta deve listar o modelo exposto pelo Hermes, normalmente como:

```text
hermes-agent
```

---

## 9. Descobrir o caminho do comando hermes

Antes de criar o serviço automático, descubra onde o Hermes foi instalado:

```bash
which hermes
```

Exemplos possíveis:

```text
/home/usuario/.local/bin/hermes
```

ou:

```text
/usr/local/bin/hermes
```

Guarde esse caminho. Ele será usado no `ExecStart` do serviço.

---

## 10. Criar serviço para iniciar com o Linux

Crie a pasta de serviços do usuário:

```bash
mkdir -p ~/.config/systemd/user
```

Crie o arquivo do serviço:

```bash
nano ~/.config/systemd/user/hermes-gateway.service
```

Cole o conteúdo abaixo.

Se o comando `which hermes` retornou `/home/usuario/.local/bin/hermes`, pode manter o exemplo com `%h/.local/bin/hermes`.

```ini
[Unit]
Description=Hermes Agent Gateway
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=%h/.local/bin/hermes gateway
Restart=always
RestartSec=5
WorkingDirectory=%h
Environment=PATH=%h/.local/bin:/usr/local/bin:/usr/bin:/bin

[Install]
WantedBy=default.target
```

Se o Hermes estiver em outro caminho, troque esta linha:

```ini
ExecStart=%h/.local/bin/hermes gateway
```

por algo como:

```ini
ExecStart=/usr/local/bin/hermes gateway
```

Salve e saia.

No `nano`:

```text
Ctrl+O
Enter
Ctrl+X
```

---

## 11. Ativar o serviço

Recarregue o systemd do usuário:

```bash
systemctl --user daemon-reload
```

Ative o serviço para iniciar automaticamente:

```bash
systemctl --user enable hermes-gateway
```

Inicie agora:

```bash
systemctl --user start hermes-gateway
```

Verifique o status:

```bash
systemctl --user status hermes-gateway
```

Ver logs em tempo real:

```bash
journalctl --user -u hermes-gateway -f
```

---

## 12. Permitir inicialização mesmo antes de abrir o terminal

Em alguns sistemas, serviços de usuário só iniciam depois do login gráfico. Para permitir que o serviço do usuário suba automaticamente após o boot, rode:

```bash
sudo loginctl enable-linger "$USER"
```

Verifique:

```bash
loginctl show-user "$USER" | grep Linger
```

Resposta esperada:

```text
Linger=yes
```

---

## 13. Testar após reiniciar o Linux

Reinicie o computador:

```bash
sudo reboot
```

Depois de voltar, verifique se o serviço subiu:

```bash
systemctl --user status hermes-gateway
```

Teste a API:

```bash
curl http://127.0.0.1:8642/health
```

Teste os modelos:

```bash
curl http://127.0.0.1:8642/v1/models \
  -H "Authorization: Bearer SUA_CHAVE_FORTE"
```

Se esses testes funcionarem, o Hermes está instalado, com API local habilitada e iniciando automaticamente com o Linux.

---

## 14. Parar, reiniciar ou desativar o serviço

Parar:

```bash
systemctl --user stop hermes-gateway
```

Reiniciar:

```bash
systemctl --user restart hermes-gateway
```

Desativar inicialização automática:

```bash
systemctl --user disable hermes-gateway
```

Remover o serviço:

```bash
systemctl --user stop hermes-gateway
systemctl --user disable hermes-gateway
rm ~/.config/systemd/user/hermes-gateway.service
systemctl --user daemon-reload
```

---

## 15. Atualizar o Hermes Agent

Como o Hermes Agent muda rapidamente, confirme no repositório oficial qual é o método de atualização recomendado para a versão atual.

Antes de atualizar, rode:

```bash
hermes doctor
```

Depois consulte a documentação oficial do projeto.

---

## 16. Remover dados locais do Hermes

Verifique onde o comando está instalado:

```bash
which hermes
```

Verifique a pasta local:

```bash
ls -la ~/.hermes
```

Para apagar configurações e dados locais do Hermes:

```bash
rm -rf ~/.hermes
```

Atenção: esse comando apaga configurações, sessões, memória e dados locais do Hermes.

---

## 17. Checklist rápido

```bash
hermes --version
hermes doctor
hermes model
hermes
hermes gateway
curl http://127.0.0.1:8642/health
curl http://127.0.0.1:8642/v1/models -H "Authorization: Bearer SUA_CHAVE_FORTE"
systemctl --user status hermes-gateway
```

Instalação concluída quando:

- `hermes --version` funciona.
- `hermes doctor` não mostra erros críticos.
- `hermes` responde no terminal.
- `curl http://127.0.0.1:8642/health` retorna `{"status":"ok"}`.
- `systemctl --user status hermes-gateway` mostra o serviço ativo.
