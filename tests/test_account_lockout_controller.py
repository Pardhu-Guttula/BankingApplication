# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller

class AccountLockoutControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        with patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Login successful')):
            response = self.client.post('/login', json={
                'user_id': 'user1',
                'password': 'password'
            })
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_failure_locked(self):
        with patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(True, 'Account locked')):
            response = self.client.post('/login', json={
                'user_id': 'user2',
                'password': 'wrongpassword'
            })
            self.assertEqual(response.status_code, 423)
            self.assertEqual(response.json, {'error': 'Account locked'})

    def test_login_failure_unauthorized(self):
        with patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Unauthorized login attempt')):
            response = self.client.post('/login', json={
                'user_id': 'user3',
                'password': 'wrongpassword'
            })
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {'error': 'Unauthorized login attempt'})

    def test_login_invalid_data(self):
        response = self.client.post('/login', json={
            'user_id': 'user1',
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

        response = self.client.post('/login', json={
            'password': 'password'
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_payload(self):
        response = self.client.post('/login', json=None)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()