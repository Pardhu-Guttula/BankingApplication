# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from account_lock_controller import account_lock_controller

class TestAccountLockController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(True, '')):
            response = self.client.post('/login', json={'user_id': 'valid_user', 'password': 'valid_password'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_failure(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(False, 'Invalid credentials')):
            response = self.client.post('/login', json={'user_id': 'invalid_user', 'password': 'invalid_password'})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'password_only'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'user_only'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_empty_payload(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_no_payload(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()