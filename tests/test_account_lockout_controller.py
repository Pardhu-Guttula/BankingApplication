# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from account_lockout_controller import account_lockout_controller

class TestAccountLockoutController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_successful(self, mock_record):
        mock_record.return_value = (False, 'Logged in successfully')
        response = self.client.post('/login', json={'user_id': 'user123', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Logged in successfully'})

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_locked_out(self, mock_record):
        mock_record.return_value = (True, 'Account locked')
        response = self.client.post('/login', json={'user_id': 'user123', 'password': 'password'})
        self.assertEqual(response.status_code, 423)
        self.assertEqual(response.json, {'error': 'Account locked'})

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_wrong_password(self, mock_record):
        mock_record.return_value = (False, 'Invalid credentials')
        success = False  # Mock the actual authentication check to fail
        response = self.client.post('/login', json={'user_id': 'user123', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_invalid_data(self, mock_record):
        response = self.client.post('/login', json={'user_id': 'user123'})  # Missing 'password'
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_no_data(self, mock_record):
        response = self.client.post('/login', json={})  # Missing both 'user_id' and 'password'
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()