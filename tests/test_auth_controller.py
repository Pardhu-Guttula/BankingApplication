# File: tests/test_auth_controller.py
import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from auth_controller import auth_controller, auth_service

class AuthControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        with patch.object(auth_service, 'authenticate', return_value=True):
            response = self.client.post('/login', json={'username': 'valid_user', 'password': 'valid_pass'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_invalid_credentials(self):
        with patch.object(auth_service, 'authenticate', return_value=False):
            response = self.client.post('/login', json={'username': 'invalid_user', 'password': 'invalid_pass'})
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_missing_username(self):
        response = self.client.post('/login', json={'password': 'some_pass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'username': 'some_user'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_invalid_json(self):
        response = self.client.post('/login', data='invalid_json', content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    def test_login_internal_server_error(self):
        with patch.object(auth_service, 'authenticate', side_effect=Exception('Test exception')):
            response = self.client.post('/login', json={'username': 'some_user', 'password': 'some_pass'})
            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()