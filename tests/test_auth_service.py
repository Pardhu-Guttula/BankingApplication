# File: tests/test_auth_service.py
import unittest
from unittest.mock import patch, MagicMock
from auth_service import AuthService

class TestAuthService(unittest.TestCase):

    @patch('backend.authentication.repositories.user_repository.UserRepository')
    def setUp(self, MockUserRepository):
        self.mock_user_repository = MockUserRepository.return_value
        self.auth_service = AuthService()

    def test_authenticate_success(self):
        self.mock_user_repository.find_by_username.return_value = MagicMock(check_password=lambda password: password == 'valid_password')
        result = self.auth_service.authenticate('valid_user', 'valid_password')
        self.assertTrue(result)

    def test_authenticate_failure_invalid_password(self):
        self.mock_user_repository.find_by_username.return_value = MagicMock(check_password=lambda password: password == 'valid_password')
        result = self.auth_service.authenticate('valid_user', 'invalid_password')
        self.assertFalse(result)

    def test_authenticate_failure_user_not_found(self):
        self.mock_user_repository.find_by_username.return_value = None
        result = self.auth_service.authenticate('invalid_user', 'any_password')
        self.assertFalse(result)

    def test_authenticate_failure_empty_username(self):
        result = self.auth_service.authenticate('', 'any_password')
        self.assertFalse(result)

    def test_authenticate_failure_empty_password(self):
        self.mock_user_repository.find_by_username.return_value = MagicMock(check_password=lambda password: password == 'valid_password')
        result = self.auth_service.authenticate('valid_user', '')
        self.assertFalse(result)

    def test_authenticate_none_username(self):
        with self.assertRaises(TypeError):
            self.auth_service.authenticate(None, 'any_password')

    def test_authenticate_none_password(self):
        with self.assertRaises(TypeError):
            self.auth_service.authenticate('valid_user', None)

if __name__ == '__main__':
    unittest.main()