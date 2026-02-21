# File: tests/test_account_lockout_controller.py
import unittest
from unittest.mock import patch
from flask import json
from account_lockout_controller import account_lockout_controller

class TestAccountLockoutController(unittest.TestCase):
    def setUp(self):
        self.app = account_lockout_controller.test_client()
        self.app.testing = True

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_success(self, mock_record_attempt_and_check_lockout):
        mock_record_attempt_and_check_lockout.return_value = (False, 'Login successful')
        response = self.app.post('/login', data=json.dumps({'user_id': 'user1', 'password': 'password'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_invalid_data(self, mock_record_attempt_and_check_lockout):
        response = self.app.post('/login', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_user_locked(self, mock_record_attempt_and_check_lockout):
        mock_record_attempt_and_check_lockout.return_value = (True, 'Account locked')
        response = self.app.post('/login', data=json.dumps({'user_id': 'user1', 'password': 'password'}), content_type='application/json')
        self.assertEqual(response.status_code, 423)
        self.assertEqual(response.json, {'error': 'Account locked'})

    @patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_unauthorized(self, mock_record_attempt_and_check_lockout):
        mock_record_attempt_and_check_lockout.return_value = (False, 'Invalid credentials')
        success = False  # Simulate authentication failure
        response = self.app.post('/login', data=json.dumps({'user_id': 'user1', 'password': 'wrong_password'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

if __name__ == '__main__':
    unittest.main()
