# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from account_lock_controller import account_lock_controller

class AccountLockControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_success(self, mock_process_login):
        mock_process_login.return_value = (True, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'user1', 'password': 'password1'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Login successful')

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_invalid_credentials(self, mock_process_login):
        mock_process_login.return_value = (False, 'Invalid credentials')
        response = self.client.post('/login', json={'user_id': 'user1', 'password': 'wrong_password'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid credentials')

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'password1'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'user1'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

    def test_login_empty_body(self):
        response = self.client.post('/login', json={})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

    def test_login_no_json_body(self):
        response = self.client.post('/login')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

if __name__ == '__main__':
    unittest.main()
