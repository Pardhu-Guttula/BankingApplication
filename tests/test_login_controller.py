# File: tests/test_login_controller.py

import unittest
from backend.authentication.controllers.login_controller import app

class LoginControllerTest(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login_success(self):
        response = self.app.post('/login', json={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.get_json())

    def test_login_failure_invalid_credentials(self):
        response = self.app.post('/login', json={'username': 'wronguser', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 401)

    def test_login_failure_missing_username(self):
        response = self.app.post('/login', json={'password': 'testpass'})
        self.assertEqual(response.status_code, 400)

    def test_login_failure_missing_password(self):
        response = self.app.post('/login', json={'username': 'testuser'})
        self.assertEqual(response.status_code, 400)

    def test_login_failure_empty_credentials(self):
        response = self.app.post('/login', json={'username': '', 'password': ''})
        self.assertEqual(response.status_code, 400)

    def test_login_failure_invalid_json(self):
        response = self.app.post('/login', data='invalid json body')
        self.assertEqual(response.status_code, 400)

    def test_protected_route_unauthenticated(self):
        response = self.app.get('/protected')
        self.assertEqual(response.status_code, 401)

    def test_protected_route_authenticated(self):
        login_response = self.app.post('/login', json={'username': 'testuser', 'password': 'testpass'})
        token = login_response.get_json()['token']
        response = self.app.get('/protected', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 200)

    def test_protected_route_expired_token(self):
        # Assuming we have a method to create an expired token for testing
        expired_token = create_expired_token_for_testing('testuser')
        response = self.app.get('/protected', headers={'Authorization': f'Bearer {expired_token}'})
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()