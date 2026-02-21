# File: tests/test_auth_controller.py

import unittest
from flask import json
from flask.testing import FlaskClient
from backend.authentication.controllers.auth_controller import auth_controller, auth_service

class AuthControllerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = auth_controller.test_client()

    def setUp(self):
        self.auth_service_mock = auth_service

    def test_login_success(self):
        self.auth_service_mock.authenticate = lambda u, p: True
        response = self.client.post('/login', data=json.dumps({'username': 'valid_user', 'password': 'valid_pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_invalid_credentials(self):
        self.auth_service_mock.authenticate = lambda u, p: False
        response = self.client.post('/login', data=json.dumps({'username': 'invalid_user', 'password': 'invalid_pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_missing_username(self):
        response = self.client.post('/login', data=json.dumps({'password': 'pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_missing_password(self):
        response = self.client.post('/login', data=json.dumps({'username': 'user'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_no_data(self):
        response = self.client.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    def test_login_exception(self):
        self.auth_service_mock.authenticate = lambda u, p: (_ for _ in ()).throw(Exception("Error"))
        response = self.client.post('/login', data=json.dumps({'username': 'user', 'password': 'pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

if __name__ == '__main__':
    unittest.main()