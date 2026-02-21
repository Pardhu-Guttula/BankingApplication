# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from backend.authentication.controllers.auth_controller import auth_controller
from backend.authentication.services.auth_service import AuthService

class AuthControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch.object(AuthService, 'authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'valid_user', 'password': 'valid_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch.object(AuthService, 'authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'invalid_user', 'password': 'invalid_pass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('backend.authentication.controllers.auth_controller.request')
    @patch('backend.authentication.controllers.auth_controller.logging')
    @patch.object(AuthService, 'authenticate')
    def test_login_exception(self, mock_authenticate, mock_logging, mock_request):
        mock_request.json = {'username': 'user', 'password': 'pass'}
        mock_authenticate.side_effect = Exception('Test exception')
        response = self.client.post('/login', json={'username': 'user', 'password': 'pass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})
        mock_logging.error.assert_called_once_with('Error in login: Test exception')

    def test_login_no_json(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    def test_login_missing_username(self):
        response = self.client.post('/login', json={'password': 'pass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'username': 'user'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()