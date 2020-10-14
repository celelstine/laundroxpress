[![CI Actions Status](https://github.com/celelstine/laundroxpress/workflows/LaundroXpress%20CI%20workflow/badge.svg)](https://github.com/{celelstine}/laundroxpress/actions)

[![codecov](https://codecov.io/gh/celelstine/laundroxpress/branch/master/graph/badge.svg?token=EXH3IH4V7L)](https://codecov.io/gh/celelstine)

# laundroxpress
web application for laundroxpress


## How projects was setup

### Backend setup
ref: https://docs.docker.com/compose/django/

- create a dockerfile for the django project
- create a docker stack with docker compose with includes 2 services: django project for playing and a postgres db
- create a django project with docker compose `docker-compose run web django-admin startproject laundroxpress-app .`
- grant permission to current user or a user of your choice `sudo chown -R $USER:$USER .`
- update the database settings for the django app
- rename project module to `config` and rename every reference


### Frontend setup


## How to setup this project
These project was built to run on docker so the setup below would not be suitable for non-docker environment

To start the project simply run `make up` then access the project at `localhost:8000`
