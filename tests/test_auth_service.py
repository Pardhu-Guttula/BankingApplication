# File: tests/test_auth_service.py

import unittest
from unittest.mock import Mock, patch
from backend.authentication.auth_service import AuthService
from backend.authentication.repositories.user_repository import UserRepository

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.auth_service = AuthService()
        self.mock_user_repository = Mock(spec=UserRepository)
        self.auth_service.user_repository = self.mock_user_repository

    def test_authenticate_success(self):
        # Setup
        mock_user = Mock()
        mock_user.check_password.return_value = True
        self.mock_user_repository.find_by_username.return_value = mock_user

        # Execute
        result = self.auth_service.authenticate('valid_user', 'valid_pass')

        # Verify
        self.assertTrue(result)
        self.mock_user_repository.find_by_username.assert_called_once_with('valid_user')
        mock_user.check_password.assert_called_once_with('valid_pass')

    def test_authenticate_failure_invalid_password(self):
        # Setup
        mock_user = Mock()
        mock_user.check_password.return_value = False
        self.mock_user_repository.find_by_username.return_value = mock_user

        # Execute
        result = self.auth_service.authenticate('valid_user', 'invalid_pass')

        # Verify
        self.assertFalse(result)
        self.mock_user_repository.find_by_username.assert_called_once_with('valid_user')
        mock_user.check_password.assert_called_once_with('invalid_pass')

    def test_authenticate_failure_no_user_found(self):
        # Setup
        self.mock_user_repository.find_by_username.return_value = None

        # Execute
        result = self.auth_service.authenticate('invalid_user', 'any_pass')

        # Verify
        self.assertFalse(result)
        self.mock_user_repository.find_by_username.assert_called_once_with('invalid_user')

    def test_authenticate_empty_username(self):
        # Execute
        result = self.auth_service.authenticate('', 'any_pass')

        # Verify
        self.assertFalse(result)
        self.mock_user_repository.find_by_username.assert_called_once_with('')

    def test_authenticate_empty_password(self):
        # Setup
        mock_user = Mock()
        mock_user.check_password.return_value = False
        self.mock_user_repository.find_by_username.return_value = mock_user

        # Execute
        result = self.auth_service.authenticate('valid_user', '')

        # Verify
        self.assertFalse(result)
        self.mock_user_repository.find_by_username.assert_called_once_with('valid_user')
        mock_user.check_password.assert_called_once_with('')

    def test_authenticate_none_username(self):
        # Execute
        result = self.auth_service.authenticate(None, 'any_pass')

        # Verify
        self.assertFalse(result)
        self.mock_user_repository.find_by_username.assert_called_once_with(None)

    def test_authenticate_none_password(self):
        # Setup
        mock_user = Mock()
        mock_user.check_password.return_value = False
        self.mock_user_repository.find_by_username.return_value = mock_user

        # Execute
        result = self.auth_service.authenticate('valid_user', None)

        # Verify
        self.assertFalse(result)
        self.mock_user_repository.find_by_username.assert_called_once_with('valid_user')
        mock_user.check_password.assert_called_once_with(None)

    def test_authenticate_sql_injection(self):
        # Setup
        mock_user = Mock()
        mock_user.check_password.return_value = False
        self.mock_user_repository.find_by_username.return_value = mock_user

        # Execute
        result = self.auth_service.authenticate("' OR 1=1;--", 'any_pass')

        # Verify
        self.assertFalse(result)
        self.mock_user_repository.find_by_username.assert_called_once_with("' OR 1=1;--")
        mock_user.check_password.assert_called_once_with('any_pass')

if __name__ == '__main__':
    unittest.main()
