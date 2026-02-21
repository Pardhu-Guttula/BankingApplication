# File: tests/test_login_service.py

import unittest
from unittest.mock import patch, MagicMock
from login_service import LoginService
from backend.authentication.models.login_attempt_model import User
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from werkzeug.security import check_password_hash

class TestLoginService(unittest.TestCase):

    @patch('login_service.User')
    @patch('login_service.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_successful(self, mock_check_password_hash, mock_login_attempt_repo, mock_user):
        user = MagicMock(username='testuser', password='hashedpassword')
        mock_user.query.filter_by.return_value.first.return_value = user
        mock_login_attempt_repo.is_account_locked.return_value = False
        mock_check_password_hash.return_value = True
        
        result = LoginService.authenticate_user('testuser', 'password123')
        
        self.assertTrue(result)
        mock_login_attempt_repo.reset_failed_attempts.assert_called_once_with(user.id)
        mock_login_attempt_repo.record_login_attempt.assert_not_called()

    @patch('login_service.User')
    @patch('login_service.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_failed_wrong_password(self, mock_check_password_hash, mock_login_attempt_repo, mock_user):
        user = MagicMock(username='testuser', password='hashedpassword')
        mock_user.query.filter_by.return_value.first.return_value = user
        mock_login_attempt_repo.is_account_locked.return_value = False
        mock_check_password_hash.return_value = False
        
        result = LoginService.authenticate_user('testuser', 'wrongpassword')
        
        self.assertFalse(result)
        mock_login_attempt_repo.record_login_attempt.assert_called_once_with(user.id, successful=False)
        mock_login_attempt_repo.reset_failed_attempts.assert_not_called()

    @patch('login_service.User')
    @patch('login_service.LoginAttemptRepository')
    @patch('werkzeug.security.check_password_hash')
    def test_authenticate_user_account_locked(self, mock_check_password_hash, mock_login_attempt_repo, mock_user):
        user = MagicMock(username='testuser', password='hashedpassword')
        mock_user.query.filter_by.return_value.first.return_value = user
        mock_login_attempt_repo.is_account_locked.return_value = True
        
        result = LoginService.authenticate_user('testuser', 'password123')
        
        self.assertFalse(result)
        mock_login_attempt_repo.record_login_attempt.assert_called_once_with(user.id, successful=False)
        mock_login_attempt_repo.reset_failed_attempts.assert_not_called()
        mock_check_password_hash.assert_not_called()

    @patch('login_service.User')
    @patch('login_service.LoginAttemptRepository')
    def test_authenticate_user_nonexistent_user(self, mock_login_attempt_repo, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = None
        
        result = LoginService.authenticate_user('nonexistent', 'password123')
        
        self.assertFalse(result)
        mock_login_attempt_repo.is_account_locked.assert_not_called()
        mock_login_attempt_repo.record_login_attempt.assert_not_called()

    @patch('login_service.User')
    @patch('login_service.LoginAttemptRepository')
    def test_authenticate_user_empty_username_password(self, mock_login_attempt_repo, mock_user):
        result = LoginService.authenticate_user('', '')
        
        self.assertFalse(result)
        mock_user.query.filter_by.assert_called_once_with(username='')
        mock_user.query.filter_by.return_value.first.return_value = None
        mock_login_attempt_repo.is_account_locked.assert_not_called()
        mock_login_attempt_repo.record_login_attempt.assert_not_called()

if __name__ == '__main__':
    unittest.main()
