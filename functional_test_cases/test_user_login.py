import requests
import pytest

BASE_URL = "http://localhost:5000"

# Test Scenarios for User Login

def test_successful_login():
    response = requests.post(f"{BASE_URL}/login", json={"username": "validUser", "password": "validPassword"})
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful"}

def test_login_with_invalid_credentials():
    response = requests.post(f"{BASE_URL}/login", json={"username": "invalidUser", "password": "invalidPassword"})
    assert response.status_code == 401
    assert response.json() == {"message": "Invalid credentials"}

def test_login_with_missing_username():
    response = requests.post(f"{BASE_URL}/login", json={"password": "validPassword"})
    assert response.status_code == 500

def test_login_with_missing_password():
    response = requests.post(f"{BASE_URL}/login", json={"username": "validUser"})
    assert response.status_code == 500

