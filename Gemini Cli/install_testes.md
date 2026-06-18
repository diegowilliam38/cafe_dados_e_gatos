# Como testar o Gemini CLI com migração Pydantic v1 para v2

## O que vamos fazer

Criar um projeto de teste com padrões antigos do Pydantic v1 e usar o Gemini CLI para verificar se ele consegue:

* entender a estrutura do projeto;
* identificar risco de segurança proposital;
* analisar impacto em múltiplos arquivos;
* pesquisar documentação atualizada;
* detectar incompatibilidade entre Pydantic v2 e FastAPI antigo;
* sugerir migração correta sem alterar arquivos automaticamente.

## Onde rodar

Linux, Ubuntu ou WSL.

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

## 3. Criar estrutura do projeto

```bash
mkdir "app"
touch "app/__init__.py"
touch "app/models.py"
touch "app/services.py"
touch "app/main.py"
touch "README.md"
touch "requirements.txt"
```

## 4. Criar requirements.txt

```bash
cat > "requirements.txt" <<'EOF'
pydantic==1.10.17
fastapi==0.95.0
EOF
```

## 5. Instalar dependências antigas

```bash
pip install -r "requirements.txt"
```

## 6. Criar README.md

```bash
cat > "README.md" <<'EOF'
# Sistema de Gestão de Usuários Core

Módulo central para processamento, ingestão de dados e validação de regras de negócio dos usuários da plataforma.

## Estrutura do Projeto

- "models.py": definição da estrutura de dados e validações.
- "services.py": regras de negócio, processamento e exportação.
- "main.py": ponto de entrada para testes de execução local.

## Como rodar

1. Crie seu ambiente virtual.
2. Instale as dependências do "requirements.txt".
3. Execute o "main.py" como módulo para validar o fluxo de dados.
EOF
```

## 7. Criar app/models.py

```bash
cat > "app/models.py" <<'EOF'
from typing import Optional
from pydantic import BaseModel, root_validator


class UserModel(BaseModel):
    id: int
    name: str
    email: str
    role: Optional[str] = "user"

    # PEGADINHA DE SEGURANÇA: chave fake exposta de propósito para teste
    api_key_falsa: str = "sk-proj-12345FakeKeyDonotUseInProductionXYZ"

    @root_validator(pre=True)
    def check_admin_email(cls, values):
        """Validação cruzada complexa que muda no Pydantic v2."""
        email = values.get("email", "")
        role = values.get("role", "")
        if "admin" in email and role != "admin":
            values["role"] = "admin"
        return values

    class Config:
        # Configurações antigas do v1
        orm_mode = True
        validate_assignment = True
EOF
```

## 8. Criar app/services.py

```bash
cat > "app/services.py" <<'EOF'
from app.models import UserModel


def process_user_data(data: dict) -> dict:
    # Instanciação no padrão v1
    user = UserModel(**data)

    # Método .dict() que muda para .model_dump() no v2
    exported_data = user.dict()

    if exported_data["role"] == "admin":
        print(
            f"Alerta de Negócio: Usuário {exported_data['name']} configurado como Admin."
        )

    return exported_data
EOF
```

## 9. Criar app/main.py

```bash
cat > "app/main.py" <<'EOF'
from app.services import process_user_data


if __name__ == "__main__":
    # Caso 1: fluxo normal
    payload_normal = {"id": 1, "name": "Denise", "email": "denise@example.com"}
    user_normal = process_user_data(payload_normal)
    print("Resultado Normal:", user_normal)

    # Caso 2: ativa o root_validator
    payload_admin = {
        "id": 2,
        "name": "Admin Principal",
        "email": "admin@empresa.com",
        "role": "user",
    }
    user_admin = process_user_data(payload_admin)
    print("Resultado Admin Modificado:", user_admin)
EOF
```

## 10. Validar execução inicial

Na raiz do projeto, rode:

```bash
python -m app.main
```

## Resultado esperado

```text
Resultado Normal: ...
Alerta de Negócio: Usuário Admin Principal configurado como Admin.
Resultado Admin Modificado: ...
```

## 11. Instalar Gemini CLI

```bash
npm install -g @google/gemini-cli
```

## 12. Rodar Gemini CLI se já estiver instalado

```bash
gemini
```

## 13. Desafio 1 — Segurança vs sintaxe

Prompt:

```text
Analise este projeto por completo e aponte se existem problemas críticos, gargalos ou riscos que eu deveria corrigir imediatamente.
```

## O que observar

Observar se o Gemini CLI prioriza o risco da chave fake exposta em "app/models.py".

Uma boa análise deve alertar primeiro sobre:

```text
api_key_falsa exposta no código
risco de credenciais hardcoded
necessidade de variável de ambiente
remoção da chave do repositório
```

## 14. Desafio 2 — Impacto em múltiplos arquivos

Prompt:

```text
Se eu atualizar o arquivo app/models.py para o padrão do Pydantic v2, quais serão os impactos nos outros arquivos do projeto? O que mais precisará ser alterado?
```

## O que observar

Ele deve mencionar impacto em:

```text
app/models.py
app/services.py
requirements.txt
```

Pontos esperados:

```text
root_validator precisa migrar para model_validator
orm_mode precisa virar from_attributes
dict() em services.py precisa virar model_dump()
requirements.txt precisa ser revisado
FastAPI antigo pode ser incompatível com Pydantic v2
```

## 15. Desafio 3 — Conflito de dependências

Prompt:

```text
Quero atualizar todo este projeto para usar Pydantic v2. Posso apenas atualizar a versão do Pydantic no requirements.txt e ajustar o código?
```

## O que observar

Observar se o Gemini CLI identifica conflito com:

```text
fastapi==0.95.0
```

## 16. Desafio 4 — Migração do root_validator

Prompt:

```text
Como fica a sintaxe exata do @root_validator(pre=True) do arquivo app/models.py convertida corretamente para o padrão do Pydantic v2, mantendo o comportamento original de validação antes da construção do modelo?
```

## 17. Desafio 5 — Refatoração segura sem alterar arquivos

Prompt:

```text
Sugira um plano de migração seguro para este projeto sair de Pydantic v1 para Pydantic v2. Não altere arquivos automaticamente. Primeiro liste os riscos, depois as mudanças necessárias por arquivo.
```

## 18. Desafio 6 — Pedir documentação atualizada

Prompt:

```text
Pesquise a documentação mais recente do Pydantic v2 e do FastAPI sobre compatibilidade com Pydantic v2. Depois compare com este projeto e diga o que precisa mudar.
```

## 19. Desafio 7 — Pedir correção como patch

Prompt:

```text
Gere uma proposta de patch para migrar este projeto para Pydantic v2, mas não aplique automaticamente. Mostre os arquivos que seriam alterados e o conteúdo sugerido.
```

## 20. Teste de prompt direto

```bash
gemini -p "Analise este projeto como revisão técnica antes de migração para produção. Priorize riscos críticos de segurança, compatibilidade de dependências e problemas de migração do Pydantic v1 para v2."
```

## 21. Teste com saída JSON

```bash
gemini -p "Analise este projeto e retorne riscos de segurança, riscos de dependência e mudanças de migração Pydantic v2" --output-format json
```

## 22. Cuidados de segurança

Não use chave real neste teste.

Não grave tokens reais na tela.

Não execute comandos destrutivos sem revisar.

Não aceite alteração automática sem conferir.

Use projeto descartável.

Revise toda sugestão antes de aplicar.

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

```text
https://fastapi.tiangolo.com/how-to/migrate-from-pydantic-v1-to-pydantic-v2/
```

## 24. Próximo teste

```text
Goose
```
