import pytest
from flask import Flask
from flask.testing import FlaskClient

from backend.authentication.controllers.auth_controller import auth_controller
from backend.authentication.controllers.account_lock_controller import account_lock_controller
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller

@pytest.fixture
def client() -> FlaskClient:
    app = Flask(__name__)
    app.register_blueprint(auth_controller, url_prefix='/auth')
    app.register_blueprint(account_lock_controller, url_prefix='/account_lock')
    app.register_blueprint(account_lockout_controller, url_prefix='/account_lockout')
    with app.test_client() as client:
        yield client

# Test cases for User Login

def test_successful_login(client):
    response = client.post('/auth/login', json={'username': 'valid_user', 'password': 'valid_password'})
    assert response.status_code == 200
    assert response.json == {"message": "Login successful"}

def test_login_invalid_credentials(client):
    response = client.post('/auth/login', json={'username': 'invalid_user', 'password': 'invalid_password'})
    assert response.status_code == 401
    assert response.json == {"message": "Invalid credentials"}

def test_login_server_error(client, mocker):
    mocker.patch('backend.authentication.services.auth_service.AuthService.authenticate', side_effect=Exception('Server error'))
    response = client.post('/auth/login', json={'username': 'valid_user', 'password': 'valid_password'})
    assert response.status_code == 500
    assert response.json == {"message": "Login failed"}

# Test cases for Account Lock

def test_account_lock_login_success(client):
    response = client.post('/account_lock/login', json={'user_id': 1, 'password': 'valid_password'})
    assert response.status_code == 200
    assert response.json == {"message": "Login successful"}

def test_account_lock_invalid_data(client):
    response = client.post('/account_lock/login', json={'user_id': None, 'password': 'valid_password'})
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid data'}

# Test cases for Account Lockout

def test_account_lockout_locked(client):
    response = client.post('/account_lockout/login', json={'user_id': 1, 'password': 'valid_password'})
    assert response.status_code == 423
    assert response.json == {'error': 'Your account is locked due to multiple failed login attempts'}

def test_account_lockout_invalid_data(client):
    response = client.post('/account_lockout/login', json={'user_id': None, 'password': 'valid_password'})
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid data'}
