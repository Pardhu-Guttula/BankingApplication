# File: tests/test_login_service.py

import unittest
from unittest.mock import patch, MagicMock
from login_service import LoginService
from backend.authentication.models.login_attempt_model import User
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from werkzeug.security import generate_password_hash

class TestLoginService(unittest.TestCase):

    @patch('login_service.User.query.filter_by')
    @patch('login_service.LoginAttemptRepository')
    def test_authenticate_user_success(self, MockLoginAttemptRepository, mock_query):
        user = User(username='test_user', password=generate_password_hash('test_pass'))
        mock_query.return_value.first.return_value = user
        MockLoginAttemptRepository.is_account_locked.return_value = False

        result = LoginService.authenticate_user('test_user', 'test_pass')

        self.assertTrue(result)
        MockLoginAttemptRepository.reset_failed_attempts.assert_called_once_with(user.id)

    @patch('login_service.User.query.filter_by')
    @patch('login_service.LoginAttemptRepository')
    def test_authenticate_user_wrong_password(self, MockLoginAttemptRepository, mock_query):
        user = User(username='test_user', password=generate_password_hash('test_pass'))
        mock_query.return_value.first.return_value = user
        MockLoginAttemptRepository.is_account_locked.return_value = False

        result = LoginService.authenticate_user('test_user', 'wrong_pass')

        self.assertFalse(result)
        MockLoginAttemptRepository.record_login_attempt.assert_called_once_with(user.id, False)

    @patch('login_service.User.query.filter_by')
    @patch('login_service.LoginAttemptRepository')
    def test_authenticate_user_account_locked(self, MockLoginAttemptRepository, mock_query):
        user = User(username='test_user', password=generate_password_hash('test_pass'))
        mock_query.return_value.first.return_value = user
        MockLoginAttemptRepository.is_account_locked.return_value = True

        result = LoginService.authenticate_user('test_user', 'test_pass')

        self.assertFalse(result)
        MockLoginAttemptRepository.record_login_attempt.assert_called_once_with(user.id, False)

    @patch('login_service.User.query.filter_by')
    @patch('login_service.LoginAttemptRepository')
    def test_authenticate_user_user_not_found(self, MockLoginAttemptRepository, mock_query):
        mock_query.return_value.first.return_value = None

        result = LoginService.authenticate_user('test_user', 'test_pass')

        self.assertFalse(result)
        MockLoginAttemptRepository.record_login_attempt.assert_not_called()

    @patch('login_service.User.query.filter_by')
    @patch('login_service.LoginAttemptRepository')
    def test_authenticate_user_null_password(self, MockLoginAttemptRepository, mock_query):
        user = User(username='test_user', password=None)
        mock_query.return_value.first.return_value = user
        MockLoginAttemptRepository.is_account_locked.return_value = False

        result = LoginService.authenticate_user('test_user', None)

        self.assertFalse(result)
        MockLoginAttemptRepository.record_login_attempt.assert_called_once_with(user.id, False)

if __name__ == '__main__':
    unittest.main()
