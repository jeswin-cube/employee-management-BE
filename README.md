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

### Set up pre-commit hook

```
$ pre-commit install
```

### Create an env file
Create a postgreSQL database in your local postgres and replace the RDS values
```
# Django
export X_ORIGIN_SECRET=<X_ORIGIN_SECRET>
export DJANGO_SECRET_KEY=<DJANGO_SECRET_KEY>
export DJANGO_DEBUG=True
export DATA_SECRET=<DATA_SECRET>

#RDS
export RDS_PORT=5432
export RDS_DB_NAME=<DB Name>
export RDS_USERNAME=<RDS_USERNAME>
export RDS_PASSWORD=<password>
export RDS_HOSTNAME=127.0.0.1
```

### Source the env file

``` source <env_filename>.env```

### Run migrations

```
$ python manage.py migrate
```

### Run the development server

```
$ python manage.py runserver
```