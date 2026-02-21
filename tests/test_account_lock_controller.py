# File: tests/test_account_lock_controller.py
import json
from flask import Flask
import unittest
from unittest.mock import patch
from account_lock_controller import account_lock_controller

class TestAccountLockController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    # Tests for the login function

    def test_login_successful(self):
        data = {'user_id': 'test_user', 'password': 'test_password'}
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(True, '')):
            response = self.client.post('/login', json=data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_invalid_credentials(self):
        data = {'user_id': 'test_user', 'password': 'wrong_password'}
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(False, 'Invalid credentials')):
            response = self.client.post('/login', json=data)
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        data = {'password': 'test_password'}
        response = self.client.post('/login', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        data = {'user_id': 'test_user'}
        response = self.client.post('/login', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_empty_request_body(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_no_json(self):
        response = self.client.post('/login', data='not json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_exception_handling(self):
        data = {'user_id': 'test_user', 'password': 'test_password'}
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', side_effect=Exception('Unexpected error')):
            response = self.client.post('/login', json=data)
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Unexpected error'})

if __name__ == '__main__':
    unittest.main()