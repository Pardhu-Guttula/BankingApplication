# File: tests/test_account_lock_controller.py

import json
from flask import Flask
import unittest
from unittest.mock import patch
from account_lock_controller import account_lock_controller

class TestAccountLockController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.register_blueprint(account_lock_controller)
        cls.client = cls.app.test_client()

    def test_login_success(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(True, '')):
            response = self.client.post('/login', data=json.dumps({'user_id': 'test_user', 'password': 'test_password'}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_invalid_data(self):
        response = self.client.post('/login', data=json.dumps({'user_id': 'test_user'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

        response = self.client.post('/login', data=json.dumps({'password': 'test_password'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

        response = self.client.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_failure(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(False, 'Login failed')):
            response = self.client.post('/login', data=json.dumps({'user_id': 'test_user', 'password': 'test_password'}), content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Login failed'})

if __name__ == '__main__':
    unittest.main()
