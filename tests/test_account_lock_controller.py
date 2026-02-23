# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch
from flask import json
from account_lock_controller import account_lock_controller, login

class AccountLockControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = account_lock_controller.test_client()
        self.app.testing = True

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_success(self, mock_process_login):
        mock_process_login.return_value = (True, 'Login successful')
        response = self.app.post('/login', data=json.dumps({'user_id': 'user1', 'password': 'password1'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_invalid_data(self, mock_process_login):
        response = self.app.post('/login', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

        response = self.app.post('/login', data=json.dumps({'password': 'password1'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_failure(self, mock_process_login):
        mock_process_login.return_value = (False, 'Invalid credentials')
        response = self.app.post('/login', data=json.dumps({'user_id': 'user1', 'password': 'password1'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_missing_payload(self, mock_process_login):
        response = self.app.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})
        
if __name__ == '__main__':
    unittest.main()