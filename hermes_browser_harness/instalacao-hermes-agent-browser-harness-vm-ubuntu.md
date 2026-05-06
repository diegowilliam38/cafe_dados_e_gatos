# Como instalar Hermes Agent + Browser Harness em uma VM Ubuntu

Este guia mostra apenas os passos de instalação para testar o **Hermes Agent** junto com o **Browser Harness** em uma VM Ubuntu.

A proposta é manter tudo em um ambiente de teste separado, sem misturar com outros projetos.

---

## 1. Atualizar o sistema

Abra o terminal da VM e rode:

```bash
sudo apt update
sudo apt upgrade -y
```

---

## 2. Instalar dependências básicas

```bash
sudo apt install -y git curl ca-certificates build-essential python3 python3-pip python3-venv
```

Confira as versões:

```bash
python3 --version
git --version
curl --version
```

---

## 3. Instalar o `uv`

O `uv` será usado para instalar o Browser Harness.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Recarregue o terminal:

```bash
source ~/.bashrc
```

Confira se instalou:

```bash
uv --version
```

Se o comando não aparecer, feche e abra o terminal novamente.

---

## 4. Criar uma pasta para o ambiente de teste

```bash
mkdir -p ~/teste-hermes-browser
cd ~/teste-hermes-browser
```

---

## 5. Instalar o Hermes Agent

Rode o instalador oficial:

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Recarregue o terminal:

```bash
source ~/.bashrc
```

Confira se o comando `hermes` está disponível:

```bash
command -v hermes
hermes --help
```

Rode o diagnóstico:

```bash
hermes doctor
```

---

## 6. Abrir o Hermes Agent pela primeira vez

```bash
hermes
```

Na primeira execução, o Hermes pode pedir configuração de modelo/provedor.

Siga o assistente de configuração exibido no terminal.

---

## 7. Clonar o Browser Harness

Saia do Hermes, se ele estiver aberto, e volte para a pasta do teste:

```bash
cd ~/teste-hermes-browser
git clone https://github.com/browser-use/browser-harness.git
cd browser-harness
```

---

## 8. Instalar o Browser Harness

Dentro da pasta `browser-harness`, rode:

```bash
uv tool install -e .
```

Confira se o comando foi instalado:

```bash
command -v browser-harness
browser-harness --help
```

Rode o diagnóstico:

```bash
browser-harness --doctor
```

---

## 9. Instalar o Google Chrome, se a VM ainda não tiver navegador

Se o Chrome ainda não estiver instalado, rode:

```bash
cd ~/Downloads
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb
```

Confira:

```bash
google-chrome --version
```

---

## 10. Criar um perfil isolado do Chrome para o teste

Este perfil separado evita usar o Chrome principal da máquina.

```bash
mkdir -p ~/teste-hermes-browser/chrome-profile
```

Abra o Chrome de teste com depuração remota:

```bash
google-chrome \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/teste-hermes-browser/chrome-profile"
```

Deixe essa janela do Chrome aberta.

---

## 11. Testar a conexão do Browser Harness com o Chrome

Abra outro terminal e rode:

```bash
export BU_CDP_URL=http://127.0.0.1:9222
browser-harness --doctor
```

Depois rode:

```bash
export BU_CDP_URL=http://127.0.0.1:9222
browser-harness -c 'print(page_info())'
```

Se aparecer informação da página atual, o Browser Harness conseguiu se conectar ao navegador.

---

## 12. Testar o Hermes com a documentação do Browser Harness

Abra o Hermes:

```bash
hermes
```

Dentro do Hermes, peça:

```text
Leia o arquivo ~/teste-hermes-browser/browser-harness/SKILL.md e explique como você pode usar o browser-harness neste ambiente de teste.
```

Depois peça:

```text
Use o browser-harness para verificar qual página está aberta no Chrome de teste.
```

---

## 13. Comandos úteis de verificação

Ver caminho do Hermes:

```bash
command -v hermes
```

Ver caminho do Browser Harness:

```bash
command -v browser-harness
```

Ver diagnóstico do Hermes:

```bash
hermes doctor
```

Ver diagnóstico do Browser Harness:

```bash
browser-harness --doctor
```

Ver se a porta 9222 está aberta:

```bash
ss -ltnp | grep 9222
```

---

## 14. Estrutura esperada do teste

Depois da instalação, a pasta deve ficar parecida com isto:

```text
~/teste-hermes-browser/
├── browser-harness/
└── chrome-profile/
```

O Hermes pode criar arquivos próprios na home do usuário, normalmente em uma pasta de configuração própria.

---

## 15. Como apagar o ambiente de teste

Para apagar os arquivos do teste:

```bash
rm -rf ~/teste-hermes-browser
```

Atenção: isso remove o repositório clonado do Browser Harness e o perfil isolado do Chrome usado no teste.

Para verificar se o Hermes continua instalado globalmente:

```bash
command -v hermes
```

---

## 16. Observação importante

Este guia é para ambiente de teste em VM.

Não use contas pessoais, senhas reais ou sessões importantes do navegador durante os testes.

Use sempre o perfil isolado do Chrome criado em:

```bash
~/teste-hermes-browser/chrome-profile
```
