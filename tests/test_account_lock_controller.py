# File: tests/test_account_lock_controller.py
import json
from flask import Flask
import unittest
from account_lock_controller import account_lock_controller
from unittest.mock import patch

class AccountLockControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(True, "Login successful")):
            response = self.client.post('/login', data=json.dumps({'user_id': '123', 'password': 'password'}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_invalid_data(self):
        response = self.client.post('/login', data=json.dumps({'invalid_key': 'value'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_no_password(self):
        response = self.client.post('/login', data=json.dumps({'user_id': '123'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_no_user_id(self):
        response = self.client.post('/login', data=json.dumps({'password': 'password'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_failure(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(False, "Invalid credentials")):
            response = self.client.post('/login', data=json.dumps({'user_id': '123', 'password': 'wrong_password'}), content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_exception(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', side_effect=Exception("Service exception")):
            response = self.client.post('/login', data=json.dumps({'user_id': '123', 'password': 'password'}), content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Service exception'})

if __name__ == '__main__':
    unittest.main()