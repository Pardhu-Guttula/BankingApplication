import unittest
from unittest.mock import MagicMock, patch
from werkzeug.security import check_password_hash
from backend.authentication.services.login_service import LoginService
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from backend.authentication.models.login_attempt_model import User

class TestLoginService(unittest.TestCase):
    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_success(self, mock_check_password_hash, mock_login_attempt_repo, mock_user_query):
        # Setup mocks
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_login_attempt_repo.is_account_locked.return_value = False
        mock_check_password_hash.return_value = True

        # Call the function
        result = LoginService.authenticate_user('test_user', 'test_password')

        # Assertions
        self.assertTrue(result)
        mock_login_attempt_repo.reset_failed_attempts.assert_called_once_with(mock_user.id)
        mock_login_attempt_repo.record_login_attempt.assert_not_called()

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_wrong_password(self, mock_check_password_hash, mock_login_attempt_repo, mock_user_query):
        # Setup mocks
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.password = 'hashed_password'
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_login_attempt_repo.is_account_locked.return_value = False
        mock_check_password_hash.return_value = False

        # Call the function
        result = LoginService.authenticate_user('test_user', 'test_password')

        # Assertions
        self.assertFalse(result)
        mock_login_attempt_repo.record_login_attempt.assert_called_once_with(mock_user.id, successful=False)

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_account_locked(self, mock_login_attempt_repo, mock_user_query):
        # Setup mocks
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user_query.filter_by.return_value.first.return_value = mock_user
        mock_login_attempt_repo.is_account_locked.return_value = True

        # Call the function
        result = LoginService.authenticate_user('test_user', 'test_password')

        # Assertions
        self.assertFalse(result)
        mock_login_attempt_repo.record_login_attempt.assert_called_once_with(mock_user.id, successful=False)

    @patch('backend.authentication.models.login_attempt_model.User.query')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_no_such_user(self, mock_login_attempt_repo, mock_user_query):
        # Setup mocks
        mock_user_query.filter_by.return_value.first.return_value = None

        # Call the function
        result = LoginService.authenticate_user('test_user', 'test_password')

        # Assertions
        self.assertFalse(result)
        mock_login_attempt_repo.record_login_attempt.assert_not_called()

if __name__ == '__main__':
    unittest.main()