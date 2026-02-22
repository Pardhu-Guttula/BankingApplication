# File: tests/test_role_service.py

import unittest
from unittest.mock import MagicMock
from backend.access_control.repositories.role_repository import RoleRepository
from backend.access_control.repositories.user_repository import UserRepository
from role_service import RoleService

class TestRoleService(unittest.TestCase):
    def setUp(self):
        self.role_repository = MagicMock(spec=RoleRepository)
        self.user_repository = MagicMock(spec=UserRepository)
        self.role_service = RoleService(self.role_repository, self.user_repository)
        
    # assign_role tests
    def test_assign_role_success(self):
        self.user_repository.find_by_email.return_value = MagicMock(user_id=1)
        self.role_repository.get_role_by_name.return_value = MagicMock(role_id=1)
        result = self.role_service.assign_role("test@example.com", "admin")
        self.assertTrue(result)
        self.user_repository.update_role.assert_called_once_with(1, 1)

    def test_assign_role_user_not_found(self):
        self.user_repository.find_by_email.return_value = None
        self.role_repository.get_role_by_name.return_value = MagicMock(role_id=1)
        result = self.role_service.assign_role("test@example.com", "admin")
        self.assertFalse(result)
        self.user_repository.update_role.assert_not_called()

    def test_assign_role_role_not_found(self):
        self.user_repository.find_by_email.return_value = MagicMock(user_id=1)
        self.role_repository.get_role_by_name.return_value = None
        result = self.role_service.assign_role("test@example.com", "admin")
        self.assertFalse(result)
        self.user_repository.update_role.assert_not_called()

    def test_assign_role_user_and_role_not_found(self):
        self.user_repository.find_by_email.return_value = None
        self.role_repository.get_role_by_name.return_value = None
        result = self.role_service.assign_role("test@example.com", "admin")
        self.assertFalse(result)
        self.user_repository.update_role.assert_not_called()

    # get_permissions tests
    def test_get_permissions_success(self):
        self.user_repository.find_by_email.return_value = MagicMock(user_id=1, role_id=1)
        self.role_repository.get_role_by_name.return_value = MagicMock(permissions=["read", "write"])
        result = self.role_service.get_permissions("test@example.com")
        self.assertEqual(result, ["read", "write"])

    def test_get_permissions_user_not_found(self):
        self.user_repository.find_by_email.return_value = None
        result = self.role_service.get_permissions("test@example.com")
        self.assertEqual(result, [])

    def test_get_permissions_role_not_found(self):
        self.user_repository.find_by_email.return_value = MagicMock(user_id=1, role_id=1)
        self.role_repository.get_role_by_name.return_value = None
        result = self.role_service.get_permissions("test@example.com")
        self.assertEqual(result, [])

    def test_get_permissions_no_permissions(self):
        self.user_repository.find_by_email.return_value = MagicMock(user_id=1, role_id=1)
        self.role_repository.get_role_by_name.return_value = MagicMock(permissions=[])
        result = self.role_service.get_permissions("test@example.com")
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()