import pytest
from flask import Flask
from backend.authentication.controllers.auth_controller import auth_controller


@pytest.fixture

def client():
    app = Flask(__name__)
    app.register_blueprint(auth_controller)
    app.testing = True
    return app.test_client()


def test_successful_login(client):
    response = client.post('/login', json={'username': 'john@example.com', 'password': 'securepassword'})
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Login successful'}


def test_login_with_invalid_credentials(client):
    response = client.post('/login', json={'username': 'john@example.com', 'password': 'wrongpassword'})
    assert response.status_code == 401
    assert response.get_json() == {'message': 'Invalid credentials'}


def test_successful_registration(client):
    response = client.post('/register', json={'name': 'John Doe', 'email': 'john@example.com', 'password': 'securepassword'})
    assert response.status_code == 201
    assert response.get_json() == {'message': 'Registration successful. Please check your email for confirmation.'}


def test_registration_with_existing_email(client):
    response = client.post('/register', json={'name': 'Jane Doe', 'email': 'jane@example.com', 'password': 'securepassword'})
    response = client.post('/register', json={'name': 'Jane Doe', 'email': 'jane@example.com', 'password': 'securepassword'})
    assert response.status_code == 400
    assert response.get_json() == {'message': 'Registration failed, email may already be in use.'}


def test_registration_with_invalid_data(client):
    response = client.post('/register', json={'name': 'Joe', 'email': 'invalid-email', 'password': '123'})
    assert response.status_code == 400
    assert response.get_json() == {'message': 'Invalid data'}


def test_successful_logout(client):
    response = client.post('/logout')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Logout successful'}


def test_logout_fail(client):
    response = client.post('/logout')
    assert response.status_code == 500
    assert response.get_json() == {'message': 'Logout failed'}


def test_account_lockout(client):
    for _ in range(5):
        client.post('/login', json={'username': 'john@example.com', 'password': 'wrongpassword'})
    response = client.post('/login', json={'username': 'john@example.com', 'password': 'wrongpassword'})
    assert response.status_code == 423
    assert response.get_json() == {'error': 'Account locked due to multiple failed login attempts'}
