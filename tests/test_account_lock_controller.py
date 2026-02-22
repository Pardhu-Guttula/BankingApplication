# File: tests/test_account_lock_controller.py
import unittest
from unittest.mock import patch
from flask import json
from account_lock_controller import account_lock_controller

class TestAccountLockController(unittest.TestCase):
    def setUp(self):
        self.app = account_lock_controller.test_client()
        self.app.testing = True

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_successful(self, mock_process_login):
        mock_process_login.return_value = (True, 'Login successful')
        response = self.app.post('/login', data=json.dumps({'user_id': 'test', 'password': 'test'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Login successful'})

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_invalid_data(self, mock_process_login):
        response = self.app.post('/login', data=json.dumps({'user_id': 'test'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {'error': 'Invalid data'})

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_failure_wrong_password(self, mock_process_login):
        mock_process_login.return_value = (False, 'Incorrect password')
        response = self.app.post('/login', data=json.dumps({'user_id': 'test', 'password': 'wrong'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {'error': 'Incorrect password'})

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_failure_account_locked(self, mock_process_login):
        mock_process_login.return_value = (False, 'Account locked')
        response = self.app.post('/login', data=json.dumps({'user_id': 'test', 'password': 'test'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {'error': 'Account locked'})

    def test_login_no_data(self):
        response = self.app.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {'error': 'Invalid data'})

    def test_login_empty_data(self):
        response = self.app.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data), {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()