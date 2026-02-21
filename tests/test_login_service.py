# File: tests/test_login_service.py
import unittest
from unittest.mock import patch, Mock
from login_service import LoginService
from backend.authentication.models.login_attempt_model import User
from werkzeug.security import generate_password_hash

class TestLoginService(unittest.TestCase):

    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.reset_failed_attempts')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    def test_authenticate_user_successful(self, mock_filter_by, mock_record_login_attempt, mock_reset_failed_attempts, mock_is_account_locked):
        # Mock user
        user = Mock()
        user.id = 1
        user.password = generate_password_hash('correct_password')
        mock_filter_by.return_value.first.return_value = user
        mock_is_account_locked.return_value = False

        result = LoginService.authenticate_user('test_user', 'correct_password')

        self.assertTrue(result)
        mock_reset_failed_attempts.assert_called_once_with(user.id)
        mock_record_login_attempt.assert_not_called()

    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    def test_authenticate_user_failed_wrong_password(self, mock_filter_by, mock_record_login_attempt, mock_is_account_locked):
        # Mock user
        user = Mock()
        user.id = 1
        user.password = generate_password_hash('correct_password')
        mock_filter_by.return_value.first.return_value = user
        mock_is_account_locked.return_value = False

        result = LoginService.authenticate_user('test_user', 'wrong_password')

        self.assertFalse(result)
        mock_record_login_attempt.assert_called_once_with(user.id, successful=False)

    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    def test_authenticate_user_account_locked(self, mock_filter_by, mock_record_login_attempt, mock_is_account_locked):
        # Mock user
        user = Mock()
        user.id = 1
        user.password = generate_password_hash('correct_password')
        mock_filter_by.return_value.first.return_value = user
        mock_is_account_locked.return_value = True

        result = LoginService.authenticate_user('test_user', 'correct_password')

        self.assertFalse(result)
        mock_record_login_attempt.assert_called_once_with(user.id, successful=False)

    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    def test_authenticate_user_user_not_found(self, mock_filter_by, mock_record_login_attempt, mock_is_account_locked):
        # Mock no user
        mock_filter_by.return_value.first.return_value = None
        mock_is_account_locked.return_value = False

        result = LoginService.authenticate_user('unknown_user', 'password')

        self.assertFalse(result)
        mock_record_login_attempt.assert_not_called()

    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.is_account_locked')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository.record_login_attempt')
    @patch('backend.authentication.models.login_attempt_model.User.query.filter_by')
    def test_authenticate_user_record_login_attempt_on_failure(self, mock_filter_by, mock_record_login_attempt, mock_is_account_locked):
        # Mock user
        user = Mock()
        user.id = 1
        user.password = generate_password_hash('correct_password')
        mock_filter_by.return_value.first.return_value = user
        mock_is_account_locked.return_value = False

        result = LoginService.authenticate_user('test_user', 'wrong_password')

        self.assertFalse(result)
        mock_record_login_attempt.assert_called_once_with(user.id, successful=False)

if __name__ == '__main__':
    unittest.main()