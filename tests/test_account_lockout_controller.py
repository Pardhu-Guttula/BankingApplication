# File: tests/test_account_lockout_controller.py

import unittest
from flask import Flask, json
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller
from backend.authentication.services.account_lockout_service import AccountLockoutService

class TestAccountLockoutController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    # Test valid login request
    def test_login_success(self):
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'correct_password'})
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json)

    # Test invalid login request with missing user_id
    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'any_password'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    # Test invalid login request with missing password
    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    # Test invalid login request with empty body
    def test_login_empty_body(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    # Test account locked scenario
    def test_login_account_locked(self):
        AccountLockoutService.record_attempt_and_check_lockout = lambda user_id, success: (True, 'Account locked')
        response = self.client.post('/login', json={'user_id': 'locked_user', 'password': 'some_password'})
        self.assertEqual(response.status_code, 423)
        self.assertIn('error', response.json)

    # Test failed login attempt
    def test_login_failed_attempt(self):
        AccountLockoutService.record_attempt_and_check_lockout = lambda user_id, success: (False, 'Invalid credentials')
        success = False
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'incorrect_password'})
        self.assertEqual(response.status_code, 401)
        self.assertIn('error', response.json)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()