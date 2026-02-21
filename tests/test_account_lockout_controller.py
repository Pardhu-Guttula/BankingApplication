# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify
from account_lockout_controller import account_lockout_controller

class TestAccountLockoutController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_successful(self, mock_record_attempt):
        mock_record_attempt.return_value = (False, 'Login successful')
        response = self.client.post('/login', json={
            'user_id': 'test_user',
            'password': 'test_password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Login successful'})

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_account_locked(self, mock_record_attempt):
        mock_record_attempt.return_value = (True, 'Account locked due to multiple failed attempts')
        response = self.client.post('/login', json={
            'user_id': 'test_user',
            'password': 'test_password'
        })
        self.assertEqual(response.status_code, 423)
        self.assertEqual(response.get_json(), {'error': 'Account locked due to multiple failed attempts'})

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_failed(self, mock_record_attempt):
        mock_record_attempt.return_value = (False, 'Invalid username or password')
        response = self.client.post('/login', json={
            'user_id': 'test_user',
            'password': 'wrong_password'
        })
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json(), {'error': 'Invalid username or password'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={
            'password': 'test_password'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={
            'user_id': 'test_user'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_empty_request(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_no_data(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()