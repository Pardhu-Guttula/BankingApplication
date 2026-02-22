# File: tests/test_login_controller.py
import unittest
from unittest.mock import patch, MagicMock
from login_controller import app, validate_email, validate_password

class TestLoginController(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('login_controller.user_repository')
    @patch('login_controller.auth_service')
    def test_register_success(self, mock_auth_service, mock_user_repository):
        mock_user_repository.find_by_email.return_value = None
        mock_auth_service.register.return_value = MagicMock()
        response = self.app.post('/register', json={'name': 'John Doe', 'email': 'john@example.com', 'password': 'Secure123'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully', response.get_data(as_text=True))

    @patch('login_controller.user_repository')
    def test_register_missing_fields(self, mock_user_repository):
        response = self.app.post('/register', json={'name': 'John Doe', 'email': 'john@example.com'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('All fields are required', response.get_data(as_text=True))

    @patch('login_controller.user_repository')
    def test_register_invalid_email(self, mock_user_repository):
        response = self.app.post('/register', json={'name': 'John Doe', 'email': 'john@invalid', 'password': 'Secure123'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid email format', response.get_data(as_text=True))

    @patch('login_controller.user_repository')
    def test_register_weak_password(self, mock_user_repository):
        response = self.app.post('/register', json={'name': 'John Doe', 'email': 'john@example.com', 'password': 'weak'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Password does not meet security criteria', response.get_data(as_text=True))

    @patch('login_controller.user_repository')
    def test_register_email_already_registered(self, mock_user_repository):
        mock_user_repository.find_by_email.return_value = True
        response = self.app.post('/register', json={'name': 'John Doe', 'email': 'john@example.com', 'password': 'Secure123'})
        self.assertEqual(response.status_code, 409)
        self.assertIn('Email already registered', response.get_data(as_text=True))

    @patch('login_controller.auth_service')
    def test_login_success(self, mock_auth_service):
        mock_auth_service.is_account_locked.return_value = False
        mock_auth_service.login.return_value = MagicMock(token='valid_token')
        response = self.app.post('/login', json={'email': 'john@example.com', 'password': 'Secure123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('valid_token', response.get_data(as_text=True))

    @patch('login_controller.auth_service')
    def test_login_account_locked(self, mock_auth_service):
        mock_auth_service.is_account_locked.return_value = True
        response = self.app.post('/login', json={'email': 'john@example.com', 'password': 'Secure123'})
        self.assertEqual(response.status_code, 403)
        self.assertIn('Account is locked', response.get_data(as_text=True))

    @patch('login_controller.auth_service')
    def test_login_invalid_credentials(self, mock_auth_service):
        mock_auth_service.is_account_locked.return_value = False
        mock_auth_service.login.return_value = None
        response = self.app.post('/login', json={'email': 'john@example.com', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid credentials', response.get_data(as_text=True))

    @patch('login_controller.auth_service')
    def test_logout_success(self, mock_auth_service):
        mock_auth_service.logout.return_value = True
        response = self.app.post('/logout', headers={'Authorization': 'Bearer valid_token'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Logged out successfully', response.get_data(as_text=True))

    @patch('login_controller.auth_service')
    def test_logout_invalid_token(self, mock_auth_service):
        mock_auth_service.logout.return_value = False
        response = self.app.post('/logout', headers={'Authorization': 'Bearer invalid_token'})
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid token', response.get_data(as_text=True))

    @patch('login_controller.auth_service')
    def test_assign_role_success(self, mock_auth_service):
        mock_auth_service.is_admin.return_value = True
        mock_auth_service.assign_role.return_value = True
        response = self.app.post('/assign-role', json={'user_id': 1, 'role': 'admin'}, headers={'Authorization': 'Bearer valid_token'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Role assigned successfully', response.get_data(as_text=True))

    @patch('login_controller.auth_service')
    def test_assign_role_admin_required(self, mock_auth_service):
        mock_auth_service.is_admin.return_value = False
        response = self.app.post('/assign-role', json={'user_id': 1, 'role': 'admin'}, headers={'Authorization': 'Bearer valid_token'})
        self.assertEqual(response.status_code, 403)
        self.assertIn('Admin privileges required', response.get_data(as_text=True))

    @patch('login_controller.auth_service')
    def test_assign_role_fail(self, mock_auth_service):
        mock_auth_service.is_admin.return_value = True
        mock_auth_service.assign_role.return_value = False
        response = self.app.post('/assign-role', json={'user_id': 1, 'role': 'admin'}, headers={'Authorization': 'Bearer valid_token'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Unable to assign role', response.get_data(as_text=True))

    def test_validate_email(self):
        self.assertTrue(validate_email('test@example.com'))
        self.assertFalse(validate_email('invalid-email'))

    def test_validate_password(self):
        self.assertTrue(validate_password('Password123'))
        self.assertFalse(validate_password('weak'))

if __name__ == '__main__':
    unittest.main()