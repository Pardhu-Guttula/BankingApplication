# File: tests/test_auth_controller.py

import pytest
from unittest.mock import Mock, patch
from flask import json
from auth_controller import auth_controller


@pytest.fixture
def client():
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(auth_controller)
    with app.test_client() as client:
        yield client


def test_login_success(client):
    with patch('auth_controller.auth_service.authenticate') as mock_authenticate:
        mock_authenticate.return_value = True
        response = client.post('/login', json={'username': 'test_user', 'password': 'test_pass'})
        assert response.status_code == 200
        assert response.json == {'message': 'Login successful'}


def test_login_invalid_credentials(client):
    with patch('auth_controller.auth_service.authenticate') as mock_authenticate:
        mock_authenticate.return_value = False
        response = client.post('/login', json={'username': 'test_user', 'password': 'wrong_pass'})
        assert response.status_code == 401
        assert response.json == {'message': 'Invalid credentials'}


def test_login_missing_username(client):
    response = client.post('/login', json={'password': 'test_pass'})
    assert response.status_code == 500
    assert response.json == {'message': 'Login failed'}


def test_login_missing_password(client):
    response = client.post('/login', json={'username': 'test_user'})
    assert response.status_code == 500
    assert response.json == {'message': 'Login failed'}


def test_login_invalid_json(client):
    response = client.post('/login', data='invalid json')
    assert response.status_code == 500
    assert response.json == {'message': 'Login failed'}


def test_login_exception_handling(client):
    with patch('auth_controller.auth_service.authenticate', side_effect=Exception('Test exception')):
        response = client.post('/login', json={'username': 'test_user', 'password': 'test_pass'})
        assert response.status_code == 500
        assert response.json == {'message': 'Login failed'}