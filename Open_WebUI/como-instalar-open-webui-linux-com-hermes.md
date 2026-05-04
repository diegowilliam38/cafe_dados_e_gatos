# Como instalar o Open WebUI no Linux sem Docker e conectar ao Hermes Agent

Este guia mostra como instalar o Open WebUI diretamente no Linux, sem Docker, e configurar uma conexão com o Hermes Agent já instalado e com o servidor de API habilitado.

Este documento parte do pressuposto de que o Hermes já está funcionando em:

```text
http://127.0.0.1:8642
```

E que o Hermes possui uma chave configurada em:

```env
API_SERVER_KEY=sua-chave-forte
```

---

## 1. Requisitos

Sistema recomendado:

- Ubuntu 22.04, Ubuntu 24.04, Debian ou distribuição equivalente.
- Terminal com acesso a `bash`.
- Usuário com permissão de `sudo`.
- Conexão com a internet.
- Hermes Agent já instalado e rodando com API local habilitada.

Também é possível usar o Open WebUI com Ollama, OpenAI e outros provedores compatíveis. Este guia foca na conexão com o Hermes Agent.

---

## 2. Atualizar o sistema

```bash
sudo apt update
sudo apt upgrade -y
```

Instale pacotes básicos:

```bash
sudo apt install -y curl git ca-certificates build-essential
```

---

## 3. Instalar o uv

O método recomendado aqui usa `uv`, porque ele permite rodar o Open WebUI com Python 3.11 sem mexer diretamente no Python do sistema.

Instale o `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Recarregue o shell:

```bash
source ~/.bashrc
```

Se estiver usando Zsh:

```bash
source ~/.zshrc
```

Verifique:

```bash
uv --version
uvx --version
```

---

## 4. Rodar o Open WebUI manualmente

Crie uma pasta para os dados:

```bash
mkdir -p ~/.open-webui
```

Inicie o Open WebUI:

```bash
DATA_DIR=~/.open-webui uvx --python 3.11 open-webui@latest serve
```

Abra no navegador:

```text
http://localhost:8080
```

Na primeira abertura, crie o primeiro usuário. O primeiro usuário criado vira administrador da instância.

---

## 5. Rodar em outra porta, se necessário

Por padrão, o Open WebUI roda na porta `8080`.

Para usar outra porta:

```bash
DATA_DIR=~/.open-webui PORT=3000 uvx --python 3.11 open-webui@latest serve
```

Acesse:

```text
http://localhost:3000
```

---

## 6. Verificar se o Hermes está acessível

Antes de configurar o Open WebUI, confirme se o Hermes está rodando.

Teste a saúde do servidor:

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

Troque `SUA_CHAVE_FORTE` pela chave configurada no Hermes em `API_SERVER_KEY`.

A resposta deve listar o modelo do Hermes, normalmente como:

```text
hermes-agent
```

---

## 7. Conectar o Open WebUI ao Hermes Agent

Com o Open WebUI aberto no navegador:

```text
http://localhost:8080
```

Entre com o usuário administrador.

Depois siga o caminho:

```text
Admin Settings -> Connections
```

Na área de conexões compatíveis com OpenAI, adicione uma nova conexão.

Use estes dados:

```text
URL: http://localhost:8642/v1
API Key: SUA_CHAVE_FORTE
```

Onde `SUA_CHAVE_FORTE` é o mesmo valor configurado no Hermes em:

```env
API_SERVER_KEY=SUA_CHAVE_FORTE
```

Salve a conexão.

Depois teste se o modelo aparece na lista de modelos.

Modelo esperado:

```text
hermes-agent
```

---

## 8. Criar serviço para o Open WebUI iniciar com o Linux

Descubra o caminho do `uvx`:

```bash
which uvx
```

Exemplo comum:

```text
/home/usuario/.local/bin/uvx
```

Crie a pasta de serviços do usuário:

```bash
mkdir -p ~/.config/systemd/user
```

Crie o serviço:

```bash
nano ~/.config/systemd/user/open-webui.service
```

Cole o conteúdo abaixo:

```ini
[Unit]
Description=Open WebUI sem Docker
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
Environment=DATA_DIR=%h/.open-webui
Environment=PORT=8080
Environment=PATH=%h/.local/bin:/usr/local/bin:/usr/bin:/bin
ExecStart=%h/.local/bin/uvx --python 3.11 open-webui@latest serve
Restart=always
RestartSec=5
WorkingDirectory=%h

