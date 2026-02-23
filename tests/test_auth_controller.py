# File: tests/test_auth_controller.py
from flask import json
from flask.testing import FlaskClient
import unittest
from unittest.mock import patch, MagicMock
from auth_controller import auth_controller

class AuthControllerTestCase(unittest.TestCase):

    def setUp(self):
        self.client = FlaskClient(auth_controller)

    @patch('auth_controller.auth_service')
    def test_login_success(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'test_user', 'password': 'test_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"message": "Login successful"})

    @patch('auth_controller.auth_service')
    def test_login_invalid_credentials(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'test_user', 'password': 'wrong_pass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(json.loads(response.data), {"message": "Invalid credentials"})

    @patch('auth_controller.auth_service')
    def test_login_missing_fields(self, mock_auth_service):
        response = self.client.post('/login', json={'username': 'test_user'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(json.loads(response.data), {"message": "Login failed"})

    @patch('auth_controller.auth_service')
    def test_login_exception(self, mock_auth_service):
        mock_auth_service.authenticate.side_effect = Exception('test')
        response = self.client.post('/login', json={'username': 'test_user', 'password': 'test_pass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(json.loads(response.data), {"message": "Login failed"})

    @patch('auth_controller.auth_service')
    def test_register_success(self, mock_auth_service):
        mock_auth_service.register.return_value = True
        response = self.client.post('/register', json={'name': 'test_name', 'email': 'test_email', 'password': 'test_pass'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), {"message": "Registration successful. Please check your email for confirmation."})

    @patch('auth_controller.auth_service')
    def test_register_email_in_use(self, mock_auth_service):
        mock_auth_service.register.return_value = False
        response = self.client.post('/register', json={'name': 'test_name', 'email': 'test_email', 'password': 'test_pass'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {"message": "Registration failed, email may already be in use."})

    @patch('auth_controller.auth_service')
    def test_register_missing_fields(self, mock_auth_service):
        response = self.client.post('/register', json={'name': 'test_name', 'email': 'test_email'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(json.loads(response.data), {"message": "Registration failed"})

    @patch('auth_controller.auth_service')
    def test_register_exception(self, mock_auth_service):
        mock_auth_service.register.side_effect = Exception('test')
        response = self.client.post('/register', json={'name': 'test_name', 'email': 'test_email', 'password': 'test_pass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(json.loads(response.data), {"message": "Registration failed"})

    @patch('auth_controller.auth_service')
    def test_logout_success(self, mock_auth_service):
        response = self.client.post('/logout')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"message": "Logout successful"})

    @patch('auth_controller.auth_service')
    def test_logout_exception(self, mock_auth_service):
        mock_auth_service.logout.side_effect = Exception('test')
        response = self.client.post('/logout')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(json.loads(response.data), {"message": "Logout failed"})

if __name__ == '__main__':
    unittest.main()