# Prompt usado no desenvolvimento

Você é um desenvolvedor full stack sênior.

Crie um site completo, com frontend público e backend administrativo, para um professor divulgar e vender cursos.

Pagamentos, aulas, certificados e acesso dos alunos ficarão na Hotmart.

## Tecnologias

Use:

- PHP 8.2+
- MySQL ou MariaDB
- PDO
- HTML, CSS e JavaScript
- Bootstrap 5
- arquitetura MVC simples
- compatibilidade com hospedagem compartilhada e cPanel

## O projeto deve ter

### Site público

- página inicial;
- página sobre o professor;
- página com todos os cursos;
- página individual de cada curso;
- cursos em destaque;
- contatos e redes sociais;
- botões direcionando para a Hotmart;
- layout responsivo;
- SEO básico com nota mínima de 95.

### Painel administrativo

- login e logout;
- dashboard;
- cadastro, edição, ativação, desativação e exclusão de cursos;
- upload de imagem;
- título, resumo, descrição, categoria, carga horária e link da Hotmart;
- edição do nome, resumo, biografia e foto do professor;
- configurações básicas do site.

## Tema

Implemente:

- modo claro;
- modo escuro;
- modo automático conforme o sistema;
- seletor de tema no site e no painel;
- preferência salva em `localStorage`.

## Segurança

Implemente:

- `password_hash` e `password_verify`;
- PDO com prepared statements;
- proteção contra SQL Injection;
- proteção contra XSS;
- proteção CSRF;
- validação no backend;
- upload seguro de JPG, PNG e WebP;
- credenciais em `.env`;
- proteção das rotas administrativas.

## Loop Engineering

Trabalhe em ciclos pequenos:

1. Analise os arquivos existentes.
2. Identifique a próxima tarefa.
3. Planeje uma alteração pequena.
4. Implemente.
5. Teste.
6. Revise.
7. Corrija.
8. Atualize `PROGRESSO.md`.
9. Repita.

Não tente construir tudo de uma vez.

Não marque uma tarefa como concluída apenas porque o código foi escrito. Ela só estará concluída depois de implementada, testada e revisada.

## Trava de erros

Para o mesmo erro, faça no máximo duas tentativas de correção.

Se o erro continuar após duas tentativas:

- pare nessa funcionalidade;
- não faça uma terceira tentativa;
- não aplique gambiarra;
- fale comigo informando:
  - erro;
  - causa provável;
  - tentativas realizadas;
  - arquivos envolvidos;
  - opções para continuar;
  - recomendação.

Peça minha orientação antes de:

- apagar arquivos;
- trocar a arquitetura;
- trocar banco ou linguagem;
- instalar dependências importantes;
- fazer alteração destrutiva no banco;
- desativar segurança;
- abandonar requisitos;
- reconstruir o projeto do zero.

## Entregáveis

Ao final, entregue:

- aplicação completa;
- script SQL;
- `.env.example`;
- sistema para criar o primeiro administrador;
- `README.md`;
- `PROGRESSO.md`;
- instruções de instalação e publicação;
- checklist de testes;
- lista de limitações.

## Design e experiência visual

O layout deve ser deslumbrante, moderno, elegante e profissional, com aparência de produto premium.

Não entregue uma interface genérica de Bootstrap, com visual de sistema administrativo antigo.

Crie uma identidade visual consistente para o site público e para o painel administrativo.

O design deve ter:

- excelente hierarquia visual;
- tipografia moderna e bem combinada;
- espaçamentos generosos;
- paleta de cores sofisticada;
- cards elegantes;
- imagens bem valorizadas;
- botões com boa presença visual;
- seções com ritmo e variedade;
- ícones coerentes;
- microinterações suaves;
- sombras discretas;
- bordas e cantos bem trabalhados;
- modo claro e escuro igualmente bonitos;
- ótima experiência em celular, tablet e desktop.

A página inicial deve causar uma ótima primeira impressão e transmitir autoridade, confiança e qualidade.

O painel administrativo deve ser bonito, organizado e agradável de usar, sem parecer um template cru.

Use Bootstrap 5 apenas como base técnica. Personalize o CSS, os componentes, as cores, a tipografia, os formulários, as tabelas, os menus e os cards.

Evite:

- aparência padrão do Bootstrap;
- excesso de caixas iguais;
- cores sem personalidade;
- gradientes exagerados;
- animações chamativas;
- textos apertados;
- páginas visualmente vazias;
- visual corporativo ultrapassado;
- aparência de projeto escolar ou protótipo inacabado.

Antes de considerar o layout concluído, revise:

- alinhamento;
- espaçamento;
- contraste;
- consistência;
- responsividade;
- legibilidade;
- equilíbrio visual;
- acabamento geral.

Não priorize apenas o funcionamento. O resultado final deve ser tecnicamente sólido e visualmente marcante.

## Início

Comece inspecionando a pasta atual.

Se estiver vazia, crie a estrutura inicial.

Se já existir código, preserve o que estiver correto.

Depois da inspeção, implemente o primeiro ciclo. Não pare apenas no planejamento.

Sirva na porta `5010`.
