# File: tests/test_account_lockout_controller.py

import unittest
from unittest.mock import patch, Mock
from flask import Flask, json
from account_lockout_controller import account_lockout_controller

class AccountLockoutControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_success(self, mock_record_attempt):
        mock_record_attempt.return_value = (False, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'correct_password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_locked(self, mock_record_attempt):
        mock_record_attempt.return_value = (True, 'Account locked due to too many attempts')
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'correct_password'})
        self.assertEqual(response.status_code, 423)
        self.assertEqual(response.json, {'error': 'Account locked due to too many attempts'})

    @patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout')
    def test_login_unsuccessful(self, mock_record_attempt):
        mock_record_attempt.return_value = (False, 'Invalid credentials')
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_invalid_data(self):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})
        response = self.client.post('/login', json={'password': 'password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_empty_data(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})