# File: tests/test_auth_controller.py
import unittest
from unittest.mock import patch, MagicMock
from flask import json
from auth_controller import auth_controller
from backend.authentication.services.auth_service import AuthService

class AuthControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = auth_controller.test_client()
        self.app.testing = True
        self.auth_service_patcher = patch('auth_controller.auth_service', autospec=True)
        self.mock_auth_service = self.auth_service_patcher.start()

    def tearDown(self):
        self.auth_service_patcher.stop()

    def test_login_successful(self):
        self.mock_auth_service.authenticate.return_value = True
        response = self.app.post('/login', data=json.dumps({'username': 'test', 'password': 'pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.get_json(), {'message': 'Login successful'})

    def test_login_invalid_credentials(self):
        self.mock_auth_service.authenticate.return_value = False
        response = self.app.post('/login', data=json.dumps({'username': 'test', 'password': 'wrongpass'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertDictEqual(response.get_json(), {'message': 'Invalid credentials'})

    def test_login_missing_username(self):
        response = self.app.post('/login', data=json.dumps({'password': 'pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertDictEqual(response.get_json(), {'message': 'Login failed'})

    def test_login_missing_password(self):
        response = self.app.post('/login', data=json.dumps({'username': 'test'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertDictEqual(response.get_json(), {'message': 'Login failed'})

    def test_login_with_invalid_json(self):
        response = self.app.post('/login', data='Invalid JSON', content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertDictEqual(response.get_json(), {'message': 'Login failed'})

    def test_login_service_throws_exception(self):
        self.mock_auth_service.authenticate.side_effect = Exception('Test Exception')
        response = self.app.post('/login', data=json.dumps({'username': 'test', 'password': 'pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertDictEqual(response.get_json(), {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()
