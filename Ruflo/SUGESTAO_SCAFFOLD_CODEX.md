# Sugestão para Começar Projetos com Codex

Antes de iniciar um projeto, você pode pedir para o Codex criar uma estrutura inicial organizada. Isso ajuda a começar com pastas, testes, documentação e comandos claros, sem precisar usar uma estrutura pesada como Ruflo/Claude Flow quando o projeto for simples ou médio.

## Pedido Simples

```text
Crie a estrutura inicial organizada para um projeto [linguagem/framework] chamado [nome do projeto].
Inclua pastas para código, testes, documentação, configuração e scripts quando fizer sentido.
Inclua README.md, arquivo de dependências, .gitignore e um arquivo AGENTS.md com regras de desenvolvimento.
Não implemente a funcionalidade ainda.
```

## Pedido com Diretriz Inicial

```text
Quero criar um projeto chamado [nome].
A ideia é: [explique em poucas frases o que o software deve fazer].
Antes de codar, monte um scaffold profissional simples, com estrutura de pastas, testes preparados, README com comandos e regras básicas no AGENTS.md.
Mantenha a estrutura leve e fácil de entender.
```

## Exemplo para Python

```text
Crie a estrutura inicial organizada para um projeto Python chamado Mini Tarefas.
A ideia é um app simples de tarefas que roda localmente pelo terminal e salva dados em JSON.
Antes de implementar, crie um scaffold profissional simples com src, tests, README.md, requirements.txt, .gitignore e AGENTS.md.
Documente como rodar e testar.
```

## Estrutura Leve Sugerida

```text
meu-projeto/
  src/
  tests/
  docs/
  scripts/
  config/
  README.md
  requirements.txt
  .gitignore
  AGENTS.md
```

Nem todo projeto precisa de todas essas pastas. O ideal é adaptar ao tamanho e objetivo do software.

## O Que Ajuda Informar Antes

Quanto mais clara for a diretriz inicial, melhor fica o scaffold. Informações úteis:

- nome do projeto
- linguagem ou framework desejado
- se será terminal, web, API, desktop ou biblioteca
- como os dados serão salvos
- se precisa de testes desde o começo
- se deve ser simples ou preparado para crescer
- comandos esperados para rodar, testar e desenvolver
- restrições importantes, como não usar banco de dados ou evitar dependências externas

## Por Que Isso Ajuda

Com uma diretriz básica, o Codex consegue montar uma estrutura mais adequada ao projeto real. Em vez de criar pastas genéricas demais, ele pode escolher uma organização compatível com o tipo de software, o nível de complexidade e os próximos passos de desenvolvimento.

Para projetos pequenos e médios, esse scaffold profissional simples costuma trazer os principais benefícios de organização sem o peso de uma estrutura multiagente como Ruflo.
