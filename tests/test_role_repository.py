# File: tests/test_role_repository.py

import unittest
from backend.access_control.models.role import Role
from backend.access_control.role_repository import RoleRepository

class TestRoleRepository(unittest.TestCase):
    def setUp(self):
        self.repo = RoleRepository()

    def test_get_role_by_name_valid(self):
        role = self.repo.get_role_by_name('admin')
        self.assertIsNotNone(role)
        self.assertEqual(role.id, 1)
        self.assertEqual(role.name, 'admin')
        self.assertEqual(role.permissions, ['manage_users', 'view_reports', 'edit_content'])

    def test_get_role_by_name_invalid(self):
        role = self.repo.get_role_by_name('invalid_role')
        self.assertIsNone(role)

    def test_get_role_by_name_case_sensitive(self):
        role = self.repo.get_role_by_name('Admin')
        self.assertIsNone(role)

    def test_get_role_by_name_empty_string(self):
        role = self.repo.get_role_by_name('')
        self.assertIsNone(role)

    def test_get_role_by_name_null(self):
        with self.assertRaises(TypeError):
            self.repo.get_role_by_name(None)

if __name__ == '__main__':
    unittest.main()