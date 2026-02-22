# File: tests/test_auth_controller.py
import unittest
import json
from unittest.mock import patch, MagicMock
from flask import Flask
from auth_controller import auth_controller

class TestAuthController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('auth_controller.auth_service.authenticate')
    @patch('auth_controller.request')
    def test_login_success(self, mock_request, mock_authenticate):
        mock_request.json = {'username': 'testuser', 'password': 'testpass'}
        mock_authenticate.return_value = True
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Login successful"})

    @patch('auth_controller.auth_service.authenticate')
    @patch('auth_controller.request')
    def test_login_invalid_credentials(self, mock_request, mock_authenticate):
        mock_request.json = {'username': 'wronguser', 'password': 'wrongpass'}
        mock_authenticate.return_value = False
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json(), {"message": "Invalid credentials"})

    @patch('auth_controller.auth_service.authenticate')
    @patch('auth_controller.request')
    def test_login_missing_username(self, mock_request, mock_authenticate):
        mock_request.json = {'password': 'testpass'}
        mock_authenticate.side_effect = Exception('Invalid input')
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {"message": "Login failed"})

    @patch('auth_controller.auth_service.authenticate')
    @patch('auth_controller.request')
    def test_login_missing_password(self, mock_request, mock_authenticate):
        mock_request.json = {'username': 'testuser'}
        mock_authenticate.side_effect = Exception('Invalid input')
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {"message": "Login failed"})

    @patch('auth_controller.auth_service.authenticate')
    @patch('auth_controller.request')
    def test_login_json_none(self, mock_request, mock_authenticate):
        mock_request.json = None
        mock_authenticate.side_effect = Exception('Invalid input')
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {"message": "Login failed"})

if __name__ == '__main__':
    unittest.main()
