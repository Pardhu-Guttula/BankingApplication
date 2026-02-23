# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import json
from account_lock_controller import account_lock_controller

class TestAccountLockController(unittest.TestCase):

    @patch('account_lock_controller.AccountLockService')
    def setUp(self, mock_account_lock_service):
        self.client = account_lock_controller.test_client()
        self.mock_account_lock_service = mock_account_lock_service

    # Positive scenarios
    def test_login_successful(self):
        self.mock_account_lock_service.process_login.return_value = (True, 'Login successful')
        response = self.client.post('/login', data=json.dumps({'user_id': 'testUser', 'password': 'testPass'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    # Negative scenarios
    def test_login_invalid_data(self):
        response = self.client.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_invalid_password(self):
        self.mock_account_lock_service.process_login.return_value = (False, 'Invalid password')
        response = self.client.post('/login', data=json.dumps({'user_id': 'testUser', 'password': 'wrongPass'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid password'})

    # Edge cases
    def test_login_missing_user_id(self):
        response = self.client.post('/login', data=json.dumps({'password': 'testPass'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', data=json.dumps({'user_id': 'testUser'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_blank_user_id(self):
        response = self.client.post('/login', data=json.dumps({'user_id': '', 'password': 'testPass'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_blank_password(self):
        response = self.client.post('/login', data=json.dumps({'user_id': 'testUser', 'password': ''}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    # Invalid inputs
    def test_login_non_json_data(self):
        response = self.client.post('/login', data='non-json-data', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_content_type(self):
        response = self.client.post('/login', data=json.dumps({'user_id': 'testUser', 'password': 'testPass'}))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()