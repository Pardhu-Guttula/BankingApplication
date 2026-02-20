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


def test_auth_controller_login_success(client, mocker):
    mock_auth_service = mocker.patch('backend.authentication.controllers.auth_controller.auth_service')
    mock_auth_service.authenticate.return_value = True
    response = client.post('/auth/login', json={'username': 'test', 'password': 'test'})
    assert response.status_code == 200
    assert response.json == {"message": "Login successful"}


def test_auth_controller_login_invalid_credentials(client, mocker):
    mock_auth_service = mocker.patch('backend.authentication.controllers.auth_controller.auth_service')
    mock_auth_service.authenticate.return_value = False
    response = client.post('/auth/login', json={'username': 'test', 'password': 'wrong'})
    assert response.status_code == 401
    assert response.json == {"message": "Invalid credentials"}


def test_auth_controller_login_exception(client, mocker):
    mock_auth_service = mocker.patch('backend.authentication.controllers.auth_controller.auth_service')
    mock_auth_service.authenticate.side_effect = Exception('Test Exception')
    response = client.post('/auth/login', json={'username': 'test', 'password': 'test'})
    assert response.status_code == 500
    assert response.json == {"message": "Login failed"}
