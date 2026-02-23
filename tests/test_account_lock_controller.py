# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from account_lock_controller import account_lock_controller

class AccountLockControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    def test_login_successful(self):
        data = {'user_id': 'valid_user', 'password': 'valid_password'}
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login') as mock_process_login:
            mock_process_login.return_value = (True, 'Login successful')
            response = self.client.post('/login', json=data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), {'message': 'Login successful'})

    def test_login_invalid_data(self):
        data = {'user_id': 'valid_user'}  # Missing password
        response = self.client.post('/login', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_failure(self):
        data = {'user_id': 'invalid_user', 'password': 'invalid_password'}
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login') as mock_process_login:
            mock_process_login.return_value = (False, 'Login failed')
            response = self.client.post('/login', json=data)
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.get_json(), {'error': 'Login failed'})

    def test_login_missing_user_id(self):
        data = {'password': 'password_only'}
        response = self.client.post('/login', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_missing_password(self):
        data = {'user_id': 'user_only'}
        response = self.client.post('/login', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_empty_body(self):
        data = {}
        response = self.client.post('/login', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_invalid_json(self):
        response = self.client.post('/login', data="not a json")
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()