# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch
from flask import Flask, jsonify
from account_lock_controller import account_lock_controller

class TestAccountLockController(unittest.TestCase):
 
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    @patch('backend.authentication.services.account_lock_service.AccountLockService.process_login')
    def test_login_success(self, mock_process_login):
        mock_process_login.return_value = (True, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'test_pass'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('backend.authentication.services.account_lock_service.AccountLockService.process_login')
    def test_login_invalid_data(self, mock_process_login):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

        response = self.client.post('/login', json={'password': 'test_pass'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    @patch('backend.authentication.services.account_lock_service.AccountLockService.process_login')
    def test_login_failure(self, mock_process_login):
        mock_process_login.return_value = (False, 'Invalid credentials')
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'invalid_pass'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

    @patch('backend.authentication.services.account_lock_service.AccountLockService.process_login')
    def test_login_service_exception(self, mock_process_login):
        mock_process_login.side_effect = Exception('Service failure')
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'test_pass'})
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'error': 'Service failure'})

if __name__ == '__main__':
    unittest.main()
