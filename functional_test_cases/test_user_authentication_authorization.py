import pytest
from flask import Flask, jsonify

# Assuming you have these imports
from backend.authentication.controllers.auth_controller import auth_controller
from backend.authentication.controllers.account_lock_controller import account_lock_controller
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(auth_controller, url_prefix='/auth')
    app.register_blueprint(account_lock_controller, url_prefix='/auth')
    app.register_blueprint(account_lockout_controller, url_prefix='/auth')
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test cases for User Registration

def test_successful_registration(client):
    response = client.post('/auth/register', json={
        'name': 'Test User',
        'email': 'testuser@example.com',
        'password': 'ValidPassword123!'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'Registration successful. Please check your email for confirmation.'

def test_registration_with_existing_email(client):
    response = client.post('/auth/register', json={
        'name': 'Test User',
        'email': 'existinguser@example.com',
        'password': 'ValidPassword123!'
    })
    assert response.status_code == 400
    assert response.json['message'] == 'Registration failed, email may already be in use.'

def test_registration_with_invalid_data(client):
    response = client.post('/auth/register', json={
        'name': '',
        'email': 'invalid-email',
        'password': 'weak'
    })
    assert response.status_code == 400
    

# Test cases for User Login

def test_successful_login(client):
    response = client.post('/auth/login', json={
        'username': 'validuser@example.com',
        'password': 'ValidPassword123!'
    })
    assert response.status_code == 200
    assert response.json['message'] == 'Login successful'

def test_login_with_invalid_credentials(client):
    response = client.post('/auth/login', json={
        'username': 'invaliduser@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert response.json['message'] == 'Invalid credentials'

def test_account_lockout(client):
    response = client.post('/auth/login', json={
        'user_id': 1,
        'password': 'wrongpassword'
    })
    assert response.status_code == 423
    assert 'error' in response.json

# Test cases for User Logout

def test_successful_logout(client):
    response = client.post('/auth/logout')
    assert response.status_code == 200
    assert response.json['message'] == 'Logout successful'

def test_logout_error(client):
    response = client.post('/auth/logout')
    assert response.status_code == 500
    assert response.json['message'] == 'Logout failed'
