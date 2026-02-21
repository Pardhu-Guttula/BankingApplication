# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, Mock
from flask import Flask, json
from backend.authentication.controllers.auth_controller import auth_controller

class TestAuthController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('backend.authentication.controllers.auth_controller.auth_service')
    def test_login_successful(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Login successful'})

    @patch('backend.authentication.controllers.auth_controller.auth_service')
    def test_login_invalid_credentials(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'testuser', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json(), {'message': 'Invalid credentials'})

    def test_login_missing_username(self):
        response = self.client.post('/login', json={'password': 'testpass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {'message': 'Login failed'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'username': 'testuser'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {'message': 'Login failed'})

    def test_login_no_json(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.get_json(), {'message': 'Login failed'})

    @patch('backend.authentication.controllers.auth_controller.logging')
    def test_login_exception_logging(self, mock_logging):
        with patch('backend.authentication.controllers.auth_controller.auth_service.authenticate', side_effect=Exception('test exception')):
            response = self.client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
            self.assertEqual(response.status_code, 500)
            self.assertEqual(response.get_json(), {'message': 'Login failed'})
            mock_logging.error.assert_called_once_with('Error in login: test exception')

if __name__ == '__main__':
    unittest.main()
