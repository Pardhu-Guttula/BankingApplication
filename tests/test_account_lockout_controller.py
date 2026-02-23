# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from account_lockout_controller import account_lockout_controller

# Create a Flask app and register the blueprint
def create_app():
    app = Flask(__name__)
    app.register_blueprint(account_lockout_controller)
    return app

class AccountLockoutControllerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_login_successful(self):
        with patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Login successful')):
            response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'test_password'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), {'message': 'Login successful'})

    def test_login_locked_account(self):
        with patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(True, 'Account locked')):
            response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'test_password'})
            self.assertEqual(response.status_code, 423)
            self.assertEqual(response.get_json(), {'error': 'Account locked'})

    def test_login_unauthorized(self):
        with patch('account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Invalid credentials')):
            with patch('account_lockout_controller.login', return_value=False):  # Mock the actual auth check to fail
                response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'wrong_password'})
                self.assertEqual(response.status_code, 401)
                self.assertEqual(response.get_json(), {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'test_password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_no_data(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()