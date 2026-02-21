# File: tests/test_login_service.py

import unittest
from unittest.mock import patch, MagicMock
from backend.authentication.services.login_service import LoginService
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from backend.authentication.models.login_attempt_model import User
from werkzeug.security import check_password_hash

class TestLoginService(unittest.TestCase):

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.reset_failed_attempts')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_success(self, mock_check_password_hash, mock_record_login_attempt, mock_reset_failed_attempts, mock_is_account_locked, mock_filter_by):
        # Setup
        username = 'testuser'
        password = 'correct_password'
        user = MagicMock()
        user.id = 1
        user.password = 'hashed_password'
        mock_filter_by.return_value.first.return_value = user
        mock_is_account_locked.return_value = False
        mock_check_password_hash.return_value = True

        # Execute
        result = LoginService.authenticate_user(username, password)

        # Assert
        self.assertTrue(result)
        mock_reset_failed_attempts.assert_called_once_with(user.id)
        mock_record_login_attempt.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.reset_failed_attempts')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_invalid_password(self, mock_check_password_hash, mock_record_login_attempt, mock_reset_failed_attempts, mock_is_account_locked, mock_filter_by):
        # Setup
        username = 'testuser'
        password = 'wrong_password'
        user = MagicMock()
        user.id = 1
        user.password = 'hashed_password'
        mock_filter_by.return_value.first.return_value = user
        mock_is_account_locked.return_value = False
        mock_check_password_hash.return_value = False

        # Execute
        result = LoginService.authenticate_user(username, password)

        # Assert
        self.assertFalse(result)
        mock_reset_failed_attempts.assert_not_called()
        mock_record_login_attempt.assert_called_once_with(user.id, successful=False)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.reset_failed_attempts')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_account_locked(self, mock_check_password_hash, mock_record_login_attempt, mock_reset_failed_attempts, mock_is_account_locked, mock_filter_by):
        # Setup
        username = 'testuser'
        password = 'any_password'
        user = MagicMock()
        user.id = 1
        user.password = 'hashed_password'
        mock_filter_by.return_value.first.return_value = user
        mock_is_account_locked.return_value = True

        # Execute
        result = LoginService.authenticate_user(username, password)

        # Assert
        self.assertFalse(result)
        mock_reset_failed_attempts.assert_not_called()
        mock_record_login_attempt.assert_called_once_with(user.id, successful=False)

    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.reset_failed_attempts')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_user_not_found(self, mock_check_password_hash, mock_record_login_attempt, mock_reset_failed_attempts, mock_is_account_locked, mock_filter_by):
        # Setup
        username = 'nonexistent_user'
        password = 'any_password'
        mock_filter_by.return_value.first.return_value = None

        # Execute
        result = LoginService.authenticate_user(username, password)

        # Assert
        self.assertFalse(result)
        mock_record_login_attempt.assert_not_called()
        mock_reset_failed_attempts.assert_not_called()
        mock_is_account_locked.assert_not_called()
        mock_check_password_hash.assert_not_called()

if __name__ == '__main__':
    unittest.main()
