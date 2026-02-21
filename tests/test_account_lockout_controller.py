# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from account_lockout_controller import account_lockout_controller

class AccountLockoutControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Login successful')):
            response = self.client.post('/login', data=json.dumps({'user_id': 'validuser', 'password': 'validpass'}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_invalid_data(self):
        response = self.client.post('/login', data=json.dumps({'user_id': 'validuser'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_account_locked(self):
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout', return_value=(True, 'Account locked')):
            response = self.client.post('/login', data=json.dumps({'user_id': 'lockeduser', 'password': 'validpass'}), content_type='application/json')
            self.assertEqual(response.status_code, 423)
            self.assertEqual(response.json, {'error': 'Account locked'})

    def test_login_authentication_failure(self):
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Authentication failed')):
            response = self.client.post('/login', data=json.dumps({'user_id': 'invaliduser', 'password': 'invalidpass'}), content_type='application/json')
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {'error': 'Authentication failed'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', data=json.dumps({'password': 'validpass'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', data=json.dumps({'user_id': 'validuser'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()