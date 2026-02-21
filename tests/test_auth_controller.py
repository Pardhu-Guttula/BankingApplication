# File: tests/test_auth_controller.py
import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from backend.authentication.controllers.auth_controller import auth_controller

class AuthControllerTests(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('backend.authentication.controllers.auth_controller.AuthService')
    def test_login_successful(self, MockAuthService):
        mock_auth_service_instance = MockAuthService.return_value
        mock_auth_service_instance.authenticate.return_value = True

        response = self.client.post('/login', json={
            'username': 'valid_user',
            'password': 'valid_pass'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Login successful'})

    @patch('backend.authentication.controllers.auth_controller.AuthService')
    def test_login_invalid_credentials(self, MockAuthService):
        mock_auth_service_instance = MockAuthService.return_value
        mock_auth_service_instance.authenticate.return_value = False

        response = self.client.post('/login', json={
            'username': 'invalid_user',
            'password': 'invalid_pass'
        })

        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data), {'message': 'Invalid credentials'})

    @patch('backend.authentication.controllers.auth_controller.AuthService')
    def test_login_missing_username(self, MockAuthService):
        response = self.client.post('/login', json={
            'password': 'password_only'
        })

        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data), {'message': 'Invalid credentials'})

    @patch('backend.authentication.controllers.auth_controller.AuthService')
    def test_login_missing_password(self, MockAuthService):
        response = self.client.post('/login', json={
            'username': 'username_only'
        })

        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data), {'message': 'Invalid credentials'})

    @patch('backend.authentication.controllers.auth_controller.AuthService')
    def test_login_empty_request_body(self, MockAuthService):
        response = self.client.post('/login', json={})

        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data), {'message': 'Invalid credentials'})

    @patch('backend.authentication.controllers.auth_controller.AuthService')
    def test_login_exception(self, MockAuthService):
        mock_auth_service_instance = MockAuthService.return_value
        mock_auth_service_instance.authenticate.side_effect = Exception('Test exception')

        response = self.client.post('/login', json={
            'username': 'error_user',
            'password': 'error_pass'
        })

        self.assertEqual(response.status_code, 500)
        self.assertEqual(json.loads(response.data), {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()
