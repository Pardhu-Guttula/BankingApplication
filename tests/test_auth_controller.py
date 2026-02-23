# File: tests/test_auth_controller.py
import unittest
from unittest.mock import patch, MagicMock
from flask import json
from your_application import app

class TestAuthController(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
    @patch('backend.authentication.services.auth_service.AuthService')
    def test_login_success(self, MockAuthService):
        mock_auth_service = MockAuthService.return_value
        mock_auth_service.authenticate.return_value = True
        
        response = self.app.post('/login', 
                                 data=json.dumps({'username': 'testuser', 'password': 'testpass'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    @patch('backend.authentication.services.auth_service.AuthService')
    def test_login_invalid_credentials(self, MockAuthService):
        mock_auth_service = MockAuthService.return_value
        mock_auth_service.authenticate.return_value = False
        
        response = self.app.post('/login', 
                                 data=json.dumps({'username': 'testuser', 'password': 'wrongpass'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'message': 'Invalid credentials'})

    @patch('backend.authentication.services.auth_service.AuthService')
    def test_login_exception(self, MockAuthService):
        mock_auth_service = MockAuthService.return_value
        mock_auth_service.authenticate.side_effect = Exception('Database error')
        
        response = self.app.post('/login', 
                                 data=json.dumps({'username': 'testuser', 'password': 'testpass'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Login failed'})

    @patch('backend.authentication.services.auth_service.AuthService')
    def test_register_success(self, MockAuthService):
        mock_auth_service = MockAuthService.return_value
        mock_auth_service.register.return_value = True
        
        response = self.app.post('/register', 
                                 data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'testpass'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': 'Registration successful. Please check your email for confirmation.'})

    @patch('backend.authentication.services.auth_service.AuthService')
    def test_register_email_in_use(self, MockAuthService):
        mock_auth_service = MockAuthService.return_value
        mock_auth_service.register.return_value = False
        
        response = self.app.post('/register', 
                                 data=json.dumps({'name': 'Test User', 'email': 'used@example.com', 'password': 'testpass'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'message': 'Registration failed, email may already be in use.'})

    @patch('backend.authentication.services.auth_service.AuthService')
    def test_register_exception(self, MockAuthService):
        mock_auth_service = MockAuthService.return_value
        mock_auth_service.register.side_effect = Exception('Database error')
        
        response = self.app.post('/register', 
                                 data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'testpass'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Registration failed'})

    @patch('backend.authentication.services.auth_service.AuthService')
    def test_logout_success(self, MockAuthService):
        mock_auth_service = MockAuthService.return_value
        
        response = self.app.post('/logout')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Logout successful'})

    @patch('backend.authentication.services.auth_service.AuthService')
    def test_logout_exception(self, MockAuthService):
        mock_auth_service = MockAuthService.return_value
        mock_auth_service.logout.side_effect = Exception('Database error')
        
        response = self.app.post('/logout')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'message': 'Logout failed'})

if __name__ == '__main__':
    unittest.main()