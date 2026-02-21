# File: tests/test_account_lock_controller.py

import pytest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from src.account_lock_controller import account_lock_controller

@pytest.fixture
def client() -> FlaskClient:
    app = Flask(__name__)
    app.register_blueprint(account_lock_controller)
    with app.test_client() as client:
        yield client

def test_login_successful(client, mocker):
    mocker.patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(True, 'Login successful'))
    response = client.post('/login', json={'user_id': 'valid_user', 'password': 'correct_password'})
    assert response.status_code == 200
    assert response.json == {'message': 'Login successful'}

def test_login_invalid_data(client):
    response = client.post('/login', json={})
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid data'}

def test_login_missing_password(client):
    response = client.post('/login', json={'user_id': 'valid_user'})
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid data'}

def test_login_missing_user_id(client):
    response = client.post('/login', json={'password': 'correct_password'})
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid data'}

def test_login_unsuccessful(client, mocker):
    mocker.patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(False, 'Login failed'))
    response = client.post('/login', json={'user_id': 'invalid_user', 'password': 'wrong_password'})
    assert response.status_code == 400
    assert response.json == {'error': 'Login failed'}

