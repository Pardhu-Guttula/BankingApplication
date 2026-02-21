# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, Mock
from flask import Flask
from auth_controller import auth_controller

class AuthControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('auth_controller.auth_service.authenticate')
    @patch('auth_controller.request')
    def test_login_success(self, mock_request, mock_authenticate):
        mock_authenticate.return_value = True
        mock_request.json = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('auth_controller.auth_service.authenticate')
    @patch('auth_controller.request')
    def test_login_invalid_credentials(self, mock_request, mock_authenticate):
        mock_authenticate.return_value = False
        mock_request.json = {'username': 'testuser', 'password': 'wrongpass'}
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service.authenticate')
    @patch('auth_controller.request')
    def test_login_missing_username(self, mock_request, mock_authenticate):
        mock_request.json = {'password': 'testpass'}
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service.authenticate')
    @patch('auth_controller.request')
    def test_login_missing_password(self, mock_request, mock_authenticate):
        mock_request.json = {'username': 'testuser'}
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service.authenticate')
    @patch('auth_controller.request')
    def test_login_exception(self, mock_request, mock_authenticate):
        mock_authenticate.side_effect = Exception('Some error')
        mock_request.json = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()
