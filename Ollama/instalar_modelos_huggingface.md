# COMO RODAR MODELOS GGUF DO HUGGING FACE NO OLLAMA
# WINDOWS + LINUX
# MODO DIRETO COM "hf.co"

---

# O QUE ESTAMOS FAZENDO

Vamos rodar modelos GGUF do Hugging Face diretamente no Ollama, sem baixar manualmente o arquivo e sem criar "Modelfile".

O comando do modelo funciona igual no Windows e no Linux.

A diferença entre Windows e Linux fica basicamente na instalação do Ollama e no terminal usado:

```text
Windows: PowerShell
Linux: Terminal
```

Depois que o Ollama está instalado, o comando para rodar o modelo é o mesmo:

```text
ollama run hf.co/USUARIO/REPOSITORIO:QUANTIZACAO
```

Exemplo:

```text
ollama run hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

---

# COMO PEGAR O COMANDO NO HUGGING FACE

Abra a página do modelo GGUF no Hugging Face.

Clique em:

```text
Use this model
```

Depois escolha:

```text
Ollama
```

Escolha a quantização, por exemplo:

```text
Q4_K_M
```

Copie o comando pronto que o Hugging Face gerar.

Exemplo:

```text
ollama run hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

---

# QUAL QUANTIZAÇÃO USAR

Para máquinas simples, use:

```text
Q4_K_M
```

Se estiver muito pesado, teste:

```text
Q3_K_M
```

Se quiser qualidade maior e tiver mais memória, teste:

```text
Q5_K_M
```

---

# PARTE 1 — WINDOWS

# 1. Instalar Ollama pelo aplicativo

Baixe e instale:

```text
https://ollama.com/download/windows
```

Depois de instalar, feche e abra o PowerShell.

---

# 2. Testar se o Ollama está funcionando

```powershell
ollama --version
```

---

# 3. Rodar modelo pequeno 1 — TinyLlama

```powershell
ollama run hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

---

# 4. Testar o modelo

Depois que abrir o chat no terminal, digite:

```text
Explique em português o que é um modelo de IA local.
```

Para sair:

```text
/bye
```

---

# 5. Rodar modelo pequeno 2 — Qwen

Escolha um repositório GGUF pequeno do Qwen no Hugging Face.

No Hugging Face, clique em:

```text
Use this model
```

Escolha:

```text
Ollama
```

Selecione a quantização:

```text
Q4_K_M
```

Copie o comando gerado.

O formato será assim:

```powershell
ollama run hf.co/USUARIO/REPOSITORIO-QWEN-GGUF:Q4_K_M
```

Exemplo de estrutura:

```powershell
ollama run hf.co/NOME_DO_AUTOR/NOME_DO_MODELO_QWEN_GGUF:Q4_K_M
```

---

# 6. Ver modelos baixados no Ollama

```powershell
ollama list
```

---

# 7. Remover modelo do Ollama

```powershell
ollama rm hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

Se o nome aparecer diferente no "ollama list", copie exatamente o nome mostrado na lista.

---

# PARTE 2 — LINUX

# 1. Instalar Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

# 2. Testar se o Ollama está funcionando

```bash
ollama --version
```

---

# 3. Rodar modelo pequeno 1 — TinyLlama

```bash
ollama run hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

---

# 4. Testar o modelo

Depois que abrir o chat no terminal, digite:

```text
Explique em português o que é um modelo de IA local.
```

Para sair:

```text
/bye
```

---

# 5. Rodar modelo pequeno 2 — Qwen

Escolha um repositório GGUF pequeno do Qwen no Hugging Face.

No Hugging Face, clique em:

```text
Use this model
```

Escolha:

```text
Ollama
```

Selecione a quantização:

```text
Q4_K_M
```

Copie o comando gerado.

O formato será assim:

```bash
ollama run hf.co/USUARIO/REPOSITORIO-QWEN-GGUF:Q4_K_M
```

Exemplo de estrutura:

```bash
ollama run hf.co/NOME_DO_AUTOR/NOME_DO_MODELO_QWEN_GGUF:Q4_K_M
```

---

# 6. Ver modelos baixados no Ollama

```bash
ollama list
```

---

# 7. Remover modelo do Ollama

```bash
ollama rm hf.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF:Q4_K_M
```

Se o nome aparecer diferente no "ollama list", copie exatamente o nome mostrado na lista.

---

# COMO SABER SE O MODELO SERVE PARA ESSE MÉTODO

No Hugging Face, o repositório precisa ter arquivos GGUF.

Procure por nomes como:

```text
GGUF
Q4_K_M
Q3_K_M
Q5_K_M
```

Exemplo de arquivo:

```text
tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
```


Esses formatos não entram direto nesse fluxo simples com Ollama.

---

