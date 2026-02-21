# File: tests/test_auth_service.py

import unittest
from unittest.mock import MagicMock
from backend.authentication.repositories.user_repository import UserRepository
from auth_service import AuthService

class TestAuthService(unittest.TestCase):

    def setUp(self):
        self.auth_service = AuthService()
        self.auth_service.user_repository = MagicMock(spec=UserRepository)

    def test_authenticate_success(self):
        user_mock = MagicMock()
        user_mock.check_password.return_value = True
        self.auth_service.user_repository.find_by_username.return_value = user_mock
        result = self.auth_service.authenticate('valid_user', 'valid_password')
        self.assertTrue(result)

    def test_authenticate_wrong_password(self):
        user_mock = MagicMock()
        user_mock.check_password.return_value = False
        self.auth_service.user_repository.find_by_username.return_value = user_mock
        result = self.auth_service.authenticate('valid_user', 'invalid_password')
        self.assertFalse(result)

    def test_authenticate_user_not_found(self):
        self.auth_service.user_repository.find_by_username.return_value = None
        result = self.auth_service.authenticate('invalid_user', 'any_password')
        self.assertFalse(result)

    def test_authenticate_empty_username(self):
        result = self.auth_service.authenticate('', 'some_password')
        self.assertFalse(result)

    def test_authenticate_empty_password(self):
        user_mock = MagicMock()
        user_mock.check_password.return_value = False
        self.auth_service.user_repository.find_by_username.return_value = user_mock
        result = self.auth_service.authenticate('valid_user', '')
        self.assertFalse(result)

    def test_authenticate_none_username(self):
        result = self.auth_service.authenticate(None, 'some_password')
        self.assertFalse(result)

    def test_authenticate_none_password(self):
        user_mock = MagicMock()
        user_mock.check_password.return_value = False
        self.auth_service.user_repository.find_by_username.return_value = user_mock
        result = self.auth_service.authenticate('valid_user', None)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()