# File: tests/test_login_service.py

import unittest
from unittest.mock import patch, MagicMock
from login_service import LoginService
from backend.authentication.models.login_attempt_model import User
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from werkzeug.security import check_password_hash

class TestLoginService(unittest.TestCase):

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('werkzeug.security.check_password_hash')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.reset_failed_attempts')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    def test_authenticate_user_successful(self, mock_record_login_attempt, mock_reset_failed_attempts, mock_check_password_hash, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = False
        mock_check_password_hash.return_value = True

        result = LoginService.authenticate_user('testuser', 'correct_password')

        mock_reset_failed_attempts.assert_called_once_with(mock_user.id)
        mock_record_login_attempt.assert_not_called()
        self.assertTrue(result)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('werkzeug.security.check_password_hash')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    def test_authenticate_user_incorrect_password(self, mock_record_login_attempt, mock_check_password_hash, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = False
        mock_check_password_hash.return_value = False

        result = LoginService.authenticate_user('testuser', 'wrong_password')

        mock_record_login_attempt.assert_called_once_with(mock_user.id, False)
        self.assertFalse(result)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    def test_authenticate_user_nonexistent_user(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = None

        result = LoginService.authenticate_user('nonexistent', 'password')

        self.assertFalse(result)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    def test_authenticate_user_locked_account(self, mock_record_login_attempt, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = True

        result = LoginService.authenticate_user('lockeduser', 'password')

        mock_record_login_attempt.assert_called_once_with(mock_user.id, False)
        self.assertFalse(result)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('werkzeug.security.check_password_hash')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    def test_authenticate_user_mixed_case_username(self, mock_record_login_attempt, mock_check_password_hash, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = False
        mock_check_password_hash.return_value = False

        result = LoginService.authenticate_user('TestUser', 'wrong_password')

        mock_record_login_attempt.assert_called_once_with(mock_user.id, False)
        self.assertFalse(result)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    def test_authenticate_user_numeric_password(self, mock_record_login_attempt, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = True

        result = LoginService.authenticate_user('user', '123456')

        mock_record_login_attempt.assert_called_once_with(mock_user.id, False)
        self.assertFalse(result)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    def test_authenticate_user_null_username(self, mock_filter_by):
        mock_filter_by.return_value.first.return_value = None

        result = LoginService.authenticate_user(None, 'password')

        self.assertFalse(result)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_empty_username(self, mock_check_password_hash, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = False
        mock_check_password_hash.return_value = False

        result = LoginService.authenticate_user('', 'correct_password')

        self.assertFalse(result)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_empty_password(self, mock_check_password_hash, mock_is_account_locked, mock_filter_by):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = False
        mock_check_password_hash.return_value = False

        result = LoginService.authenticate_user('testuser', '')

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
