import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from backend.authentication.controllers.auth_controller import auth_controller

class TestUserAuthentication(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_successful_login(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'test_user', 'password': 'test_password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'test_user', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('backend.authentication.services.auth_service.AuthService.register')
    def test_successful_registration(self, mock_register):
        mock_register.return_value = True
        response = self.client.post('/register', json={'name': 'test_name', 'email': 'test@example.com', 'password': 'test_password'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': 'Registration successful. Please check your email for confirmation.'})

    @patch('backend.authentication.services.auth_service.AuthService.register')
    def test_registration_with_existing_email(self, mock_register):
        mock_register.return_value = False
        response = self.client.post('/register', json={'name': 'test_name', 'email': 'existing@example.com', 'password': 'test_password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'message': 'Registration failed, email may already be in use.'})

    @patch('backend.authentication.services.auth_service.AuthService.logout')
    def test_successful_logout(self, mock_logout):
        response = self.client.post('/logout')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Logout successful'})

if __name__ == '__main__':
    unittest.main()
