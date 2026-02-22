# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from account_lockout_controller import account_lockout_controller

class TestAccountLockoutController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_success(self, mock_record_attempt_and_check_lockout):
        mock_record_attempt_and_check_lockout.return_value = (False, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'user1', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Login successful'})

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_fail(self, mock_record_attempt_and_check_lockout):
        mock_record_attempt_and_check_lockout.return_value = (False, 'Login failed')
        response = self.client.post('/login', json={'user_id': 'user1', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json(), {'error': 'Login failed'})

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_account_locked(self, mock_record_attempt_and_check_lockout):
        mock_record_attempt_and_check_lockout.return_value = (True, 'Account locked')
        response = self.client.post('/login', json={'user_id': 'user1', 'password': 'password'})
        self.assertEqual(response.status_code, 423)
        self.assertEqual(response.get_json(), {'error': 'Account locked'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'user1'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_invalid_request_data(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()