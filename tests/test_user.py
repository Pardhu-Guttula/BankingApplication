# File: tests/test_user.py

import unittest
from user import User

class TestUser(unittest.TestCase):
    
    def test_user_creation(self):
        user = User(1, 'John Doe', 'john@example.com', 2)
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.email, 'john@example.com')
        self.assertEqual(user.role_id, 2)
    
    def test_user_creation_with_invalid_user_id(self):
        with self.assertRaises(TypeError):
            User('1', 'John Doe', 'john@example.com', 2)
    
    def test_user_creation_with_invalid_email(self):
        with self.assertRaises(TypeError):
            User(1, 'John Doe', 123, 2)
    
    def test_user_creation_with_missing_arguments(self):
        with self.assertRaises(TypeError):
            User(1, 'John Doe')
    
    def test_user_creation_with_none_values(self):
        user = User(None, None, None, None)
        self.assertIsNone(user.user_id)
        self.assertIsNone(user.name)
        self.assertIsNone(user.email)
        self.assertIsNone(user.role_id)
    
    def test_user_creation_with_boundary_values(self):
        user = User(0, '', 'email@example.com', 0)
        self.assertEqual(user.user_id, 0)
        self.assertEqual(user.name, '')
        self.assertEqual(user.email, 'email@example.com')
        self.assertEqual(user.role_id, 0)

if __name__ == '__main__':
    unittest.main()