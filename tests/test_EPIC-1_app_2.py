import pytest
from app import create_app, db
from flask import url_for

@pytest.fixture
def client():
    app = create_app({'TESTING': True})

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

    with app.app_context():
        db.drop_all()


def test_register(client):
    response = client.post(url_for('auth.register'), data={
        'username': 'testuser',
        'password': 'testpass',
        'email': 'test@example.com'
    })
    assert response.status_code == 200
    assert b'Registration successful' in response.data


def test_login(client):
    # Register first
    client.post(url_for('auth.register'), data={
        'username': 'testuser',
        'password': 'testpass',
        'email': 'test@example.com'
    })

    # Attempt login
    response = client.post(url_for('auth.login'), data={
        'username': 'testuser',
        'password': 'testpass'
    })
    assert response.status_code == 200
    assert b'Login successful' in response.data