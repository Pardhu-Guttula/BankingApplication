# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from account_lockout_controller import account_lockout_controller

class AccountLockoutControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    @patch('account_lockout_controller.AccountLockoutService')
    def test_login_successful(self, MockAccountLockoutService):
        # Arrange
        MockAccountLockoutService.record_attempt_and_check_lockout.return_value = (False, 'Login successful')
        data = {'user_id': 'test_user', 'password': 'test_password'}
        # Act
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Login successful'})

    @patch('account_lockout_controller.AccountLockoutService')
    def test_login_user_locked(self, MockAccountLockoutService):
        # Arrange
        MockAccountLockoutService.record_attempt_and_check_lockout.return_value = (True, 'Account locked')
        data = {'user_id': 'test_user', 'password': 'test_password'}
        # Act
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        # Assert
        self.assertEqual(response.status_code, 423)
        self.assertEqual(response.get_json(), {'error': 'Account locked'})

    @patch('account_lockout_controller.AccountLockoutService')
    def test_login_failed(self, MockAccountLockoutService):
        # Arrange
        MockAccountLockoutService.record_attempt_and_check_lockout.return_value = (False, 'Invalid credentials')
        success = False  # indicating a failed login attempt
        data = {'user_id': 'test_user', 'password': 'wrong_password'}
        # Act
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        # Assert
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.get_json(), {'error': 'Invalid credentials'})

    @patch('account_lockout_controller.AccountLockoutService')
    def test_login_missing_user_id(self, MockAccountLockoutService):
        # Arrange
        data = {'password': 'test_password'}
        # Act
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    @patch('account_lockout_controller.AccountLockoutService')
    def test_login_missing_password(self, MockAccountLockoutService):
        # Arrange
        data = {'user_id': 'test_user'}
        # Act
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    @patch('account_lockout_controller.AccountLockoutService')
    def test_login_empty_json(self, MockAccountLockoutService):
        # Arrange
        data = {}
        # Act
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    @patch('account_lockout_controller.AccountLockoutService')
    def test_login_invalid_json(self, MockAccountLockoutService):
        # Act
        response = self.client.post('/login', data='invalid json', content_type='application/json')
        # Assert
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()