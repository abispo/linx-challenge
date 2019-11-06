# Linx Challenge
Repositório com o código do desafio Linx.

[![Build Status](https://travis-ci.org/abispo/linx-challenge.svg?branch=master)](https://travis-ci.org/abispo/linx-challenge)
[![codecov](https://codecov.io/gh/abispo/linx-challenge/branch/master/graph/badge.svg)](https://codecov.io/gh/abispo/linx-challenge)
![GitHub Pipenv locked Python version (branch)](https://img.shields.io/github/pipenv/locked/python-version/abispo/linx-challenge/master)

## Baixando o projeto
Execute os comandos abaixo no terminal:
```bash
git clone https://github.com/abispo/linx-challenge.git
cd linx-challenge
```

Crie o arquivo `.env` no diretório raiz do projeto com o seguinte conteúdo:
```
OPENWEATHER_API_KEY=<API_KEY>
OPENWEATHER_API_URL=http://api.openweathermap.org/data/2.5/forecast
DATABASE_URL=postgresql://linx:linx@postgresql/linx_challenge
LINX_CHALLENGE_TESTING=False
```

O projeto consiste de uma API que salva o resultado de um POST em uma API de previsão do tempo no banco de dados, depois mostra esses resultados. Depois do projeto instalado e executando, para fazer uma requisição você pode digitar no terminal:
```bash
curl -X POST http://127.0.0.1:8000/city/London
curl -X GET http://127.0.0.1:8000/city/London?limit=3
```

Ou acessar a documentação da API em `http://127.0.0.1:8000/docs` ou `http://127.0.0.1:8000/redoc`.

## Executando o projeto usando Docker

> **Requisitos:**
> - Docker 19.03.4
> - docker-compose 1.24.1

Execute o comando abaixo no terminal:
```bash
docker-compose up -d
```

### Executando os testes pelo docker
Execute o comando abaixo no terminal:
```bash
docker exec -e LINX_CHALLENGE_TESTING=True -it linx_challenge pipenv run pytest --cov=app tests/ --disable-warnings
```

## Executando o projeto usando Python com pipenv
> **Requisitos:**
> - Python 3.6
> - pip 9.0.1
> - pipenv 2018.11.26

Crie o arquivo `.env` no diretório raiz do projeto com o seguinte conteúdo:
```
OPENWEATHER_API_KEY=<API_KEY>
OPENWEATHER_API_URL=http://api.openweathermap.org/data/2.5/forecast
DATABASE_URL=postgresql://linx:linx@127.0.0.1/linx_challenge
LINX_CHALLENGE_TESTING=False
```

Execute os comandos abaixo no terminal:
```bash
pipenv install --dev
pipenv run uvicorn app.main:app --reload
```

### Executando os testes pelo pipenv
Execute o comando abaixo no terminal:
```bash
LINX_CHALLENGE_TESTING=True pipenv run pytest --cov=app tests/ --disable-warnings
```

### Principais libs
> - FastAPI
> - encode/databases
> - encode/orm
> - pytest
> - python-decouple

Escolhi a FastAPI por ela usar a sintaxe async/await do Python 3.4+, ou seja, pois segue o modelo do Python para desenvolvimento de programas que usam assincronia. E também por ser um framework Flask-like. O projeto poderia ter sido desenvolvido inteiramente em Flask, mas isso foi mais um gosto pessoal. Utilizei também o pytest para rodar os testes da aplicação. O python-decouple foi utilizado para ler variáveis de ambiente necessárias ao sistema.