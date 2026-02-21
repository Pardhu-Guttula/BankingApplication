# File: tests/test_auth_service.py
import unittest
from unittest.mock import MagicMock
from backend.authentication.services.auth_service import AuthService
from backend.authentication.repositories.user_repository import User

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.auth_service = AuthService()
        self.user_mock = MagicMock(spec=User)
        self.auth_service.user_repository.find_by_username = MagicMock()

    def test_authenticate_success(self):
        username = "valid_user"
        password = "valid_password"
        self.user_mock.check_password.return_value = True
        self.auth_service.user_repository.find_by_username.return_value = self.user_mock

        result = self.auth_service.authenticate(username, password)

        self.assertTrue(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with(username)
        self.user_mock.check_password.assert_called_once_with(password)

    def test_authenticate_failure_invalid_password(self):
        username = "valid_user"
        password = "invalid_password"
        self.user_mock.check_password.return_value = False
        self.auth_service.user_repository.find_by_username.return_value = self.user_mock

        result = self.auth_service.authenticate(username, password)

        self.assertFalse(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with(username)
        self.user_mock.check_password.assert_called_once_with(password)

    def test_authenticate_failure_non_existent_user(self):
        username = "non_existent_user"
        password = "some_password"
        self.auth_service.user_repository.find_by_username.return_value = None

        result = self.auth_service.authenticate(username, password)

        self.assertFalse(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with(username)

    def test_authenticate_failure_username_is_none(self):
        username = None
        password = "some_password"

        result = self.auth_service.authenticate(username, password)

        self.assertFalse(result)
        self.auth_service.user_repository.find_by_username.assert_called_once()

    def test_authenticate_failure_password_is_none(self):
        username = "valid_user"
        password = None
        self.auth_service.user_repository.find_by_username.return_value = self.user_mock

        result = self.auth_service.authenticate(username, password)

        self.assertFalse(result)
        self.auth_service.user_repository.find_by_username.assert_called_once_with(username)
        self.user_mock.check_password.assert_not_called()
