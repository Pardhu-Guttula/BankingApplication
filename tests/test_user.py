# File: tests/test_user.py
import unittest

from user import User

class TestUser(unittest.TestCase):
    def test_create_user_valid(self):
        user = User(1, 'John Doe', 'john.doe@example.com', 2)
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.email, 'john.doe@example.com')
        self.assertEqual(user.role_id, 2)

    def test_create_user_invalid_id(self):
        with self.assertRaises(TypeError):
            User('one', 'John Doe', 'john.doe@example.com', 2)

    def test_create_user_invalid_name(self):
        with self.assertRaises(TypeError):
            User(1, 123, 'john.doe@example.com', 2)

    def test_create_user_invalid_email(self):
        with self.assertRaises(TypeError):
            User(1, 'John Doe', 123, 2)

    def test_create_user_invalid_role_id(self):
        with self.assertRaises(TypeError):
            User(1, 'John Doe', 'john.doe@example.com', 'two')

    def test_create_user_null_name(self):
        user = User(1, None, 'john.doe@example.com', 2)
        self.assertIsNone(user.name)

    def test_create_user_null_email(self):
        user = User(1, 'John Doe', None, 2)
        self.assertIsNone(user.email)

    def test_create_user_null_role_id(self):
        user = User(1, 'John Doe', 'john.doe@example.com', None)
        self.assertIsNone(user.role_id)

if __name__ == '__main__':
    unittest.main()