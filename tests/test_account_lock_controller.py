# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch
from flask import Flask
from account_lock_controller import account_lock_controller

class AccountLockControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    # Positive Test: Valid login
    @patch('backend.authentication.services.account_lock_service.AccountLockService.process_login')
    def test_login_successful(self, mock_process_login):
        mock_process_login.return_value = (True, 'Success')
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'test_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    # Negative Test: Missing user_id
    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'test_pass'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    # Negative Test: Missing password
    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    # Negative Test: Invalid login credentials
    @patch('backend.authentication.services.account_lock_service.AccountLockService.process_login')
    def test_login_invalid_credentials(self, mock_process_login):
        mock_process_login.return_value = (False, 'Invalid credentials')
        response = self.client.post('/login', json={'user_id': 'wrong_user', 'password': 'wrong_pass'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

    # Edge Case: Empty JSON payload
    def test_login_empty_json(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    # Edge Case: No JSON payload
    def test_login_no_json(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})
