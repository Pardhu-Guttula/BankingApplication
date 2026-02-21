# File: tests/test_account_lock_controller.py

import unittest
from unittest.mock import patch, MagicMock
from app import account_lock_controller
from flask import Flask, jsonify

class TestAccountLockController(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(account_lock_controller)
        self.client = self.app.test_client()

    def test_login_success(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(True, "Success")) as mock_process_login:
            response = self.client.post('/login', json={"user_id": "testuser", "password": "password"})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.get_json(), {'message': 'Login successful'})

    def test_login_invalid_data(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

        response = self.client.post('/login', json={'user_id': 'testuser'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

        response = self.client.post('/login', json={'password': 'password'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

    def test_login_failure(self):
        with patch('backend.authentication.services.account_lock_service.AccountLockService.process_login', return_value=(False, "Invalid credentials")) as mock_process_login:
            response = self.client.post('/login', json={"user_id": "invaliduser", "password": "wrongpassword"})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.get_json(), {'error': 'Invalid credentials'})

    def test_null_json_body(self):
        response = self.client.post('/login', data=None)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Invalid data'})

if __name__ == '__main__':
    unittest.main()
