# Como instalar o Browser Harness e usar com Hermes + Brave visível

## Objetivo

Instalar o Browser Harness em uma VM Linux, abrir o Brave com CDP na porta `9222`, testar o controle visual do navegador e depois chamar esse fluxo pelo Hermes.

## Fluxo geral

```text
Hermes → Terminal → Browser Harness → Brave visível via CDP
```

## Ordem do processo

```text
1. Instalar ou confirmar o Hermes
2. Instalar dependências básicas
3. Instalar ou confirmar o uv
4. Instalar o Browser Harness
5. Abrir o Brave com CDP na porta 9222
6. Testar o Browser Harness controlando o Brave visível
7. Criar comando fixo para subir Brave + Hermes
8. Abrir o Hermes TUI
9. Pedir para o Hermes usar o Browser Harness
```

---

## 1. Confirmar se o Hermes já está instalado

```bash
which hermes || true
hermes --version || true
```

Se o Hermes não existir, instale:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Depois feche e abra o terminal.

Teste novamente:

```bash
which hermes
hermes --version
```

---

## 2. Instalar dependências básicas

```bash
sudo apt update
sudo apt install -y git curl python3 python3-venv python3-pip
```

---

## 3. Confirmar se o uv já está instalado

```bash
uv --version || true
```

Se o `uv` não existir, instale:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"
uv --version
```

---

## 4. Instalar o Browser Harness

```bash
mkdir -p ~/Developer
cd ~/Developer
git clone https://github.com/browser-use/browser-harness
cd ~/Developer/browser-harness
uv tool install -e .
```

---

## 5. Testar se o Browser Harness foi instalado

```bash
command -v browser-harness
browser-harness --doctor
```

Resultado esperado:

```text
Installed executable: browser-harness
/home/usuario/.local/bin/browser-harness
```

Antes do navegador estar aberto com CDP, o `browser-harness --doctor` pode mostrar algo assim:

```text
[FAIL] chrome running
[FAIL] daemon alive
[FAIL] active browser connections - 0
```

Isso é normal nessa etapa.

---

## 6. Fechar Brave antigo

```bash
pkill -f brave || true
```

---

## 7. Abrir o Brave visível com CDP

```bash
brave-browser \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/.hermes/brave-debug" \
  --no-first-run \
  --no-default-browser-check &
```

Nesta etapa, o Brave deve abrir visivelmente na tela da VM.

No terminal, deve aparecer algo parecido com:

```text
DevTools listening on ws://127.0.0.1:9222/devtools/browser/...
```

---

## 8. Confirmar que a porta 9222 está funcionando

```bash
curl http://127.0.0.1:9222/json/version
```

Resultado esperado:

```json
{
  "Browser": "Chrome/...",
  "Protocol-Version": "1.3",
  "User-Agent": "...",
  "webSocketDebuggerUrl": "ws://127.0.0.1:9222/devtools/browser/..."
}
```

Se aparecer `Browser`, `Protocol-Version` ou `webSocketDebuggerUrl`, o Brave está pronto para ser controlado.

---

## 9. Rodar novamente o doctor

```bash
browser-harness --doctor
```

Agora o item `chrome running` deve aparecer como `[OK]`.

Exemplo:

```text
[OK] chrome running
```

Ainda podem aparecer falhas como:

```text
[FAIL] daemon alive
[FAIL] active browser connections - 0
```

O teste decisivo é o teste real com `BU_CDP_URL`.

---

## 10. Testar Browser Harness controlando o Brave visível

```bash
export BU_CDP_URL=http://127.0.0.1:9222

browser-harness -c '
new_tab("https://example.com")
wait_for_load()
print(page_info())
'
```

Resultado esperado no terminal:

```text
{'url': 'https://example.com/', 'title': 'Example Domain', ...}
```

Resultado esperado no Brave:

```text
Uma nova aba deve abrir com https://example.com
```

Aqui estamos provando:

```text
Browser Harness → controla Brave visível
```

---

## 11. Teste visual com Wikipedia

```bash
export BU_CDP_URL=http://127.0.0.1:9222

browser-harness -c '
new_tab("https://www.wikipedia.org")
wait_for_load()
print(page_info())
'
```

Resultado esperado no terminal:

```text
{'url': 'https://www.wikipedia.org/', 'title': 'Wikipedia', ...}
```

Resultado esperado no Brave:

```text
Uma nova aba deve abrir com https://www.wikipedia.org
```

---

## 12. Teste visual com qualquer site

Troque a URL abaixo pelo site desejado:

```bash
export BU_CDP_URL=http://127.0.0.1:9222

browser-harness -c '
new_tab("https://example.com")
wait_for_load()
print(page_info())
'
```

Resultado esperado:

```text
O Brave deve abrir o site em uma nova aba.
```

---

# Como deixar o fluxo fixo

## 13. Criar comando único para subir Brave + Hermes

Este comando faz:

```text
1. Fecha Brave antigo
2. Abre Brave com CDP na porta 9222
3. Aguarda a porta 9222 responder
4. Exporta BU_CDP_URL
5. Abre o Hermes
```

Criar a pasta de comandos locais:

```bash
mkdir -p ~/bin
```

Criar o script:

```bash
nano ~/bin/hermes-browser
```

Cole dentro:

```bash
#!/usr/bin/env bash

