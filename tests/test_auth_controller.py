# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify
from auth_controller import auth_controller

class TestAuthController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('auth_controller.auth_service.authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'user1', 'password': 'password1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_failure_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'user1', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.request')
    def test_login_failure_missing_json_body(self, mock_request):
        mock_request.json = None
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('auth_controller.request')
    @patch('auth_controller.auth_service.authenticate')
    def test_login_failure_exception_handling(self, mock_authenticate, mock_request):
        mock_request.json = {'username': 'user1', 'password': 'password1'}
        mock_authenticate.side_effect = Exception('Forced Exception')
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()