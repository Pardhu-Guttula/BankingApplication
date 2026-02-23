# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import json
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller

class TestAccountLockoutController(unittest.TestCase):

    def setUp(self):
        self.app = account_lockout_controller.test_client()
        self.app.testing = True

    @patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_success(self, mock_record_attempt):
        mock_record_attempt.return_value = (False, 'Login successful')

        response = self.app.post('/login', data=json.dumps({'user_id': 'user123', 'password': 'pass123'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_locked_account(self, mock_record_attempt):
        mock_record_attempt.return_value = (True, 'Account locked')

        response = self.app.post('/login', data=json.dumps({'user_id': 'user123', 'password': 'pass123'}), content_type='application/json')
        self.assertEqual(response.status_code, 423)
        self.assertEqual(response.json, {'error': 'Account locked'})

    @patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_failed_authentication(self, mock_record_attempt):
        mock_record_attempt.return_value = (False, 'Invalid credentials')

        response = self.app.post('/login', data=json.dumps({'user_id': 'user123', 'password': 'wrongpass'}), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.app.post('/login', data=json.dumps({'password': 'pass123'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.app.post('/login', data=json.dumps({'user_id': 'user123'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_empty_request(self):
        response = self.app.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_invalid_json(self):
        response = self.app.post('/login', data='{invalid json}', content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()