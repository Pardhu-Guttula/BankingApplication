import requests
import pytest

BASE_URL = "http://localhost:5000"

# Test Scenarios for Account Lock Service

def test_lock_account():
    response = requests.post(f"{BASE_URL}/login", json={"user_id": 1, "password": "wrongPassword"})
    assert response.status_code == 423
    assert response.json() == {"error": "Account locked due to too many failed login attempts"}

def test_unlock_account():
    response = requests.post(f"{BASE_URL}/unlock_account", json={"user_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Account unlocked successfully"}

def test_lock_account_invalid_user_id():
    response = requests.post(f"{BASE_URL}/login", json={"user_id": 9999, "password": "wrongPassword"})
    assert response.status_code == 400
    assert response.json() == {"error": "Invalid user ID or password"}
