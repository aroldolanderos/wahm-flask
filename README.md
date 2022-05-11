# What And How Much ? (WAHM)
Project to keep records of income and expenditure It is an example project with
the purpose of learning how to use the different features of the flask framework

> Previously you should create a virtual environment for python 3, this example
> more precisely uses version 3.8

## Install dependencies
``` python
$ pip install -r requirements.txt
```

## Install postgres using docker
Create volume
``` sh
$ docker volume create postgres_db_data
```

Create container from alpine postgres image
``` sh
$ docker run -d  --name postgres_local -e POSTGRES_PASSWORD=1234 -p 5432:5432 -v postgres_db_data:/var/lib/postgresql/data postgres:alpine
```

## Set enviroment variables
Duplicate example .env files
``` sh
$ cp .env.example .env
$ cp .flaskenv.example .flaskenv
```

Complete the necessary values for each file, mainly for the database
``` env
SQLALCHEMY_DATABASE_URI_DEV='postgresql://postgres:1234@localhost:5432/<your_db_name>'
```




## Migrations

Create migration repository, this will add a migrations folder 
to your application
``` python
$ flask db init
```

You can then generate an initial migration:
``` python
$ flask db migrate -m "Initial migration."
```


The migration script needs to be reviewed and edited, as Alembic currently does 
not detect every change you make to your models. In particular, Alembic is 
currently unable to detect table name changes, column name changes, or 
anonymously named constraints. A detailed summary of limitations can be found 
in the [Alembic autogenerate documentation](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect). Once finalized, the migration script 
also needs to be added to version control.

Then you can apply the migration to the database:
``` python
$ flask db upgrade
```

Then each time the database models change repeat the migrate and upgrade commands.

To sync the database in another system just refresh the migrations folder from 
source control and run the upgrade command.

To see all the commands that are available run this command:
``` python
$ flask db --help
```

All documentation of Flask migrations -> [here](https://flask-migrate.readthedocs.io/en/latest/)

## Run app on Local
``` python
$ flask run
```