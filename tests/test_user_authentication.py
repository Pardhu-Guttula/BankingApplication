import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def client():
    app = create_app({'TESTING': True})

    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()


def test_register_user(client):
    response = client.post('/auth/register', data={
        'username': 'testuser',
        'password': 'testpass123'
    })
    assert response.status_code == 200
    assert b'You have successfully registered' in response.data


def test_login_user(client):
    # First, register the user
    client.post('/auth/register', data={
        'username': 'testuser',
        'password': 'testpass123'
    })

    # Then, login
    response = client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'testpass123'
    })
    assert response.status_code == 200
    assert b'Login successful' in response.data


def test_logout_user(client):
    # First, register and login the user
    client.post('/auth/register', data={
        'username': 'testuser',
        'password': 'testpass123'
    })
    client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'testpass123'
    })

    # Then, logout
    response = client.get('/auth/logout')
    assert response.status_code == 200
    assert b'You have been logged out' in response.data
