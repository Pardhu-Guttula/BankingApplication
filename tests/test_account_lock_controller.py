# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch, Mock
from flask import Flask
from account_lock_controller import account_lock_controller

class AccountLockControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_success(self, mock_process_login):
        mock_process_login.return_value = (True, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'test_password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Login successful'})

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_failure(self, mock_process_login):
        mock_process_login.return_value = (False, 'Incorrect password')
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Incorrect password'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'test_password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_empty_data(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_no_data(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()
