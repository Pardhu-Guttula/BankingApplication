# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, Mock
from flask import Flask
from account_lockout_controller import account_lockout_controller

class TestAccountLockoutController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_success(self, mock_record_attempt_and_check_lockout):
        mock_record_attempt_and_check_lockout.return_value = (False, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'user', 'password': 'pass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_locked_account(self, mock_record_attempt_and_check_lockout):
        mock_record_attempt_and_check_lockout.return_value = (True, 'Account is locked')
        response = self.client.post('/login', json={'user_id': 'user', 'password': 'pass'})
        self.assertEqual(response.status_code, 423)
        self.assertEqual(response.json, {'error': 'Account is locked'})

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_invalid_credentials(self, mock_record_attempt_and_check_lockout):
        mock_record_attempt_and_check_lockout.return_value = (False, 'Invalid credentials')
        response = self.client.post('/login', json={'user_id': 'user', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'pass'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'user'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_no_json(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()
