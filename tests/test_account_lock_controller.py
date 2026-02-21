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

    @patch('account_lock_controller.AccountLockService.process_login', return_value=(True, 'Login successful'))
    def test_login_successful(self, mock_process_login):
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'secret'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Login successful'})

    @patch('account_lock_controller.AccountLockService.process_login', return_value=(False, 'Invalid credentials'))
    def test_login_invalid_credentials(self, mock_process_login):
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'secret'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_missing_body(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_no_body(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_invalid_method(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 405)
