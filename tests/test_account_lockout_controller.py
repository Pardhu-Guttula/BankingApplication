# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import json
from app import app

class TestAccountLockoutController(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login_success(self):
        with patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Login successful')):
            response = self.app.post('/login', data=json.dumps({'user_id': 'user1', 'password': 'correct_password'}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Login successful', response.get_data(as_text=True))

    def test_login_locked_account(self):
        with patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(True, 'Account locked due to too many failed attempts')):
            response = self.app.post('/login', data=json.dumps({'user_id': 'user1', 'password': 'correct_password'}), content_type='application/json')
            self.assertEqual(response.status_code, 423)
            self.assertIn('Account locked due to too many failed attempts', response.get_data(as_text=True))

    def test_login_invalid_credentials(self):
        with patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Invalid credentials')):
            response = self.app.post('/login', data=json.dumps({'user_id': 'user1', 'password': 'wrong_password'}), content_type='application/json')
            self.assertEqual(response.status_code, 401)
            self.assertIn('Invalid credentials', response.get_data(as_text=True))

    def test_login_missing_user_id(self):
        response = self.app.post('/login', data=json.dumps({'password': 'some_password'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid data', response.get_data(as_text=True))

    def test_login_missing_password(self):
        response = self.app.post('/login', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid data', response.get_data(as_text=True))

    def test_login_empty_request_body(self):
        response = self.app.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid data', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
