# File: tests/test_login_service.py

import unittest
from unittest.mock import patch, MagicMock
from werkzeug.security import check_password_hash
from login_service import LoginService
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from backend.authentication.models.login_attempt_model import User

class TestLoginService(unittest.TestCase):
    
    def setUp(self):
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = MagicMock()
        self.user.id = 1
        self.user.password = 'hashed_password'

    @patch.object(User, 'query')
    @patch.object(LoginAttemptRepository, 'is_account_locked', return_value=False)
    @patch('werkzeug.security.check_password_hash', return_value=True)
    @patch.object(LoginAttemptRepository, 'reset_failed_attempts')
    def test_authenticate_user_successful_login(self, mock_reset_failed_attempts, mock_check_password_hash, mock_is_account_locked, mock_user_query):
        mock_user_query.filter_by.return_value.first.return_value = self.user
        self.assertTrue(LoginService.authenticate_user(self.username, self.password))
        mock_reset_failed_attempts.assert_called_once_with(self.user.id)
        mock_check_password_hash.assert_called_once_with(self.user.password, self.password)
        mock_is_account_locked.assert_called_once_with(self.user.id)

    @patch.object(User, 'query')
    @patch.object(LoginAttemptRepository, 'is_account_locked', return_value=True)
    @patch.object(LoginAttemptRepository, 'record_login_attempt')
    def test_authenticate_user_account_locked(self, mock_record_login_attempt, mock_is_account_locked, mock_user_query):
        mock_user_query.filter_by.return_value.first.return_value = self.user
        self.assertFalse(LoginService.authenticate_user(self.username, self.password))
        mock_record_login_attempt.assert_called_once_with(self.user.id, successful=False)
        mock_is_account_locked.assert_called_once_with(self.user.id)

    @patch.object(User, 'query')
    @patch.object(LoginAttemptRepository, 'is_account_locked', return_value=False)
    @patch('werkzeug.security.check_password_hash', return_value=False)
    @patch.object(LoginAttemptRepository, 'record_login_attempt')
    def test_authenticate_user_invalid_password(self, mock_record_login_attempt, mock_check_password_hash, mock_is_account_locked, mock_user_query):
        mock_user_query.filter_by.return_value.first.return_value = self.user
        self.assertFalse(LoginService.authenticate_user(self.username, self.password))
        mock_record_login_attempt.assert_called_once_with(self.user.id, successful=False)
        mock_check_password_hash.assert_called_once_with(self.user.password, self.password)
        mock_is_account_locked.assert_called_once_with(self.user.id)

    @patch.object(User, 'query')
    @patch.object(LoginAttemptRepository, 'record_login_attempt')
    def test_authenticate_user_nonexistent_user(self, mock_record_login_attempt, mock_user_query):
        mock_user_query.filter_by.return_value.first.return_value = None
        self.assertFalse(LoginService.authenticate_user(self.username, self.password))
        mock_record_login_attempt.assert_not_called()

    @patch.object(User, 'query')
    @patch.object(LoginAttemptRepository, 'is_account_locked', return_value=False)
    @patch.object(LoginAttemptRepository, 'record_login_attempt')
    def test_authenticate_user_locked_after_failed_attempts(self, mock_record_login_attempt, mock_is_account_locked, mock_user_query):
        mock_user_query.filter_by.return_value.first.return_value = self.user
        for _ in range(5):
            with patch('werkzeug.security.check_password_hash', return_value=False):
                self.assertFalse(LoginService.authenticate_user(self.username, self.password))
        mock_record_login_attempt.assert_called_with(self.user.id, successful=False)

if __name__ == '__main__':
    unittest.main()
