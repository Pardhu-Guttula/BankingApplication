# File: tests/test_account_lockout_controller.py

import unittest
from flask import Flask, json
from account_lockout_controller import account_lockout_controller
from unittest.mock import patch

class AccountLockoutControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        with patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Login successful')):
            response = self.client.post('/login', data=json.dumps({'user_id': 'test_user', 'password': 'test_password'}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_account_locked(self):
        with patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(True, 'Account locked')):
            response = self.client.post('/login', data=json.dumps({'user_id': 'test_user', 'password': 'test_password'}), content_type='application/json')
            self.assertEqual(response.status_code, 423)
            self.assertEqual(response.json, {'error': 'Account locked'})

    def test_login_invalid_credentials(self):
        with patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Invalid credentials')):
            response = self.client.post('/login', data=json.dumps({'user_id': 'test_user', 'password': 'wrong_password'}), content_type='application/json')
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', data=json.dumps({'password': 'test_password'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', data=json.dumps({'user_id': 'test_user'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_invalid_json(self):
        response = self.client.post('/login', data='invalid json', content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
