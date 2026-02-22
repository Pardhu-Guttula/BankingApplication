import requests
import pytest

BASE_URL = "http://localhost:5000"

# Test cases for the User Authentication and Security epic

def test_login_successful():
    url = f"{BASE_URL}/login"
    payload = {"username": "testuser", "password": "testpassword"}
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"

def test_login_invalid_credentials():
    url = f"{BASE_URL}/login"
    payload = {"username": "invaliduser", "password": "invalidpassword"}
    response = requests.post(url, json=payload)
    assert response.status_code == 401
    assert response.json()["message"] == "Invalid credentials"

def test_login_missing_data():
    url = f"{BASE_URL}/login"
    payload = {"username": "", "password": ""}
    response = requests.post(url, json=payload)
    assert response.status_code == 500
    assert response.json()["message"] == "Login failed"
