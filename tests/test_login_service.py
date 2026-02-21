# File: tests/test_login_service.py

import unittest
from unittest.mock import patch, MagicMock
from login_service import LoginService
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from backend.authentication.models.login_attempt_model import User

class TestLoginService(unittest.TestCase):

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_successful(self, mock_check_password_hash, mock_login_attempt_repository, mock_user_query):
        user = MagicMock()
        user.id = 1
        user.username = 'testuser'
        user.password = 'hashed_password'
        mock_user_query.filter_by.return_value.first.return_value = user
        mock_login_attempt_repository.is_account_locked.return_value = False
        mock_check_password_hash.return_value = True

        result = LoginService.authenticate_user('testuser', 'correct_password')

        mock_user_query.filter_by.assert_called_once_with(username='testuser')
        mock_login_attempt_repository.is_account_locked.assert_called_once_with(user.id)
        mock_check_password_hash.assert_called_once_with('hashed_password', 'correct_password')
        mock_login_attempt_repository.reset_failed_attempts.assert_called_once_with(user.id)
        self.assertTrue(result)

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_wrong_password(self, mock_check_password_hash, mock_login_attempt_repository, mock_user_query):
        user = MagicMock()
        user.id = 1
        user.username = 'testuser'
        user.password = 'hashed_password'
        mock_user_query.filter_by.return_value.first.return_value = user
        mock_login_attempt_repository.is_account_locked.return_value = False
        mock_check_password_hash.return_value = False

        result = LoginService.authenticate_user('testuser', 'wrong_password')

        mock_user_query.filter_by.assert_called_once_with(username='testuser')
        mock_login_attempt_repository.is_account_locked.assert_called_once_with(user.id)
        mock_check_password_hash.assert_called_once_with('hashed_password', 'wrong_password')
        mock_login_attempt_repository.record_login_attempt.assert_called_once_with(user.id, successful=False)
        self.assertFalse(result)

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_account_locked(self, mock_check_password_hash, mock_login_attempt_repository, mock_user_query):
        user = MagicMock()
        user.id = 1
        user.username = 'testuser'
        user.password = 'hashed_password'
        mock_user_query.filter_by.return_value.first.return_value = user
        mock_login_attempt_repository.is_account_locked.return_value = True

        result = LoginService.authenticate_user('testuser', 'correct_password')

        mock_user_query.filter_by.assert_called_once_with(username='testuser')
        mock_login_attempt_repository.is_account_locked.assert_called_once_with(user.id)
        mock_check_password_hash.assert_not_called()
        mock_login_attempt_repository.record_login_attempt.assert_called_once_with(user.id, successful=False)
        self.assertFalse(result)

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_nonexistent_user(self, mock_check_password_hash, mock_login_attempt_repository, mock_user_query):
        mock_user_query.filter_by.return_value.first.return_value = None

        result = LoginService.authenticate_user('nonexistent_user', 'any_password')

        mock_user_query.filter_by.assert_called_once_with(username='nonexistent_user')
        mock_login_attempt_repository.is_account_locked.assert_not_called()
        mock_check_password_hash.assert_not_called()
        mock_login_attempt_repository.record_login_attempt.assert_not_called()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()