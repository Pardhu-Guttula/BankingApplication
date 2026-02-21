# File: tests/test_auth_service.py

import unittest
from unittest.mock import MagicMock
from auth_service import AuthService
from backend.authentication.repositories.user_repository import UserRepository

class TestAuthService(unittest.TestCase):

    def setUp(self):
        self.auth_service = AuthService()
        self.auth_service.user_repository = MagicMock(spec=UserRepository)

    def test_authenticate_success(self):
        # Happy path
        self.auth_service.user_repository.find_by_username.return_value = user = MagicMock()
        user.check_password.return_value = True
        result = self.auth_service.authenticate('valid_user', 'valid_password')
        self.assertTrue(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with('valid_user')
        user.check_password.assert_called_once_with('valid_password')

    def test_authenticate_wrong_password(self):
        # Wrong password
        self.auth_service.user_repository.find_by_username.return_value = user = MagicMock()
        user.check_password.return_value = False
        result = self.auth_service.authenticate('valid_user', 'invalid_password')
        self.assertFalse(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with('valid_user')
        user.check_password.assert_called_once_with('invalid_password')

    def test_authenticate_user_not_found(self):
        # User not found
        self.auth_service.user_repository.find_by_username.return_value = None
        result = self.auth_service.authenticate('invalid_user', 'any_password')
        self.assertFalse(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with('invalid_user')

    def test_authenticate_empty_username(self):
        # Edge case: empty username
        self.auth_service.user_repository.find_by_username.return_value = None
        result = self.auth_service.authenticate('', 'any_password')
        self.assertFalse(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with('')

    def test_authenticate_empty_password(self):
        # Edge case: empty password
        self.auth_service.user_repository.find_by_username.return_value = user = MagicMock()
        user.check_password.return_value = False
        result = self.auth_service.authenticate('valid_user', '')
        self.assertFalse(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with('valid_user')
        user.check_password.assert_called_once_with('')

    def test_authenticate_both_empty(self):
        # Edge case: both username and password are empty
        self.auth_service.user_repository.find_by_username.return_value = None
        result = self.auth_service.authenticate('', '')
        self.assertFalse(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with('')

if __name__ == '__main__':
    unittest.main()
