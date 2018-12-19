Situação problema: Dificuldade na montagem de uma grade horária e definição de conteúdo para os alunos.
**Objetivo**

A ideia do projeto é montar um sistema  voltado para professores de reforço autônomos com o intuito de facilitar o gerenciamento financeiro, dos alunos e conteúdo ministrado.

**Tecnologias:**

Para o back-end será usado o framework **Django** como uma API REST. A princípio seria utilizado o framework Laravel, porém pelo fato de pouca documentação de uso como API a ideia foi descartada.

**Plataformas:**

A princípio o projeto será feito para ser utilizado apenas em navegadores (chrome, firefox...) porém caso feita no formato de api no futuro poderá ser feito aplicativo mobile.
**Principais necessidades do usuário:**

|Necessidade|Interesses|Solução atual|Solução proposta|Prioridade|
|-|---|---|---|---|
|Montar uma grade horária semanal|Facilitar a visualização e montagem da grade horária|Feita manualmente, sem controle algum|Montagem automática e online|Alta|
|Determinar o conteúdo por aluno|Permitir o professor determinar e saber qual o conteúdo será dado em determinado período|Não há. O conteúdo é ministrado de acordo com a evolução do aluno|Permitir que o professor grave previamente no sistema a matéria (provavelmente por hora aula)|Média|
|Cálculo de valores (mensalidade?)|Determinar o valor total que o professor ganha e também por aluno|Não há. O cálculo é feito manualmente.|Automatizar o cálculo, fazendo o sistema exigir a inserção do valor da aula (determinar se por mês ou hora/aula)|Média|

**Capacidades:**

|Benefícios para o cliente|Recursos de|
|-|-|
|Consulta rápida aos alunos|Banco de dados|
|Visualização da parte financeira|Funcionalidade do sistema|

(Ainda em construção)

**Recursos do sistema:**

Ver [Requisitos](https://github.com/Non-Devs/gerencial-API/wiki/Requisitos)


**Alternativas e concorrentes:**

Sponte, um bem completo. E também o Sophia. O diferencial do nosso projeto é ser mais voltado para professores de reforço/autônomos.