import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.authentication.controllers.auth_controller import auth_controller
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller

@pytest.fixture
def client() -> FlaskClient:
    app = Flask(__name__)
    app.register_blueprint(auth_controller, url_prefix='/auth')
    app.register_blueprint(account_lockout_controller, url_prefix='/account_lockout')
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_user_login_success(client: FlaskClient):
    response = client.post('/auth/login', json={
        'username': 'valid_user',
        'password': 'valid_password'
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "Login successful"}

def test_user_login_invalid_credentials(client: FlaskClient):
    response = client.post('/auth/login', json={
        'username': 'invalid_user',
        'password': 'invalid_password'
    })
    assert response.status_code == 401
    assert response.get_json() == {"message": "Invalid credentials"}

def test_user_login_exception(client: FlaskClient, mocker):
    mocker.patch('backend.authentication.services.auth_service.AuthService.authenticate', side_effect=Exception('Test exception'))
    response = client.post('/auth/login', json={
        'username': 'any_user',
        'password': 'any_password'
    })
    assert response.status_code == 500
    assert response.get_json() == {"message": "Login failed"}
