# File: tests/test_account_lock_controller.py

import unittest
from flask import Flask, json
from account_lock_controller import account_lock_controller
from unittest.mock import patch

class AccountLockControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        data = {'user_id': 'test_user', 'password': 'test_pass'}
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(True, 'Login successful')):
            response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), {'message': 'Login successful'})

    def test_login_invalid_data(self):
        data = {'user_id': 'test_user'}
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_failure(self):
        data = {'user_id': 'test_user', 'password': 'wrong_pass'}
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(False, 'Invalid credentials')):
            response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.get_json(), {'error': 'Invalid credentials'})

    def test_login_no_data(self):
        response = self.client.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_user_id_none(self):
        data = {'user_id': None, 'password': 'test_pass'}
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_password_none(self):
        data = {'user_id': 'test_user', 'password': None}
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_empty_json(self):
        response = self.client.post('/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_empty_string_values(self):
        data = {'user_id': '', 'password': ''}
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_malformed_json(self):
        response = self.client.post('/login', data='this is not json', content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()