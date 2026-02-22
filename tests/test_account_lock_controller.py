# File: tests/test_account_lock_controller.py
import unittest
from unittest.mock import patch
from flask import Flask
from account_lock_controller import account_lock_controller

class TestAccountLockController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    # Positive test case: valid login
    @patch('backend.authentication.services.account_lock_service.AccountLockService.process_login')
    def test_login_success(self, mock_process_login):
        mock_process_login.return_value = (True, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'valid_user', 'password': 'valid_password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    # Negative test case: invalid login
    @patch('backend.authentication.services.account_lock_service.AccountLockService.process_login')
    def test_login_failure(self, mock_process_login):
        mock_process_login.return_value = (False, 'Invalid credentials')
        response = self.client.post('/login', json={'user_id': 'invalid_user', 'password': 'invalid_password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

    # Edge case: missing user_id
    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'password_only'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    # Edge case: missing password
    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'user_only'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    # Edge case: missing user_id and password
    def test_login_missing_user_id_and_password(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    # Error case: invalid JSON data
    def test_login_invalid_json(self):
        response = self.client.post('/login', data='Invalid JSON')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    # Error case: unexpected exception
    @patch('account_lock_controller.login')
    def test_login_unexpected_exception(self, mock_login):
        mock_login.side_effect = Exception('Unexpected error')
        response = self.client.post('/login', json={'user_id': 'user', 'password': 'password'})
        self.assertEqual(response.status_code, 500)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()
