# File: tests/test_auth_service.py

import unittest
from unittest.mock import MagicMock
from backend.authentication.repositories.user_repository import UserRepository
from auth_service import AuthService

class AuthServiceTests(unittest.TestCase):

    def setUp(self):
        self.auth_service = AuthService()
        self.user_repository_mock = MagicMock(spec=UserRepository)
        self.auth_service.user_repository = self.user_repository_mock

    def test_authenticate_successful(self):
        user_mock = MagicMock()
        user_mock.check_password.return_value = True
        self.user_repository_mock.find_by_username.return_value = user_mock

        result = self.auth_service.authenticate('valid_user', 'valid_password')

        self.assertTrue(result)
        self.user_repository_mock.find_by_username.assert_called_once_with('valid_user')
        user_mock.check_password.assert_called_once_with('valid_password')

    def test_authenticate_invalid_password(self):
        user_mock = MagicMock()
        user_mock.check_password.return_value = False
        self.user_repository_mock.find_by_username.return_value = user_mock

        result = self.auth_service.authenticate('valid_user', 'invalid_password')

        self.assertFalse(result)
        self.user_repository_mock.find_by_username.assert_called_once_with('valid_user')
        user_mock.check_password.assert_called_once_with('invalid_password')

    def test_authenticate_nonexistent_user(self):
        self.user_repository_mock.find_by_username.return_value = None

        result = self.auth_service.authenticate('nonexistent_user', 'any_password')

        self.assertFalse(result)
        self.user_repository_mock.find_by_username.assert_called_once_with('nonexistent_user')

    def test_authenticate_empty_username(self):
        result = self.auth_service.authenticate('', 'any_password')

        self.assertFalse(result)
        self.user_repository_mock.find_by_username.assert_called_once_with('')

    def test_authenticate_empty_password(self):
        user_mock = MagicMock()
        user_mock.check_password.return_value = False
        self.user_repository_mock.find_by_username.return_value = user_mock

        result = self.auth_service.authenticate('valid_user', '')

        self.assertFalse(result)
        self.user_repository_mock.find_by_username.assert_called_once_with('valid_user')
        user_mock.check_password.assert_called_once_with('')

    def test_authenticate_null_username(self):
        result = self.auth_service.authenticate(None, 'any_password')

        self.assertFalse(result)
        self.user_repository_mock.find_by_username.assert_called_once_with(None)

    def test_authenticate_null_password(self):
        user_mock = MagicMock()
        user_mock.check_password.return_value = False
        self.user_repository_mock.find_by_username.return_value = user_mock

        result = self.auth_service.authenticate('valid_user', None)

        self.assertFalse(result)
        self.user_repository_mock.find_by_username.assert_called_once_with('valid_user')
        user_mock.check_password.assert_called_once_with(None)

if __name__ == '__main__':
    unittest.main()