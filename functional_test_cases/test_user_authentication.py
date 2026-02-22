import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.authentication.controllers.auth_controller import auth_controller
from backend.authentication.services.auth_service import AuthService


@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(auth_controller)
    return app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_login_success(client: FlaskClient, mocker):
    mock_auth_service = mocker.patch.object(AuthService, 'authenticate', return_value=True)
    response = client.post('/login', json={'username': 'validuser', 'password': 'validpass'})
    assert response.status_code == 200
    assert response.json == {"message": "Login successful"}
    mock_auth_service.assert_called_once_with('validuser', 'validpass')


def test_login_invalid_credentials(client: FlaskClient, mocker):
    mock_auth_service = mocker.patch.object(AuthService, 'authenticate', return_value=False)
    response = client.post('/login', json={'username': 'invaliduser', 'password': 'invalidpass'})
    assert response.status_code == 401
    assert response.json == {"message": "Invalid credentials"}
    mock_auth_service.assert_called_once_with('invaliduser', 'invalidpass')


def test_login_missing_data(client: FlaskClient):
    response = client.post('/login', json={'username': 'validuser'})
    assert response.status_code == 500
    assert response.json == {"message": "Login failed"}

    response = client.post('/login', json={'password': 'validpass'})
    assert response.status_code == 500
    assert response.json == {"message": "Login failed"}


def test_login_exception(client: FlaskClient, mocker):
    mock_auth_service = mocker.patch.object(AuthService, 'authenticate', side_effect=Exception('Unexpected Error'))
    response = client.post('/login', json={'username': 'validuser', 'password': 'validpass'})
    assert response.status_code == 500
    assert response.json == {"message": "Login failed"}
    mock_auth_service.assert_called_once_with('validuser', 'validpass')