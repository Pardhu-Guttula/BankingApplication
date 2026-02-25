# File: tests/test_role_service.py

import unittest
from unittest.mock import Mock, MagicMock
from backend.access_control.services.role_service import RoleService
from backend.access_control.repositories.role_repository import RoleRepository
from backend.access_control.repositories.user_repository import UserRepository

class TestRoleService(unittest.TestCase):
    def setUp(self):
        self.mock_role_repository = Mock(spec=RoleRepository)
        self.mock_user_repository = Mock(spec=UserRepository)
        self.role_service = RoleService(self.mock_role_repository, self.mock_user_repository)

    def test_assign_role_success(self):
        self.mock_user_repository.find_by_email.return_value = Mock(user_id=1)
        self.mock_role_repository.get_role_by_name.return_value = Mock(role_id=2)
        result = self.role_service.assign_role('user@example.com', 'admin')
        self.assertTrue(result)
        self.mock_user_repository.update_role.assert_called_once_with(1, 2)

    def test_assign_role_user_not_found(self):
        self.mock_user_repository.find_by_email.return_value = None
        result = self.role_service.assign_role('user@example.com', 'admin')
        self.assertFalse(result)
        self.mock_user_repository.update_role.assert_not_called()

    def test_assign_role_role_not_found(self):
        self.mock_user_repository.find_by_email.return_value = Mock(user_id=1)
        self.mock_role_repository.get_role_by_name.return_value = None
        result = self.role_service.assign_role('user@example.com', 'admin')
        self.assertFalse(result)
        self.mock_user_repository.update_role.assert_not_called()

    def test_get_permissions_success(self):
        self.mock_user_repository.find_by_email.return_value = Mock(user_id=1, role_id='admin')
        self.mock_role_repository.get_role_by_name.return_value = Mock(permissions=['read', 'write'])
        result = self.role_service.get_permissions('user@example.com')
        self.assertEqual(result, ['read', 'write'])

    def test_get_permissions_user_not_found(self):
        self.mock_user_repository.find_by_email.return_value = None
        result = self.role_service.get_permissions('user@example.com')
        self.assertEqual(result, [])

    def test_get_permissions_role_not_found(self):
        self.mock_user_repository.find_by_email.return_value = Mock(user_id=1, role_id='admin')
        self.mock_role_repository.get_role_by_name.return_value = None
        result = self.role_service.get_permissions('user@example.com')
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
