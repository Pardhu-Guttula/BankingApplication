import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller
from backend.authentication.services.account_lockout_service import AccountLockoutService


@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(account_lockout_controller)
    return app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_account_lockout_login_success(client: FlaskClient, mocker):
    mock_account_lockout_service = mocker.patch.object(AccountLockoutService, 'record_attempt_and_check_lockout', return_value=(False, 'Login successful'))
    response = client.post('/login', json={'user_id': 1, 'password': 'correct_password'})
    assert response.status_code == 200
    assert response.json == {"message": "Login successful"}
    mock_account_lockout_service.assert_called_once_with(1, True)


def test_account_lockout_login_invalid_credentials(client: FlaskClient, mocker):
    mock_account_lockout_service = mocker.patch.object(AccountLockoutService, 'record_attempt_and_check_lockout', return_value=(False, 'Invalid credentials'))
    response = client.post('/login', json={'user_id': 1, 'password': 'wrong_password'})
    assert response.status_code == 401
    assert response.json == {"error": "Invalid credentials"}
    mock_account_lockout_service.assert_called_once_with(1, False)


def test_account_lockout_login_account_locked(client: FlaskClient, mocker):
    mock_account_lockout_service = mocker.patch.object(AccountLockoutService, 'record_attempt_and_check_lockout', return_value=(True, 'Account locked'))
    response = client.post('/login', json={'user_id': 1, 'password': 'any_password'})
    assert response.status_code == 423
    assert response.json == {"error": "Account locked"}
    mock_account_lockout_service.assert_called_once_with(1, True)  # 1 for user_id and success=True for successful login attempt


def test_account_lockout_login_missing_data(client: FlaskClient):
    response = client.post('/login', json={'user_id': 1})
    assert response.status_code == 400
    assert response.json == {"error": "Invalid data"}

    response = client.post('/login', json={'password': 'some_password'})
    assert response.status_code == 400
    assert response.json == {"error": "Invalid data"}