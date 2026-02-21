# File: tests/test_account_lockout_controller.py

import unittest
from flask import Flask, json
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller
from backend.authentication.services.account_lockout_service import AccountLockoutService
from unittest.mock import patch

class TestAccountLockoutController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    @patch.object(AccountLockoutService, 'record_attempt_and_check_lockout')
    def test_login_success(self, mock_record):
        mock_record.return_value = (False, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'user123', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Login successful'})

    @patch.object(AccountLockoutService, 'record_attempt_and_check_lockout')
    def test_login_locked_account(self, mock_record):
        mock_record.return_value = (True, 'Account locked due to too many failed attempts')
        response = self.client.post('/login', json={'user_id': 'user123', 'password': 'password'})
        self.assertEqual(response.status_code, 423)
        self.assertEqual(response.get_json(), {'error': 'Account locked due to too many failed attempts'})

    @patch.object(AccountLockoutService, 'record_attempt_and_check_lockout')
    def test_login_invalid_data(self, mock_record):
        response = self.client.post('/login', json={'user_id': 'user123'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    @patch.object(AccountLockoutService, 'record_attempt_and_check_lockout')
    def test_login_missing_request_body(self, mock_record):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    @patch.object(AccountLockoutService, 'record_attempt_and_check_lockout')
    def test_login_failed_authentication(self, mock_record):
        mock_record.return_value = (False, 'Invalid credentials')
        response = self.client.post('/login', json={'user_id': 'user123', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json(), {'error': 'Invalid credentials'})

if __name__ == '__main__':
    unittest.main()