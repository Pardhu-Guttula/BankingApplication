# Test cases for Role-Based Access Control

import pytest
from app import create_app, db
from app.models import User, Role

@pytest.fixture(scope='module')
def new_user():
    user = User(username='testuser', email='testuser@example.com')
    user.set_password('testpassword')
    return user

@pytest.fixture(scope='module')
def init_db():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()

def test_create_user(init_db, new_user):
    init_db.session.add(new_user)
    init_db.session.commit()
    assert new_user in init_db.session

def test_user_role(init_db, new_user):
    role = Role(name='User')
    new_user.roles.append(role)
    init_db.session.commit()
    assert role in new_user.roles
