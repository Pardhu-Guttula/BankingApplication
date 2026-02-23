# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from account_lock_controller import account_lock_controller

class AccountLockControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    def test_login_successful(self):
        data = {'user_id': 'valid_user', 'password': 'valid_password'}
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(True, '')):
            response = self.client.post('/login', json=data)
            self.assertEqual(response.status_code, 200)
            self.assertDictEqual(response.get_json(), {'message': 'Login successful'})

    def test_login_invalid_data(self):
        data = {'user_id': None, 'password': 'valid_password'}
        response = self.client.post('/login', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.get_json(), {'error': 'Invalid data'})

        data = {'user_id': 'valid_user', 'password': None}
        response = self.client.post('/login', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.get_json(), {'error': 'Invalid data'})

        data = {'user_id': None, 'password': None}
        response = self.client.post('/login', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_unknown_user(self):
        data = {'user_id': 'unknown_user', 'password': 'some_password'}
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(False, 'Invalid credentials')):
            response = self.client.post('/login', json=data)
            self.assertEqual(response.status_code, 400)
            self.assertDictEqual(response.get_json(), {'error': 'Invalid credentials'})

    def test_login_account_locked(self):
        data = {'user_id': 'locked_user', 'password': 'some_password'}
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(False, 'Account locked')):
            response = self.client.post('/login', json=data)
            self.assertEqual(response.status_code, 400)
            self.assertDictEqual(response.get_json(), {'error': 'Account locked'})

    def test_login_empty_request_body(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response.get_json(), {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()