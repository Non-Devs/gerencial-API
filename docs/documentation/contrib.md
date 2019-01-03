# Contribuindo com o projeto

Caso queira contribuir com o projeto, talvez seja uma boa ideia começar pelo [README](https://github.com/Non-Devs/gerencial-API/) para conhecer melhor sobre nós.
Obrigado por contribuir!Sua ajuda será recebida com muita gratidão!


## Como eu posso contribuir?

### Reportando um Bug

* Esse projeto segue um padrão de _Issues_, o qual está disponível aqui na wiki. Logo, caso encontre um bug, verifique se ele não se encontra em uma das nossas _Issues_. Os bugs devem ser marcados com _tag (label)_ __bug__.

* Se o bug encontrado não consta nas _Isses_, basta abrir uma [Nova _Issue_](https://github.com/Non-Devs/gerencial-API/issues/new).


#3# Adicionando e/ou modificando alguma funcionalidade

* Primeiro verifique que não existe nenhuma [_Issue_](https://github.com/Non-Devs/gerencial-API/issues) a respeito dessa modificação e/ou adição.

* Caso não exista, crie uma [Nova _Issue_](https://github.com/Non-Devs/gerencial-API/issues/new). Dê um título significativo a ela, coloque uma descrição e pelo menos uma _label_.

* As mudanças devem ser submetidas através de [_Pull Requests_](https://github.com/Non-Devs/gerencial-API/compare).

## Padrão de _Commit_

#### Por questões de padronização recomendamos que sigam nosso estilo de _commit_:

* Ele deve conter um título curto e objetivo do que foi feito naquele _commit_;

* Após esse título, deve-se descrever, com um pouco mais de detalhes, todas as atividades executadas.

* Caso esteja trabalhando em com algum associado assine nos seus _commits_ os seus parceiros

__Exemplo:__

    **XXXXX** (Título curto e objetivo)

    XXXXX (Descrição de uma das atividades)

    XXXXX (Descrição de uma das atividades)

    XXXXX (Descrição de uma das atividades)

    Co-authored-by: seu-nome <email@host.com> (Assinatura de parceria)

## Política de _Branchs_

Tendo como meta manter a integralidade e confiabilidade do código do projeto foi proposta a utilização de política de branches.
Essa Política de Branches deverá guiar os desenvolvedores na forma de organização de suas contribuições ao repositório.
__OBS__: A política de _branchs_ foi idealizada para trabalhar em conjunto com a ferramenta do _git flow_, sua documentação e mais informações podem ser acessadas [aqui](https://github.com/nvie/gitflow).

* __master__ - Branch principal do repositório onde será permitida somente a integração de software consolidado e testado. Essa branch será exclusiva para a entrega de Realeases, ou seja, um conjunto maior de funcionalidades que integram o software, aqui estará a versão _**stable**_ do software.

* __develop__ - Branch para integração de novas funcionalidades, onde será permitido a entrega das features desenvolvidas e que estão em um estágio avançado de completude. Será o branch base para o início do desenvolvimento das features e da correção de bugs. Aqui também serão _mergeadas_ as releases.

* __feature/<nome-da-feature>__ - Branch utilizada para o desenvolvimento de novas features do _backlog_. Caso a feature tenha sida proposta por uma _issue_ do repositório e aceita no _backlog_ o nome deverá conter o número da _issue_. 
Ex: feature/1-<nome-da-nova-feature> (Considerando que a feature tenha sido solicitada na _issue_ #1)

* __bugfix/<nome-do-bug>__ - Branch utilizada para corrigir bugs de baixa/média urgência e que não estão presentes na branch __master__. Caso o bug tenha sido reportado por uma _issue_ do repositório o nome deverá conter o número da _issue_. 
 Ex: bugfix/1-<descrição-do-bug> (Considerando que o bug tenha sido reportado na _issue_ #1)

* __hotfix/<nome-do-bug>__ - Branch utilizada para corrigir bugs de alta urgência e que estão presentes na branch __master__. Caso o bug tenha sido reportado por uma _issue_ do repositório o nome deverá conter o número da _issue_. 
 Ex: bugfix/1-<descrição-do-bug> (Considerando que o bug tenha sido reportado na _issue_ #1)

* __release/<versão-da-release>__ - Branch onde será feito os ajustes finais/build antes da entrega de uma versão do produto de software. Constará no nome da branch a versão da release a ser entregue.

* __support/<tema-ou-natureza>__ - Branch onde serão executadas tarefas de suporte relacionadas ao software, como elaboração de documentações, correções de natureza de gerência de configuração e etc.