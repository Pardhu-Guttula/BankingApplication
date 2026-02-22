# File: tests/test_auth_controller.py
import json
from unittest import TestCase
from unittest.mock import patch
from flask import Flask
from auth_controller import auth_controller

class AuthControllerTests(TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', json={"username": "correct_user", "password": "correct_password"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Login successful"})

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_login_failure_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', json={"username": "incorrect_user", "password": "incorrect_password"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"message": "Invalid credentials"})

    def test_login_failure_no_request_data(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"message": "Invalid credentials"})

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_login_failure_exception(self, mock_authenticate):
        mock_authenticate.side_effect = Exception("Service error")
        response = self.client.post('/login', json={"username": "any_user", "password": "any_password"})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"message": "Login failed"})

    def test_login_failure_missing_username(self):
        response = self.client.post('/login', json={"password": "any_password"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"message": "Invalid credentials"})

    def test_login_failure_missing_password(self):
        response = self.client.post('/login', json={"username": "any_user"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"message": "Invalid credentials"})
