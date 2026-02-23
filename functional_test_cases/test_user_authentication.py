import pytest
from flask import Flask
from backend.authentication.controllers.account_lock_controller import account_lock_controller
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller
from unittest.mock import patch

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(account_lock_controller)
    app.register_blueprint(account_lockout_controller)
    with app.test_client() as client:
        yield client

# Test cases for account_lock_controller

def test_account_lock_login_success(client):
    data = {'user_id': 'valid_user', 'password': 'valid_password'}
    with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login') as mock_process_login:
        mock_process_login.return_value = (True, 'Login successful')
        response = client.post('/login', json=data)
        assert response.status_code == 200
        assert response.get_json() == {'message': 'Login successful'}

def test_account_lock_login_invalid_data(client):
    data = {'user_id': 'valid_user'}
    response = client.post('/login', json=data)
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid data'}

def test_account_lock_login_failure(client):
    data = {'user_id': 'invalid_user', 'password': 'invalid_password'}
    with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login') as mock_process_login:
        mock_process_login.return_value = (False, 'Login failed')
        response = client.post('/login', json=data)
        assert response.status_code == 400
        assert response.get_json() == {'error': 'Login failed'}

def test_account_lock_login_missing_user_id(client):
    data = {'password': 'password_only'}
    response = client.post('/login', json=data)
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid data'}

def test_account_lock_login_missing_password(client):
    data = {'user_id': 'user_only'}
    response = client.post('/login', json=data)
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid data'}

def test_account_lock_login_empty_body(client):
    data = {}
    response = client.post('/login', json=data)
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid data'}

def test_account_lock_login_invalid_json(client):
    response = client.post('/login', data="not a json")
    assert response.status_code == 400

# Test cases for account_lockout_controller

def test_account_lockout_login_success(client):
    with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout') as mock_record:
        mock_record.return_value = (False, "Login successful.")
        response = client.post('/login', json={'user_id': 'test_user', 'password': 'test_password'})
        assert response.status_code == 200
        assert response.get_json() == {'message': 'Login successful.'}

def test_account_lockout_login_lockout(client):
    with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout') as mock_record:
        mock_record.return_value = (True, "Account is locked.")
        response = client.post('/login', json={'user_id': 'test_user', 'password': 'test_password'})
        assert response.status_code == 423
        assert response.get_json() == {'error': 'Account is locked.'}

def test_account_lockout_login_invalid_data(client):
    response = client.post('/login', json={'user_id': 'test_user'})
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid data'}

def test_account_lockout_login_wrong_credentials(client):
    with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout') as mock_record:
        mock_record.return_value = (False, "Invalid credentials.")
        response = client.post('/login', json={'user_id': 'test_user', 'password': 'wrong_password'})
        assert response.status_code == 401
        assert response.get_json() == {'error': 'Invalid credentials.'}

def test_account_lockout_login_no_data(client):
    response = client.post('/login', json={})
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid data'}
