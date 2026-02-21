# File: tests/test_login_service.py
import unittest
from unittest.mock import patch, MagicMock
from login_service import LoginService
from werkzeug.security import check_password_hash
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from backend.authentication.models.login_attempt_model import User

class TestLoginService(unittest.TestCase):

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_successful_login(self, mock_repo, mock_user_query):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_repo.is_account_locked.return_value = False
        
        with patch('werkzeug.security.check_password_hash', return_value=True):
            result = LoginService.authenticate_user('username', 'correct_password')
            self.assertTrue(result)
            mock_repo.reset_failed_attempts.assert_called_once_with(1)

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_failed_login_incorrect_password(self, mock_repo, mock_user_query):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_repo.is_account_locked.return_value = False

        with patch('werkzeug.security.check_password_hash', return_value=False):
            result = LoginService.authenticate_user('username', 'wrong_password')
            self.assertFalse(result)
            mock_repo.record_login_attempt.assert_called_once_with(1, successful=False)

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_account_locked(self, mock_repo, mock_user_query):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_repo.is_account_locked.return_value = True

        result = LoginService.authenticate_user('username', 'any_password')
        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_called_once_with(1, successful=False)

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_user_not_found(self, mock_repo, mock_user_query):
        mock_user_query.filter_by.return_value.first.return_value = None

        result = LoginService.authenticate_user('unknown_user', 'any_password')
        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_null_username(self, mock_repo, mock_user_query):
        result = LoginService.authenticate_user(None, 'any_password')
        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_not_called()
        
    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_null_password(self, mock_repo, mock_user_query):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_repo.is_account_locked.return_value = False

        result = LoginService.authenticate_user('username', None)
        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_invalid_username_type(self, mock_repo, mock_user_query):
        result = LoginService.authenticate_user(1234, 'any_password')
        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_invalid_password_type(self, mock_repo, mock_user_query):
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_repo.is_account_locked.return_value = False

        result = LoginService.authenticate_user('username', 1234)
        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_not_called()

if __name__ == '__main__':
    unittest.main()