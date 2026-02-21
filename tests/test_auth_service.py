# File: tests/test_auth_service.py

import unittest
from unittest.mock import MagicMock, patch
from backend.authentication.auth_service import AuthService
from backend.authentication.repositories.user_repository import UserRepository


class TestAuthService(unittest.TestCase):

    def setUp(self):
        self.auth_service = AuthService()

    def test_authenticate_success(self):
        mock_user = MagicMock()
        mock_user.check_password.return_value = True
        with patch.object(UserRepository, 'find_by_username', return_value=mock_user):
            self.assertTrue(self.auth_service.authenticate('valid_user', 'valid_password'))

    def test_authenticate_failure_wrong_password(self):
        mock_user = MagicMock()
        mock_user.check_password.return_value = False
        with patch.object(UserRepository, 'find_by_username', return_value=mock_user):
            self.assertFalse(self.auth_service.authenticate('valid_user', 'invalid_password'))

    def test_authenticate_failure_no_user(self):
        with patch.object(UserRepository, 'find_by_username', return_value=None):
            self.assertFalse(self.auth_service.authenticate('invalid_user', 'any_password'))

    def test_authenticate_logging_success(self):
        mock_user = MagicMock()
        mock_user.check_password.return_value = True
        with patch.object(UserRepository, 'find_by_username', return_value=mock_user):
            with self.assertLogs('backend.authentication.auth_service', level='INFO') as cm:
                self.auth_service.authenticate('valid_user', 'valid_password')
                self.assertIn('User valid_user authenticated successfully.', cm.output[0])

    def test_authenticate_logging_failure(self):
        with patch.object(UserRepository, 'find_by_username', return_value=None):
            with self.assertLogs('backend.authentication.auth_service', level='WARNING') as cm:
                self.auth_service.authenticate('invalid_user', 'any_password')
                self.assertIn('Failed authentication attempt for user invalid_user.', cm.output[0])

    def test_authenticate_input_types(self):
        with patch.object(UserRepository, 'find_by_username', return_value=None):
            self.assertFalse(self.auth_service.authenticate(123, 'password'))
            self.assertFalse(self.auth_service.authenticate('username', 123))
            self.assertFalse(self.auth_service.authenticate(None, 'password'))
            self.assertFalse(self.auth_service.authenticate('username', None))
            self.assertFalse(self.auth_service.authenticate(None, None))
            self.assertFalse(self.auth_service.authenticate('', 'password'))
            self.assertFalse(self.auth_service.authenticate('username', ''))

if __name__ == '__main__':
    unittest.main()
