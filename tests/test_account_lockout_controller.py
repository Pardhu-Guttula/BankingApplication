# File: tests/test_account_lockout_controller.py

import unittest
from flask import Flask, json
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller
from backend.authentication.services.account_lockout_service import AccountLockoutService
from unittest.mock import patch, MagicMock

class AccountLockoutControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_success(self, mock_record_attempt):
        mock_record_attempt.return_value = (False, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'user1', 'password': 'password1'})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Login successful')

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_locked_out(self, mock_record_attempt):
        mock_record_attempt.return_value = (True, 'Account locked out')
        response = self.client.post('/login', json={'user_id': 'user1', 'password': 'password1'})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 423)
        self.assertEqual(data['error'], 'Account locked out')

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_unauthorized(self, mock_record_attempt):
        mock_record_attempt.return_value = (False, 'Invalid credentials')
        response = self.client.post('/login', json={'user_id': 'user1', 'password': 'wrongpassword'})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['error'], 'Invalid credentials')

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'password1'})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'user1'})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

    def test_login_missing_data(self):
        response = self.client.post('/login', json={})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

    def test_login_no_json(self):
        response = self.client.post('/login')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

if __name__ == '__main__':
    unittest.main()