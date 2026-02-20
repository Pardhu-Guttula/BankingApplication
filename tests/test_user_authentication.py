import pytest
from flask import Flask
from backend.authentication.controllers.auth_controller import auth_controller
from backend.authentication.controllers.account_lock_controller import account_lock_controller
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(auth_controller)
    app.register_blueprint(account_lock_controller)
    app.register_blueprint(account_lockout_controller)
    with app.test_client() as client:
        yield client

# Test cases for auth_controller
def test_auth_controller_login_success(client, mocker):
    mocker.patch("backend.authentication.services.auth_service.AuthService.authenticate",
                 return_value=True)
    response = client.post('/login', json={'username': 'user1', 'password': 'password'})
    assert response.status_code == 200
    assert response.get_json() == {"message": "Login successful"}

def test_auth_controller_login_invalid_credentials(client, mocker):
    mocker.patch("backend.authentication.services.auth_service.AuthService.authenticate",
                 return_value=False)
    response = client.post('/login', json={'username': 'user1', 'password': 'wrongpassword'})
    assert response.status_code == 401
    assert response.get_json() == {"message": "Invalid credentials"}

def test_auth_controller_login_exception(client, mocker):
    mocker.patch("backend.authentication.services.auth_service.AuthService.authenticate",
                 side_effect=Exception("Database error"))
    response = client.post('/login', json={'username': 'user1', 'password': 'password'})
    assert response.status_code == 500
    assert response.get_json() == {"message": "Login failed"}

# Test cases for account_lock_controller
def test_account_lock_controller_login_success(client, mocker):
    mocker.patch("backend.authentication.services.account_lock_service.AccountLockService.process_login",
                 return_value=(True, "Login successful"))
    response = client.post('/login', json={'user_id': 'user1', 'password': 'password'})
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Login successful'}

def test_account_lock_controller_login_fail(client, mocker):
    mocker.patch("backend.authentication.services.account_lock_service.AccountLockService.process_login",
                 return_value=(False, "Account locked"))
    response = client.post('/login', json={'user_id': 'user1', 'password': 'wrongpassword'})
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Account locked'}

def test_account_lock_controller_invalid_data(client):
    response = client.post('/login', json={})
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid data'}

# Test cases for account_lockout_controller
def test_account_lockout_controller_login_success(client, mocker):
    mocker.patch("backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout",
                 return_value=(False, "Login successful"))
    response = client.post('/login', json={'user_id': 'user1', 'password': 'password'})
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Login successful'}

def test_account_lockout_controller_login_locked(client, mocker):
    mocker.patch("backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout",
                 return_value=(True, "Account locked"))
    response = client.post('/login', json={'user_id': 'user1', 'password': 'wrongpassword'})
    assert response.status_code == 423
    assert response.get_json() == {'error': 'Account locked'}

def test_account_lockout_controller_invalid_data(client):
    response = client.post('/login', json={})
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid data'}

