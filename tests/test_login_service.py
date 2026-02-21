# File: tests/test_login_service.py

import unittest
from unittest.mock import patch, MagicMock
from werkzeug.security import check_password_hash
from login_service import LoginService
from backend.authentication.models.login_attempt_model import User
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository

class TestLoginService(unittest.TestCase):

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('login_service.LoginAttemptRepository.is_account_locked')
    @patch('login_service.LoginAttemptRepository.reset_failed_attempts')
    @patch('login_service.LoginAttemptRepository.record_login_attempt')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_successful(self, mock_check_password_hash, mock_record_login_attempt, mock_reset_failed_attempts, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_check_password_hash.return_value = True
        mock_is_account_locked.return_value = False
        mock_filter_by.return_value.first.return_value = mock_user

        result = LoginService.authenticate_user('valid_username', 'valid_password')

        self.assertTrue(result)
        mock_filter_by.assert_called_once_with(username='valid_username')
        mock_check_password_hash.assert_called_once_with('hashed_password', 'valid_password')
        mock_reset_failed_attempts.assert_called_once_with(1)
        mock_record_login_attempt.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('login_service.LoginAttemptRepository.is_account_locked')
    @patch('login_service.LoginAttemptRepository.reset_failed_attempts')
    @patch('login_service.LoginAttemptRepository.record_login_attempt')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_invalid_password(self, mock_check_password_hash, mock_record_login_attempt, mock_reset_failed_attempts, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_check_password_hash.return_value = False
        mock_is_account_locked.return_value = False
        mock_filter_by.return_value.first.return_value = mock_user

        result = LoginService.authenticate_user('valid_username', 'invalid_password')

        self.assertFalse(result)
        mock_filter_by.assert_called_once_with(username='valid_username')
        mock_check_password_hash.assert_called_once_with('hashed_password', 'invalid_password')
        mock_reset_failed_attempts.assert_not_called()
        mock_record_login_attempt.assert_called_once_with(1, successful=False)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('login_service.LoginAttemptRepository.is_account_locked')
    @patch('login_service.LoginAttemptRepository.reset_failed_attempts')
    @patch('login_service.LoginAttemptRepository.record_login_attempt')
    def test_authenticate_user_account_locked(self, mock_record_login_attempt, mock_reset_failed_attempts, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_is_account_locked.return_value = True
        mock_filter_by.return_value.first.return_value = mock_user

        result = LoginService.authenticate_user('valid_username', 'valid_password')

        self.assertFalse(result)
        mock_filter_by.assert_called_once_with(username='valid_username')
        mock_is_account_locked.assert_called_once_with(1)
        mock_reset_failed_attempts.assert_not_called()
        mock_record_login_attempt.assert_called_once_with(1, successful=False)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('login_service.LoginAttemptRepository.is_account_locked')
    @patch('login_service.LoginAttemptRepository.reset_failed_attempts')
    def test_authenticate_user_nonexistent_user(self, mock_reset_failed_attempts, mock_is_account_locked, mock_filter_by):
        mock_filter_by.return_value.first.return_value = None

        result = LoginService.authenticate_user('invalid_username', 'any_password')

        self.assertFalse(result)
        mock_filter_by.assert_called_once_with(username='invalid_username')
        mock_is_account_locked.assert_not_called()
        mock_reset_failed_attempts.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('login_service.LoginAttemptRepository.is_account_locked')
    @patch('login_service.LoginAttemptRepository.reset_failed_attempts')
    @patch('login_service.LoginAttemptRepository.record_login_attempt')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_username_case_sensitive(self, mock_check_password_hash, mock_record_login_attempt, mock_reset_failed_attempts, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_check_password_hash.return_value = True
        mock_is_account_locked.return_value = False
        mock_filter_by.side_effect = lambda username: {'valid_username': mock_user}.get(username)

        result = LoginService.authenticate_user('Valid_Username', 'valid_password')

        self.assertFalse(result)
        mock_filter_by.assert_called_once_with(username='Valid_Username')
        mock_check_password_hash.assert_not_called()
        mock_reset_failed_attempts.assert_not_called()
        mock_record_login_attempt.assert_not_called()

if __name__ == '__main__':
    unittest.main()
