import pytest
from flask import Flask
from flask.testing import FlaskClient

from backend.authentication.controllers.account_lockout_controller import account_lockout_controller

@pytest.fixture()
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(account_lockout_controller)
    return app

@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()

def test_login_invalid_data(client: FlaskClient):
    response = client.post('/login', json={})
    assert response.status_code == 400
    assert response.json == {"error": "Invalid data"}


def test_account_locked(client: FlaskClient, mocker):
    mocker.patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout', return_value=(True, 'Account locked'))
    response = client.post('/login', json={"user_id": 1, "password": "any_password"})
    assert response.status_code == 423
    assert response.json == {"error": "Account locked"}


def test_login_failed(client: FlaskClient, mocker):
    mocker.patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Invalid credentials'))
    response = client.post('/login', json={"user_id": 1, "password": "invalid_password"})
    assert response.status_code == 401
    assert response.json == {"error": "Invalid credentials"}
