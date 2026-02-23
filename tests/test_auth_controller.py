# File: tests/test_auth_controller.py
import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask.testing import FlaskClient
from auth_controller import auth_controller

class AuthControllerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('auth_service.AuthService.authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'user', 'password': 'pass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('auth_service.AuthService.authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'user', 'password': 'wrong'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_service.AuthService.authenticate')
    def test_login_exception(self, mock_authenticate):
        mock_authenticate.side_effect = Exception('Test exception')
        response = self.client.post('/login', json={'username': 'user', 'password': 'pass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('auth_service.AuthService.register')
    def test_register_success(self, mock_register):
        mock_register.return_value = True
        response = self.client.post('/register', json={'name': 'name', 'email': 'email@example.com', 'password': 'pass'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': 'Registration successful. Please check your email for confirmation.'})

    @patch('auth_service.AuthService.register')
    def test_register_failed(self, mock_register):
        mock_register.return_value = False
        response = self.client.post('/register', json={'name': 'name', 'email': 'email@example.com', 'password': 'pass'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'message': 'Registration failed, email may already be in use.'})

    @patch('auth_service.AuthService.register')
    def test_register_exception(self, mock_register):
        mock_register.side_effect = Exception('Test exception')
        response = self.client.post('/register', json={'name': 'name', 'email': 'email@example.com', 'password': 'pass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Registration failed'})

    @patch('auth_service.AuthService.logout')
    def test_logout_success(self, mock_logout):
        response = self.client.post('/logout')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Logout successful'})

    @patch('auth_service.AuthService.logout')
    def test_logout_exception(self, mock_logout):
        mock_logout.side_effect = Exception('Test exception')
        response = self.client.post('/logout')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Logout failed'})

if __name__ == '__main__':
    unittest.main()