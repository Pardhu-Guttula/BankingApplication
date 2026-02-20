import pytest
from flask import Flask, json
from backend.authentication.controllers.auth_controller import auth_controller
from backend.authentication.controllers.account_lock_controller import account_lock_controller
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(auth_controller, url_prefix='/auth')
    app.register_blueprint(account_lock_controller, url_prefix='/account_lock')
    app.register_blueprint(account_lockout_controller, url_prefix='/account_lockout')
    with app.test_client() as client:
        yield client

# Auth Controller Tests

def test_login_success(client):
    response = client.post('/auth/login', json={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 200
    assert response.json['message'] == 'Login successful'

def test_login_invalid_credentials(client):
    response = client.post('/auth/login', json={'username': 'invaliduser', 'password': 'invalidpass'})
    assert response.status_code == 401
    assert response.json['message'] == 'Invalid credentials'

def test_login_exception(client, monkeypatch):
    def mock_authenticate(username, password):
        raise Exception('Mocked exception')
    monkeypatch.setattr('backend.authentication.services.auth_service.AuthService.authenticate', mock_authenticate)
    response = client.post('/auth/login', json={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 500
    assert response.json['message'] == 'Login failed'

# Account Lock Controller Tests

def test_account_lock_login_success(client):
    response = client.post('/account_lock/login', json={'user_id': 'testuser', 'password': 'testpass'})
    assert response.status_code == 200
    assert response.json['message'] == 'Login successful'

def test_account_lock_login_invalid_data(client):
    response = client.post('/account_lock/login', json={'user_id': 'testuser'})
    assert response.status_code == 400
    assert response.json['error'] == 'Invalid data'

def test_account_lock_login_failed(client):
    response = client.post('/account_lock/login', json={'user_id': 'invaliduser', 'password': 'invalidpass'})
    assert response.status_code == 400
    assert response.json['error'] == 'Mocked invalid credentials'

# Account Lockout Controller Tests

def test_account_lockout_login_success(client):
    response = client.post('/account_lockout/login', json={'user_id': 'testuser', 'password': 'testpass'})
    assert response.status_code == 200
    assert response.json['message'] == 'Mocked success message'

def test_account_lockout_login_invalid_data(client):
    response = client.post('/account_lockout/login', json={'user_id': 'testuser'})
    assert response.status_code == 400
    assert response.json['error'] == 'Invalid data'

def test_account_lockout_login_locked(client):
    response = client.post('/account_lockout/login', json={'user_id': 'lockeduser', 'password': 'testpass'})
    assert response.status_code == 423
    assert response.json['error'] == 'Mocked account locked error'