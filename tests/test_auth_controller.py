# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, Blueprint, json
from auth_controller import auth_controller

class TestAuthController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('auth_controller.auth_service.authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', json={"username": "testuser", "password": "testpass"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"message": "Login successful"})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', json={"username": "testuser", "password": "wrongpass"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data), {"message": "Invalid credentials"})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_missing_username(self, mock_authenticate):
        response = self.client.post('/login', json={"password": "testpass"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data), {"message": "Invalid credentials"})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_missing_password(self, mock_authenticate):
        response = self.client.post('/login', json={"username": "testuser"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data), {"message": "Invalid credentials"})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_empty_request_body(self, mock_authenticate):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data), {"message": "Invalid credentials"})

    @patch('auth_controller.logging.error')
    @patch('auth_controller.auth_service.authenticate')
    def test_login_exception(self, mock_authenticate, mock_logging_error):
        mock_authenticate.side_effect = Exception("Authentication error")
        response = self.client.post('/login', json={"username": "testuser", "password": "testpass"})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(json.loads(response.data), {"message": "Login failed"})
        mock_logging_error.assert_called_once()

if __name__ == '__main__':
    unittest.main()