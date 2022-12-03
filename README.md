# Citecontroller
[![Build](https://github.com/neoh1/ohtugroup2/actions/workflows/main.yaml/badge.svg)](https://github.com/neoh1/ohtugroup2/actions/workflows/main.yaml)
[![codecov](https://codecov.io/gh/neoh1/ohtugroup2/branch/main/graph/badge.svg?token=E0SILZYIFV)](https://codecov.io/gh/neoh1/ohtugroup2)
Ohjelmistotuotanto Miniprojekti  
Etäryhmä 2

Deployed at: https://citecontroller.herokuapp.com/


## Backlogit


Product- sekä sprint backlogit samassa Google Docs tiedostossa: [backlogit](https://docs.google.com/spreadsheets/d/1rT_qqeMHwjVh0V5nsZWkXJ-ITP9PoduPhPwhL3oXlmU/)


## Definition of done
- The acceptance criteria for the user story have been met
- The code has been reviewed
- New functions pass tests on the development team's own computers and GitHub Actions
- New functions have been integrated into the release version of the software


## Deployment on Heroku
Using moneymeets poetry buildback, so no requirements.txt need to be implemented.

Deployed at: https://citecontroller.herokuapp.com/

`heroku buildpacks:clear -a citecontroller`

`heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git -a citecontroller`

`heroku buildpacks:add heroku/python -a citecontroller`

`heroku addons:create heroku-postgresql -a citecontroller`

`heroku config:set PYTHON_RUNTIME_VERSION=3.9.15 -a citecontroller`

`heroku config:set POETRY_VERSION=1.2.2 -a citecontroller`

## References
[OhTu example app](https://github.com/ohjelmistotuotanto-hy/todo-web
)

