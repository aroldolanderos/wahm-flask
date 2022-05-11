import pytest
from components import create_app


@pytest.fixture()
def app():
    app = create_app('config.Testing')
    # other setup can go here
    yield app
    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()
