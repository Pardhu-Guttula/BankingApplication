# File: tests/test_login_service.py

import unittest
from unittest.mock import patch, Mock
from werkzeug.security import check_password_hash
from backend.authentication.services.login_service import LoginService
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from backend.authentication.models.login_attempt_model import User

class TestLoginService(unittest.TestCase):

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_successful(self, mock_check_password_hash, mock_login_attempt_repository, mock_user_query):
        mock_user = Mock()
        mock_user.username = 'testuser'
        mock_user.password = 'hashedpassword'
        mock_user.id = 1
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_login_attempt_repository.is_account_locked.return_value = False
        mock_check_password_hash.return_value = True

        result = LoginService.authenticate_user('testuser', 'correctpassword')

        mock_login_attempt_repository.reset_failed_attempts.assert_called_once_with(mock_user.id)
        self.assertTrue(result)

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_invalid_password(self, mock_check_password_hash, mock_login_attempt_repository, mock_user_query):
        mock_user = Mock()
        mock_user.username = 'testuser'
        mock_user.password = 'hashedpassword'
        mock_user.id = 1
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_login_attempt_repository.is_account_locked.return_value = False
        mock_check_password_hash.return_value = False

        result = LoginService.authenticate_user('testuser', 'wrongpassword')

        mock_login_attempt_repository.record_login_attempt.assert_called_once_with(mock_user.id, successful=False)
        self.assertFalse(result)

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_locked_account(self, mock_check_password_hash, mock_login_attempt_repository, mock_user_query):
        mock_user = Mock()
        mock_user.username = 'testuser'
        mock_user.password = 'hashedpassword'
        mock_user.id = 1
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_login_attempt_repository.is_account_locked.return_value = True

        result = LoginService.authenticate_user('testuser', 'anyPassword')

        mock_login_attempt_repository.record_login_attempt.assert_called_once_with(mock_user.id, successful=False)
        self.assertFalse(result)

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_not_found(self, mock_check_password_hash, mock_login_attempt_repository, mock_user_query):
        mock_user_query.filter_by.return_value.first.return_value = None

        result = LoginService.authenticate_user('unknownuser', 'anyPassword')

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()