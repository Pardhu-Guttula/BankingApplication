# File: tests/test_account_lockout_controller.py

import unittest
from flask import json
from flask.testing import FlaskClient
from account_lockout_controller import account_lockout_controller
from backend.authentication.services.account_lockout_service import AccountLockoutService

class TestAccountLockoutController(unittest.TestCase):
    def setUp(self):
        self.app = account_lockout_controller.test_client()
        self.app.testing = True

    def mock_record_attempt_and_check_lockout(self, user_id, success):
        if user_id == 'locked_user':
            return True, 'User account is locked'
        elif success:
            return False, 'Login successful'
        else:
            return False, 'Invalid credentials'

    def test_login_success(self):
        AccountLockoutService.record_attempt_and_check_lockout = self.mock_record_attempt_and_check_lockout
        response = self.app.post('/login', data=json.dumps({'user_id': 'user1', 'password': 'password1'}), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Login successful')

    def test_login_failure_locked(self):
        AccountLockoutService.record_attempt_and_check_lockout = self.mock_record_attempt_and_check_lockout
        response = self.app.post('/login', data=json.dumps({'user_id': 'locked_user', 'password': 'password1'}), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 423)
        self.assertEqual(data['error'], 'User account is locked')

    def test_login_failure_invalid_credentials(self):
        AccountLockoutService.record_attempt_and_check_lockout = self.mock_record_attempt_and_check_lockout
        response = self.app.post('/login', data=json.dumps({'user_id': 'user1', 'password': 'wrong_password'}), content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['error'], 'Invalid credentials')

    def test_login_invalid_data(self):
        # Test with missing user_id
        response = self.app.post('/login', data=json.dumps({'password': 'password1'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {'error': 'Invalid data'})

        # Test with missing password
        response = self.app.post('/login', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {'error': 'Invalid data'})

    def test_login_no_data(self):
        # Test with empty request body
        response = self.app.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {'error': 'Invalid data'})

    def test_login_none_data(self):
        # Test with None values for user_id and password
        response = self.app.post('/login', data=json.dumps({'user_id': None, 'password': None}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()