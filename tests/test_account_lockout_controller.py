# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.account_lockout_controller import account_lockout_controller
from backend.authentication.services.account_lockout_service import AccountLockoutService

class TestAccountLockoutController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        with patch.object(AccountLockoutService, 'record_attempt_and_check_lockout') as mock_record:
            mock_record.return_value = (False, "Login successful.")
            response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'test_password'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful.'})

    def test_login_lockout(self):
        with patch.object(AccountLockoutService, 'record_attempt_and_check_lockout') as mock_record:
            mock_record.return_value = (True, "Account is locked.")
            response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'test_password'})
            self.assertEqual(response.status_code, 423)
            self.assertEqual(response.json, {'error': 'Account is locked.'})

    def test_login_invalid_data(self):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_wrong_credentials(self):
        with patch.object(AccountLockoutService, 'record_attempt_and_check_lockout') as mock_record:
            mock_record.return_value = (False, "Invalid credentials.")
            response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'wrong_password'})
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {'error': 'Invalid credentials.'})

    def test_login_no_data(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()
