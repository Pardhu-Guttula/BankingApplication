import unittest
from unittest.mock import MagicMock
from backend.authentication.services.auth_service import AuthService
from backend.authentication.repositories.user_repository import UserRepository

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.auth_service = AuthService()
        self.user_repository_mock = MagicMock(spec=UserRepository)
        self.auth_service.user_repository = self.user_repository_mock

    def test_authenticate_success(self):
        # Arrange
        username = 'valid_user'
        password = 'valid_pass'
        user = MagicMock()
        user.check_password.return_value = True
        self.user_repository_mock.find_by_username.return_value = user

        # Act
        result = self.auth_service.authenticate(username, password)

        # Assert
        self.assertTrue(result)
        self.user_repository_mock.find_by_username.assert_called_with(username)
        user.check_password.assert_called_with(password)

    def test_authenticate_failure_wrong_password(self):
        # Arrange
        username = 'valid_user'
        password = 'invalid_pass'
        user = MagicMock()
        user.check_password.return_value = False
        self.user_repository_mock.find_by_username.return_value = user

        # Act
        result = self.auth_service.authenticate(username, password)

        # Assert
        self.assertFalse(result)
        self.user_repository_mock.find_by_username.assert_called_with(username)
        user.check_password.assert_called_with(password)

    def test_authenticate_failure_user_not_found(self):
        # Arrange
        username = 'nonexistent_user'
        password = 'any_pass'
        self.user_repository_mock.find_by_username.return_value = None

        # Act
        result = self.auth_service.authenticate(username, password)

        # Assert
        self.assertFalse(result)
        self.user_repository_mock.find_by_username.assert_called_with(username)

    def test_authenticate_empty_username(self):
        # Arrange
        username = ''
        password = 'any_pass'

        # Act
        result = self.auth_service.authenticate(username, password)

        # Assert
        self.assertFalse(result)
        self.user_repository_mock.find_by_username.assert_not_called()

    def test_authenticate_empty_password(self):
        # Arrange
        username = 'valid_user'
        password = ''

        # Act
        result = self.auth_service.authenticate(username, password)

        # Assert
        self.assertFalse(result)
        self.user_repository_mock.find_by_username.assert_not_called()

if __name__ == '__main__':
    unittest.main()