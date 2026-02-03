````md
<p align="center">
  <img src="https://raw.githubusercontent.com/djeannie29/cafe_dados_e_gatos/main/banner_github.png" width="1000" alt="Café com Dados & Gatos — Datasets Sintéticos"/>
</p>

# Datasets Sintéticos — Café com Dados & Gatos

Este repositório reúne **datasets 100% sintéticos** (não contêm dados pessoais), criados exclusivamente para vídeos do YouTube sobre **Pandas** no canal **@CafecomDadoseGatos**.

A proposta é ser um “laboratório de exemplos” para **Data Science** e **Machine Learning**, incluindo cenários comuns do dia a dia (CSV do Excel, separador `;` vs `,`, decimal com vírgula, encoding, datas, zeros à esquerda etc.).

---

## 📁 Estrutura do projeto

- `data/` → datasets (.csv / .xlsx) usados nos vídeos  
- `notebooks/` → notebooks (.ipynb) com os exemplos (se você tiver/passar a criar)

---

## ✅ Como usar

### Opção A — Rodar no Google Colab (recomendado)
1) Abra um Colab e execute:

```bash
git clone https://github.com/djeannie29/cafe_dados_e_gatos.git
cd cafe_dados_e_gatos
ls
ls data
````

2. Leia os arquivos da pasta `data/`:

```python
import pandas as pd
from pathlib import Path

ARQ = Path("data") / "dataset_gatos_com_nans.csv"  # troque pelo arquivo desejado
df = pd.read_csv(ARQ)

df.head()
```

---

### Opção B — Rodar local (VS Code / Jupyter)

1. Clone o repositório:

```bash
git clone https://github.com/djeannie29/cafe_dados_e_gatos.git
cd cafe_dados_e_gatos
```

2. Use os mesmos caminhos relativos nos notebooks/scripts:

```python
import pandas as pd
from pathlib import Path

df = pd.read_csv(Path("data") / "dataset_gatos_com_nans.csv")
df.head()
```

> Dica: para evitar erro de caminho, rode sempre com o diretório atual na **raiz do projeto** (onde existe a pasta `data/`).

---

## 🧩 Dicas rápidas (bugs comuns de CSV do Excel)

### 1) “Virou uma coluna só”

Geralmente é separador errado (`;` vs `,`):

```python
df = pd.read_csv(Path("data") / "arquivo.csv", sep=";")  # ou sep=","
```

### 2) “3,14 virou texto e mean() quebra”

Use `decimal=","`:

```python
df = pd.read_csv(Path("data") / "arquivo.csv", sep=";", decimal=",")
```

### 3) Acentos quebrados / UnicodeDecodeError

Teste `utf-8` e depois `latin-1`:

```python
df = pd.read_csv(Path("data") / "arquivo.csv", sep=";", encoding="utf-8")
# se precisar:
df = pd.read_csv(Path("data") / "arquivo.csv", sep=";", encoding="latin-1")
```

### 4) Zero à esquerda sumiu (CEP/ID)

Force como texto:

```python
df = pd.read_csv(Path("data") / "arquivo.csv", sep=";", dtype={"cep": str})
```

### 5) Datas invertendo dia/mês

Parseie datas com `dayfirst=True`:

```python
df = pd.read_csv(Path("data") / "arquivo.csv", sep=";", parse_dates=["data"], dayfirst=True)
```

---

## 🔒 Privacidade

Todos os dados são **sintéticos** e usados apenas para fins didáticos.

---

## ✨ Créditos

Conteúdo e datasets: **Café com Dados & Gatos**
YouTube: **@CafecomDadoseGatos**



