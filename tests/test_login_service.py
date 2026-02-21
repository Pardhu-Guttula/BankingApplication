# File: tests/test_login_service.py

import unittest
from unittest.mock import patch, MagicMock
from backend.authentication.services.login_service import LoginService
from backend.authentication.models.login_attempt_model import User
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from werkzeug.security import check_password_hash

class TestLoginService(unittest.TestCase):

    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_success(self, mock_check_password_hash, mock_login_attempt_repository, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = User(id=1, username='user', password='hashed_password')
        mock_login_attempt_repository.is_account_locked.return_value = False
        mock_check_password_hash.return_value = True
        mock_login_attempt_repository.reset_failed_attempts.return_value = None
        result = LoginService.authenticate_user('user', 'password')
        self.assertTrue(result)
        mock_login_attempt_repository.reset_failed_attempts.assert_called_once_with(1)
        mock_login_attempt_repository.record_login_attempt.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_failure_incorrect_password(self, mock_check_password_hash, mock_login_attempt_repository, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = User(id=1, username='user', password='hashed_password')
        mock_login_attempt_repository.is_account_locked.return_value = False
        mock_check_password_hash.return_value = False
        result = LoginService.authenticate_user('user', 'wrong_password')
        self.assertFalse(result)
        mock_login_attempt_repository.record_login_attempt.assert_called_once_with(1, successful=False)

    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_failure_account_locked(self, mock_check_password_hash, mock_login_attempt_repository, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = User(id=1, username='user', password='hashed_password')
        mock_login_attempt_repository.is_account_locked.return_value = True
        result = LoginService.authenticate_user('user', 'password')
        self.assertFalse(result)
        mock_login_attempt_repository.record_login_attempt.assert_called_once_with(1, successful=False)

    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_failure_no_user(self, mock_check_password_hash, mock_login_attempt_repository, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = None
        result = LoginService.authenticate_user('nonexistent_user', 'password')
        self.assertFalse(result)
        mock_login_attempt_repository.record_login_attempt.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_password_check_raises_exception(self, mock_check_password_hash, mock_login_attempt_repository, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = User(id=1, username='user', password='hashed_password')
        mock_login_attempt_repository.is_account_locked.return_value = False
        mock_check_password_hash.side_effect = Exception('Unexpected error')
        result = LoginService.authenticate_user('user', 'password')
        self.assertFalse(result)
        mock_login_attempt_repository.record_login_attempt.assert_called_once_with(1, successful=False)

if __name__ == '__main__':
    unittest.main()