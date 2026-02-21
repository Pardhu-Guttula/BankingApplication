# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from auth_controller import auth_controller

class TestAuthController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('auth_controller.auth_service.authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = True

        response = self.client.post('/login', data=json.dumps({
            'username': 'valid_user',
            'password': 'valid_password'
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False

        response = self.client.post('/login', data=json.dumps({
            'username': 'invalid_user',
            'password': 'invalid_password'
        }), content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_missing_username(self, mock_authenticate):
        response = self.client.post('/login', data=json.dumps({
            'password': 'some_password'
        }), content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_missing_password(self, mock_authenticate):
        response = self.client.post('/login', data=json.dumps({
            'username': 'some_user'
        }), content_type='application/json')

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_exception(self):
        with patch('auth_controller.auth_service.authenticate', side_effect=Exception('Some error')):
            response = self.client.post('/login', data=json.dumps({
                'username': 'user',
                'password': 'pass'
            }), content_type='application/json')

            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()