import pytest
from cleanPony.db.models import db
from cleanPony.rest.app import app as application
from pony.orm import set_sql_debug


def pytest_sessionstart(session):
    db.bind(provider='sqlite', filename=':memory:')
    db.generate_mapping(create_tables=True)
    set_sql_debug(True)


@pytest.fixture
def app():
    application.debug = True
    yield application


@pytest.fixture
def client(app):
    return app.test_client()
