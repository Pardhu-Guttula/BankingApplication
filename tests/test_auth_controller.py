# File: tests/test_auth_controller.py
import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from auth_controller import auth_controller

class TestAuthController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'test_user', 'password': 'test_pass'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Login successful')

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'test_user', 'password': 'wrong_pass'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['message'], 'Invalid credentials')

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_login_missing_username(self, mock_authenticate):
        response = self.client.post('/login', json={'password': 'test_pass'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['message'], 'Login failed')

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_login_missing_password(self, mock_authenticate):
        response = self.client.post('/login', json={'username': 'test_user'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['message'], 'Login failed')

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_login_non_json_request(self, mock_authenticate):
        response = self.client.post('/login', data='username=test_user&password=test_pass')
        self.assertEqual(response.status_code, 500)
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Login failed')


if __name__ == '__main__':
    unittest.main()
