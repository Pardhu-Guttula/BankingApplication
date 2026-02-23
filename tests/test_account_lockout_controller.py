# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from account_lockout_controller import account_lockout_controller

class TestAccountLockoutController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    def test_login_successful(self):
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout') as mock_service:
            mock_service.return_value = (False, 'Login Successful')
            response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'password'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), {'message': 'Login Successful'})

    def test_login_user_locked_out(self):
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout') as mock_service:
            mock_service.return_value = (True, 'User is locked out')
            response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'password'})
            self.assertEqual(response.status_code, 423)
            self.assertEqual(response.get_json(), {'error': 'User is locked out'})

    def test_login_invalid_credentials(self):
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout') as mock_service:
            mock_service.return_value = (False, 'Invalid credentials')
            response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'wrong_password'})
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.get_json(), {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()
