import pytest
from platform import PARAMS, create_app

class TestConfig:
    SECRET_KEY =  PARAMS['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

@pytest.fixture()
def app():
    app = create_app(config=TestConfig)
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()