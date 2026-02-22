# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from account_lockout_controller import account_lockout_controller

class AccountLockoutControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Authenticated'))
    def test_login_success(self, mock_record_attempt):
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'test_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Authenticated'})

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Invalid credentials'))
    def test_login_invalid_credentials(self, mock_record_attempt):
        response = self.client.post('/login', json={'user_id': 'test_user2', 'password': 'wrong_pass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(True, 'Account locked'))
    def test_login_account_locked(self, mock_record_attempt):
        response = self.client.post('/login', json={'user_id': 'locked_user', 'password': 'test_pass'})
        self.assertEqual(response.status_code, 423)
        self.assertEqual(response.json, {'error': 'Account locked'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'test_pass'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_data(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_no_data(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()