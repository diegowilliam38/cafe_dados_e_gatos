![Café com Dados & Gatos — Capa do Projeto](https://raw.githubusercontent.com/djeannie29/cafe_dados_e_gatos/main/banner_github.png)

# Datasets Sintéticos — Café com Dados & Gatos

Este repositório reúne **datasets 100% sintéticos** (não contêm dados pessoais), criados exclusivamente para vídeos do YouTube sobre **Pandas** no canal **@CafecomDadoseGatos**.

A proposta é ser um “laboratório de exemplos” para **Data Science** e **Machine Learning**, incluindo cenários comuns do dia a dia (CSV do Excel, separador `;` vs `,`, decimal com vírgula, encoding, datas, zeros à esquerda etc.).

---

## 📁 Estrutura do projeto

- `data/` → datasets (.csv / .xlsx) usados nos vídeos  
- `notebooks/` → notebooks (.ipynb) com os exemplos

---

## ✅ Como usar

### Opção A — Rodar no Google Colab (recomendado)

1) Abra um Colab e execute:

```bash
git clone https://github.com/djeannie29/cafe_dados_e_gatos.git
cd cafe_dados_e_gatos
ls
ls data
```

2) Leia os arquivos da pasta \data/`:`
```python
import pandas as pd
from pathlib import Path

ARQ = Path("data") / "arquivo.csv"  # troque pelo arquivo desejado
df = pd.read_csv(ARQ)
df.head()
```

### Opção B — Rodar local (VS Code / Jupyter)

Clone o repositório:
```bash
git clone https://github.com/djeannie29/cafe_dados_e_gatos.git
cd cafe_dados_e_gatos
```
> Dica: rode sempre com o diretório atual na raiz do projeto (onde existe a pasta data/).

## 🧩 Dicas rápidas (bugs comuns de CSV do Excel)
1) “Virou uma coluna só” (separador ; vs ,)
```python
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path("data") / "arquivo.csv", sep=";")  # ou sep=","
```
2) “3,14 virou texto” (decimal com vírgula)
```python
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path("data") / "arquivo.csv", sep=";", decimal=",")
```
3) Acentos quebrados / UnicodeDecodeError (encoding)
```python
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path("data") / "arquivo.csv", sep=";", encoding="utf-8")
# se precisar:
df = pd.read_csv(Path("data") / "arquivo.csv", sep=";", encoding="latin-1")
```
4) Zero à esquerda sumiu (CEP/ID)
```python
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path("data") / "arquivo.csv", sep=";", dtype={"cep": str})
```
5) Datas invertendo dia/mês
```python
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path("data") / "arquivo.csv", sep=";", parse_dates=["data"], dayfirst=True)
```
---
---

## 📦 Arquivos disponíveis (pasta `data/`)

### 🐱 Datasets de gatos (para Shorts de Pandas)
- `dataset_small_gatos.csv` → base pequena (boa para `loc`, `iloc`, `sort_values`)
- `dataset_big_gatos.csv` → base maior (boa para exemplos mais “realistas”)
- `dataset_gatos_com_nans.csv` → base com valores ausentes (boa para `isnull().sum()` e `fillna()`)

### 💉 Datasets para exemplos de `merge`
- `dataset_vacinas_para_merge.csv` → tabela auxiliar com `id_gato` e `data_ultima_vacina`
- `dataset_gatos_vacina_small.csv` → base pequena com coluna `vacinado` (boa para merge rápido)
- `dataset_gatos_vacina_big.csv` → base maior com coluna `vacinado`

### 🧩 Datasets de “bugs do Excel” (CSV/XLSX)
- `bugs_excel_1000.xlsx` → arquivo Excel base
- `bugs_excel_1000_utf8sig.csv` → CSV exportado (útil para testar separador/encoding)
- `bugs_excel_1000_latin1.csv` → CSV exportado em latin-1 (útil para simular problema de acentos)

---

## 🧪 Exemplos rápidos

### Ler um dataset “normal” (gatos)
```python
import pandas as pd
from pathlib import Path

df = pd.read_csv(Path("data") / "dataset_small_gatos.csv")
df.head()


## 🔒 Privacidade
Todos os dados são **sintéticos** e usados apenas para fins didáticos.

---

## ✨ Créditos
Conteúdo e datasets: **Café com Dados & Gatos**  
YouTube: **@CafecomDadoseGatos**


   
