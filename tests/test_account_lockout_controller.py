# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, Mock
from flask import Flask, json
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller

class AccountLockoutControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    @patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_success(self, mock_record_attempt):
        mock_record_attempt.return_value = (False, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'testuser', 'password': 'correctpassword'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Login successful')

    @patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_locked(self, mock_record_attempt):
        mock_record_attempt.return_value = (True, 'Account is locked')
        response = self.client.post('/login', json={'user_id': 'lockeduser', 'password': 'any'})
        data = response.get_json()
        self.assertEqual(response.status_code, 423)
        self.assertEqual(data['error'], 'Account is locked')

    @patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_invalid_credentials(self, mock_record_attempt):
        mock_record_attempt.return_value = (False, 'Invalid credentials')
        response = self.client.post('/login', json={'user_id': 'testuser', 'password': 'wrongpassword'})
        data = response.get_json()
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['error'], 'Invalid credentials')

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'any'})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'testuser'})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

    def test_login_empty_json(self):
        response = self.client.post('/login', json={})
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

    def test_login_no_json(self):
        response = self.client.post('/login')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

if __name__ == '__main__':
    unittest.main()
