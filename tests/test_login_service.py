# File: tests/test_login_service.py

import unittest
from unittest.mock import patch, MagicMock
from login_service import LoginService
from backend.authentication.models.login_attempt_model import User
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from werkzeug.security import generate_password_hash

class TestLoginService(unittest.TestCase):

    @patch.object(User, 'query')
    @patch.object(LoginAttemptRepository, 'is_account_locked')
    @patch.object(LoginAttemptRepository, 'reset_failed_attempts')
    @patch.object(LoginAttemptRepository, 'record_login_attempt')
    def test_authenticate_user_successful(self, mock_record_login_attempt, mock_reset_failed_attempts, mock_is_account_locked, mock_user_query):
        mock_user = User(id=1, username='test_user', password=generate_password_hash('correct_password'))
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = False

        result = LoginService.authenticate_user('test_user', 'correct_password')

        self.assertTrue(result)
        mock_reset_failed_attempts.assert_called_once_with(mock_user.id)
        mock_record_login_attempt.assert_not_called()

    @patch.object(User, 'query')
    @patch.object(LoginAttemptRepository, 'is_account_locked')
    @patch.object(LoginAttemptRepository, 'reset_failed_attempts')
    @patch.object(LoginAttemptRepository, 'record_login_attempt')
    def test_authenticate_user_incorrect_password(self, mock_record_login_attempt, mock_reset_failed_attempts, mock_is_account_locked, mock_user_query):
        mock_user = User(id=1, username='test_user', password=generate_password_hash('correct_password'))
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = False

        result = LoginService.authenticate_user('test_user', 'wrong_password')

        self.assertFalse(result)
        mock_record_login_attempt.assert_called_once_with(mock_user.id, successful=False)
        mock_reset_failed_attempts.assert_not_called()

    @patch.object(User, 'query')
    @patch.object(LoginAttemptRepository, 'is_account_locked')
    @patch.object(LoginAttemptRepository, 'record_login_attempt')
    def test_authenticate_user_account_locked(self, mock_record_login_attempt, mock_is_account_locked, mock_user_query):
        mock_user = User(id=1, username='test_user', password=generate_password_hash('correct_password'))
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_is_account_locked.return_value = True

        result = LoginService.authenticate_user('test_user', 'correct_password')

        self.assertFalse(result)
        mock_record_login_attempt.assert_called_once_with(mock_user.id, successful=False)

    @patch.object(User, 'query')
    @patch.object(LoginAttemptRepository, 'is_account_locked')
    @patch.object(LoginAttemptRepository, 'record_login_attempt')
    def test_authenticate_user_user_not_found(self, mock_record_login_attempt, mock_is_account_locked, mock_user_query):
        mock_user_query.filter_by.return_value.first.return_value = None

        result = LoginService.authenticate_user('non_existent_user', 'any_password')

        self.assertFalse(result)
        mock_record_login_attempt.assert_not_called()

    @patch.object(User, 'query')
    @patch.object(LoginAttemptRepository, 'reset_failed_attempts')
    @patch.object(LoginAttemptRepository, 'record_login_attempt')
    def test_authenticate_user_is_account_locked_exception(self, mock_record_login_attempt, mock_reset_failed_attempts, mock_user_query):
        mock_user = User(id=1, username='test_user', password=generate_password_hash('correct_password'))
        mock_user_query.filter_by.return_value.first.return_value = mock_user

        with patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked', side_effect=Exception('Database error')) as mock_is_account_locked:
            result = LoginService.authenticate_user('test_user', 'correct_password')

        self.assertFalse(result)
        mock_is_account_locked.assert_called_once_with(mock_user.id)
        mock_record_login_attempt.assert_called_once_with(mock_user.id, successful=False)
        mock_reset_failed_attempts.assert_not_called()

    @patch.object(User, 'query')
    @patch.object(LoginAttemptRepository, 'reset_failed_attempts')
    @patch.object(LoginAttemptRepository, 'record_login_attempt')
    def test_authenticate_user_check_password_hash_exception(self, mock_record_login_attempt, mock_reset_failed_attempts, mock_user_query):
        mock_user = User(id=1, username='test_user', password='invalid_password_hash')
        mock_user_query.filter_by.return_value.first.return_value = mock_user

        with patch('werkzeug.security.check_password_hash', side_effect=Exception('Hash error')) as mock_check_password_hash:
            result = LoginService.authenticate_user('test_user', 'correct_password')

        self.assertFalse(result)
        mock_check_password_hash.assert_called_once_with('invalid_password_hash', 'correct_password')
        mock_record_login_attempt.assert_called_once_with(mock_user.id, successful=False)
        mock_reset_failed_attempts.assert_not_called()

if __name__ == '__main__':
    unittest.main()