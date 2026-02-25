import pytest
from flask import Flask
from backend.authentication.controllers.auth_controller import auth_controller

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(auth_controller)
    with app.test_client() as client:
        yield client

# User Registration Tests

def test_registration_success(client, mocker):
    mocker.patch('backend.authentication.services.auth_service.AuthService.register', return_value=True)
    response = client.post('/register', json={"name": "new_user", "email": "new_user@example.com", "password": "SecurePass123!"})
    assert response.status_code == 201
    assert response.json == {"message": "Registration successful. Please check your email for confirmation."}

def test_registration_existing_email(client, mocker):
    mocker.patch('backend.authentication.services.auth_service.AuthService.register', return_value=False)
    response = client.post('/register', json={"name": "existing_user", "email": "existing_user@example.com", "password": "SecurePass123!"})
    assert response.status_code == 400
    assert response.json == {"message": "Registration failed, email may already be in use."}

def test_registration_invalid_data(client):
    response = client.post('/register', json={"name": "", "email": "invalid_email", "password": "123"})
    assert response.status_code == 500
    assert response.json == {"message": "Registration failed"}

# User Login Tests

def test_login_success(client, mocker):
    mocker.patch('backend.authentication.services.auth_service.AuthService.authenticate', return_value=True)
    response = client.post('/login', json={"username": "valid_user", "password": "valid_pass"})
    assert response.status_code == 200
    assert response.json == {"message": "Login successful"}

def test_login_invalid_credentials(client, mocker):
    mocker.patch('backend.authentication.services.auth_service.AuthService.authenticate', return_value=False)
    response = client.post('/login', json={"username": "invalid_user", "password": "wrong_pass"})
    assert response.status_code == 401
    assert response.json == {"message": "Invalid credentials"}

def test_login_account_lockout(client, mocker):
    mocker.patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout', return_value=(True, "Account is locked due to multiple failed attempts"))
    response = client.post('/login', json={"username": "locked_out_user", "password": "wrong_pass"})
    assert response.status_code == 423
    assert response.json == {"error": "Account is locked due to multiple failed attempts"}

# User Logout Tests

def test_logout_success(client):
    response = client.post('/logout')
    assert response.status_code == 200
    assert response.json == {"message": "Logout successful"}

def test_logout_exception(client, mocker):
    mocker.patch('backend.authentication.services.auth_service.AuthService.logout', side_effect=Exception("Service error"))
    response = client.post('/logout')
    assert response.status_code == 500
    assert response.json == {"message": "Logout failed"}

# Role-Based Access Control Tests

def test_assign_role_success(client, mocker):
    mocker.patch('backend.access_control.services.role_service.RoleService.assign_role', return_value=True)
    response = client.post('/assign-role', json={"email": "user@example.com", "role": "admin"})
    assert response.status_code == 200
    assert response.json == {"message": "Role assigned successfully"}

def test_assign_role_failure(client, mocker):
    mocker.patch('backend.access_control.services.role_service.RoleService.assign_role', return_value=False)
    response = client.post('/assign-role', json={"email": "user@example.com", "role": "invalid_role"})
    assert response.status_code == 400
    assert response.json == {"error": "Failed to assign role"}

def test_get_permissions_success(client, mocker):
    mocker.patch('backend.access_control.services.role_service.RoleService.get_permissions', return_value=["view_content"])
    response = client.get('/permissions', query_string={"email": "user@example.com"})
    assert response.status_code == 200
    assert response.json == {"permissions": ["view_content"]}