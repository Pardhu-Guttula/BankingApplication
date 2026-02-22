import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.authentication.controllers.account_lock_controller import account_lock_controller
from backend.authentication.services.account_lock_service import AccountLockService

@pytest.fixture
def client() -> FlaskClient:
    app = Flask(__name__)
    app.register_blueprint(account_lock_controller, url_prefix='/auth')
    with app.test_client() as client:
        yield client

@pytest.fixture
def account_lock_service(mocker) -> AccountLockService:
    return mocker.patch('backend.authentication.services.account_lock_service.AccountLockService', autospec=True)


def test_account_lock_login_success(client: FlaskClient, account_lock_service: AccountLockService) -> None:
    account_lock_service.process_login.return_value = (True, 'Login successful')
    response = client.post('/auth/login', json={
        'user_id': 'valid_user',
        'password': 'valid_password'
    })
    assert response.status_code == 200
    assert response.json == {'message': 'Login successful'}


def test_account_lock_login_invalid_credentials(client: FlaskClient, account_lock_service: AccountLockService) -> None:
    account_lock_service.process_login.return_value = (False, 'Invalid credentials')
    response = client.post('/auth/login', json={
        'user_id': 'invalid_user',
        'password': 'invalid_password'
    })
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid credentials'}


def test_account_lock_login_invalid_data(client: FlaskClient) -> None:
    response = client.post('/auth/login', json={
        'user_id': None,
        'password': None
    })
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid data'}