echo "Iniciando Brave com CDP na porta 9222..."

pkill -f brave || true

brave-browser \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/.hermes/brave-debug" \
  --no-first-run \
  --no-default-browser-check &

echo "Aguardando Brave/CDP responder..."

for i in {1..20}; do
  if curl -s http://127.0.0.1:9222/json/version >/dev/null; then
    echo "Brave CDP ativo em http://127.0.0.1:9222"
    break
  fi
  sleep 1
done

export BU_CDP_URL=http://127.0.0.1:9222

echo "BU_CDP_URL=$BU_CDP_URL"
echo "Abrindo Hermes..."

hermes
```

Salvar no nano:

```text
CTRL + O
ENTER
CTRL + X
```

Dar permissão de execução:

```bash
chmod +x ~/bin/hermes-browser
```

Garantir que `~/bin` está no PATH:

```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Testar:

```bash
hermes-browser
```

Resultado esperado:

```text
O Brave abre com CDP na porta 9222.
O script confirma que a porta está ativa.
O Hermes abre no terminal.
```

---

## 14. Usar Browser Harness dentro do Hermes

Com o Hermes aberto pelo comando:

```bash
hermes-browser
```

Dentro do Hermes TUI, envie:

```text
Use o terminal para executar o Browser Harness no Brave já aberto.

Execute:

browser-harness -c '
new_tab("https://example.com")
wait_for_load()
print(page_info())
'
```

Como o Hermes foi aberto pelo script, ele deve herdar a variável:

```bash
BU_CDP_URL=http://127.0.0.1:9222
```

---

## 15. Teste dentro do Hermes

Dentro do Hermes TUI, envie:

```text
Use o terminal para controlar o Brave já aberto com Browser Harness.

Execute este comando:

browser-harness -c '
new_tab("https://example.com")
wait_for_load()
print(page_info())
'

Depois me diga qual URL e título retornaram.
```

Resultado esperado:

```text
O Hermes deve executar o comando pelo terminal.
O Browser Harness deve abrir uma nova aba no Brave.
O terminal deve retornar a URL e o título da página.
```

---

# Como deixar o Brave subir junto com o Ubuntu

## 16. Criar script separado só para o Brave com CDP

Este script abre apenas o Brave com CDP.

Criar o arquivo:

```bash
nano ~/bin/start-brave-cdp
```

Cole dentro:

```bash
#!/usr/bin/env bash

pkill -f brave || true

brave-browser \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/.hermes/brave-debug" \
  --no-first-run \
  --no-default-browser-check &
```

Salvar no nano:

```text
CTRL + O
ENTER
CTRL + X
```

Dar permissão de execução:

```bash
chmod +x ~/bin/start-brave-cdp
```

Testar:

```bash
start-brave-cdp
```

Confirmar se a porta respondeu:

```bash
curl http://127.0.0.1:9222/json/version
```

---

## 17. Adicionar o Brave CDP na inicialização do Ubuntu

Abrir o gerenciador de aplicativos de sessão:

```bash
gnome-session-properties
```

Clique em:

```text
Adicionar
```

Preencha assim:

```text
Nome:
Brave CDP para Browser Harness
```

```text
Comando:
/home/SEU_USUARIO/bin/start-brave-cdp
```

Troque `SEU_USUARIO` pelo nome do usuário Linux.

Exemplo:

```text
/home/usuario/bin/start-brave-cdp
```

Comentário:

```text
Abre Brave com CDP na porta 9222 para Browser Harness
```

Depois salve.

Quando a VM iniciar e o usuário entrar no Ubuntu, o Brave deve abrir automaticamente com CDP na porta `9222`.

---

# Comandos rápidos

## 18. Comando rápido para iniciar Brave + Hermes

```bash
hermes-browser
```

---

## 19. Comando rápido para iniciar apenas o Brave com CDP

```bash
start-brave-cdp
```

---

## 20. Comando rápido para verificar CDP

```bash
curl http://127.0.0.1:9222/json/version
```

---

## 21. Comando rápido para testar Browser Harness

```bash
export BU_CDP_URL=http://127.0.0.1:9222

browser-harness -c '
new_tab("https://example.com")
wait_for_load()
print(page_info())
'
```

---

# Observação importante

O Browser Harness precisa de um navegador aberto com CDP para controlar o Brave visível.

Neste tutorial, o Brave é iniciado com:

```bash
--remote-debugging-port=9222
```

E o Browser Harness recebe a conexão por:

```bash
export BU_CDP_URL=http://127.0.0.1:9222
```

Sem isso, o Browser Harness pode instalar corretamente, mas não controlar o navegador visível.

---

# Resultado final esperado

```text
✅ Hermes instalado ou confirmado
✅ Browser Harness instalado
✅ Brave aberto com CDP na porta 9222
✅ Porta 9222 respondendo via curl
✅ Browser Harness abrindo páginas no Brave visível
✅ Comando hermes-browser criado
✅ Brave CDP podendo subir no login do Ubuntu
✅ Hermes chamando o Browser Harness pelo terminal
```
