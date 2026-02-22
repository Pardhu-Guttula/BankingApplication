# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import json
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller

class AccountLockoutControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = account_lockout_controller.test_client()
        self.app.testing = True

    def test_login_success(self):
        with patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Login successful')):
            response = self.app.post('/login', data=json.dumps({'user_id': 'test_user', 'password': 'test_pass'}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], 'Login successful')

    def test_login_account_locked(self):
        with patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(True, 'Account locked temporarily')):
            response = self.app.post('/login', data=json.dumps({'user_id': 'test_user', 'password': 'test_pass'}), content_type='application/json')
            self.assertEqual(response.status_code, 423)
            self.assertEqual(response.json['error'], 'Account locked temporarily')

    def test_login_invalid_credentials(self):
        with patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Invalid credentials')):
            response = self.app.post('/login', data=json.dumps({'user_id': 'test_user', 'password': 'wrong_pass'}), content_type='application/json')
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json['error'], 'Invalid credentials')

    def test_login_invalid_data(self):
        response = self.app.post('/login', data=json.dumps({'user_id': 'test_user'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Invalid data')

        response = self.app.post('/login', data=json.dumps({'password': 'test_pass'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Invalid data')

    def test_login_no_data(self):
        response = self.app.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Invalid data')

    def test_login_non_json_data(self):
        response = self.app.post('/login', data='non-json-data', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['error'], 'Invalid data')

if __name__ == '__main__':
    unittest.main()