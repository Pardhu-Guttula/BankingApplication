import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller
from backend.authentication.services.account_lockout_service import AccountLockoutService

@pytest.fixture
def client() -> FlaskClient:
    app = Flask(__name__)
    app.register_blueprint(account_lockout_controller, url_prefix='/auth')
    with app.test_client() as client:
        yield client

@pytest.fixture
def account_lockout_service(mocker) -> AccountLockoutService:
    return mocker.patch('backend.authentication.services.account_lockout_service.AccountLockoutService', autospec=True)


def test_lockout_login_success(client: FlaskClient, account_lockout_service: AccountLockoutService) -> None:
    account_lockout_service.record_attempt_and_check_lockout.return_value = (False, 'Login successful')
    response = client.post('/auth/login', json={
        'user_id': 'valid_user',
        'password': 'valid_password'
    })
    assert response.status_code == 200
    assert response.json == {'message': 'Login successful'}


def test_lockout_login_invalid_credentials(client: FlaskClient, account_lockout_service: AccountLockoutService) -> None:
    account_lockout_service.record_attempt_and_check_lockout.return_value = (False, 'Invalid credentials')
    response = client.post('/auth/login', json={
        'user_id': 'invalid_user',
        'password': 'invalid_password'
    })
    assert response.status_code == 401
    assert response.json == {'error': 'Invalid credentials'}


def test_lockout_login_locked(client: FlaskClient, account_lockout_service: AccountLockoutService) -> None:
    account_lockout_service.record_attempt_and_check_lockout.return_value = (True, 'Account locked')
    response = client.post('/auth/login', json={
        'user_id': 'locked_user',
        'password': 'any_password'
    })
    assert response.status_code == 423
    assert response.json == {'error': 'Account locked'}


def test_lockout_login_invalid_data(client: FlaskClient) -> None:
    response = client.post('/auth/login', json={
        'user_id': None,
        'password': None
    })
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid data'}
