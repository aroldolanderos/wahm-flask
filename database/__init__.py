from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def init_database(app: Flask):
    db.init_app(app)


def init_migrations(app: Flask):
    migrate.init_app(app, db)
