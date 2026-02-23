# File: tests/test_auth_controller.py
import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from auth_controller import auth_controller

class AuthControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('auth_controller.auth_service.authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'user', 'password': 'pass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_failure(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'user', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.request')
    def test_login_exception(self, mock_request):
        mock_request.json = None
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('auth_controller.auth_service.register')
    def test_register_success(self, mock_register):
        mock_register.return_value = True
        response = self.client.post('/register', json={'name': 'name', 'email': 'email@example.com', 'password': 'pass'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': 'Registration successful. Please check your email for confirmation.'})

    @patch('auth_controller.auth_service.register')
    def test_register_failure(self, mock_register):
        mock_register.return_value = False
        response = self.client.post('/register', json={'name': 'name', 'email': 'email@example.com', 'password': 'pass'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'message': 'Registration failed, email may already be in use.'})

    @patch('auth_controller.request')
    def test_register_exception(self, mock_request):
        mock_request.json = None
        response = self.client.post('/register')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Registration failed'})

    @patch('auth_controller.auth_service.logout')
    def test_logout_success(self, mock_logout):
        response = self.client.post('/logout')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Logout successful'})

    @patch('auth_controller.auth_service.logout')
    def test_logout_exception(self, mock_logout):
        mock_logout.side_effect = Exception('Error')
        response = self.client.post('/logout')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Logout failed'})

if __name__ == '__main__':
    unittest.main()