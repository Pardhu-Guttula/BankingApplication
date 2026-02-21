# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from auth_controller import auth_controller
from backend.authentication.services.auth_service import AuthService

class AuthControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch.object(AuthService, 'authenticate')
    def test_login_successful(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', data=json.dumps({'username': 'testuser', 'password': 'testpass'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch.object(AuthService, 'authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', data=json.dumps({'username': 'wronguser', 'password': 'wrongpass'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch.object(AuthService, 'authenticate')
    def test_login_missing_username(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', data=json.dumps({'password': 'testpass'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch.object(AuthService, 'authenticate')
    def test_login_missing_password(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', data=json.dumps({'username': 'testuser'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.logging.error')
    @patch.object(AuthService, 'authenticate', side_effect=Exception('test exception'))
    def test_login_exception(self, mock_authenticate, mock_logging_error):
        response = self.client.post('/login', data=json.dumps({'username': 'testuser', 'password': 'testpass'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})
        mock_logging_error.assert_called_with('Error in login: test exception')
        

if __name__ == '__main__':
    unittest.main()
