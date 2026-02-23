# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch
from flask import Flask, json
from account_lock_controller import account_lock_controller
from backend.authentication.services.account_lock_service import AccountLockService

class AccountLockControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller, url_prefix='/auth')
        self.client = self.app.test_client()

    def test_login_success(self):
        with patch.object(AccountLockService, 'process_login', return_value=(True, '')) as mock_process_login:
            response = self.client.post('/auth/login', json={'user_id': 'test_user', 'password': 'test_password'})
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data, {'message': 'Login successful'})
            mock_process_login.assert_called_once_with('test_user', 'test_password')

    def test_login_invalid_data(self):
        response = self.client.post('/auth/login', json={'user_id': 'test_user'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data, {'error': 'Invalid data'})

        response = self.client.post('/auth/login', json={'password': 'test_password'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data, {'error': 'Invalid data'})

        response = self.client.post('/auth/login', json={})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data, {'error': 'Invalid data'})

    def test_login_invalid_json(self):
        response = self.client.post('/auth/login', data='invalid_json', content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login_process_login_failure(self):
        with patch.object(AccountLockService, 'process_login', return_value=(False, 'Account locked')) as mock_process_login:
            response = self.client.post('/auth/login', json={'user_id': 'test_user', 'password': 'test_password'})
            data = json.loads(response.data)
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data, {'error': 'Account locked'})
            mock_process_login.assert_called_once_with('test_user', 'test_password')

if __name__ == '__main__':
    unittest.main()