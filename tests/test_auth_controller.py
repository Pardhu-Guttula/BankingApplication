# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from auth_controller import auth_controller

class AuthControllerTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.register_blueprint(auth_controller)
        cls.client = cls.app.test_client()

    @patch('auth_controller.auth_service')
    def test_login_successful(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'user', 'password': 'pass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('auth_controller.auth_service')
    def test_login_invalid_credentials(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'user', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service')
    def test_login_missing_username(self, mock_auth_service):
        response = self.client.post('/login', json={'password': 'pass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('auth_controller.auth_service')
    def test_login_missing_password(self, mock_auth_service):
        response = self.client.post('/login', json={'username': 'user'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('auth_controller.auth_service')
    def test_login_internal_server_error(self, mock_auth_service):
        mock_auth_service.authenticate.side_effect = Exception('Internal server error')
        response = self.client.post('/login', json={'username': 'user', 'password': 'pass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()