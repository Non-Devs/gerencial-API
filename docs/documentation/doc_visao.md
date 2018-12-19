# 1. Introdução
O presente documento tem por finalidade descrever, em partes, o desenvolvimento do projeto e apresentar a visão deste de forma a obter um entendimento comum, além de expor toda tecnologia e estudo aplicado para construção do sistema de gerenciamento escolar que será entregue pela organização *Non-Devs*. Será explicitado os aspectos deste processo, seus pontos vitais e as técnicas utilizadas durante a execução, para então, na melhor forma, ir de encontro a uma visão bem definida do produto de software a ser construído, de forma simples e satisfatória.

### 1.1	Propósito
Este documento busca encontrar e explicitar para todas as partes envolvidas durante o desenvolvimento do sistema supracitado uma visão de comum acordo, apresentando então ambas partes, além do sistema e todas as demais informações relacionadas ou correlacionadas que venham a fazer parte de quaisquer dos processos envolvidos.

Tem por objetivo definir e levantar partes dos requisitos, do escopo inicial do projeto, selecionando pontos principais que deverão ser abordados durante as fases iniciais do desenvolvimento. Buscará a definição das necessidades dos usuários, do projeto e da equipe, especificando temas estratégicos e pontuando, onde necessário, as restrições e dificuldades. 

### 1.2	Escopo
Estão associados a este documento, primeiramente, o sistema back-end do projeto **gerencial**, assim como todo suporte subjacente para os usuários do mesmo e as demais funcionalidades do sistema. 


### 1.3	Referências
Para a elaboração do documento supracitado foi levado em consideração o acervo descrito sobre o tema pela empresa *IBM*, na subdivisão da *IBM Knowledge Center*, que apresenta de forma simples e estruturada os passos, tópicos e temas a serem seguidos na elaboração do mesmo, assim como guia para equipes que não tenham contato com este artefato. O material pode ser acessado via navegador web no seguinte link:

