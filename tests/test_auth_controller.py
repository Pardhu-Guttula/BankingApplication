# File: tests/test_auth_controller.py
import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify
from auth_controller import auth_controller

class AuthControllerTestCase(unittest.TestCase):

    @patch('auth_controller.auth_service.authenticate')
    def setUp(self, mock_auth_service):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()
        self.mock_auth_service = mock_auth_service

    def test_login_successful(self):
        self.mock_auth_service.authenticate.return_value = True
        response = self.client.post('/login', json={"username": "admin", "password": "admin"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Login successful"})

    def test_invalid_credentials(self):
        self.mock_auth_service.authenticate.return_value = False
        response = self.client.post('/login', json={"username": "admin", "password": "wrongpassword"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"message": "Invalid credentials"})

    def test_login_missing_username(self):
        response = self.client.post('/login', json={"password": "admin"})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"message": "Login failed"})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={"username": "admin"})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"message": "Login failed"})

    @patch('auth_controller.request')
    def test_login_json_error(self, mock_request):
        mock_request.json = None
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"message": "Login failed"})

    @patch('auth_controller.logging.error')
    @patch('auth_controller.request.json', side_effect=Exception('Test Exception'))
    def test_login_general_exception(self, mock_request_json, mock_logging_error):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"message": "Login failed"})
        mock_logging_error.assert_called_with('Error in login: Test Exception')

if __name__ == '__main__':
    unittest.main()