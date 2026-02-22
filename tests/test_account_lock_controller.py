# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch
from flask import Flask, json
from account_lock_controller import account_lock_controller

class AccountLockControllerTest(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    @patch('account_lock_controller.AccountLockService.process_login', return_value=(True, 'Login successful'))
    def test_login_successful(self, mock_process_login):
        data = {'user_id': 'test_user', 'password': 'correct_password'}
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Login successful'})

    @patch('account_lock_controller.AccountLockService.process_login', return_value=(False, 'Invalid user or password'))
    def test_login_invalid_credentials(self, mock_process_login):
        data = {'user_id': 'test_user', 'password': 'wrong_password'}
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid user or password'})

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_missing_user_id(self, mock_process_login):
        data = {'password': 'any_password'}
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})
        mock_process_login.assert_not_called()

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_missing_password(self, mock_process_login):
        data = {'user_id': 'test_user'}
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})
        mock_process_login.assert_not_called()

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_empty_user_id(self, mock_process_login):
        data = {'user_id': '', 'password': 'any_password'}
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})
        mock_process_login.assert_not_called()

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_empty_password(self, mock_process_login):
        data = {'user_id': 'test_user', 'password': ''}
        response = self.client.post('/login', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})
        mock_process_login.assert_not_called()

    @patch('account_lock_controller.AccountLockService.process_login')
    def test_login_no_data(self, mock_process_login):
        response = self.client.post('/login', data=None, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})
        mock_process_login.assert_not_called()

if __name__ == '__main__':
    unittest.main()
