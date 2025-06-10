import pytest
from app import app, db
from models.user import User
from models.bug import Bug

@pytest.fixture
def admin_client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            admin = User(username="admin", email="admin@example.com", is_admin=True)
            admin.set_password("admin123")
            db.session.add(admin)
            db.session.commit()
        yield client

def test_bug_crud(admin_client):
    # TODO: Login + test POST/GET/PUT/DELETE
    pass  # Placeholder for full CRUD test coverage
