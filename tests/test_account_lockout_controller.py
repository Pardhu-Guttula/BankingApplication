# File: tests/test_account_lockout_controller.py
import unittest
from unittest.mock import patch, mock_open
from flask import Flask
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller

class TestAccountLockoutController(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    def test_login_successful(self):
        with patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout') as mock_record:
            mock_record.return_value = (False, 'Login successful')
            response = self.client.post('/login', json={'user_id': 'user1', 'password': 'correctpassword'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_account_locked(self):
        with patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout') as mock_record:
            mock_record.return_value = (True, 'Account locked due to too many failed attempts')
            response = self.client.post('/login', json={'user_id': 'user1', 'password': 'correctpassword'})
            self.assertEqual(response.status_code, 423)
            self.assertEqual(response.json, {'error': 'Account locked due to too many failed attempts'})

    def test_login_invalid_credentials(self):
        with patch('backend.authentication.controllers.account_lockout_controller.AccountLockoutService.record_attempt_and_check_lockout') as mock_record:
            mock_record.return_value = (False, 'Invalid credentials')
            response = self.client.post('/login', json={'user_id': 'user1', 'password': 'wrongpassword'})
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'user1'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_user_id_and_password(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_empty_user_id_and_password(self):
        response = self.client.post('/login', json={'user_id': '', 'password': ''})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAccountLockoutController))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
