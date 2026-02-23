# File: tests/test_account_lock_controller.py

import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from unittest.mock import patch
from account_lock_controller import account_lock_controller

class AccountLockControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client: FlaskClient = self.app.test_client()

    def test_login_successful(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(True, '')) as mock_process_login:
            response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'password'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), {'message': 'Login successful'})
            mock_process_login.assert_called_once_with('test_user', 'password')

    def test_login_invalid_data(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_process_login_failure(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(False, 'Login failed')) as mock_process_login:
            response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'password'})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.get_json(), {'error': 'Login failed'})
            mock_process_login.assert_called_once_with('test_user', 'password')

if __name__ == '__main__':
    unittest.main()