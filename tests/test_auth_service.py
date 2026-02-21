# File: tests/test_auth_service.py

import unittest
from unittest.mock import Mock, patch
from auth_service import AuthService

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.auth_service = AuthService()
        self.mock_user_repo = Mock()
        self.auth_service.user_repository = self.mock_user_repo

    def test_authenticate_success(self):
        user = Mock()
        user.check_password.return_value = True
        self.mock_user_repo.find_by_username.return_value = user

        result = self.auth_service.authenticate('valid_user', 'valid_password')

        self.assertTrue(result)
        self.mock_user_repo.find_by_username.assert_called_once_with('valid_user')
        user.check_password.assert_called_once_with('valid_password')

    def test_authenticate_failure_invalid_username(self):
        self.mock_user_repo.find_by_username.return_value = None

        result = self.auth_service.authenticate('invalid_user', 'valid_password')

        self.assertFalse(result)
        self.mock_user_repo.find_by_username.assert_called_once_with('invalid_user')

    def test_authenticate_failure_invalid_password(self):
        user = Mock()
        user.check_password.return_value = False
        self.mock_user_repo.find_by_username.return_value = user

        result = self.auth_service.authenticate('valid_user', 'invalid_password')

        self.assertFalse(result)
        self.mock_user_repo.find_by_username.assert_called_once_with('valid_user')
        user.check_password.assert_called_once_with('invalid_password')

    def test_authenticate_edge_case_empty_username(self):
        self.mock_user_repo.find_by_username.return_value = None

        result = self.auth_service.authenticate('', 'valid_password')

        self.assertFalse(result)
        self.mock_user_repo.find_by_username.assert_called_once_with('')

    def test_authenticate_edge_case_empty_password(self):
        user = Mock()
        user.check_password.return_value = False
        self.mock_user_repo.find_by_username.return_value = user

        result = self.auth_service.authenticate('valid_user', '')

        self.assertFalse(result)
        self.mock_user_repo.find_by_username.assert_called_once_with('valid_user')
        user.check_password.assert_called_once_with('')

    def test_authenticate_edge_case_empty_username_password(self):
        self.mock_user_repo.find_by_username.return_value = None

        result = self.auth_service.authenticate('', '')

        self.assertFalse(result)
        self.mock_user_repo.find_by_username.assert_called_once_with('')
