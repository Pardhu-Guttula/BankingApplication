# File: tests/test_auth_controller.py
import unittest
from unittest.mock import patch, MagicMock
from flask import json
from auth_controller import auth_controller

class AuthControllerTest(unittest.TestCase):

    def setUp(self):
        app = auth_controller.test_client()
        self.client = app

    @patch('auth_controller.auth_service.authenticate')
    def test_login_success(self, mock_authenticate):
        mock_authenticate.return_value = True
        response = self.client.post('/login', data=json.dumps({'username': 'user1', 'password': 'pass1'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('auth_controller.auth_service.authenticate')
    def test_login_invalid_credentials(self, mock_authenticate):
        mock_authenticate.return_value = False
        response = self.client.post('/login', data=json.dumps({'username': 'user1', 'password': 'wrongpass'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('auth_controller.auth_service.authenticate')
    @patch('auth_controller.logging.error')
    def test_login_exception_handling(self, mock_logging_error, mock_authenticate):
        mock_authenticate.side_effect = Exception('Authentication Service Failure')
        response = self.client.post('/login', data=json.dumps({'username': 'user1', 'password': 'pass1'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})
        mock_logging_error.assert_called_once_with('Error in login: Authentication Service Failure')

    def test_login_missing_username(self):
        response = self.client.post('/login', data=json.dumps({'password': 'pass1'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    def test_login_missing_password(self):
        response = self.client.post('/login', data=json.dumps({'username': 'user1'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    def test_login_empty_payload(self):
        response = self.client.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    def test_login_invalid_content_type(self):
        response = self.client.post('/login', data='username=user1&password=pass1', content_type='text/plain')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    def test_login_null_payload(self):
        response = self.client.post('/login', data=None, content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()