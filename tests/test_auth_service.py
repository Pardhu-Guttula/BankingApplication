# File: tests/test_auth_service.py

import unittest
from unittest.mock import Mock, patch
from backend.authentication.services.auth_service import AuthService
from backend.authentication.repositories.user_repository import UserRepository

class TestAuthService(unittest.TestCase):

    def setUp(self):
        self.auth_service = AuthService()
        self.user_repository_mock = Mock(spec=UserRepository)
        self.auth_service.user_repository = self.user_repository_mock

    def test_authenticate_success(self):
        # Set up successful authentication scenario
        user_mock = Mock()
        user_mock.check_password.return_value = True
        self.user_repository_mock.find_by_username.return_value = user_mock

        result = self.auth_service.authenticate("valid_user", "valid_password")
        self.assertTrue(result)
        self.user_repository_mock.find_by_username.assert_called_once_with("valid_user")
        user_mock.check_password.assert_called_once_with("valid_password")

    def test_authenticate_failure_invalid_password(self):
        # Set up failure scenario with invalid password
        user_mock = Mock()
        user_mock.check_password.return_value = False
        self.user_repository_mock.find_by_username.return_value = user_mock

        result = self.auth_service.authenticate("valid_user", "invalid_password")
        self.assertFalse(result)
        self.user_repository_mock.find_by_username.assert_called_once_with("valid_user")
        user_mock.check_password.assert_called_once_with("invalid_password")

    def test_authenticate_failure_no_user(self):
        # Set up failure scenario with no user found
        self.user_repository_mock.find_by_username.return_value = None

        result = self.auth_service.authenticate("unknown_user", "any_password")
        self.assertFalse(result)
        self.user_repository_mock.find_by_username.assert_called_once_with("unknown_user")

    def test_authenticate_with_empty_username(self):
        # Set up scenario with empty username
        result = self.auth_service.authenticate("", "some_password")
        self.assertFalse(result)

    @patch('logging.warning')
    def test_authenticate_logs_warning_on_failure(self, mock_logging_warning):
        # Set up a failure scenario to test logging
        self.user_repository_mock.find_by_username.return_value = None

        result = self.auth_service.authenticate("invalid_user", "invalid_password")
        self.assertFalse(result)
        mock_logging_warning.assert_called_once_with('Failed authentication attempt for user invalid_user.')

    @patch('logging.info')
    def test_authenticate_logs_info_on_success(self, mock_logging_info):
        # Set up a success scenario to test logging
        user_mock = Mock()
        user_mock.check_password.return_value = True
        self.user_repository_mock.find_by_username.return_value = user_mock

        result = self.auth_service.authenticate("valid_user", "valid_password")
        self.assertTrue(result)
        mock_logging_info.assert_called_once_with('User valid_user authenticated successfully.')

    def test_authenticate_with_empty_password(self):
        # Set up scenario with empty password
        result = self.auth_service.authenticate("some_user", "")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
