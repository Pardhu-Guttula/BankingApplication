# File: tests/test_role_repository.py

import unittest
from backend.access_control.models.role import Role
from backend.access_control.repositories.role_repository import RoleRepository

class TestRoleRepository(unittest.TestCase):

    def setUp(self):
        self.repo = RoleRepository()

    def test_get_role_by_name_existing_role(self):
        role = self.repo.get_role_by_name("admin")
        self.assertIsNotNone(role)
        self.assertEqual(role.id, 1)
        self.assertEqual(role.name, "admin")
        self.assertListEqual(role.permissions, ["manage_users", "view_reports", "edit_content"])

    def test_get_role_by_name_non_existing_role(self):
        role = self.repo.get_role_by_name("superuser")
        self.assertIsNone(role)

    def test_get_role_by_name_case_sensitive(self):
        role = self.repo.get_role_by_name("Admin")
        self.assertIsNone(role)

    def test_get_role_by_name_empty_string(self):
        role = self.repo.get_role_by_name("")
        self.assertIsNone(role)

    def test_get_role_by_name_none(self):
        role = self.repo.get_role_by_name(None)
        self.assertIsNone(role)

if __name__ == '__main__':
    unittest.main()