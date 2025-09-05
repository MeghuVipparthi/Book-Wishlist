import pytest
from app import create_app
from app.db import db

@pytest.fixture()
def client():
    app = create_app({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite+pysqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    })
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_health(client):
    rv = client.get('/healthz')
    assert rv.status_code == 200

def test_add_book(client):
    rv = client.post('/book', data={"title": "1984", "author": "Orwell"}, follow_redirects=True)
    assert rv.status_code == 200
    assert b"1984" in rv.data
