import pytest
from flask import Flask, json
from backend.authentication.controllers.auth_controller import auth_controller

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(auth_controller)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Scenario: Successful login
# Given a registered user provides valid credentials
# When they submit the login form
# Then they are logged into their account
# And a session is started
@pytest.mark.parametrize('username, password', [
    ('valid_user', 'correct_password'),
])
def test_successful_login(client, monkeypatch, username, password):
    monkeypatch.setattr('backend.authentication.services.auth_service.AuthService.authenticate', lambda s, u, p: True)
    response = client.post('/login', data=json.dumps({'username': username, 'password': password}), content_type='application/json')
    assert response.status_code == 200
    assert response.json['message'] == 'Login successful'

# Scenario: Login with invalid credentials
# Given a user provides invalid credentials
# When they attempt to log in
# Then an error message is displayed indicating invalid username or password
@pytest.mark.parametrize('username, password', [
    ('invalid_user', 'wrong_password'),
])
def test_login_with_invalid_credentials(client, monkeypatch, username, password):
    monkeypatch.setattr('backend.authentication.services.auth_service.AuthService.authenticate', lambda s, u, p: False)
    response = client.post('/login', data=json.dumps({'username': username, 'password': password}), content_type='application/json')
    assert response.status_code == 401
    assert response.json['message'] == 'Invalid credentials'

# Scenario: Login with inactive account
# Given a user with an inactive account
# When they attempt to log in
# Then an error message is displayed indicating their account is inactive
@pytest.mark.parametrize('username, password', [
    ('inactive_user', 'correct_password'),
])
def test_login_with_inactive_account(client, monkeypatch, username, password):
    monkeypatch.setattr('backend.authentication.services.auth_service.AuthService.authenticate', lambda s, u, p: False)
    response = client.post('/login', data=json.dumps({'username': username, 'password': password}), content_type='application/json')
    assert response.status_code == 401
    assert response.json['message'] == 'Invalid credentials'

# Scenario: Login failure
# Given a user attempts to log in
# When an error occurs
# Then an appropriate error message is displayed
# And the user remains logged out
@pytest.mark.parametrize('username, password', [
    ('any_user', 'any_password'),
])
def test_login_failure(client, monkeypatch, username, password):
    monkeypatch.setattr('backend.authentication.services.auth_service.AuthService.authenticate', lambda s, u, p: 1 / 0)  # Force error
    response = client.post('/login', data=json.dumps({'username': username, 'password': password}), content_type='application/json')
    assert response.status_code == 500
    assert response.json['message'] == 'Login failed'