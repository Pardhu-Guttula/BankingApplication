import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.authentication.controllers.auth_controller import auth_controller
import json

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(auth_controller, url_prefix='/auth')
    return app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_successful_login(client: FlaskClient):
    response = client.post('/auth/login', json={'username': 'valid_user', 'password': 'valid_password'})
    assert response.status_code == 200
    assert response.json == {"message": "Login successful"}


def test_invalid_credentials(client: FlaskClient):
    response = client.post('/auth/login', json={'username': 'invalid_user', 'password': 'invalid_password'})
    assert response.status_code == 401
    assert response.json == {"message": "Invalid credentials"}


def test_login_failure(client: FlaskClient, monkeypatch):
    def mock_authenticate(username: str, password: str) -> bool:
        raise Exception("Authentication error")

    monkeypatch.setattr('backend.authentication.services.auth_service.AuthService.authenticate', mock_authenticate)
    response = client.post('/auth/login', json={'username': 'error_user', 'password': 'error_password'})
    assert response.status_code == 500
    assert response.json == {"message": "Login failed"}