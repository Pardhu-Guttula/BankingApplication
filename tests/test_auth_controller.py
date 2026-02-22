# File: tests/test_auth_controller.py
import unittest
from unittest.mock import patch, MagicMock
from flask import json
from auth_controller import auth_controller
from backend.authentication.services.auth_service import AuthService

class AuthControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = auth_controller.test_client()
        self.app.testing = True

    @patch.object(AuthService, 'authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.app.post('/login', data=json.dumps({'username': 'user1', 'password': 'pass1'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Login successful')

    @patch.object(AuthService, 'authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.app.post('/login', data=json.dumps({'username': 'user1', 'password': 'wrongpass'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['message'], 'Invalid credentials')

    @patch.object(AuthService, 'authenticate')
    def test_login_missing_username(self, mock_authenticate):
        response = self.app.post('/login', data=json.dumps({'password': 'pass1'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json['message'], 'Login failed')

    @patch.object(AuthService, 'authenticate')
    def test_login_missing_password(self, mock_authenticate):
        response = self.app.post('/login', data=json.dumps({'username': 'user1'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json['message'], 'Login failed')

    @patch.object(AuthService, 'authenticate')
    def test_login_exception(self, mock_authenticate):
        mock_authenticate.side_effect = Exception('Simulated error')
        response = self.app.post('/login', data=json.dumps({'username': 'user1', 'password': 'pass1'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json['message'], 'Login failed')

if __name__ == '__main__':
    unittest.main()