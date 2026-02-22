import pytest
from flask import Flask
from flask.testing import FlaskClient

from backend.authentication.controllers.account_lock_controller import account_lock_controller

@pytest.fixture()
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(account_lock_controller)
    return app

@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()

def test_login_invalid_data(client: FlaskClient):
    response = client.post('/login', json={})
    assert response.status_code == 400
    assert response.json == {"error": "Invalid data"}


def test_login_successful(client: FlaskClient, mocker):
    mocker.patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(True, 'Login successful'))
    response = client.post('/login', json={"user_id": 1, "password": "valid_password"})
    assert response.status_code == 200
    assert response.json == {"message": "Login successful"}


def test_login_failed(client: FlaskClient, mocker):
    mocker.patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(False, 'Invalid credentials'))
    response = client.post('/login', json={"user_id": 1, "password": "invalid_password"})
    assert response.status_code == 400
    assert response.json == {"error": "Invalid credentials"}
