# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch
from account_lockout_controller import account_lockout_controller
from flask import json

class TestAccountLockoutController(unittest.TestCase):

    def setUp(self):
        account_lockout_controller.testing = True
        self.client = account_lockout_controller.test_client()

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_success(self, mock_record_attempt_and_check_lockout):
        mock_record_attempt_and_check_lockout.return_value = (False, 'Login successful')
        response = self.client.post('/login', data=json.dumps({'user_id': 'test_user', 'password': 'test_password'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_locked_account(self, mock_record_attempt_and_check_lockout):
        mock_record_attempt_and_check_lockout.return_value = (True, 'Account locked')
        response = self.client.post('/login', data=json.dumps({'user_id': 'locked_user', 'password': 'test_password'}), content_type='application/json')
        self.assertEqual(response.status_code, 423)
        self.assertEqual(response.json, {'error': 'Account locked'})

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_invalid_credentials(self, mock_record_attempt_and_check_lockout):
        mock_record_attempt_and_check_lockout.return_value = (False, 'Invalid credentials')
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

    def test_login_empty_request_body(self):
        response = self.client.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()
