# Como instalar o AionUI no Linux

## 1. Acessar o download oficial

Baixar o AionUI para Linux pelo GitHub Releases:

```text
https://github.com/iOfficeAI/AionUi/releases
```

## 2. Baixar a versão Linux correta

Para Ubuntu/Linux comum em computador Intel ou AMD 64-bit, baixar:

```text
AionUi-2.1.4-linux-amd64.deb
```

Para máquina ARM, baixar:

```text
AionUi-2.1.4-linux-arm64.deb
```

Na maioria dos notebooks e PCs comuns, usar a versão:

```text
linux-amd64.deb
```

## 3. Entrar na pasta de downloads

```bash
cd "$HOME/Downloads"
```

## 4. Instalar o pacote .deb

```bash
sudo dpkg -i "AionUi-2.1.4-linux-amd64.deb"
```

## 5. Corrigir dependências, se precisar

Se aparecer erro de dependência, rodar:

```bash
sudo apt --fix-broken install -y
```

Depois tentar instalar novamente:

```bash
sudo dpkg -i "AionUi-2.1.4-linux-amd64.deb"
```

## 6. Abrir o AionUI

Tentar abrir pelo terminal:

```bash
aionui
```

Ou procurar no menu do Ubuntu por:

```text
AionUI
```

## 7. Testar Hermes no terminal

```bash
hermes --help
```

## 8. Testar OpenClaw no terminal

```bash
openclaw --help
```

## 9. Configurar no AionUI

Dentro do AionUI, verificar se ele detecta Hermes e OpenClaw automaticamente.

Se não detectar, procurar a opção de adicionar comando local ou CLI manualmente.

Adicionar:

```bash
hermes
```

E também:

```bash
openclaw
```

## 10. Primeiro teste

Pedir no AionUI:

```text
Crie um arquivo chamado teste-aionui.txt dizendo qual agente executou a tarefa.
```

## 11. Conferir o arquivo

```bash
ls -la
cat "teste-aionui.txt"
```
