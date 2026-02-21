# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from auth_controller import auth_controller

class AuthControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('auth_controller.auth_service')
    def test_login_successful(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'validuser', 'password': 'validpass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('auth_controller.auth_service')
    def test_login_invalid_credentials(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'invaliduser', 'password': 'invalidpass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service')
    def test_login_missing_username(self, mock_auth_service):
        response = self.client.post('/login', json={'password': 'somepass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('auth_controller.auth_service')
    def test_login_missing_password(self, mock_auth_service):
        response = self.client.post('/login', json={'username': 'someuser'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('auth_controller.auth_service')
    def test_login_empty_request_body(self, mock_auth_service):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('auth_controller.auth_service')
    def test_login_invalid_content_type(self, mock_auth_service):
        response = self.client.post('/login', data='username=someuser&password=somepass')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('auth_controller.auth_service')
    def test_login_service_exception(self, mock_auth_service):
        mock_auth_service.authenticate.side_effect = Exception('Service failure')
        response = self.client.post('/login', json={'username': 'someuser', 'password': 'somepass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()