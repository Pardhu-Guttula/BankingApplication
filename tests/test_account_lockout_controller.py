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

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'password123'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'user123'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_successful(self):
        with patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Login successful')) as mock_service:
            response = self.client.post('/login', json={'user_id': 'user123', 'password': 'password123'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})
            mock_service.assert_called_once_with('user123', True)

    def test_login_account_locked(self):
        with patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(True, 'Account locked due to multiple failed attempts')) as mock_service:
            response = self.client.post('/login', json={'user_id': 'user123', 'password': 'password123'})
            self.assertEqual(response.status_code, 423)
            self.assertEqual(response.json, {'error': 'Account locked due to multiple failed attempts'})
            mock_service.assert_called_once_with('user123', True)

    def test_login_unsuccessful(self):
        with patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Invalid credentials')) as mock_service:
            response = self.client.post('/login', json={'user_id': 'user123', 'password': 'wrongpassword'})
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {'error': 'Invalid credentials'})
            mock_service.assert_called_once_with('user123', True)

if __name__ == '__main__':
    unittest.main()