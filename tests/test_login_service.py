# File: tests/test_login_service.py

import unittest
from unittest.mock import patch, MagicMock
from werkzeug.security import check_password_hash
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from backend.authentication.models.login_attempt_model import User
from login_service import LoginService

class TestLoginService(unittest.TestCase):
    def setUp(self):
        self.username = "test_user"
        self.password = "correct_password"

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.reset_failed_attempts')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_successful(self, mock_check_password_hash, mock_reset_failed_attempts, mock_record_login_attempt, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_user.password = 'hashed_correct_password'
        mock_filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = False
        mock_check_password_hash.return_value = True

        result = LoginService.authenticate_user(self.username, self.password)

        self.assertTrue(result)
        mock_reset_failed_attempts.assert_called_once_with(mock_user.id)
        mock_record_login_attempt.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_invalid_password(self, mock_check_password_hash, mock_record_login_attempt, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_user.password = 'hashed_correct_password'
        mock_filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = False
        mock_check_password_hash.return_value = False

        result = LoginService.authenticate_user(self.username, self.password)

        self.assertFalse(result)
        mock_record_login_attempt.assert_called_once_with(mock_user.id, successful=False)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    def test_authenticate_user_account_locked(self, mock_record_login_attempt, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = True

        result = LoginService.authenticate_user(self.username, self.password)

        self.assertFalse(result)
        mock_record_login_attempt.assert_called_once_with(mock_user.id, successful=False)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    def test_authenticate_user_user_not_found(self, mock_record_login_attempt, mock_filter_by):
        mock_filter_by.return_value.first.return_value = None

        result = LoginService.authenticate_user(self.username, self.password)

        self.assertFalse(result)
        mock_record_login_attempt.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    def test_authenticate_user_null_username(self, mock_record_login_attempt, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = False

        result = LoginService.authenticate_user(None, self.password)

        self.assertFalse(result)
        mock_record_login_attempt.assert_called_once_with(mock_user.id, successful=False)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    def test_authenticate_user_null_password(self, mock_record_login_attempt, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = False

        result = LoginService.authenticate_user(self.username, None)

        self.assertFalse(result)
        mock_record_login_attempt.assert_called_once_with(mock_user.id, successful=False)

if __name__ == '__main__':
    unittest.main()
