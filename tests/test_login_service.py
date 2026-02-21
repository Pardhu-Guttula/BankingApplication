# File: tests/test_login_service.py
import unittest
from unittest.mock import patch, MagicMock
from login_service import LoginService
from backend.authentication.models.login_attempt_model import User
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository

class TestLoginService(unittest.TestCase):

    @patch('login_service.User')
    @patch('login_service.LoginAttemptRepository')
    @patch('login_service.check_password_hash')
    def test_authenticate_user_successful(self, mock_check_password, mock_repo, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = MagicMock(id=1, username='test', password='hashed_pwd')
        mock_check_password.return_value = True
        mock_repo.is_account_locked.return_value = False

        result = LoginService.authenticate_user('test', 'password')
        self.assertTrue(result)
        mock_repo.reset_failed_attempts.assert_called_with(1)
        mock_repo.record_login_attempt.assert_not_called()

    @patch('login_service.User')
    @patch('login_service.LoginAttemptRepository')
    @patch('login_service.check_password_hash')
    def test_authenticate_user_wrong_password(self, mock_check_password, mock_repo, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = MagicMock(id=1, username='test', password='hashed_pwd')
        mock_check_password.return_value = False
        mock_repo.is_account_locked.return_value = False

        result = LoginService.authenticate_user('test', 'password')
        self.assertFalse(result)
        mock_repo.reset_failed_attempts.assert_not_called()
        mock_repo.record_login_attempt.assert_called_with(1, successful=False)

    @patch('login_service.User')
    @patch('login_service.LoginAttemptRepository')
    @patch('login_service.check_password_hash')
    def test_authenticate_user_account_locked(self, mock_check_password, mock_repo, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = MagicMock(id=1, username='test', password='hashed_pwd')
        mock_check_password.return_value = True
        mock_repo.is_account_locked.return_value = True

        result = LoginService.authenticate_user('test', 'password')
        self.assertFalse(result)
        mock_repo.reset_failed_attempts.assert_not_called()
        mock_repo.record_login_attempt.assert_called_with(1, successful=False)

    @patch('login_service.User')
    @patch('login_service.LoginAttemptRepository')
    @patch('login_service.check_password_hash')
    def test_authenticate_user_non_existent_user(self, mock_check_password, mock_repo, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = None

        result = LoginService.authenticate_user('test', 'password')
        self.assertFalse(result)
        mock_repo.reset_failed_attempts.assert_not_called()
        mock_repo.record_login_attempt.assert_not_called()

if __name__ == '__main__':
    unittest.main()
