# File: tests/test_account_lockout_controller.py
import unittest
from flask import Flask, json
from backend.authentication.services.account_lockout_service import AccountLockoutService
from account_lockout_controller import account_lockout_controller

class MockAccountLockoutService:
    def __init__(self):
        self.attempts = {}

    def record_attempt_and_check_lockout(self, user_id, success):
        if user_id not in self.attempts:
            self.attempts[user_id] = 0
        self.attempts[user_id] += 1
        if self.attempts[user_id] >= 3:
            return True, "Account locked"
        return False, "Success"

class AccountLockoutControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()
        # Mocking AccountLockoutService
        self.app.config['TESTING'] = True
        AccountLockoutService.record_attempt_and_check_lockout = MockAccountLockoutService().record_attempt_and_check_lockout

    def test_login_success(self):
        response = self.client.post('/login', json={'user_id': 'user1', 'password': 'pass'} )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Success")

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'pass'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'user1'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'Invalid data')

    def test_login_account_locked(self):
        for _ in range(3):
            response = self.client.post('/login', json={'user_id': 'user2', 'password': 'pass'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 423)
        self.assertEqual(data['error'], 'Account locked')

    def test_login_account_not_locked_after_one_attempt(self):
        response = self.client.post('/login', json={'user_id': 'user3', 'password': 'pass'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Success")

    def test_login_account_not_locked_after_two_attempts(self):
        for _ in range(2):
            response = self.client.post('/login', json={'user_id': 'user4', 'password': 'pass'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Success")

if __name__ == '__main__':
    unittest.main()