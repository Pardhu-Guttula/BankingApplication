# File: tests/test_auth_controller.py

import unittest
from unittest.mock import MagicMock, patch
from flask import json
from backend.authentication.controllers.auth_controller import auth_controller
from backend.app import create_app

class AuthControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    @patch('backend.authentication.controllers.auth_controller.auth_service')
    def test_login_success(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = True
        response = self.app.post('/login', data=json.dumps(dict(username='test_user', password='test_pass')), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Login successful"})

    @patch('backend.authentication.controllers.auth_controller.auth_service')
    def test_login_invalid_credentials(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = False
        response = self.app.post('/login', data=json.dumps(dict(username='wrong_user', password='wrong_pass')), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"message": "Invalid credentials"})

    @patch('backend.authentication.controllers.auth_controller.auth_service')
    def test_login_exception(self, mock_auth_service):
        mock_auth_service.authenticate.side_effect = Exception('Unexpected Error')
        response = self.app.post('/login', data=json.dumps(dict(username='test_user', password='test_pass')), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"message": "Login failed"})

    @patch('backend.authentication.controllers.auth_controller.auth_service')
    def test_register_success(self, mock_auth_service):
        mock_auth_service.register.return_value = True
        response = self.app.post('/register', data=json.dumps(dict(name='test_name', email='test_email', password='test_pass')), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Registration successful. Please check your email for confirmation."})

    @patch('backend.authentication.controllers.auth_controller.auth_service')
    def test_register_email_in_use(self, mock_auth_service):
        mock_auth_service.register.return_value = False
        response = self.app.post('/register', data=json.dumps(dict(name='test_name', email='existing_email', password='test_pass')), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"message": "Registration failed, email may already be in use."})

    @patch('backend.authentication.controllers.auth_controller.auth_service')
    def test_register_exception(self, mock_auth_service):
        mock_auth_service.register.side_effect = Exception('Unexpected Error')
        response = self.app.post('/register', data=json.dumps(dict(name='test_name', email='test_email', password='test_pass')), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"message": "Registration failed"})

    @patch('backend.authentication.controllers.auth_controller.auth_service')
    def test_logout_success(self, mock_auth_service):
        response = self.app.post('/logout')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Logout successful"})

    @patch('backend.authentication.controllers.auth_controller.auth_service')
    def test_logout_exception(self, mock_auth_service):
        mock_auth_service.logout.side_effect = Exception('Unexpected Error')
        response = self.app.post('/logout')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"message": "Logout failed"})

if __name__ == '__main__':
    unittest.main()