import unittest
from unittest.mock import patch, MagicMock
from werkzeug.security import check_password_hash
from backend.authentication.services.login_service import LoginService
from backend.authentication.repositories.login_attempt_repository import LoginAttemptRepository
from backend.authentication.models.login_attempt_model import User

class TestLoginService(unittest.TestCase):
    
    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_success(self, mock_repo, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = MagicMock(password='hashed_password')
        mock_repo.is_account_locked.return_value = False
        
        with patch('werkzeug.security.check_password_hash', return_value=True):
            result = LoginService.authenticate_user('test_user', 'correct_password')
            self.assertTrue(result)
            mock_repo.reset_failed_attempts.assert_called_once()

    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_wrong_password(self, mock_repo, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = MagicMock(password='hashed_password')
        mock_repo.is_account_locked.return_value = False
        
        with patch('werkzeug.security.check_password_hash', return_value=False):
            result = LoginService.authenticate_user('test_user', 'wrong_password')
            self.assertFalse(result)
            mock_repo.record_login_attempt.assert_called_once_with(mock_user.query.filter_by.return_value.first.return_value.id, successful=False)
            
    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_account_locked(self, mock_repo, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = MagicMock(password='hashed_password')
        mock_repo.is_account_locked.return_value = True
        
        result = LoginService.authenticate_user('test_user', 'any_password')
        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_called_once_with(mock_user.query.filter_by.return_value.first.return_value.id, successful=False)
        
    @patch('backend.authentication.models.login_attempt_model.User')
    @patch('backend.authentication.repositories.login_attempt_repository.LoginAttemptRepository')
    def test_authenticate_user_no_user_found(self, mock_repo, mock_user):
        mock_user.query.filter_by.return_value.first.return_value = None
        
        result = LoginService.authenticate_user('test_user', 'any_password')
        self.assertFalse(result)
        mock_repo.record_login_attempt.assert_not_called()