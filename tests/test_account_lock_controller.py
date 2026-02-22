# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch
from flask import Flask, json
from backend.authentication.controllers.account_lock_controller import account_lock_controller

class TestAccountLockController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(True, 'Login successful')):
            response = self.client.post('/login', data=json.dumps({'user_id': 'user1', 'password': 'pass1'}), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_failure(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(False, 'Invalid credentials')):
            response = self.client.post('/login', data=json.dumps({'user_id': 'user1', 'password': 'wrongpass'}), content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', data=json.dumps({'password': 'pass1'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', data=json.dumps({'user_id': 'user1'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_empty_json(self):
        response = self.client.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_invalid_content_type(self):
        response = self.client.post('/login', data=json.dumps({'user_id': 'user1', 'password': 'pass1'}))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_no_data(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()