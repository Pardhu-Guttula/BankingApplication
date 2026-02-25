import pytest
import requests

BASE_URL = "http://localhost:5000"

@pytest.fixture
    return {"username": "existing_user", "password": "correct_password"}

def test_successful_login(valid_credentials):
    response = requests.post(
        f"{BASE_URL}/login", json=valid_credentials
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"

def test_login_with_invalid_credentials():
    invalid_credentials = {"username": "nonexistent_user", "password": "wrong_password"}
    response = requests.post(
        f"{BASE_URL}/login", json=invalid_credentials
    )
    assert response.status_code == 401
    assert response.json()["message"] == "Invalid credentials"

def test_successful_registration():
    registration_data = {
        "name": "New User",
        "email": "newuser@example.com",
        "password": "SecurePassword123"
    }
    response = requests.post(
        f"{BASE_URL}/register", json=registration_data
    )
    assert response.status_code == 201
    assert response.json()["message"] == "Registration successful. Please check your email for confirmation."

def test_registration_with_existing_email():
    existing_email_data = {
        "name": "Existing User",
        "email": "existinguser@example.com",
        "password": "AnotherSecurePassword456"
    }
    response = requests.post(
        f"{BASE_URL}/register", json=existing_email_data
    )
    assert response.status_code == 400
    assert response.json()["message"] == "Registration failed, email may already be in use."

def test_registration_with_invalid_data():
    invalid_data = {
        "name": "",
        "email": "invalid_email_format",
        "password": "123"
    }
    response = requests.post(
        f"{BASE_URL}/register", json=invalid_data
    )
    assert response.status_code == 400

def test_successful_logout(valid_credentials):
    login_response = requests.post(
        f"{BASE_URL}/login", json=valid_credentials
    )
    token = login_response.json().get("token")
    logout_response = requests.post(
        f"{BASE_URL}/logout", headers={"Authorization": f"Bearer {token}"}
    )
    assert logout_response.status_code == 200
    assert logout_response.json()["message"] == "Logout successful"
