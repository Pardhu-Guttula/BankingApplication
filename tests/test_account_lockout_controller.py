# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import json
from account_lockout_controller import account_lockout_controller

class AccountLockoutControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = account_lockout_controller.test_client()
        self.app.testing = True

    def test_login_successful(self):
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout') as mock_service:
            mock_service.return_value = (False, 'Login successful')
            response = self.app.post('/login', data=json.dumps({'user_id': 'testuser', 'password': 'correctpassword'}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_failure_locked(self):
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout') as mock_service:
            mock_service.return_value = (True, 'Account locked')
            response = self.app.post('/login', data=json.dumps({'user_id': 'testuser', 'password': 'correctpassword'}), content_type='application/json')
            self.assertEqual(response.status_code, 423)
            self.assertEqual(response.json, {'error': 'Account locked'})

    def test_login_failure_unauthorized(self):
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout') as mock_service:
            mock_service.return_value = (False, 'Invalid credentials')
            response = self.app.post('/login', data=json.dumps({'user_id': 'testuser', 'password': 'wrongpassword'}), content_type='application/json')
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_invalid_data(self):
        response = self.app.post('/login', data=json.dumps({'user_id': 'testuser'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_empty_payload(self):
        response = self.app.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_no_json(self):
        response = self.app.post('/login', data='invalid', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()