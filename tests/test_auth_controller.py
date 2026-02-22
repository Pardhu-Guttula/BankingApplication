# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from auth_controller import auth_controller
from backend.authentication.services.auth_service import AuthService

class TestAuthController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch.object(AuthService, 'authenticate')
    def test_login_successful(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'test', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch.object(AuthService, 'authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'test', 'password': 'password'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch.object(AuthService, 'authenticate')
    def test_login_missing_username(self, mock_authenticate):
        response = self.client.post('/login', json={'password': 'password'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch.object(AuthService, 'authenticate')
    def test_login_missing_password(self, mock_authenticate):
        response = self.client.post('/login', json={'username': 'test'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('auth_controller.logging.error')
    @patch.object(AuthService, 'authenticate', side_effect=Exception('Test Exception'))
    def test_login_authentication_exception(self, mock_authenticate, mock_logging_error):
        response = self.client.post('/login', json={'username': 'test', 'password': 'password'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})
        mock_logging_error.assert_called_once_with('Error in login: Test Exception')

    @patch('auth_controller.request')
    def test_login_no_json_body(self, mock_request):
        mock_request.json = None
        response = self.client.post('/login', json=None)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()
