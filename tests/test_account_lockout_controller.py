# File: tests/test_account_lockout_controller.py
import unittest
from flask import json
from backend.authentication.services.account_lockout_service import AccountLockoutService
from account_lockout_controller import account_lockout_controller
from flask import Flask

class MockAccountLockoutService:
    def __init__(self):
        self.attempts = {}

    def record_attempt_and_check_lockout(self, user_id, success):
        if user_id not in self.attempts:
            self.attempts[user_id] = 0
        if not success:
            self.attempts[user_id] += 1
        if self.attempts[user_id] > 3:
            return True, 'Account locked due to too many failed login attempts.'
        return False, 'Login successful' if success else 'Invalid credentials'

class TestAccountLockoutController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()
        global AccountLockoutService
        AccountLockoutService = MockAccountLockoutService()

    def test_login_successful(self):
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'correct_password'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Login successful')

    def test_login_invalid_data_missing_user_id(self):
        response = self.client.post('/login', json={'password': '12345'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

    def test_login_invalid_data_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

    def test_login_unsuccessful(self):
        AccountLockoutService.record_attempt_and_check_lockout('test_user', False)
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'wrong_password'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['error'], 'Invalid credentials')

    def test_login_account_locked(self):
        for _ in range(4):
            AccountLockoutService.record_attempt_and_check_lockout('locked_user', False)
        response = self.client.post('/login', json={'user_id': 'locked_user', 'password': 'correct_password'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 423)
        self.assertEqual(data['error'], 'Account locked due to too many failed login attempts.')

if __name__ == '__main__':
    unittest.main()