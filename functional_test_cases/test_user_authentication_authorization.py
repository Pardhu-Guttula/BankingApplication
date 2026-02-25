import requests

BASE_URL = 'http://localhost:5000'

class TestUserAuthenticationAuthorization:

    def test_successful_registration(self):
        payload = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "StrongPass123!"
        }
        response = requests.post(f'{BASE_URL}/register', json=payload)
        assert response.status_code == 201
        assert response.json()["message"] == "Registration successful. Please check your email for confirmation."

    def test_registration_with_existing_email(self):
        payload = {
            "name": "John Doe",
            "email": "john@example.com",
            "password": "StrongPass123!"
        }
        response = requests.post(f'{BASE_URL}/register', json=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Registration failed, email may already be in use."

    def test_registration_with_invalid_data(self):
        # Test with weak password
        payload = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "weak"
        }
        response = requests.post(f'{BASE_URL}/register', json=payload)
        assert response.status_code == 400
        
        # Test with invalid email
        payload = {
            "name": "John Doe",
            "email": "invalid-email",
            "password": "StrongPass123!"
        }
        response = requests.post(f'{BASE_URL}/register', json=payload)
        assert response.status_code == 400

    def test_successful_login(self):
        payload = {
            "username": "john@example.com",
            "password": "StrongPass123!"
        }
        response = requests.post(f'{BASE_URL}/login', json=payload)
        assert response.status_code == 200
        assert response.json()["message"] == "Login successful"

    def test_login_with_invalid_credentials(self):
        payload = {
            "username": "john@example.com",
            "password": "WrongPass"
        }
        response = requests.post(f'{BASE_URL}/login', json=payload)
        assert response.status_code == 401
        assert response.json()["message"] == "Invalid credentials"

    def test_login_with_account_lockout(self):
        payload = {
            "user_id": "locked_user",
            "password": "WrongPass"
        }
        # Simulate multiple failed login attempts
        for _ in range(5):
            response = requests.post(f'{BASE_URL}/login', json=payload)
        assert response.status_code == 423
        assert response.json()["error"] == "Account locked"

    def test_successful_logout(self):
        response = requests.post(f'{BASE_URL}/logout')
        assert response.status_code == 200
        assert response.json()["message"] == "Logout successful"

    def test_logout_with_invalid_token(self):
        response = requests.post(f'{BASE_URL}/logout')
        assert response.status_code == 500
        assert response.json()["message"] == "Logout failed"