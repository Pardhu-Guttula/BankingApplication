# File: tests/test_auth_service.py

import unittest
from unittest.mock import MagicMock
from auth_service import AuthService
from backend.authentication.repositories.user_repository import UserRepository

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.auth_service = AuthService()
        self.mock_user_repository = MagicMock(spec=UserRepository)
        self.auth_service.user_repository = self.mock_user_repository

    def test_authenticate_valid_user(self):
        user_mock = MagicMock()
        user_mock.check_password.return_value = True
        self.mock_user_repository.find_by_username.return_value = user_mock
        result = self.auth_service.authenticate("username", "password")
        self.assertTrue(result)
        self.mock_user_repository.find_by_username.assert_called_once_with("username")
        user_mock.check_password.assert_called_once_with("password")

    def test_authenticate_invalid_password(self):
        user_mock = MagicMock()
        user_mock.check_password.return_value = False
        self.mock_user_repository.find_by_username.return_value = user_mock
        result = self.auth_service.authenticate("username", "wrong_password")
        self.assertFalse(result)
        self.mock_user_repository.find_by_username.assert_called_once_with("username")
        user_mock.check_password.assert_called_once_with("wrong_password")

    def test_authenticate_user_not_found(self):
        self.mock_user_repository.find_by_username.return_value = None
        result = self.auth_service.authenticate("unknown_user", "password")
        self.assertFalse(result)
        self.mock_user_repository.find_by_username.assert_called_once_with("unknown_user")

    def test_authenticate_empty_username(self):
        self.mock_user_repository.find_by_username.return_value = None
        result = self.auth_service.authenticate("", "password")
        self.assertFalse(result)
        self.mock_user_repository.find_by_username.assert_called_once_with("")

    def test_authenticate_empty_password(self):
        user_mock = MagicMock()
        user_mock.check_password.return_value = False
        self.mock_user_repository.find_by_username.return_value = user_mock
        result = self.auth_service.authenticate("username", "")
        self.assertFalse(result)
        self.mock_user_repository.find_by_username.assert_called_once_with("username")
        user_mock.check_password.assert_called_once_with("")

    def test_authenticate_null_username(self):
        with self.assertRaises(TypeError):
            self.auth_service.authenticate(None, "password")

    def test_authenticate_null_password(self):
        with self.assertRaises(TypeError):
            self.auth_service.authenticate("username", None)

if __name__ == '__main__':
    unittest.main()