[Install]
WantedBy=default.target
```

Se o comando `which uvx` retornou outro caminho, ajuste a linha `ExecStart`.

Exemplo:

```ini
ExecStart=/usr/local/bin/uvx --python 3.11 open-webui@latest serve
```

Salve e saia.

No `nano`:

```text
Ctrl+O
Enter
Ctrl+X
```

---

## 9. Ativar o serviço do Open WebUI

Recarregue o systemd de usuário:

```bash
systemctl --user daemon-reload
```

Ative a inicialização automática:

```bash
systemctl --user enable open-webui
```

Inicie agora:

```bash
systemctl --user start open-webui
```

Verifique o status:

```bash
systemctl --user status open-webui
```

Ver logs em tempo real:

```bash
journalctl --user -u open-webui -f
```

Acesse:

```text
http://localhost:8080
```

---

## 10. Permitir inicialização mesmo antes de abrir o terminal

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

## 11. Reiniciar e testar tudo

Reinicie o Linux:

```bash
sudo reboot
```

Depois de voltar, confira o Open WebUI:

```bash
systemctl --user status open-webui
```

Confira o Hermes:

```bash
systemctl --user status hermes-gateway
```

Teste as URLs:

```bash
curl http://localhost:8080
curl http://127.0.0.1:8642/health
```

Abra no navegador:

```text
http://localhost:8080
```

Verifique se o modelo `hermes-agent` aparece e responda uma mensagem de teste.

---

## 12. Parar, reiniciar ou desativar o Open WebUI

Parar:

```bash
systemctl --user stop open-webui
```

Reiniciar:

```bash
systemctl --user restart open-webui
```

Desativar inicialização automática:

```bash
systemctl --user disable open-webui
```

Remover o serviço:

```bash
systemctl --user stop open-webui
systemctl --user disable open-webui
rm ~/.config/systemd/user/open-webui.service
systemctl --user daemon-reload
```

---

## 13. Atualizar o Open WebUI

Pare o serviço:

```bash
systemctl --user stop open-webui
```

Limpe o cache opcionalmente:

```bash
uv cache clean
```

Rode novamente manualmente para testar a versão mais recente:

```bash
DATA_DIR=~/.open-webui uvx --python 3.11 open-webui@latest serve
```

Se tudo funcionar, pare com `Ctrl+C` e reinicie o serviço:

```bash
systemctl --user start open-webui
```

---

## 14. Remover dados locais do Open WebUI

Para apagar os dados locais:

```bash
rm -rf ~/.open-webui
```

Atenção: esse comando apaga usuários, chats, configurações, conexões e dados locais do Open WebUI.

---

## 15. Checklist rápido

```bash
uv --version
uvx --version
DATA_DIR=~/.open-webui uvx --python 3.11 open-webui@latest serve
curl http://localhost:8080
curl http://127.0.0.1:8642/health
curl http://127.0.0.1:8642/v1/models -H "Authorization: Bearer SUA_CHAVE_FORTE"
systemctl --user status open-webui
systemctl --user status hermes-gateway
```

Instalação concluída quando:

- O Open WebUI abre em `http://localhost:8080`.
- O Hermes responde em `http://127.0.0.1:8642/health`.
- A conexão OpenAI-compatible do Open WebUI aponta para `http://localhost:8642/v1`.
- O modelo `hermes-agent` aparece no Open WebUI.
- O Open WebUI e o Hermes sobem automaticamente com o Linux.
