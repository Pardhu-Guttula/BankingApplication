# File: tests/test_auth_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import json
from auth_controller import auth_controller

class AuthControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = auth_controller.test_client()
        self.app.testing = True

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.app.post('/login', data=json.dumps({'username': 'test_user', 'password': 'pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.app.post('/login', data=json.dumps({'username': 'test_user', 'password': 'wrong_pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_login_missing_data(self, mock_authenticate):
        mock_authenticate.side_effect = Exception('Missing data')
        response = self.app.post('/login', data=json.dumps({'username': 'test_user'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('backend.authentication.services.auth_service.AuthService.authenticate')
    def test_login_exception(self, mock_authenticate):
        mock_authenticate.side_effect = Exception('Unexpected error')
        response = self.app.post('/login', data=json.dumps({'username': 'test_user', 'password': 'pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()