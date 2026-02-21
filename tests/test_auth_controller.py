# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from backend.authentication.controllers.auth_controller import auth_controller
from backend.authentication.services.auth_service import AuthService

class AuthControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(auth_controller)
        self.client = self.app.test_client()

    @patch.object(AuthService, 'authenticate', return_value=True)
    def test_login_success(self, mock_authenticate):
        response = self.client.post('/login', json={'username': 'user1', 'password': 'pass1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})
        mock_authenticate.assert_called_with('user1', 'pass1')

    @patch.object(AuthService, 'authenticate', return_value=False)
    def test_login_invalid_credentials(self, mock_authenticate):
        response = self.client.post('/login', json={'username': 'user1', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})
        mock_authenticate.assert_called_with('user1', 'wrongpass')

    @patch.object(AuthService, 'authenticate', side_effect=Exception('Service error'))
    def test_login_service_exception(self, mock_authenticate):
        response = self.client.post('/login', json={'username': 'user1', 'password': 'pass1'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})
        mock_authenticate.assert_called_with('user1', 'pass1')

    def test_login_missing_data(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    def test_login_none_data(self):
        response = self.client.post('/login', data=None)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()