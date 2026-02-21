# File: tests/test_auth_service.py

import unittest
from unittest.mock import MagicMock, patch
from backend.authentication.repositories.user_repository import UserRepository
from auth_service import AuthService

class TestAuthService(unittest.TestCase):

    def setUp(self):
        self.auth_service = AuthService()
        self.mock_repo = MagicMock()
        self.auth_service.user_repository = self.mock_repo

    def test_authenticate_success(self):
        mock_user = MagicMock()
        mock_user.check_password.return_value = True
        self.mock_repo.find_by_username.return_value = mock_user

        result = self.auth_service.authenticate('test_user', 'correct_password')
        self.assertTrue(result)
        mock_user.check_password.assert_called_once_with('correct_password')

    def test_authenticate_wrong_password(self):
        mock_user = MagicMock()
        mock_user.check_password.return_value = False
        self.mock_repo.find_by_username.return_value = mock_user

        result = self.auth_service.authenticate('test_user', 'wrong_password')
        self.assertFalse(result)
        mock_user.check_password.assert_called_once_with('wrong_password')

    def test_authenticate_nonexistent_user(self):
        self.mock_repo.find_by_username.return_value = None

        result = self.auth_service.authenticate('nonexistent_user', 'any_password')
        self.assertFalse(result)

    @patch('auth_service.logging.warning')
    def test_authenticate_logging_warning(self, mock_warning):
        self.mock_repo.find_by_username.return_value = None

        self.auth_service.authenticate('user', 'password')
        mock_warning.assert_called_once_with('Failed authentication attempt for user user.')

    @patch('auth_service.logging.info')
    def test_authenticate_logging_info(self, mock_info):
        mock_user = MagicMock()
        mock_user.check_password.return_value = True
        self.mock_repo.find_by_username.return_value = mock_user

        self.auth_service.authenticate('test_user', 'correct_password')
        mock_info.assert_called_once_with('User test_user authenticated successfully.')

if __name__ == '__main__':
    unittest.main()