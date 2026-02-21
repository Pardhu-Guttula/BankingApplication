# File: tests/test_login_service.py

import unittest
from unittest.mock import patch, MagicMock
from backend.authentication.services.login_service import LoginService
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from backend.authentication.models.login_attempt_model import User
from werkzeug.security import check_password_hash

class TestLoginService(unittest.TestCase):

    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_successful(self, mock_repository, mock_user):
        user = MagicMock()
        user.id = 1
        user.password = 'hashed_password'
        mock_user.query.filter_by.return_value.first.return_value = user
        mock_repository.is_account_locked.return_value = False
        
        with patch('werkzeug.security.check_password_hash', return_value=True):
            result = LoginService.authenticate_user('username', 'password')
            self.assertTrue(result)
            mock_repository.reset_failed_attempts.assert_called_once_with(user.id)
            mock_repository.record_login_attempt.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_failed_password(self, mock_repository, mock_user):
        user = MagicMock()
        user.id = 1
        user.password = 'hashed_password'
        mock_user.query.filter_by.return_value.first.return_value = user
        mock_repository.is_account_locked.return_value = False

        with patch('werkzeug.security.check_password_hash', return_value=False):
            result = LoginService.authenticate_user('username', 'password')
            self.assertFalse(result)
            mock_repository.record_login_attempt.assert_called_once_with(user.id, successful=False)
            mock_repository.reset_failed_attempts.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_account_locked(self, mock_repository, mock_user):
        user = MagicMock()
        user.id = 1
        user.password = 'hashed_password'
        mock_user.query.filter_by.return_value.first.return_value = user
        mock_repository.is_account_locked.return_value = True

        result = LoginService.authenticate_user('username', 'password')
        self.assertFalse(result)
        mock_repository.record_login_attempt.assert_called_once_with(user.id, successful=False)
        mock_repository.reset_failed_attempts.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_no_such_user(self, mock_repository, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = None

        result = LoginService.authenticate_user('username', 'password')
        self.assertFalse(result)
        mock_repository.record_login_attempt.assert_not_called()
        mock_repository.reset_failed_attempts.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_check_password_raises_exception(self, mock_repository, mock_user):
        user = MagicMock()
        user.id = 1
        user.password = 'hashed_password'
        mock_user.query.filter_by.return_value.first.return_value = user
        mock_repository.is_account_locked.return_value = False

        with patch('werkzeug.security.check_password_hash', side_effect=Exception('test')):
            result = LoginService.authenticate_user('username', 'password')
            self.assertFalse(result)
            mock_repository.record_login_attempt.assert_called_once_with(user.id, successful=False)
            mock_repository.reset_failed_attempts.assert_not_called()

if __name__ == '__main__':
    unittest.main()