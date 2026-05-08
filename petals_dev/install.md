# Instalação do Petals no Linux com Llama

## Versão mínima do Python

O Petals exige Python 3.8 ou superior.

Recomendado para este teste:

- Python 3.10
- Python 3.11

Verificar versão instalada:

```bash
python3 --version
```

---

## Instalar dependências

```bash
sudo apt update
sudo apt install -y git python3 python3-pip python3-venv
```

---

## Criar pasta do projeto

```bash
mkdir -p ~/petals-teste
cd ~/petals-teste
```

---

## Criar ambiente virtual

```bash
python3 -m venv .venv
```

---

## Ativar ambiente virtual

```bash
source .venv/bin/activate
```

---

## Atualizar pip

```bash
pip install --upgrade pip
```

---

## Instalar Petals

```bash
pip install git+https://github.com/bigscience-workshop/petals
```

---

## Instalar Hugging Face CLI

```bash
pip install huggingface_hub
```

---

## Login na Hugging Face

```bash
huggingface-cli login
```

Cole o token da Hugging Face quando pedir.

Antes disso, verifique se você já aceitou a licença do modelo Llama na Hugging Face.

---

# Como fazer perguntas ao modelo

O Petals não funciona exatamente como o Ollama.

No Ollama usamos algo como:

```bash
ollama run nome-do-modelo
```

No Petals, a inferência normalmente é feita via Python, usando:

- transformers
- petals
- AutoTokenizer
- AutoDistributedModelForCausalLM

Abaixo estão dois modos de teste.

---

# Modo 1: teste simples com uma pergunta fixa

## Criar arquivo de teste

```bash
nano teste_llama_petals.py
```

Cole:

```python
from transformers import AutoTokenizer
from petals import AutoDistributedModelForCausalLM

model_name = "meta-llama/Meta-Llama-3.1-405B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoDistributedModelForCausalLM.from_pretrained(model_name)

prompt = "Explique em português, de forma simples, o que é uma rede peer-to-peer em inteligência artificial."

inputs = tokenizer(prompt, return_tensors="pt")["input_ids"]

outputs = model.generate(
    inputs,
    max_new_tokens=120,
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
python3 teste_llama_petals.py
```

---

# Modo 2: chat simples pelo terminal

## Criar arquivo de chat

```bash
nano chat.py
```

Cole:

```python
from transformers import AutoTokenizer
from petals import AutoDistributedModelForCausalLM

model_name = "meta-llama/Meta-Llama-3.1-405B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoDistributedModelForCausalLM.from_pretrained(model_name)

print("Chat Petals + Llama iniciado.")
print("Digite 'sair' para encerrar.\n")

while True:
    prompt = input("Você: ")

    if prompt.lower().strip() in ["sair", "exit", "quit"]:
        break

    inputs = tokenizer(prompt, return_tensors="pt")["input_ids"]

    outputs = model.generate(
        inputs,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7
    )

    resposta = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print("\nLlama:")
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

# CLI do Petals

A CLI do Petals existe, mas ela é usada principalmente para rodar um servidor e colaborar com a rede.

Exemplo:

```bash
python3 -m petals.cli.run_server meta-llama/Meta-Llama-3.1-405B-Instruct
```

Esse comando é para participar como peer/servidor.

Para fazer perguntas como cliente, usamos os scripts Python acima.

---

# Monitor público do Petals

Consultar modelos e saúde da rede:

https://health.petals.dev
