# Como instalar Hermes Agent + Browser Harness no Ubuntu VM

## Objetivo

Instalar e testar o Hermes Agent e o Browser Harness em uma VM Ubuntu, usando o caminho mais simples possível para teste e gravação de vídeo.

Este roteiro usa:

- Ubuntu em VM
- Brave Browser já instalado
- Hermes Agent instalado pelo instalador oficial
- Browser Harness instalado pelo repositório oficial
- Sem pasta de ambiente separada
- Sem perfil isolado de navegador
- Sem configuração avançada

---

## 1. Atualizar o sistema e instalar dependência mínima

```bash
sudo apt update
sudo apt install -y git curl
```

---

## 2. Instalar Hermes Agent

Instalação oficial:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Recarregar o terminal:

```bash
source ~/.bashrc
```

Verificar se o comando ficou disponível:

```bash
command -v hermes
```

Verificar versão:

```bash
hermes --version
```

Abrir o Hermes:

```bash
hermes
```

---

## 3. Configurar o Hermes Agent

Abrir o assistente de configuração completo:

```bash
hermes setup
```

Ou configurar apenas modelo/provedor:

```bash
hermes model
```

Diagnóstico:

```bash
hermes doctor
```

---

## 4. Testar o Hermes sozinho

Abrir o Hermes:

```bash
hermes
```

Enviar uma mensagem simples no terminal:

```text
Olá, Hermes. Responda apenas: funcionando.
```

Se o Hermes responder, ele está funcionando sozinho.

---

## 5. Instalar Browser Harness

Ir para a home:

```bash
cd ~
```

Clonar o repositório oficial:

```bash
git clone https://github.com/browser-use/browser-harness
```

Entrar na pasta:

```bash
cd ~/browser-harness
```

Instalar como ferramenta global com uv:

```bash
uv tool install -e .
```

Verificar se o comando ficou disponível:

```bash
command -v browser-harness
```

---

## 6. Testar Browser Harness sozinho

Abrir o Brave Browser normalmente.

Depois, no terminal, rodar:

```bash
browser-harness -c 'print(page_info())'
```

Se imprimir informações da página, o Browser Harness está funcionando.

---

## 7. Diagnóstico do Browser Harness

Se o teste não funcionar, rodar:

```bash
browser-harness --doctor
```

Observar principalmente:

- `chrome running`
- `daemon alive`

---

## 8. Liberar debug remoto no navegador

Se o navegador estiver aberto, mas o daemon falhar, abrir no Brave:

```text
chrome://inspect/#remote-debugging
```

Marcar a opção:

```text
Allow remote debugging for this browser instance
```

Se aparecer popup pedindo permissão:

```text
Allow
```

Depois testar novamente:

```bash
browser-harness -c 'print(page_info())'
```

---

## 9. Reiniciar daemon se necessário

Se o navegador e o daemon aparecerem como ativos, mas o teste ainda falhar:

```bash
browser-harness -c 'restart_daemon()'
```

Depois testar novamente:

```bash
browser-harness -c 'print(page_info())'
```

---

## 10. Limpeza simples em caso de travamento

Fechar o Brave.

Remover arquivos temporários do daemon:

```bash
rm -f /tmp/bu-default.sock /tmp/bu-default.pid
```

Abrir o Brave novamente.

Testar:

```bash
browser-harness -c 'print(page_info())'
```

---

## 11. Atualizar Browser Harness

Se aparecer aviso de atualização:

```bash
browser-harness --update -y
```

Depois testar novamente:

```bash
browser-harness -c 'print(page_info())'
```

---

## 12. Ordem correta de teste

Testar primeiro o Hermes:

```bash
hermes
```

Depois testar o Browser Harness:

```bash
browser-harness -c 'print(page_info())'
```

Somente depois tentar usar os dois juntos.
