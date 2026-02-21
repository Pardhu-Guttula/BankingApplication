import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from unittest.mock import patch, Mock
from backend.authentication.controllers.account_lock_controller import login

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.testing = True
        self.client = self.app.test_client()

    @patch('backend.authentication.services.account_lock_service.AccountLockService.process_login')
    def test_login_successful(self, mock_process_login):
        mock_process_login.return_value = (True, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'test_password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Login successful'})

    @patch('backend.authentication.services.account_lock_service.AccountLockService.process_login')
    def test_login_failure_invalid_credentials(self, mock_process_login):
        mock_process_login.return_value = (False, 'Invalid credentials')
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'test_password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_empty_body(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_no_body(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()