from flask import Flask, Blueprint
from database import init_database, init_migrations
from components.income.resources import api_incomes
from os import environ


api = Blueprint('api', __name__, url_prefix='/v1')
api.register_blueprint(api_incomes)


def create_app(app_config=environ.get('FILE_CONFIG')):
    app = Flask(__name__)
    app.config.from_object(app_config)
    init_database(app)
    init_migrations(app)

    with app.app_context():
        app.register_blueprint(api)
        return app
