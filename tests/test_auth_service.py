# File: tests/test_auth_service.py

import unittest
from unittest.mock import MagicMock
from backend.authentication.services.auth_service import AuthService
from backend.authentication.repositories.user_repository import UserRepository

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.auth_service = AuthService()
        self.auth_service.user_repository = MagicMock()

    def test_authenticate_success(self):
        user = MagicMock()
        user.check_password.return_value = True
        self.auth_service.user_repository.find_by_username.return_value = user
        result = self.auth_service.authenticate('valid_user', 'valid_password')
        self.assertTrue(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with('valid_user')
        user.check_password.assert_called_once_with('valid_password')

    def test_authenticate_failure_invalid_user(self):
        self.auth_service.user_repository.find_by_username.return_value = None
        result = self.auth_service.authenticate('invalid_user', 'valid_password')
        self.assertFalse(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with('invalid_user')

    def test_authenticate_failure_invalid_password(self):
        user = MagicMock()
        user.check_password.return_value = False
        self.auth_service.user_repository.find_by_username.return_value = user
        result = self.auth_service.authenticate('valid_user', 'invalid_password')
        self.assertFalse(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with('valid_user')
        user.check_password.assert_called_once_with('invalid_password')

    def test_authenticate_with_none_username(self):
        result = self.auth_service.authenticate(None, 'any_password')
        self.assertFalse(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with(None)

    def test_authenticate_with_none_password(self):
        user = MagicMock()
        user.check_password.return_value = False
        self.auth_service.user_repository.find_by_username.return_value = user
        result = self.auth_service.authenticate('any_user', None)
        self.assertFalse(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with('any_user')
        user.check_password.assert_called_once_with(None)

if __name__ == '__main__':
    unittest.main()
