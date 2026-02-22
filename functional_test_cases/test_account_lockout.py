import requests
import pytest

BASE_URL = "http://localhost:5000"

# Test Scenarios for Account Lockout

def test_successful_account_lockout():
    response = requests.post(f"{BASE_URL}/login", json={"user_id": 1, "password": "wrongPassword"})
    assert response.status_code == 423
    assert response.json() == {"error": "Account locked due to too many failed login attempts"}

def test_login_with_locked_account():
    response = requests.post(f"{BASE_URL}/login", json={"user_id": 1, "password": "anyPassword"})
    assert response.status_code == 423
    assert response.json() == {"error": "Account locked due to too many failed login attempts"}

def test_login_account_not_locked():
    response = requests.post(f"{BASE_URL}/login", json={"user_id": 2, "password": "validPassword"})
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful"}

def test_login_with_invalid_user_id():
    response = requests.post(f"{BASE_URL}/login", json={"user_id": 9999, "password": "validPassword"})
    assert response.status_code == 400
    assert response.json() == {"error": "Invalid user ID or password"}
