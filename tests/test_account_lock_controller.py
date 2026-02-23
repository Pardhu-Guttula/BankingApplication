# File: tests/test_account_lock_controller.py
import unittest
from unittest.mock import patch, Mock
from flask import Flask
from account_lock_controller import account_lock_controller

class TestAccountLockController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login') as mock_process_login:
            mock_process_login.return_value = (True, 'Login successful')
            response = self.client.post('/login', json={'user_id': 'user123', 'password': 'secret'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_invalid_data(self):
        response = self.client.post('/login', json={'user_id': 'user123'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_failure(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login') as mock_process_login:
            mock_process_login.return_value = (False, 'Invalid credentials')
            response = self.client.post('/login', json={'user_id': 'user123', 'password': 'wrong'})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_no_data(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_malformed_json(self):
        response = self.client.post('/login', data='not a json')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()