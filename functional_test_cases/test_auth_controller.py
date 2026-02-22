import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.authentication.controllers.auth_controller import auth_controller
from backend.authentication.services.auth_service import AuthService

@pytest.fixture
def client() -> FlaskClient:
    app = Flask(__name__)
    app.register_blueprint(auth_controller, url_prefix='/auth')
    with app.test_client() as client:
        yield client

@pytest.fixture
def auth_service(mocker) -> AuthService:
    return mocker.patch('backend.authentication.services.auth_service.AuthService', autospec=True)


def test_login_success(client: FlaskClient, auth_service: AuthService) -> None:
    auth_service.authenticate.return_value = True
    response = client.post('/auth/login', json={
        'username': 'valid_user',
        'password': 'valid_password'
    })
    assert response.status_code == 200
    assert response.json == {'message': 'Login successful'}


def test_login_invalid_credentials(client: FlaskClient, auth_service: AuthService) -> None:
    auth_service.authenticate.return_value = False
    response = client.post('/auth/login', json={
        'username': 'invalid_user',
        'password': 'invalid_password'
    })
    assert response.status_code == 401
    assert response.json == {'message': 'Invalid credentials'}


def test_login_exception(client: FlaskClient, auth_service: AuthService, mocker) -> None:
    mocker.patch('backend.authentication.controllers.auth_controller.auth_service', autospec=True)
    auth_service.authenticate.side_effect = Exception('Test exception')
    response = client.post('/auth/login', json={
        'username': 'any_user',
        'password': 'any_password'
    })
    assert response.status_code == 500
    assert response.json == {'message': 'Login failed'}
