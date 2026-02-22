# File: tests/test_account_lock_controller.py
import unittest
from flask import Flask, json
from backend.authentication.controllers.account_lock_controller import account_lock_controller
from backend.authentication.services.account_lock_service import AccountLockService

class MockAccountLockService:
    @staticmethod
    def process_login(user_id, password):
        if user_id == "valid_user" and password == "correct_password":
            return True, ""
        elif user_id == "locked_user":
            return False, "Account is locked"
        else:
            return False, "Invalid credentials"

class AccountLockControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()
        AccountLockService.process_login = MockAccountLockService.process_login

    def test_login_success(self):
        response = self.client.post('/login',json={"user_id": "valid_user","password": "correct_password"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "Login successful")

    def test_login_invalid_data(self):
        response = self.client.post('/login',json={})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Invalid data")

    def test_login_invalid_user(self):
        response = self.client.post('/login',json={"user_id": "invalid_user","password": "wrong_password"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Invalid credentials")

    def test_login_locked_account(self):
        response = self.client.post('/login',json={"user_id": "locked_user","password": "wrong_password"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Account is locked")

    def test_login_missing_userid(self):
        response = self.client.post('/login',json={"password": "some_password"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Invalid data")

    def test_login_missing_password(self):
        response = self.client.post('/login',json={"user_id": "some_user"})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["error"], "Invalid data")

if __name__ == '__main__':
    unittest.main()