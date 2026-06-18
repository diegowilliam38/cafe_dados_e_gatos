# Como testar o Gemini CLI com Pydantic v1 e v2

## O que vamos fazer

Criar um projeto simples com código no estilo Pydantic v1 e usar o Gemini CLI para testar se ele consegue:

* entender a arquitetura do projeto;
* identificar os arquivos principais;
* encontrar pontos frágeis;
* pesquisar documentação atualizada;
* comparar o código local com o padrão atual do Pydantic v2;
* sugerir atualização sem alterar arquivos automaticamente.

## 1. Criar pasta do teste

```bash
mkdir "teste-gemini-cli-pydantic"
cd "teste-gemini-cli-pydantic"
```

## 2. Criar ambiente virtual

```bash
python3 -m venv ".venv"
source ".venv/bin/activate"
```

## 3. Instalar Pydantic

```bash
pip install "pydantic"
```

## 4. Verificar versão instalada

```bash
python -c "import pydantic; print(pydantic.__version__)"
```

## 5. Criar arquivo do projeto

```bash
mkdir "app"
touch "app/main.py"
```

## 6. Colocar código antigo no arquivo

Abra o arquivo:

```bash
nano "app/main.py"
```

Cole este conteúdo:

```python
from pydantic import BaseModel, validator


class User(BaseModel):
    name: str
    age: int

    @validator("age")
    def age_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("age must be positive")
        return value

    class Config:
        validate_assignment = True


user = User(name="Denise", age=10)
print(user.dict())
```

Salve e saia.

## 7. Testar o código

```bash
python "app/main.py"
```

## 8. Criar README simples

```bash
nano "README.md"
```

Cole:

```md
# Teste Gemini CLI com Pydantic

Este projeto é um exemplo simples para testar se o Gemini CLI consegue analisar código local, pesquisar documentação atualizada e comparar padrões antigos do Pydantic v1 com o padrão atual do Pydantic v2.
```

Salve e saia.

## 9. Rodar o Gemini CLI sem instalar

```bash
npx "@google/gemini-cli"
```

## 10. Rodar o Gemini CLI se já estiver instalado

```bash
gemini
```

## 11. Teste 1 — Entendimento do projeto

Prompt:

```text
Explique a arquitetura deste projeto.
```

Observar se ele identifica:

```text
pasta app
arquivo main.py
uso de Pydantic
modelo User
validação de idade
README do projeto
```

## 12. Teste 2 — Navegação pelo projeto

Prompt:

```text
Quais arquivos eu deveria ler primeiro para entender este projeto?
```

Observar se ele aponta:

```text
README.md
app/main.py
```

## 13. Teste 3 — Investigação e troubleshooting

Prompt:

```text
Encontre possíveis gargalos, erros ou pontos frágeis neste projeto.
```

Observar se ele menciona:

```text
uso de validator
uso de Config
uso de dict()
possível padrão antigo do Pydantic
necessidade de conferir compatibilidade com Pydantic v2
```

## 14. Teste 4 — Busca Google + documentação atualizada

Prompt principal:

```text
Pesquise a documentação mais recente do Pydantic v2 e diga se este código ainda segue o padrão atual.
```

Prompt mais direcionado:

```text
Compare este arquivo app/main.py com o padrão atual do Pydantic v2. Primeiro explique o que mudou. Não altere arquivos automaticamente.
```

Prompt para sugestão de atualização:

```text
Sugira como atualizar este código para o padrão atual do Pydantic v2, sem alterar arquivos automaticamente.
```

## 15. O que observar no Teste 4

Observar se o Gemini CLI identifica mudanças como:

```text
@validator foi substituído por @field_validator em muitos casos
Config passou a ser substituído por model_config em muitos casos
dict() passou a ter alternativa model_dump()
padrões de validação mudaram no Pydantic v2
```

## 16. Pedir versão atualizada sem aplicar automaticamente

Prompt:

```text
Mostre uma versão atualizada deste arquivo para Pydantic v2, mas apenas como sugestão em bloco de código. Não altere o arquivo ainda.
```

## 17. Exemplo esperado de código atualizado

```python
from pydantic import BaseModel, ConfigDict, field_validator


class User(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    name: str
    age: int

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("age must be positive")
        return value


user = User(name="Denise", age=10)
print(user.model_dump())
```

## 18. Aplicar atualização manualmente

Abra o arquivo:

```bash
nano "app/main.py"
```

Substitua pelo código atualizado.

## 19. Rodar novamente

```bash
python "app/main.py"
```

## 20. Teste de prompt direto

```bash
gemini -p "Explique a arquitetura deste projeto em linguagem simples"
```

## 21. Teste com saída JSON

```bash
gemini -p "Analise este projeto e diga se o código segue Pydantic v2" --output-format json
```

## 22. Cuidados de segurança

Não execute comandos perigosos sem revisar.

Não exponha chaves de API.

Não grave tokens na tela.

Não teste primeiro em projeto importante.

Não aceite alteração automática sem conferir.

Use projeto de teste quando possível.

## 23. Links oficiais

```text
https://github.com/google-gemini/gemini-cli
```

```text
https://github.com/google-gemini/gemini-cli/blob/main/docs/index.md
```

```text
https://docs.pydantic.dev/latest/migration/
```

## 24. Próximo teste

```text
Goose
```
