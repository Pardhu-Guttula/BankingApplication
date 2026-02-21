# File: tests/test_login_service.py
import unittest
from unittest.mock import patch, MagicMock
from login_service import LoginService
from backend.authentication.models.login_attempt_model import User

class TestLoginService(unittest.TestCase):

    @patch('login_service.LoginAttemptRepository')
    @patch('login_service.User')
    @patch('login_service.check_password_hash')
    def test_authenticate_user_success(self, mock_check_password_hash, mock_user, mock_repo):
        # Setup
        mock_user.query.filter_by.return_value.first.return_value = mock_user.return_value
        mock_user.return_value.id = 1
        mock_check_password_hash.return_value = True
        mock_repo.is_account_locked.return_value = False

        result = LoginService.authenticate_user('valid_user', 'valid_password')

        self.assertTrue(result)
        mock_repo.reset_failed_attempts.assert_called_once_with(1)

    @patch('login_service.LoginAttemptRepository')
    @patch('login_service.User')
    @patch('login_service.check_password_hash')
    def test_authenticate_user_invalid_password(self, mock_check_password_hash, mock_user, mock_repo):
        # Setup
        mock_user.query.filter_by.return_value.first.return_value = mock_user.return_value
        mock_user.return_value.id = 1
        mock_check_password_hash.return_value = False
        mock_repo.is_account_locked.return_value = False

        result = LoginService.authenticate_user('valid_user', 'invalid_password')

        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_called_once_with(1, successful=False)

    @patch('login_service.LoginAttemptRepository')
    @patch('login_service.User')
    def test_authenticate_user_account_locked(self, mock_user, mock_repo):
        # Setup
        mock_user.query.filter_by.return_value.first.return_value = mock_user.return_value
        mock_user.return_value.id = 1
        mock_repo.is_account_locked.return_value = True

        result = LoginService.authenticate_user('valid_user', 'any_password')

        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_called_once_with(1, successful=False)

    @patch('login_service.LoginAttemptRepository')
    @patch('login_service.User')
    def test_authenticate_user_user_not_found(self, mock_user, mock_repo):
        # Setup
        mock_user.query.filter_by.return_value.first.return_value = None

        result = LoginService.authenticate_user('unknown_user', 'any_password')

        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_not_called()

    @patch('login_service.LoginAttemptRepository')
    @patch('login_service.User')
    def test_authenticate_user_no_username(self, mock_user, mock_repo):
        # Setup
        result = LoginService.authenticate_user('', 'any_password')

        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_not_called()

    @patch('login_service.LoginAttemptRepository')
    @patch('login_service.User')
    def test_authenticate_user_no_password(self, mock_user, mock_repo):
        # Setup
        result = LoginService.authenticate_user('user', '')

        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_not_called()

    @patch('login_service.LoginAttemptRepository')
    @patch('login_service.User')
    def test_authenticate_user_null_username(self, mock_user, mock_repo):
        # Setup
        result = LoginService.authenticate_user(None, 'any_password')

        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_not_called()

    @patch('login_service.LoginAttemptRepository')
    @patch('login_service.User')
    def test_authenticate_user_null_password(self, mock_user, mock_repo):
        # Setup
        result = LoginService.authenticate_user('user', None)

        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_not_called()

if __name__ == '__main__':
    unittest.main()