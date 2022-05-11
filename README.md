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