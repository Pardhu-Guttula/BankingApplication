import unittest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from backend.authentication.controllers.account_lockout_controller import account_lockout_controller

class AccountLockoutControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lockout_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        response = self.client.post('/login', json={
            'user_id': 'test_user',
            'password': 'test_password'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.get_json())

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={
            'password': 'test_password'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_login_missing_password(self):
        response = self.client.post('/login', json={
            'user_id': 'test_user'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_login_account_locked(self):
        with unittest.mock.patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout') as mock_service:
            mock_service.return_value = (True, 'Account is locked. Too many failed attempts.')
            response = self.client.post('/login', json={
                'user_id': 'test_user',
                'password': 'test_password'
            })
            self.assertEqual(response.status_code, 423)
            self.assertIn('error', response.get_json())

    def test_login_unauthorized(self):
        with unittest.mock.patch('backend.authentication.services.account_lockout_service.AccountLockoutService.record_attempt_and_check_lockout') as mock_service:
            mock_service.return_value = (False, 'Unauthorized access')
            response = self.client.post('/login', json={
                'user_id': 'test_user',
                'password': 'wrong_password'
            })
            self.assertEqual(response.status_code, 401)
            self.assertIn('error', response.get_json())

if __name__ == '__main__':
    unittest.main()