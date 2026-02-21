# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, Mock
from flask import Flask
from auth_controller import auth_controller
from backend.authentication.services.auth_service import AuthService

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch.object(AuthService, 'authenticate')
    def test_login_success(self, mock_authenticate):
        # Positive scenario: valid credentials
        mock_authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'valid_user', 'password': 'valid_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch.object(AuthService, 'authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        # Negative scenario: invalid credentials
        mock_authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'invalid_user', 'password': 'invalid_pass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch.object(AuthService, 'authenticate')
    def test_login_missing_data(self, mock_authenticate):
        # Edge case: missing password
        response = self.client.post('/login', json={'username': 'user_without_password'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch.object(AuthService, 'authenticate')
    def test_login_no_json_body(self, mock_authenticate):
        # Negative scenario: no JSON body
        response = self.client.post('/login', data='')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch.object(AuthService, 'authenticate')
    def test_login_partial_data(self, mock_authenticate):
        # Edge case: only username
        response = self.client.post('/login', json={'username': 'partial_user'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('auth_controller.logging.error')
    @patch.object(AuthService, 'authenticate', side_effect=Exception('Test exception'))
    def test_login_unhandled_exception(self, mock_authenticate, mock_logging_error):
        # Exception path: unhandled exception in service
        response = self.client.post('/login', json={'username': 'exception_user', 'password': 'exception_pass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})
        mock_logging_error.assert_called_once_with('Error in login: Test exception')

if __name__ == '__main__':
    unittest.main()