# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, Mock
from flask import Flask, jsonify
from auth_controller import auth_controller

class AuthControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('auth_controller.auth_service')
    def test_login_success(self, mock_auth_service):
        # Happy path test case
        mock_auth_service.authenticate.return_value = True
        response = self.client.post('/login', json={"username": "testuser", "password": "testpass"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Login successful"})

    @patch('auth_controller.auth_service')
    def test_login_invalid_credentials(self, mock_auth_service):
        # Test invalid credentials
        mock_auth_service.authenticate.return_value = False
        response = self.client.post('/login', json={"username": "testuser", "password": "wrongpass"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"message": "Invalid credentials"})

    @patch('auth_controller.auth_service')
    def test_login_missing_fields(self, mock_auth_service):
        # Test missing 'username' and 'password' in request
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"message": "Login failed"})

    def test_login_internal_server_error(self):
        # Test internal server error
        with patch('auth_controller.request') as mock_request, \
             patch('auth_controller.auth_service.authenticate', side_effect=Exception('Test Exception')):
            mock_request.json = {"username": "testuser", "password": "testpass"}
            response = self.client.post('/login')
            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.json, {"message": "Login failed"})

if __name__ == '__main__':
    unittest.main()