# gerencial-API
[![codecov](https://codecov.io/gh/Non-Devs/gerencial-API/branch/master/graph/badge.svg)](https://codecov.io/gh/Non-Devs/gerencial-API)
[![Build Status](https://travis-ci.org/Non-Devs/gerencial-API.svg?branch=master)](https://travis-ci.org/Non-Devs/gerencial-API)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Repositório da [API](https://api-prod-gerencial.herokuapp.com/) do sistema de Gerenciamento de Alunos. 
Caso esteja procurando a documentação, [dê uma olhada aqui](http://Non-Devs.github.io/gerencial-API/).
Caso queira contribuir para o projeto, por favor leia o arquivo de contribuição antes. Toda ajuda será bem vinda!

# Pré requisitos

- [Docker compose](https://docs.docker.com/compose/install//)

# Desenvolvimento local

Inicie o servidor local para o desenvolvimento:
```bash
make up
```
Para construir os containeirs:
```bash
make build
```
Para rodar os testes e ver a cobertura:
```bash
make test-all
```
