# File: tests/test_role.py
import unittest

from role import Role

class TestRole(unittest.TestCase):

    def test_role_initialization(self):
        role = Role(1, 'admin', ['read', 'write'])
        self.assertEqual(role.role_id, 1)
        self.assertEqual(role.name, 'admin')
        self.assertEqual(role.permissions, ['read', 'write'])
    
    def test_role_empty_permissions(self):
        role = Role(2, 'guest', [])
        self.assertEqual(role.role_id, 2)
        self.assertEqual(role.name, 'guest')
        self.assertEqual(role.permissions, [])

    def test_role_none_input(self):
        with self.assertRaises(TypeError):
            Role(None, None, None)

    def test_role_invalid_role_id(self):
        with self.assertRaises(TypeError):
            Role('one', 'admin', ['read', 'write'])

    def test_role_invalid_name(self):
        with self.assertRaises(TypeError):
            Role(1, 123, ['read', 'write'])

    def test_role_invalid_permissions(self):
        with self.assertRaises(TypeError):
            Role(1, 'admin', 'read')

    def test_permissions_includes_empty_string(self):
        role = Role(3, 'user', ['read', ''])
        self.assertIn('', role.permissions)

    def test_permissions_duplicate_entries(self):
        role = Role(4, 'editor', ['read', 'read', 'write'])
        self.assertEqual(role.permissions, ['read', 'read', 'write'])

if __name__ == '__main__':
    unittest.main()
