# File: tests/test_account_lockout_controller.py

import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from account_lockout_controller import account_lockout_controller
from unittest.mock import patch

class TestAccountLockoutController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.register_blueprint(account_lockout_controller)
        cls.client = cls.app.test_client()

    def test_login_success(self):
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Welcome!')):
            response = self.client.post('/login', json={'user_id': 'testuser', 'password': 'testpass'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json, {'message': 'Welcome!'})

    def test_login_locked(self):
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout', return_value=(True, 'Account locked')):
            response = self.client.post('/login', json={'user_id': 'lockeduser', 'password': 'testpass'})
            self.assertEqual(response.status_code, 423)
            self.assertEqual(response.json, {'error': 'Account locked'})

    def test_login_unauthorized(self):
        with patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout', return_value=(False, 'Invalid credentials')):
            response = self.client.post('/login', json={'user_id': 'wronguser', 'password': 'wrongpass'})
            self.assertEqual(response.status_code, 401)
            self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_invalid_data(self):
        response = self.client.post('/login', json={'user_id': 'userwithoutpassword'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})
        
        response = self.client.post('/login', json={'password': 'passwordwithoutuser'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()
