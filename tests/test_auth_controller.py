# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, Mock
from flask import Flask, json
from auth_controller import auth_controller

class TestAuthController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('auth_controller.auth_service')
    def test_login_successful(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'user1', 'password': 'securepassword'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Login successful'})

    @patch('auth_controller.auth_service')
    def test_login_invalid_credentials(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'user1', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json(), {'message': 'Invalid credentials'})

    def test_login_missing_username(self):
        response = self.client.post('/login', json={'password': 'securepassword'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {'message': 'Login failed'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'username': 'user1'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {'message': 'Login failed'})

    def test_login_empty_payload(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {'message': 'Login failed'})

    def test_login_invalid_payload(self):
        response = self.client.post('/login', data='invalid json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {'message': 'Login failed'})
        
    @patch('auth_controller.auth_service')
    def test_login_raises_exception(self, mock_auth_service):
        mock_auth_service.authenticate.side_effect = Exception('Unexpected error')
        response = self.client.post('/login', json={'username': 'user1', 'password': 'securepassword'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()