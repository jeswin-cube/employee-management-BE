# README.md

### Install Poetry

```
$ curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.4.0 python3.8 -
```

### Setup project

```
$ git clone https://github.com/cube-fi/django-boilerplate.git

$ poetry env use python3.8
$ poetry install --no-root

$ source .venv/bin/activate
```

(Optional) Run the following command to install dependencies from an existing requirements file.

```
$ poetry add $(cat requirements/base.txt)
$ poetry add --dev $(cat requirements/dev.txt)
```

### Set up pre-commit hook

```
$ pre-commit install
```

### Run migrations

```
$ python manage.py migrate
```

### Run the development server

```
$ python manage.py runserver
```

### Run cron jobs locally

Install Redis Server locally and then run the following commands in three different shells with all the
environment variables exported.

```
$ redis-server
$ celery -A config.celery:app worker -l INFO
$ celery -A config.celery:app beat --loglevel=INFO
```