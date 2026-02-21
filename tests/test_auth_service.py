# File: tests/test_auth_service.py

import unittest
from unittest.mock import MagicMock
from auth_service import AuthService

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.auth_service = AuthService()
        self.auth_service.user_repository = MagicMock()

    def test_authenticate_success(self):
        user = MagicMock()
        user.check_password.return_value = True
        self.auth_service.user_repository.find_by_username.return_value = user
        result = self.auth_service.authenticate('valid_user', 'valid_password')
        self.assertTrue(result)

    def test_authenticate_failure_wrong_password(self):
        user = MagicMock()
        user.check_password.return_value = False
        self.auth_service.user_repository.find_by_username.return_value = user
        result = self.auth_service.authenticate('valid_user', 'invalid_password')
        self.assertFalse(result)

    def test_authenticate_failure_user_not_found(self):
        self.auth_service.user_repository.find_by_username.return_value = None
        result = self.auth_service.authenticate('invalid_user', 'any_password')
        self.assertFalse(result)

    def test_authenticate_empty_username(self):
        self.auth_service.user_repository.find_by_username.return_value = None
        result = self.auth_service.authenticate('', 'any_password')
        self.assertFalse(result)

    def test_authenticate_empty_password(self):
        user = MagicMock()
        user.check_password.return_value = False
        self.auth_service.user_repository.find_by_username.return_value = user
        result = self.auth_service.authenticate('valid_user', '')
        self.assertFalse(result)

    def test_authenticate_null_username(self):
        self.auth_service.user_repository.find_by_username.return_value = None
        result = self.auth_service.authenticate(None, 'any_password')
        self.assertFalse(result)

    def test_authenticate_null_password(self):
        user = MagicMock()
        user.check_password.return_value = False
        self.auth_service.user_repository.find_by_username.return_value = user
        result = self.auth_service.authenticate('valid_user', None)
        self.assertFalse(result)

    def test_authenticate_sql_injection(self):
        self.auth_service.user_repository.find_by_username.return_value = None
        result = self.auth_service.authenticate("' OR '1'='1", 'any_password')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()