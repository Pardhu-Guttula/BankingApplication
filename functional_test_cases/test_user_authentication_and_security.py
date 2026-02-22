import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.authentication.controllers.auth_controller import auth_controller
from backend.authentication.controllers.account_lock_controller import account_lock_controller
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller

@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(auth_controller)
    app.register_blueprint(account_lock_controller)
    app.register_blueprint(account_lockout_controller)
    return app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()

# Test Cases for Auth Controller
def test_login_success(client: FlaskClient):
    response = client.post('/login', json={'username': 'valid_user', 'password': 'valid_password'})
    assert response.status_code == 200
    assert response.json == {'message': 'Login successful'}

def test_login_invalid_credentials(client: FlaskClient):
    response = client.post('/login', json={'username': 'invalid_user', 'password': 'wrong_password'})
    assert response.status_code == 401
    assert response.json == {'message': 'Invalid credentials'}

def test_login_missing_data(client: FlaskClient):
    response = client.post('/login', json={'username': 'valid_user'})
    assert response.status_code == 400

# Test Cases for Account Lock Controller
def test_account_lock_login_success(client: FlaskClient):
    response = client.post('/login', json={'user_id': 1, 'password': 'valid_password'})
    assert response.status_code == 200
    assert response.json == {'message': 'Login successful'}

def test_account_lock_invalid_data(client: FlaskClient):
    response = client.post('/login', json={'user_id': 1})
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid data'}

# Test Cases for Account Lockout Controller
def test_account_lockout_login_success(client: FlaskClient):
    response = client.post('/login', json={'user_id': 1, 'password': 'valid_password'})
    assert response.status_code == 200


def test_account_lockout_locked_account(client: FlaskClient):
    response = client.post('/login', json={'user_id': 2, 'password': 'valid_password'})
    assert response.status_code == 423


def test_account_lockout_invalid_password(client: FlaskClient):
    response = client.post('/login', json={'user_id': 1, 'password': 'wrong_password'})
    assert response.status_code == 401
