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
    def test_login_successful(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'user', 'password': 'pass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'user', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_missing_username(self):
        response = self.client.post('/login', json={'password': 'pass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'username': 'user'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    def test_login_no_data(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    def test_login_invalid_json(self):
        response = self.client.post('/login', data='invalid json', content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()