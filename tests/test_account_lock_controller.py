# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch, Mock
from flask import json
from account_lock_controller import account_lock_controller

class TestAccountLockController(unittest.TestCase):

    def setUp(self):
        self.app = account_lock_controller.test_client()
        self.app.testing = True

    @patch('backend.authentication.services.account_lock_service.AccountLockService.process_login')
    def test_login_successful(self, mock_process_login):
        mock_process_login.return_value = (True, 'Login successful')
        response = self.app.post('/login', data=json.dumps({'user_id': 'test_user', 'password': 'test_password'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('backend.authentication.services.account_lock_service.AccountLockService.process_login')
    def test_login_failure(self, mock_process_login):
        mock_process_login.return_value = (False, 'Invalid credentials')
        response = self.app.post('/login', data=json.dumps({'user_id': 'test_user', 'password': 'wrong_password'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.app.post('/login', data=json.dumps({'password': 'test_password'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.app.post('/login', data=json.dumps({'user_id': 'test_user'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_no_data(self):
        response = self.app.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_invalid_json(self):
        response = self.app.post('/login', data='invalid_json', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()