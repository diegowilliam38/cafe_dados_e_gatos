# Como estudar e testar OpenJarvis

Curso prático do canal Café com Dados & Gatos para estudar, instalar e testar o OpenJarvis com foco em documentação oficial, teste real e aprendizado progressivo.

Este repositório mantém os arquivos Markdown de referência técnica do curso.

O material editorial do curso, incluindo apostilas, roteiros de produção, exercícios revisados e PDFs finais para anexar no YouTube, fica no Google Drive da conta Café com Dados & Gatos.

## Objetivo do curso

Entender o OpenJarvis como projeto de IA pessoal local, começando pela proposta e arquitetura, avançando para os testes práticos nas interfaces principais.

O curso trabalha com foco educacional, técnico e prático:

- o que o OpenJarvis propõe;
- o que a documentação oficial mostra;
- como preparar o ambiente;
- como testar na prática;
- como validar se funcionou;
- como registrar limites, erros e ajustes encontrados.

## Estrutura oficial do curso

```text
Aula 1 - Como entender, preparar e testar o OpenJarvis pela CLI
Aula 2 - Como testar o OpenJarvis no Browser App
Aula 3 - Como testar o OpenJarvis no Desktop App
```

Esta estrutura de três aulas é específica para o Curso OpenJarvis.

Outros cursos do canal podem ter estruturas diferentes.

## Aula 1 - Como entender, preparar e testar o OpenJarvis pela CLI

Esta é a aula-base do curso.

Conteúdo:

- o que é OpenJarvis;
- proposta do projeto;
- Stanford Scaling Intelligence Lab;
- arquitetura geral;
- cinco pilares: Intelligence, Engine, Agents, Tools & Memory e Learning;
- modelos locais;
- Ollama;
- requisitos de hardware;
- por que máquinas com GPU RTX são mais indicadas;
- preparação do ambiente;
- primeiro teste pela CLI no Linux.

Resultado esperado:

- preparar o ambiente;
- iniciar o OpenJarvis pela CLI;
- executar um teste básico;
- identificar se houve erro de ambiente, modelo ou dependência.

## Aula 2 - Como testar o OpenJarvis no Browser App

Conteúdo:

- o que é o Browser App;
- como iniciar a interface web;
- como acessar pelo navegador;
- como realizar testes básicos;
- como validar se o backend está funcionando;
- como registrar erros e ajustes encontrados.

Resultado esperado:

- iniciar o Browser App;
- acessar a interface pelo navegador;
- executar um teste básico;
- confirmar se a interface está conectada ao backend local.

## Aula 3 - Como testar o OpenJarvis no Desktop App

Conteúdo:

- o que é o Desktop App;
- como preparar o aplicativo;
- como conectar ao backend local;
- como realizar testes práticos;
- como validar se a comunicação está funcionando;
- quais limitações observar durante o teste.

Resultado esperado:

- abrir o Desktop App;
- conectar ao backend local;
- realizar um teste básico;
- identificar se o problema está no app, no backend, no modelo ou no ambiente.

## Organização do GitHub

```text
CURSOS/OPENJARVIS/
├── README.md
├── PLANO_DO_CURSO.md
├── REFERENCIAS_OFICIAIS.md
└── materiais-tecnicos/
    ├── comandos.md
    ├── links-oficiais.md
    └── notas-de-teste.md
```

## Organização do Google Drive

```text
OpenJarvis/
├── Aula 1 - CLI
├── Aula 2 Browser App
├── Aula 3 Desktop App
└── PDFs Finais
```

Link da pasta principal:

https://drive.google.com/drive/folders/1UQlQ7XTAvK4JlUhzFUWEw6SbxAvltJRT

Uso do Drive:

- produzir apostilas;
- produzir roteiros de gravação;
- revisar exercícios;
- guardar materiais editoriais;
- gerar PDFs finais;
- organizar anexos do Curso do YouTube.

## Como usar este material

Use o GitHub como base de referência técnica e rastreio do curso.

Use o Google Drive como área de produção dos materiais finais.

## PDFs finais

Os PDFs serão produzidos por último, depois da revisão dos materiais.

Arquivos previstos:

```text
OpenJarvis_Aula_01_CLI.pdf
OpenJarvis_Aula_02_Browser_App.pdf
OpenJarvis_Aula_03_Desktop_App.pdf
```

Cada PDF deve acompanhar a aula correspondente no recurso Curso do YouTube.

## Fontes oficiais

- Paper no arXiv: https://arxiv.org/abs/2605.17172
- Site oficial: https://open-jarvis.github.io/OpenJarvis/
- Pesquisa: https://open-jarvis.github.io/OpenJarvis/#research
- Repositório oficial: https://github.com/open-jarvis/OpenJarvis
- Blog do Stanford Scaling Intelligence Lab: https://scalingintelligence.stanford.edu/blogs/openjarvis/
- Cursos no YouTube: https://support.google.com/youtube/answer/15128409?hl=pt-BR

## Observação

Este curso será ampliado conforme os testes forem avançando. A estrutura inicial tem três aulas para manter o curso direto, prático e fácil de publicar.
