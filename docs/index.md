# gerencial-API
[![Coverage Status](https://coveralls.io/repos/github/Non-Devs/gerencial-API/badge.svg?branch=develop)](https://coveralls.io/github/Non-Devs/gerencial-API?branch=develop)
[![Build Status](https://travis-ci.org/Non-Devs/gerencial-API.svg?branch=master)](https://travis-ci.org/Non-Devs/gerencial-API)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Repositório da API do sistema de Gerenciamento de Alunos. Check out the project's [documentation](http://Non-Devs.github.io/gerencial-API/).

## **Sistema de gerenciamento escolar**	

(Página em construção)

Bem vindo à wiki! Esse é o local onde você encontra a documentação do projeto, tutoriais e algumas outras coisas. Caso queira contribuir para o projeto sinta-se à vontade. 

O índice geral encontra-se na lateral.

<!-- 
# Pré-requisitos

- [Docker](https://docs.docker.com/docker-for-mac/install/)  
- [Travis CLI](http://blog.travis-ci.com/2013-01-14-new-client/)
- [Heroku Toolbelt](https://toolbelt.heroku.com/)


# Inicializando o 

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```


# Continuous Deployment

Deployment automated via Travis. When builds pass on the master or qa branch, Travis will deploy that branch to Heroku. Enable this by:

Creating the production sever:

```
heroku create API-prod --remote prod && \
    heroku addons:create newrelic:wayne --app API-prod && \
    heroku addons:create heroku-postgresql:hobby-dev --app API-prod && \
    heroku config:set DJANGO_SECRET=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="API-prod" \
        --app API-prod
```

Creating the qa sever:

```
heroku create `API-qa --remote qa && \
    heroku addons:create newrelic:wayne && \
    heroku addons:create heroku-postgresql:hobby-dev && \
    heroku config:set DJANGO_SECRET=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="API-qa" \
```

Securely add your heroku credentials to travis so it can automatically deploy your changes.

```bash
travis encrypt HEROKU_AUTH_TOKEN="$(heroku auth:token)" --add
```

Commit your changes and push to master and qa to trigger your first deploys:

```bash
git commit -m "ci(travis): added heroku credentials" && \
git push origin master && \
git checkout -b qa && \
git push -u origin qa
```
You're ready to continuously ship! ✨ 💅 🛳
-->