# Instalação do Petals no Linux com BLOOM Petals

## Objetivo

Instalar o Petals no Linux para testar inferência distribuída em rede peer-to-peer.

Neste tutorial, o modelo principal usado será:

```text
bigscience/bloom-petals
```

Esse modelo foi escolhido porque funcionou melhor no teste inicial e não exige aprovação manual da Meta como os modelos Llama.

---

# Aviso importante

O Petals usa uma rede pública peer-to-peer.

Isso significa que partes do processamento podem depender de máquinas de outras pessoas conectadas à rede.

Teste com responsabilidade.

Nunca envie:

- senhas
- tokens
- chaves de API
- dados bancários
- documentos pessoais
- informações privadas
- informações empresariais sensíveis

Para dados sensíveis, use modelo local, infraestrutura privada ou ambiente controlado.

---

# Limpeza antes de recomeçar

Se você já apagou a pasta `~/petals-teste`, não precisa apagar de novo.

Mas, para limpar caches antigos, rode:

```bash
rm -rf ~/.cache/huggingface
rm -rf ~/.cache/torch
rm -rf ~/.cache/petals
rm -rf ~/.cache/hivemind
```

Opcionalmente, limpar cache do pip:

```bash
python3 -m pip cache purge
```

---

# Versão do Python

Use Python 3.11.

Evite Python 3.12, porque algumas dependências podem falhar durante a instalação.

Verificar versão atual:

```bash
python3 --version
```

---

# Instalar suporte para PPA

```bash
sudo apt update
sudo apt install -y software-properties-common
```

---

# Adicionar repositório Deadsnakes

```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
```

---

# Atualizar repositórios

```bash
sudo apt update
```

---

# Instalar Python 3.11

```bash
sudo apt install -y python3.11 python3.11-venv python3.11-dev
```

---

# Verificar Python 3.11

```bash
python3.11 --version
```

---

# Instalar dependências gerais

```bash
sudo apt install -y git python3-pip python3-venv
```

---

# Criar pasta do projeto

```bash
mkdir -p ~/petals-teste
cd ~/petals-teste
```

---

# Criar ambiente virtual com Python 3.11

```bash
python3.11 -m venv .venv
```

---

# Ativar ambiente virtual

```bash
source .venv/bin/activate
```

---

# Confirmar versão ativa

```bash
python --version
```

Deve aparecer algo parecido com:

```text
Python 3.11.x
```

---

# Atualizar ferramentas base

```bash
pip install --upgrade "pip<24" "setuptools<70" wheel
```

---

# Criar arquivo de constraints

Essa correção evita erro do `hivemind` com `pkg_resources`.

```bash
echo "setuptools<82" > /tmp/petals-constraints.txt
echo "wheel" >> /tmp/petals-constraints.txt
```

---

# Instalar Hivemind

```bash
PIP_CONSTRAINT=/tmp/petals-constraints.txt pip install hivemind
```

---

# Instalar Petals

```bash
PIP_CONSTRAINT=/tmp/petals-constraints.txt pip install git+https://github.com/bigscience-workshop/petals
```

---

# Instalar Transformers e SentencePiece

```bash
pip install transformers sentencepiece
```

---

# Instalar Hugging Face CLI

```bash
pip install huggingface_hub
```

---

# Login na Hugging Face

A CLI nova da Hugging Face usa:

```bash
hf auth login
```

Cole o token da Hugging Face quando pedir.

Se perguntar se deseja salvar como credencial do Git, pode responder:

```text
Y
```

---

# Criar teste simples

```bash
nano teste_petals.py
```

Cole:

```python
from transformers import AutoTokenizer
from petals import AutoDistributedModelForCausalLM

model_name = "bigscience/bloom-petals"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoDistributedModelForCausalLM.from_pretrained(model_name)

prompt = "Explique em português, de forma simples, o que é uma rede peer-to-peer em inteligência artificial."

inputs = tokenizer(prompt, return_tensors="pt")["input_ids"]

outputs = model.generate(
    inputs,
    max_new_tokens=80,
    do_sample=True,
    temperature=0.7
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

Rodar:

```bash
python3 teste_petals.py
```

---

# Criar chat simples pelo terminal

```bash
nano chat.py
```

Cole:

```python
from transformers import AutoTokenizer
from petals import AutoDistributedModelForCausalLM

model_name = "bigscience/bloom-petals"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoDistributedModelForCausalLM.from_pretrained(model_name)

print("Chat Petals iniciado.")
print("Digite 'sair' para encerrar.\n")

while True:
    prompt = input("Você: ")

    if prompt.lower().strip() in ["sair", "exit", "quit"]:
        break

    inputs = tokenizer(prompt, return_tensors="pt")["input_ids"]

    outputs = model.generate(
        inputs,
        max_new_tokens=120,
        do_sample=True,
        temperature=0.7
    )

    resposta = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print("\nPetals:")
    print(resposta)
    print()
```

Salvar:

```text
CTRL + O
ENTER
CTRL + X
```

Rodar:

```bash
python3 chat.py
```

Para sair:

```text
sair
```

---

# Observação sobre Llama

Modelos Llama, como:

```text
meta-llama/Meta-Llama-3.1-405B-Instruct
meta-llama/Llama-2-70b-chat-hf
```

podem exigir aprovação manual na Hugging Face.

Se aparecer erro `403 Forbidden` ou `GatedRepoError`, significa que a conta ainda não tem acesso autorizado ao modelo.

Por isso, para o primeiro teste, usamos:

```text
bigscience/bloom-petals
```

---

# Observação sobre MissingBlocksError

Se aparecer erro parecido com:

```text
MissingBlocksError
No servers holding blocks are online
```

isso significa que não há peers suficientes online hospedando os blocos daquele modelo no momento.

O Petals depende da rede pública peer-to-peer.

Mesmo que a instalação esteja correta, a inferência pode falhar se não houver servidores ativos para o modelo escolhido.

---

# Monitor público do Petals

Consultar estado da rede:

```text
https://health.petals.dev
```

---

# CLI do Petals

A CLI existe, mas é usada principalmente para rodar um servidor/peer e colaborar com a rede.

Exemplo:

```bash
python3 -m petals.cli.run_server bigscience/bloom-petals
```

Esse comando é para participar da rede como peer.

Para fazer perguntas como cliente, usamos os scripts Python acima.

---

# Uninstall / limpeza

## Sair do ambiente virtual

```bash
deactivate
```

Se aparecer erro dizendo que `deactivate` não existe, pode ignorar.

---

## Apagar pasta do projeto

```bash
rm -rf ~/petals-teste
```

---

## Apagar cache do pip

```bash
python3 -m pip cache purge
```

---

## Apagar cache da Hugging Face

```bash
rm -rf ~/.cache/huggingface
```

---

## Apagar cache do Torch

```bash
rm -rf ~/.cache/torch
```

---

## Apagar cache do Petals e Hivemind

```bash
rm -rf ~/.cache/petals
rm -rf ~/.cache/hivemind
```

---

## Remover login salvo da Hugging Face

```bash
rm -f ~/.cache/huggingface/token
rm -f ~/.huggingface/token
```

---

## Verificar se a pasta foi removida

```bash
ls ~/petals-teste
```

Se aparecer erro dizendo que o arquivo ou diretório não existe, a pasta foi removida.

---

# Observação final

Não é necessário remover o Python 3.11.

Ele pode continuar instalado para outros testes.

Se quiser remover mesmo assim:

```bash
sudo apt remove -y python3.11 python3.11-venv python3.11-dev
sudo apt autoremove -y
```
