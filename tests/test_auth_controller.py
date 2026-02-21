# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json

from auth_controller import auth_controller

class AuthControllerTests(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    def test_login_successful(self):
        with patch('backend.authentication.services.auth_service.AuthService.authenticate', return_value=True):
            response = self.client.post('/login', json={'username': 'test', 'password': 'test'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_invalid_credentials(self):
        with patch('backend.authentication.services.auth_service.AuthService.authenticate', return_value=False):
            response = self.client.post('/login', json={'username': 'test', 'password': 'wrong'})
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_missing_username(self):
        response = self.client.post('/login', json={'password': 'test'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'username': 'test'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_no_json_body(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_service_exception(self):
        with patch('backend.authentication.services.auth_service.AuthService.authenticate', side_effect=Exception('Service failure')):
            response = self.client.post('/login', json={'username': 'test', 'password': 'test'})
            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()