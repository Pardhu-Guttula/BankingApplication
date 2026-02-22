# File: tests/test_account_lockout_controller.py

import unittest
from flask import Flask, jsonify, Blueprint, request
from flask.testing import FlaskClient
from unittest.mock import patch, MagicMock
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller
from backend.authentication.services.account_lockout_service import AccountLockoutService

class TestAccountLockoutController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()
        self.mock_service = patch('backend.authentication.services.account_lockout_service.AccountLockoutService').start()
        
    def tearDown(self):
        patch.stopall()

    def test_login_success(self):
        self.mock_service.record_attempt_and_check_lockout.return_value = (False, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'user1', 'password': 'password1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_locked_out(self):
        self.mock_service.record_attempt_and_check_lockout.return_value = (True, 'Account is locked')
        response = self.client.post('/login', json={'user_id': 'user2', 'password': 'password2'})
        self.assertEqual(response.status_code, 423)
        self.assertEqual(response.json, {'error': 'Account is locked'})

    def test_login_invalid_credentials(self):
        self.mock_service.record_attempt_and_check_lockout.return_value = (False, 'Invalid credentials')
        response = self.client.post('/login', json={'user_id': 'user3', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'password1'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'user4'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_no_data(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_empty_data(self):
        response = self.client.post('/login', json=None)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()