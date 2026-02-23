# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch
from flask import json
from account_lockout_controller import account_lockout_controller
from app import create_app

class AccountLockoutControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_login_success(self):
        data = {'user_id': 'test_user', 'password': 'correct_password'}
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Login successful')):
            response = self.app.post('/login', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_user_locked_out(self):
        data = {'user_id': 'test_user', 'password': 'correct_password'}
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout', return_value=(True, 'User account is locked')):
            response = self.app.post('/login', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 423)
            self.assertEqual(response.json, {'error': 'User account is locked'})

    def test_login_failure(self):
        data = {'user_id': 'test_user', 'password': 'wrong_password'}
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Login failed')):
            response = self.app.post('/login', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {'error': 'Login failed'})

    def test_login_missing_user_id(self):
        data = {'password': 'some_password'}
        response = self.app.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        data = {'user_id': 'test_user'}
        response = self.app.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_null_values(self):
        data = {'user_id': None, 'password': None}
        response = self.app.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()