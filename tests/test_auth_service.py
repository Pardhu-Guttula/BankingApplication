# File: tests/test_auth_service.py

import unittest
from unittest.mock import Mock, patch
from backend.authentication.services.auth_service import AuthService
from backend.authentication.repositories.user_repository import UserRepository

class TestAuthService(unittest.TestCase):
    
    def setUp(self):
        self.auth_service = AuthService()
        self.user_repository_mock = Mock(spec=UserRepository)
        self.auth_service.user_repository = self.user_repository_mock

    def test_authenticate_success(self):
        self.user_repository_mock.find_by_username.return_value = Mock(check_password=lambda password: password == 'correct_password')
        result = self.auth_service.authenticate('valid_user', 'correct_password')
        self.assertTrue(result)

    def test_authenticate_failure_invalid_password(self):
        self.user_repository_mock.find_by_username.return_value = Mock(check_password=lambda password: password == 'correct_password')
        result = self.auth_service.authenticate('valid_user', 'wrong_password')
        self.assertFalse(result)

    def test_authenticate_failure_nonexistent_user(self):
        self.user_repository_mock.find_by_username.return_value = None
        result = self.auth_service.authenticate('nonexistent_user', 'any_password')
        self.assertFalse(result)

    def test_authenticate_edge_case_empty_username(self):
        self.user_repository_mock.find_by_username.return_value = None
        result = self.auth_service.authenticate('', 'correct_password')
        self.assertFalse(result)

    def test_authenticate_edge_case_empty_password(self):
        self.user_repository_mock.find_by_username.return_value = Mock(check_password=lambda password: password == 'correct_password')
        result = self.auth_service.authenticate('valid_user', '')
        self.assertFalse(result)

    def test_authenticate_exception_in_user_repository(self):
        self.user_repository_mock.find_by_username.side_effect = Exception('Repository error')
        with self.assertRaises(Exception):
            self.auth_service.authenticate('valid_user', 'correct_password')

if __name__ == '__main__':
    unittest.main()
