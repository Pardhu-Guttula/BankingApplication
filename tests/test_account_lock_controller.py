# File: tests/test_account_lock_controller.py

import pytest
import json
from flask import Flask
from backend.authentication.account_lock_controller import account_lock_controller
from backend.authentication.services.account_lock_service import AccountLockService

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(account_lock_controller)
    with app.test_client() as client:
        with app.app_context():
            yield client

# Positive Test Case - Valid login
@pytest.mark.parametrize("user_id, password, process_result, expected_status_code, expected_response", [
    ("valid_user", "valid_password", (True, ""), 200, {'message': 'Login successful'})
])
def test_login_valid(client, monkeypatch, user_id, password, process_result, expected_status_code, expected_response):
    def mock_process_login(user_id, password):
        return process_result
    monkeypatch.setattr(AccountLockService, "process_login", mock_process_login)
    response = client.post('/login', data=json.dumps({'user_id': user_id, 'password': password}), content_type='application/json')
    assert response.status_code == expected_status_code
    assert response.get_json() == expected_response

# Negative Test Case - Missing user_id
@pytest.mark.parametrize("data, expected_status_code, expected_response", [
    ({'password': 'some_password'}, 400, {'error': 'Invalid data'})
])
def test_login_missing_user_id(client, data, expected_status_code, expected_response):
    response = client.post('/login', data=json.dumps(data), content_type='application/json')
    assert response.status_code == expected_status_code
    assert response.get_json() == expected_response

# Negative Test Case - Missing password
@pytest.mark.parametrize("data, expected_status_code, expected_response", [
    ({'user_id': 'some_user'}, 400, {'error': 'Invalid data'})
])
def test_login_missing_password(client, data, expected_status_code, expected_response):
    response = client.post('/login', data=json.dumps(data), content_type='application/json')
    assert response.status_code == expected_status_code
    assert response.get_json() == expected_response

# Negative Test Case - Failed login
@pytest.mark.parametrize("user_id, password, process_result, expected_status_code, expected_response", [
    ("invalid_user", "invalid_password", (False, "Invalid credentials"), 400, {'error': 'Invalid credentials'})
])
def test_login_failed(client, monkeypatch, user_id, password, process_result, expected_status_code, expected_response):
    def mock_process_login(user_id, password):
        return process_result
    monkeypatch.setattr(AccountLockService, "process_login", mock_process_login)
    response = client.post('/login', data=json.dumps({'user_id': user_id, 'password': password}), content_type='application/json')
    assert response.status_code == expected_status_code
    assert response.get_json() == expected_response

# Edge Case - Empty JSON data
@pytest.mark.parametrize("data, expected_status_code, expected_response", [
    ({}, 400, {'error': 'Invalid data'})
])
def test_login_empty_json(client, data, expected_status_code, expected_response):
    response = client.post('/login', data=json.dumps(data), content_type='application/json')
    assert response.status_code == expected_status_code
    assert response.get_json() == expected_response

# Edge Case - Invalid JSON format
def test_login_invalid_json(client):
    response = client.post('/login', data="{invalid_json}", content_type='application/json')
    assert response.status_code == 400
    assert response.get_json() == {'error': 'Invalid data'}