[IBM - Documento de Visão](https://www.ibm.com/support/knowledgecenter/pt-br/SSYMRC_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html).

### 1.4	Visão geral
Almejando a representação de forma simples o documento será descrito em estrutura de tópicos, subdividos em 10 categorias que vão de posicionamento do software e contexto inserido até requisitos de produto e documentação, quaisquer demais informações relacionadas estarão inseridade em _n_ apêndices ao final do documento (caso julgado necessário).

# 2. Posicionando

### 2.1 Oportunidade de Negócios
O **gerencial** é um sistema voltado para professores de reforço autônomos com o intuito de facilitar o gerenciamento financeiro, dos alunos e conteúdo ministrado.

### 2.2 Instrução do Problema


|||
| ------------- |:-------------:|
| **O problema é** | Dificuldade na gerência de alunos e montagem de uma grade horária além da definição de conteúdo das aulas.|
| **Quem afeta** | Professores autônomos. |
| **Isso causa**| Dificuldade na gerência de pessoal e financeira, limitando as capacidades de atuação dos professores.|
| **Uma solução seria** | Um sistema online que permita os professores automatizar todo esse processo.|

### 2.3 Instrução de Posição do Produto

|||
| ------------- |:-------------:|
| **Para** | Professores autônomos e profissionais da area de educação |
| **Que**   | necessitam de uma plataforma de gerência estudantil e um maior controle de forma automatizada |
| **O**| gerencial |
|**É uma**| ferramenta que facilita o controle de alunos e agenda do profissional de educação.|
| **Diferente de**     | Outras aplicações que são voltadas para escolas e não professores autônomos.|

# 3. Descrições da Parte Interessada e do Usuário

### 3.1	Resumo da Parte Interessada

| Nome        | Descrição    | Responsabilidade |
| ------------- |:-------------:| :-----:|
| Equipe     | Graduandos de Engenharia pela Universidade de Brasília e professores  | Desenvolver e manter o software, preparar aulas e tirar dúvidas dos usuários |
| Clientes      | Profissionais da area de educação | Utilizar o software para fazer o gerenciamento |


### 3.2	Resumo do Usuário

|Nome     |Descrição | Parte Interessada  |
| ------------- |:-------------:|:-----:|
| Profissionais da area de educação   | Equipe que trabalhará com a plataforma | Usuário|
| Equipe de desenvolvimento | Equipe que fará a manutenção da aplicação | Usuário |

### 3.3	Ambiente do Usuário

A proposta é, a princípio, ser uma aplicação web leve que possa ser acessada em navegadores de Internet. A plataforma deve conter opções intuitivas que não trarão dificuldades para o usuário.

### 3.4	Perfis das Partes Interessadas

#### 3.4.1 Usuários

|||
| ------------- |:-------------:|
| **Representantes**| Profissionais da area de educação |
| **Descrição** | Usuários que irão utilizar os serviços da plataforma |
|**Tipo**| Usuário informal |
| **Responsabilidade** | Utilizar a plataforma para fazer a gerência dos seus alunos |
| **Critérios de sucesso** | Utilizar o sistema ao invés de fazer o gerenciamento no papel|
| **Envolvimento** |Alto|
| **Comentários** | -|


### 3.5	Perfis do Usuário

#### 3.5.1 Profissionais da area de educação

|||
| ------------- |:-------------:|
| **Representantes**| Usuários |
| **Descrição** | Profissionais autônomos que buscam automatizar a gerência de alunos |
|**Tipo**| Usuário avançado |
| **Responsabilidade** | Cadastrar alunos e aulas |
| **Critérios de sucesso** | Utilizar o sistema |
| **Envolvimento** |Alto|
| **Comentários** | -|

### 3.6	Principais Necessidades da Parte Interessada ou do Usuário

|Necessidade|Interesses|Solução atual|Solução proposta|Prioridade|
|-|---|---|---|---|
|Montar uma grade horária semanal|Facilitar a visualização e montagem da grade horária|Feita manualmente, sem controle algum|Montagem automática e online|Alta|
|Determinar o conteúdo por aluno|Permitir o professor determinar e saber qual o conteúdo será dado em determinado período|Não há. O conteúdo é ministrado de acordo com a evolução do aluno|Permitir que o professor grave previamente no sistema a matéria (provavelmente por hora aula)|Média|
|Cálculo de valores (mensalidade?)|Determinar o valor total que o professor ganha e também por aluno|Não há. O cálculo é feito manualmente.|Automatizar o cálculo, fazendo o sistema exigir a inserção do valor da aula (determinar se por mês ou hora/aula)|Média|


### 3.7	Alternativas e Concorrência

Sponte, um bem completo. E também o Sophia. O diferencial do nosso projeto é ser mais voltado para professores de reforço/autônomos.

# 4. Visão Geral do Produto

### 4.1	Perspectiva do Produto

O **gerencial** é uma plataforma independente que fornece a possibilidade de profissionais autônomos da area de educação fazerem a gerência de seus alunos, tendo acesso às informações necessárias sobre os mesmos, grade horária e financeiro. 


### 4.2	Resumo das Capacidades

|Benefícios para o cliente|Recursos de|
|-|-|
|Consulta rápida aos alunos|Banco de dados|
|Visualização da parte financeira|Funcionalidade do sistema|


### 4.3	Suposições e Dependências

- Acesso à Internet
- Máquina (_Desktops_, _Notebooks_ e etc.) com navegador de Internet.
- Dispositivo móvel com navegador de Internet.
- Cadastro no sistema.

# 5. Recursos do Produto
### 5.1 Cadastro
Para a utlização da plataforma é necessário efetuar o login, fazendo um cadastro, no qual ficará salvo seus progressos e exercícios.

### 5.2 Grade horária
Haverá uma grade horária, montada automaticamente de acordo com o horário das aulas (informadas previamente pelos professores).

# 6. Restrições

O sistema terá uma interface intuitiva de fácil usabilidade para que todos os tipos de usuário possam navegar sem dificuldade. A aplicação será desenvolvida para navegadores de Internet de qualquer dispositivo, por isso, será necessário ter conexão de Internet. Será desenvolvida no ambiente Django com  a linguagem Python.

# 7. Faixas de Qualidade

Para maior eficiência a aplicação será exclusivamente web, assim há maior facilidade para acessar de qualquer dispositivo com conexão. 
