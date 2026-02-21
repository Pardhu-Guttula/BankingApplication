# File: tests/test_auth_service.py

import unittest
from unittest.mock import Mock, patch
from backend.authentication.auth_service import AuthService
from backend.authentication.repositories.user_repository import UserRepository

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.auth_service = AuthService()

    @patch.object(UserRepository, 'find_by_username')
    def test_authenticate_success(self, mock_find_by_username):
        mock_user = Mock()
        mock_user.check_password.return_value = True
        mock_find_by_username.return_value = mock_user
        result = self.auth_service.authenticate('valid_user', 'valid_password')
        self.assertTrue(result)

    @patch.object(UserRepository, 'find_by_username')
    def test_authenticate_failure_incorrect_password(self, mock_find_by_username):
        mock_user = Mock()
        mock_user.check_password.return_value = False
        mock_find_by_username.return_value = mock_user
        result = self.auth_service.authenticate('valid_user', 'invalid_password')
        self.assertFalse(result)

    @patch.object(UserRepository, 'find_by_username')
    def test_authenticate_failure_user_not_found(self, mock_find_by_username):
        mock_find_by_username.return_value = None
        result = self.auth_service.authenticate('invalid_user', 'any_password')
        self.assertFalse(result)

    @patch.object(UserRepository, 'find_by_username')
    def test_authenticate_empty_username_password(self, mock_find_by_username):
        result = self.auth_service.authenticate('', '')
        self.assertFalse(result)

    @patch.object(UserRepository, 'find_by_username')
    def test_authenticate_null_username_password(self, mock_find_by_username):
        result = self.auth_service.authenticate(None, None)
        self.assertFalse(result)

    @patch.object(UserRepository, 'find_by_username')
    def test_authenticate_logging_on_success(self, mock_find_by_username):
        mock_user = Mock()
        mock_user.check_password.return_value = True
        mock_find_by_username.return_value = mock_user
        with self.assertLogs('backend.authentication.auth_service', level='INFO') as log:
            self.auth_service.authenticate('valid_user', 'valid_password')
            self.assertIn('User valid_user authenticated successfully.', log.output)

    @patch.object(UserRepository, 'find_by_username')
    def test_authenticate_logging_on_failure(self, mock_find_by_username):
        mock_find_by_username.return_value = None
        with self.assertLogs('backend.authentication.auth_service', level='WARNING') as log:
            self.auth_service.authenticate('invalid_user', 'any_password')
            self.assertIn('Failed authentication attempt for user invalid_user.', log.output)

if __name__ == '__main__':
    unittest.main()