# File: tests/test_auth_controller.py

import json
from flask import Flask, Blueprint, jsonify
import pytest
from backend.authentication.controllers.auth_controller import auth_controller
from backend.authentication.services.auth_service import AuthService

app = Flask(__name__)
app.register_blueprint(auth_controller)

auth_service = AuthService()

def setup_module(module):
    auth_service.authenticate = lambda username, password: username == 'valid_user' and password == 'valid_pass'

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_login_success(client):
    response = client.post('/login', json={'username': 'valid_user', 'password': 'valid_pass'})
    assert response.status_code == 200
    assert response.get_json() == {'message': 'Login successful'}

def test_login_invalid_credentials(client):
    response = client.post('/login', json={'username': 'invalid_user', 'password': 'invalid_pass'})
    assert response.status_code == 401
    assert response.get_json() == {'message': 'Invalid credentials'}

def test_login_missing_username(client):
    response = client.post('/login', json={'password': 'no_username'})
    assert response.status_code == 401
    assert response.get_json() == {'message': 'Invalid credentials'}

def test_login_missing_password(client):
    response = client.post('/login', json={'username': 'no_password'})
    assert response.status_code == 401
    assert response.get_json() == {'message': 'Invalid credentials'}

def test_login_invalid_json(client):
    response = client.post('/login', data='invalid_json')
    assert response.status_code == 500
    assert response.get_json() == {'message': 'Login failed'}


def test_login_long_username(client):
    long_username = 'a' * 256
    response = client.post('/login', json={'username': long_username, 'password': 'valid_pass'})
    assert response.status_code == 401
    assert response.get_json() == {'message': 'Invalid credentials'}

def test_login_long_password(client):
    long_password = 'a' * 256
    response = client.post('/login', json={'username': 'valid_user', 'password': long_password})
    assert response.status_code == 401
    assert response.get_json() == {'message': 'Invalid credentials'}

def test_login_empty_credentials(client):
    response = client.post('/login', json={'username': '', 'password': ''})
    assert response.status_code == 401
    assert response.get_json() == {'message': 'Invalid credentials'}

def test_login_none_username(client):
    response = client.post('/login', json={'username': None, 'password': 'valid_pass'})
    assert response.status_code == 401
    assert response.get_json() == {'message': 'Invalid credentials'}

def test_login_none_password(client):
    response = client.post('/login', json={'username': 'valid_user', 'password': None})
    assert response.status_code == 401
    assert response.get_json() == {'message': 'Invalid credentials'}


def test_login_sql_injection_username(client):
    sql_injection_string = "' OR '1'='1"
    response = client.post('/login', json={'username': sql_injection_string, 'password': 'valid_pass'})
    assert response.status_code == 401
    assert response.get_json() == {'message': 'Invalid credentials'}

def test_login_sql_injection_password(client):
    sql_injection_string = "' OR '1'='1"
    response = client.post('/login', json={'username': 'valid_user', 'password': sql_injection_string})
    assert response.status_code == 401
    assert response.get_json() == {'message': 'Invalid credentials'}