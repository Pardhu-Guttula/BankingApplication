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
    def test_login_success(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = True
        response = self.client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('backend.authentication.controllers.auth_controller.auth_service')
    def test_login_invalid_credentials(self, mock_auth_service):
        mock_auth_service.authenticate.return_value = False
        response = self.client.post('/login', json={'username': 'wronguser', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('backend.authentication.controllers.auth_controller.auth_service')
    def test_login_missing_password(self, mock_auth_service):
        response = self.client.post('/login', json={'username': 'testuser'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('backend.authentication.controllers.auth_controller.auth_service')
    def test_login_exception(self, mock_auth_service):
        mock_auth_service.authenticate.side_effect = Exception('Service failure')
        response = self.client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})
