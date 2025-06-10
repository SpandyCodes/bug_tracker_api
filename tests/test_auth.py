import pytest
from app import app, db
from models.user import User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            user = User(username="test", email="test@example.com")
            user.set_password("test123")
            db.session.add(user)
            db.session.commit()
        yield client

def test_login(client):
    res = client.post('/login', data={"email": "test@example.com", "password": "test123"}, follow_redirects=True)
    assert b"Welcome" in res.data

def test_register(client):
    res = client.post('/register', data={"username": "new", "email": "new@example.com", "password": "newpass"}, follow_redirects=True)
    assert b"login" in res.data.lower()
