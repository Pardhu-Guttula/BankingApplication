# File: tests/test_role_repository.py

import unittest
from backend.access_control.models.role import Role
from backend.access_control.role_repository import RoleRepository

class TestRoleRepository(unittest.TestCase):

    def setUp(self):
        self.repository = RoleRepository()

    def test_get_role_by_name_valid(self):
        """Test getting a valid role by name"""
        admin_role = self.repository.get_role_by_name("admin")
        self.assertIsNotNone(admin_role)
        self.assertEqual(admin_role.name, "admin")
        self.assertEqual(admin_role.permissions, ["manage_users", "view_reports", "edit_content"])

        user_role = self.repository.get_role_by_name("user")
        self.assertIsNotNone(user_role)
        self.assertEqual(user_role.name, "user")
        self.assertEqual(user_role.permissions, ["view_content", "comment"])

        guest_role = self.repository.get_role_by_name("guest")
        self.assertIsNotNone(guest_role)
        self.assertEqual(guest_role.name, "guest")
        self.assertEqual(guest_role.permissions, ["view_content"])

    def test_get_role_by_name_invalid(self):
        """Test getting an invalid role by name"""
        no_role = self.repository.get_role_by_name("non_existing_role")
        self.assertIsNone(no_role)

    def test_get_role_by_name_edge_case_empty_string(self):
        """Test getting a role by an empty string"""
        empty_role = self.repository.get_role_by_name("")
        self.assertIsNone(empty_role)

    def test_get_role_by_name_edge_case_whitespace(self):
        """Test getting a role by a whitespace string"""
        whitespace_role = self.repository.get_role_by_name(" ")
        self.assertIsNone(whitespace_role)

    def test_get_role_by_name_edge_case_none(self):
        """Test getting a role by None"""
        none_role = self.repository.get_role_by_name(None)
        self.assertIsNone(none_role)

if __name__ == '__main__':
    unittest.main()
