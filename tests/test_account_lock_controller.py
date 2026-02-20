import pytest
from flask import Flask
from backend.authentication.controllers.auth_controller import auth_controller
from backend.authentication.controllers.account_lock_controller import account_lock_controller
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller


@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(auth_controller, url_prefix='/auth')
    app.register_blueprint(account_lock_controller, url_prefix='/lock')
    app.register_blueprint(account_lockout_controller, url_prefix='/lockout')
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_account_lock_controller_login_success(client, mocker):
    mock_account_lock_service = mocker.patch('backend.authentication.controllers.account_lock_controller.AccountLockService')
    mock_account_lock_service.process_login.return_value = (True, 'Login successful')
    response = client.post('/lock/login', json={'user_id': 'test', 'password': 'test'})
    assert response.status_code == 200
    assert response.json == {'message': 'Login successful'}


def test_account_lock_controller_invalid_data(client):
    response = client.post('/lock/login', json={'user_id': 'test'})
    assert response.status_code == 400
    assert response.json == {'error': 'Invalid data'}


def test_account_lock_controller_login_failure(client, mocker):
    mock_account_lock_service = mocker.patch('backend.authentication.controllers.account_lock_controller.AccountLockService')
    mock_account_lock_service.process_login.return_value = (False, 'Login failed')
    response = client.post('/lock/login', json={'user_id': 'test', 'password': 'wrong'})
    assert response.status_code == 400
    assert response.json == {'error': 'Login failed'}
