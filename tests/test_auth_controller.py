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

    @patch('auth_controller.auth_service.authenticate')
    def test_login_successful(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'test', 'password': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'test', 'password': 'wrong'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.request')
    def test_login_missing_username(self, mock_request):
        mock_request.json = {'password': 'test'}
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.request')
    def test_login_missing_password(self, mock_request):
        mock_request.json = {'username': 'test'}
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.request')
    def test_login_no_json_payload(self, mock_request):
        mock_request.json = None
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('auth_controller.auth_service.authenticate')
    @patch('auth_controller.request')
    def test_login_auth_service_exception(self, mock_request, mock_authenticate):
        mock_request.json = {'username': 'test', 'password': 'test'}
        mock_authenticate.side_effect = Exception('Service error')
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()