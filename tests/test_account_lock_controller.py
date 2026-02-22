# File: tests/test_account_lock_controller.py
import unittest
from unittest.mock import patch
from backend.authentication.controllers.account_lock_controller import account_lock_controller

class TestAccountLockController(unittest.TestCase):
    def setUp(self):
        self.client = account_lock_controller.test_client()

    @patch('backend.authentication.controllers.account_lock_controller.AccountLockService.process_login')
    def test_login_success(self, mock_process_login):
        mock_process_login.return_value = (True, 'Login successful')
        response = self.client.post('/login', json={'user_id': 'user1', 'password': 'pass123'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('backend.authentication.controllers.account_lock_controller.AccountLockService.process_login')
    def test_login_failure(self, mock_process_login):
        mock_process_login.return_value = (False, 'Invalid credentials')
        response = self.client.post('/login', json={'user_id': 'user1', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid credentials'})

    def test_login_missing_user_id(self):
        response = self.client.post('/login', json={'password': 'pass123'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'user_id': 'user1'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_empty_request(self):
        response = self.client.post('/login', data={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})

    def test_login_invalid_json(self):
        response = self.client.post('/login', data='Invalid JSON', content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid data'})
