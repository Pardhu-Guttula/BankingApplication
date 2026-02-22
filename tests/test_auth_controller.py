# File: tests/test_auth_controller.py
import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from auth_controller import auth_controller

class AuthServiceMock:
    def authenticate(self, username, password):
        if username == 'valid_user' and password == 'valid_pass':
            return True
        return False

class AuthControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('auth_controller.auth_service', new_callable=lambda: AuthServiceMock())
    def test_login_success(self, mock_auth_service):
        response = self.client.post('/login', json={'username': 'valid_user', 'password': 'valid_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('auth_controller.auth_service', new_callable=lambda: AuthServiceMock())
    def test_login_invalid_credentials(self, mock_auth_service):
        response = self.client.post('/login', json={'username': 'invalid_user', 'password': 'invalid_pass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service', new_callable=lambda: AuthServiceMock())
    def test_login_missing_username(self, mock_auth_service):
        response = self.client.post('/login', json={'password': 'valid_pass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service', new_callable=lambda: AuthServiceMock())
    def test_login_missing_password(self, mock_auth_service):
        response = self.client.post('/login', json={'username': 'valid_user'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service', new_callable=lambda: AuthServiceMock())
    def test_login_empty_request_body(self, mock_auth_service):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service', new_callable=lambda: AuthServiceMock())
    def test_login_no_json_body(self, mock_auth_service):
        response = self.client.post('/login', data='not a json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service', new_callable=lambda: AuthServiceMock())
    @patch('auth_controller.logging.error')
    def test_login_exception(self, mock_logging_error, mock_auth_service):
        mock_auth_service.authenticate.side_effect = Exception('Unexpected error')
        response = self.client.post('/login', json={'username': 'valid_user', 'password': 'valid_pass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})
        mock_logging_error.assert_called_once_with('Error in login: Unexpected error')

if __name__ == '__main__':
    unittest.main()
