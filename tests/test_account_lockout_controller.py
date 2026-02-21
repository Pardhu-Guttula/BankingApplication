# File: tests/test_account_lockout_controller.py
import json
from flask import Flask
import unittest
from account_lockout_controller import account_lockout_controller

class AccountLockoutControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    def test_login_successful(self):
        with self.app.test_request_context('/login', method='POST',
                                           data=json.dumps({'user_id': 'test_user', 'password': 'password'}),
                                           content_type='application/json'):
            response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'password'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Success'})  # Assuming the placeholder returns 'Success'

    def test_login_locked_account(self):
        with self.app.test_request_context('/login', method='POST',
                                           data=json.dumps({'user_id': 'locked_user', 'password': 'password'}),
                                           content_type='application/json'):
            response = self.client.post('/login', json={'user_id': 'locked_user', 'password': 'password'})
            self.assertEqual(response.status_code, 423)
            self.assertEqual(response.json, {'error': 'Account locked'})  # Assuming the lock message is 'Account locked'

    def test_login_invalid_credentials(self):
        with self.app.test_request_context('/login', method='POST',
                                           data=json.dumps({'user_id': 'test_user', 'password': 'wrong_password'}),
                                           content_type='application/json'):
            response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'wrong_password'})
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {'error': 'Invalid credentials'})  # Assuming the message is 'Invalid credentials'

    def test_login_missing_user_id(self):
        with self.app.test_request_context('/login', method='POST',
                                           data=json.dumps({'password': 'password'}),
                                           content_type='application/json'):
            response = self.client.post('/login', json={'password': 'password'})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        with self.app.test_request_context('/login', method='POST',
                                           data=json.dumps({'user_id': 'test_user'}),
                                           content_type='application/json'):
            response = self.client.post('/login', json={'user_id': 'test_user'})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()