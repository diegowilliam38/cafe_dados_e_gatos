# Como testei o Gemini CLI na prática

Repositório com experimentos e avaliações reais do Gemini CLI utilizando projetos de teste controlados.

O objetivo não é apenas verificar se o Gemini CLI gera respostas, mas avaliar sua capacidade de:

* analisar código existente;
* identificar problemas de segurança;
* detectar incompatibilidades de dependências;
* avaliar impacto de alterações em múltiplos arquivos;
* consultar documentação atualizada;
* propor migrações técnicas;
* sugerir correções sem modificar arquivos automaticamente.

---

# O que existe nesta pasta

## install_testes.md

Guia completo para criar um projeto de teste baseado em:

* Python
* Pydantic v1
* FastAPI antigo
* Casos de segurança propositalmente vulneráveis

O cenário foi criado para desafiar o Gemini CLI a identificar:

* credenciais expostas;
* regras inseguras de autorização;
* problemas de compatibilidade;
* impacto da migração para Pydantic v2;
* necessidade de atualização do FastAPI.

## Achados_codex.txt

Registro dos resultados obtidos durante as análises com o CODEX.

Inclui observações sobre:

* falhas encontradas;
* riscos de segurança;
* problemas de compatibilidade;
* sugestões de correção;
* validações realizadas;
* comparação entre versões do código.

---

# Pré-requisitos

## Node.js

Verificar instalação:

```bash
node --version
npm --version
```

## Gemini CLI

Instalar:

```bash
npm install -g @google/gemini-cli
```

Verificar instalação:

```bash
gemini --version
```

---

# Como iniciar os testes

Entrar na pasta do projeto:

```bash
cd "Gemini Cli"
```

Seguir o passo a passo descrito em:

```text
install_testes.md
```

O documento cria um projeto Python propositalmente preparado para avaliar capacidades do Gemini CLI.

---

# Exemplos de prompts utilizados

## Revisão de segurança

```text
Analise este projeto por completo e aponte se existem problemas críticos, gargalos ou riscos que eu deveria corrigir imediatamente.
```

## Impacto de alterações

```text
Se eu atualizar o arquivo app/models.py para o padrão do Pydantic v2, quais serão os impactos nos outros arquivos do projeto?
```

## Compatibilidade de dependências

```text
Quero atualizar todo este projeto para usar Pydantic v2. Posso apenas atualizar a versão do Pydantic no requirements.txt e ajustar o código?
```

## Plano de migração

```text
Sugira um plano de migração seguro para este projeto sair de Pydantic v1 para Pydantic v2.
```

---

# O que está sendo avaliado

* Qualidade da análise técnica
* Capacidade de localizar riscos reais
* Entendimento de múltiplos arquivos
* Consulta à documentação oficial
* Consistência das recomendações
* Segurança das sugestões
* Precisão em migrações de dependências

---

# Cuidados durante os testes

* Não utilizar chaves reais.
* Não armazenar credenciais em código.
* Não executar comandos destrutivos sem revisão.
* Revisar patches antes da aplicação.
* Utilizar projetos descartáveis para experimentos.

---

# Links Oficiais

Gemini CLI:

```text
https://github.com/google-gemini/gemini-cli
```

Documentação:

```text
https://github.com/google-gemini/gemini-cli/tree/main/docs
```

Pydantic Migration Guide:

```text
https://docs.pydantic.dev/latest/migration/
```

FastAPI Migration Guide:

```text
https://fastapi.tiangolo.com/how-to/migrate-from-pydantic-v1-to-pydantic-v2/
```

---

# Objetivo deste laboratório

Realizar testes práticos e reproduzíveis para entender até onde o Gemini CLI consegue ajudar em revisões técnicas, análise de código, segurança, documentação e migração de projetos reais.
