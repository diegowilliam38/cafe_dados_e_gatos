# OpenHuman no Ubuntu 24.04 com Ollama Local

## Contexto do teste

Este guia documenta o fluxo real testado no Ubuntu 24.04.4 LTS.

Durante o teste, o OpenHuman funcionou melhor usando o pacote ".deb". O método via AppImage/script apresentou erros de bibliotecas, EGL, GLIBC, sandbox e renderização.

Também foi possível ativar o runtime local com Ollama, baixar modelos locais e deixar o OpenHuman reconhecendo o modelo local.

Ponto importante: mesmo com o runtime local funcionando, o "Agent Chat" ainda parece depender do backend da OpenHuman. Quando o budget da conta acaba, o chat mostra erro de "Insufficient budget".

Esse modelo gemma3:1b-it-qat foi o OpenHuman que sugeriu de acordo com a minha máquina, acredito que para cada máquina será sugerido o que mais se adequa.
---

## 1. Instalar dependências

```bash
sudo apt update
sudo apt install -y curl tar python3 ca-certificates libxdo3 libgtk-3-0 libwebkit2gtk-4.1-0 libayatana-appindicator3-1 libssl3
```

---

## 2. Baixar o pacote .deb

Acesse a página oficial de releases:

```text
https://github.com/tinyhumansai/openhuman/releases
```

Baixe o arquivo:

```text
OpenHuman_0.53.43_amd64.deb
```

---

## 3. Instalar o OpenHuman

Depois de baixar o arquivo:

```bash
cd ~/Downloads
sudo apt install ./OpenHuman_0.53.43_amd64.deb
```

---

## 4. Abrir o OpenHuman

```bash
/usr/bin/OpenHuman
```

ou procure no menu do Ubuntu por:

```text
OpenHuman
```

---

## 5. Criar conta e fazer login

Ao abrir o OpenHuman, faça login com uma das opções disponíveis, como Google ou GitHub.

Durante o login, atenção às permissões solicitadas.

Se aparecer permissão de Gmail com acesso para ler, escrever, enviar e excluir e-mails, avalie com cuidado. Para testes, o ideal é usar uma conta secundária.

---

## 6. Entender o aviso de budget

Se aparecer:

```text
Your included budget is complete. Add credits or upgrade to continue.
```

ou:

```text
OpenHuman API error (400 Bad Request): {"success":false,"error":"Insufficient budget"}
```

isso indica que o limite gratuito da conta/cloud acabou.

O plano free pode existir, mas o uso cloud depende de créditos/budget.

---

## 7. Instalar ou testar Ollama

Se o Ollama ainda não estiver instalado:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verificar se o Ollama está ativo:

```bash
ollama list
```

Se aparecer erro dizendo que a porta já está em uso:

```text
listen tcp 127.0.0.1:11434: bind: address already in use
```

isso significa que o Ollama já está rodando.

---

## 8. Baixar modelos locais necessários

O OpenHuman usou no teste:

```text
gemma3:1b-it-qat
```

e para embeddings:

```text
bge-m3
```

Baixar os modelos:

```bash
ollama pull gemma3:1b-it-qat
ollama pull bge-m3
```

Testar o modelo:

```bash
ollama run gemma3:1b-it-qat
```

---

## 9. Configurar modelo local no OpenHuman

No OpenHuman, vá em:

```text
Settings → AI & Models → Local AI Model
```

Selecione:

```text
Gemma 3 1B
```

Marque:

```text
Enable local AI runtime
```

Marque também, se quiser testar o máximo de recursos locais:

```text
Memory summarizer
Embeddings
Heartbeat
Learning / reflection
Subconscious
```

Depois clique em:

```text
Download Models
```

ou:

```text
Refresh
```

O estado esperado é:

```text
State: ready
```

---

## 10. Verificar runtime local

Vá em:

```text
Settings → Developer Options → Local Model Debug
```

O estado esperado é:

```text
State: Ready
Provider: ollama
Backend: ollama
Model: gemma3:1b-it-qat
Running
```

No teste, apareceu também geração local com TPS:

```text
Generation TPS: 16.2 tok/s
```

Isso indica que o OpenHuman conseguiu usar o Ollama local.

---

## 11. Configurar LLM Provider

Vá em:

```text
Settings → AI & Models → LLM Provider
```

Selecione:

```text
Ollama (local)
```

Deixe a API key em branco.

Nos modelos por função, para evitar erro de modelo inexistente, use:

```text
Reasoning: gemma3:1b-it-qat
Coding: gemma3:1b-it-qat
Agentic: gemma3:1b-it-qat
Summarization: gemma3:1b-it-qat
```

Clique em:

```text
Save
```

---

## 12. Atualizar configuração de IA

Vá em:

```text
Settings → Developer Options → AI Configuration
```

Clique em:

```text
Refresh All AI Configuration
```

Confirme que aparece:

```text
Local Model Runtime
State: ready
Target Model: gemma3:1b-it-qat
```

---

## 13. Limitação encontrada no Agent Chat

Mesmo com o runtime local pronto, o "Agent Chat" mostrou:

```text
OpenHuman API error (400 Bad Request): {"success":false,"error":"Insufficient budget"}
```

A tela do Agent Chat informa:

```text
Inference uses your OpenHuman backend
```

Conclusão do teste:

```text
O runtime local, Ollama, embeddings, STT e modelos locais funcionam.
Mas o Agent Chat ainda parece depender do backend da OpenHuman nesta versão beta.
```

Portanto, o OpenHuman é híbrido neste momento:

```text
Parte local: funciona
Chat principal: ainda pode depender de budget/cloud
```

---

## 14. Remover o OpenHuman

```bash
sudo apt remove -y open-human
sudo apt autoremove -y
```

Se quiser remover dados locais do usuário:

```bash
rm -rf ~/.config/OpenHuman
rm -rf ~/.local/share/OpenHuman
rm -rf ~/.cache/OpenHuman
rm -rf ~/.openhuman
```

---

## 15. Resumo final do teste

Funcionou:

```text
Instalação via .deb
Abertura do app
Login
Ollama local
Modelo gemma3:1b-it-qat
Embedding bge-m3
Runtime local ready
Local Model Debug running
```

Não funcionou completamente sem cloud:

```text
Agent Chat
```

Motivo:

```text
Insufficient budget no backend OpenHuman
```

Conclusão:

```text
O OpenHuman tem runtime local real com Ollama, mas o chat principal ainda parece depender da infraestrutura da OpenHuman no beta atual.
```
