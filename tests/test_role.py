# File: tests/test_role.py

import unittest
from your_module import Role

class TestRole(unittest.TestCase):

    def test_role_creation(self):
        role = Role(1, 'admin', ['read', 'write'])
        self.assertEqual(role.role_id, 1)
        self.assertEqual(role.name, 'admin')
        self.assertEqual(role.permissions, ['read', 'write'])

    def test_role_creation_empty_permissions(self):
        role = Role(2, 'guest', [])
        self.assertEqual(role.role_id, 2)
        self.assertEqual(role.name, 'guest')
        self.assertEqual(role.permissions, [])

    def test_role_creation_null_values(self):
        with self.assertRaises(TypeError):
            Role(None, None, None)

    def test_role_id_boundary_values(self):
        role = Role(0, 'user', ['view'])
        self.assertEqual(role.role_id, 0)
        role = Role(2147483647, 'user', ['view'])
        self.assertEqual(role.role_id, 2147483647)

    def test_role_invalid_permissions(self):
        with self.assertRaises(TypeError):
            Role(3, 'user', None)
        with self.assertRaises(TypeError):
            Role(3, 'user', 'not-a-list')

    def test_role_invalid_role_id(self):
        with self.assertRaises(TypeError):
            Role('invalid', 'user', ['view'])

    def test_role_invalid_name(self):
        with self.assertRaises(TypeError):
            Role(4, None, ['view'])
        with self.assertRaises(TypeError):
            Role(4, 1234, ['view'])

if __name__ == '__main__':
    unittest.main()