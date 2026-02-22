# File: tests/test_auth_controller.py
import unittest
from unittest.mock import patch, MagicMock
from auth_controller import auth_controller
from flask import Flask, json

class TestAuthController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('auth_controller.auth_service.authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'test_user', 'password': 'test_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Login successful'})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'invalid_user', 'password': 'invalid_pass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json(), {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_missing_username(self, mock_authenticate):
        response = self.client.post('/login', json={'password': 'test_pass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json(), {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_missing_password(self, mock_authenticate):
        response = self.client.post('/login', json={'username': 'test_user'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json(), {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_service_exception(self, mock_authenticate):
        mock_authenticate.side_effect = Exception('Service failed')
        response = self.client.post('/login', json={'username': 'test_user', 'password': 'test_pass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {'message': 'Login failed'})

    def test_login_invalid_json(self):
        response = self.client.post('/login', data='invalid json')
        self.assertEqual(response.status_code, 500)
        self.assertIn('message', response.get_json())

if __name__ == '__main__':
    unittest.main()