# File: tests/test_auth.py

import unittest
from your_module import Role

class TestRole(unittest.TestCase):

    def test_role_creation(self):
        role = Role(role_id=1, name="Admin", permissions=["create", "read", "update"])
        self.assertEqual(role.role_id, 1)
        self.assertEqual(role.name, "Admin")
        self.assertEqual(role.permissions, ["create", "read", "update"])

    def test_role_empty_permissions(self):
        role = Role(role_id=2, name="User", permissions=[])
        self.assertEqual(role.role_id, 2)
        self.assertEqual(role.name, "User")
        self.assertEqual(role.permissions, [])

    def test_role_special_characters(self):
        role = Role(role_id=3, name="@dmin", permissions=["read*"])
        self.assertEqual(role.role_id, 3)
        self.assertEqual(role.name, "@dmin")
        self.assertEqual(role.permissions, ["read*"])

    def test_role_negative_id(self):
        role = Role(role_id=-1, name="Guest", permissions=["read"])
        self.assertEqual(role.role_id, -1)
        self.assertEqual(role.name, "Guest")
        self.assertEqual(role.permissions, ["read"])

    def test_role_large_id(self):
        role = Role(role_id=999999999999, name="SuperUser", permissions=["all"])
        self.assertEqual(role.role_id, 999999999999)
        self.assertEqual(role.name, "SuperUser")
        self.assertEqual(role.permissions, ["all"])

    def test_role_null_name(self):
        with self.assertRaises(TypeError):
            Role(role_id=4, name=None, permissions=["read"])

    def test_role_null_permissions(self):
        with self.assertRaises(TypeError):
            Role(role_id=5, name="User", permissions=None)

if __name__ == '__main__':
    unittest.main()
