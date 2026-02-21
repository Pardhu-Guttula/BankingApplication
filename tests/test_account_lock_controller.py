import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask.testing import FlaskClient
from backend.authentication.controllers.account_lock_controller import account_lock_controller
from backend.authentication.services.account_lock_service import AccountLockService

class TestAccountLockController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    @patch.object(AccountLockService, 'process_login')
    def test_login_success(self, mock_process_login):
        mock_process_login.return_value = (True, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'test_password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch.object(AccountLockService, 'process_login')
    def test_login_failure_invalid_credentials(self, mock_process_login):
        mock_process_login.return_value = (False, 'Invalid credentials')
        response = self.client.post('/login', json={'user_id': 'test_user', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'test_password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'test_user'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_user_id_and_password(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    @patch.object(AccountLockService, 'process_login')
    def test_login_account_locked(self, mock_process_login):
        mock_process_login.return_value = (False, 'Account locked')
        response = self.client.post('/login', json={'user_id': 'locked_user', 'password': 'any_password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Account locked'})

    @patch.object(AccountLockService, 'process_login')
    def test_login_mfa_required(self, mock_process_login):
        mock_process_login.return_value = (False, 'MFA required')
        response = self.client.post('/login', json={'user_id': 'mfa_user', 'password': 'correct_password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'MFA required'})

if __name__ == '__main__':
    unittest.main()