import unittest
from unittest.mock import MagicMock
from backend.authentication.services.auth_service import AuthService
from backend.authentication.repositories.user_repository import UserRepository

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.user_repository = MagicMock(spec=UserRepository)
        self.auth_service = AuthService()
        self.auth_service.user_repository = self.user_repository

    def test_authenticate_success(self):
        user_mock = MagicMock()
        user_mock.check_password.return_value = True
        self.user_repository.find_by_username.return_value = user_mock

        result = self.auth_service.authenticate('valid_user', 'valid_password')

        self.assertTrue(result)
        self.user_repository.find_by_username.assert_called_once_with('valid_user')
        user_mock.check_password.assert_called_once_with('valid_password')

    def test_authenticate_failure_invalid_password(self):
        user_mock = MagicMock()
        user_mock.check_password.return_value = False
        self.user_repository.find_by_username.return_value = user_mock

        result = self.auth_service.authenticate('valid_user', 'invalid_password')

        self.assertFalse(result)
        self.user_repository.find_by_username.assert_called_once_with('valid_user')
        user_mock.check_password.assert_called_once_with('invalid_password')

    def test_authenticate_failure_invalid_username(self):
        self.user_repository.find_by_username.return_value = None

        result = self.auth_service.authenticate('invalid_user', 'valid_password')

        self.assertFalse(result)
        self.user_repository.find_by_username.assert_called_once_with('invalid_user')

if __name__ == '__main__':
    unittest.main()