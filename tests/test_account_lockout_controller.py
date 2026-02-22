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

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_success(self, mock_record):
        mock_record.return_value = (False, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'user123', 'password': 'correct_password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Login successful'})

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_failure(self, mock_record):
        mock_record.return_value = (False, 'Login failed')
        response = self.client.post('/login', json={'user_id': 'user123', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json(), {'error': 'Login failed'})

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_user_locked(self, mock_record):
        mock_record.return_value = (True, 'User account locked')
        response = self.client.post('/login', json={'user_id': 'locked_user', 'password': 'any_password'})
        self.assertEqual(response.status_code, 423)
        self.assertEqual(response.get_json(), {'error': 'User account locked'})

    def test_login_invalid_data(self):
        response = self.client.post('/login', json={'user_id': 'user123'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})
        
        response = self.client.post('/login', json={'password': 'password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})
        
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()