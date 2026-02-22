# File: tests/test_user.py
import unittest
from user import User

class TestUser(unittest.TestCase):

    def test_user_initialization(self):
        user = User(1, 'John Doe', 'johndoe@example.com', 2)
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.email, 'johndoe@example.com')
        self.assertEqual(user.role_id, 2)

    def test_user_initialization_with_invalid_id(self):
        with self.assertRaises(TypeError):
            user = User('one', 'John Doe', 'johndoe@example.com', 2)

    def test_user_initialization_with_missing_name(self):
        with self.assertRaises(TypeError):
            user = User(1, None, 'johndoe@example.com', 2)

    def test_user_initialization_with_invalid_email_format(self):
        user = User(1, 'John Doe', 'invalidemailformat', 2)
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.email, 'invalidemailformat')
        self.assertEqual(user.role_id, 2)

    def test_user_edge_case_max_int_user_id(self):
        user = User(2147483647, 'John Doe', 'johndoe@example.com', 2)
        self.assertEqual(user.user_id, 2147483647)
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.email, 'johndoe@example.com')
        self.assertEqual(user.role_id, 2)

    def test_user_edge_case_min_int_user_id(self):
        user = User(-2147483648, 'John Doe', 'johndoe@example.com', 2)
        self.assertEqual(user.user_id, -2147483648)
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.email, 'johndoe@example.com')
        self.assertEqual(user.role_id, 2)

    def test_user_initialization_none_user_id(self):
        with self.assertRaises(TypeError):
            user = User(None, 'John Doe', 'johndoe@example.com', 2)

    def test_user_initialization_none_name(self):
        user = User(1, None, 'johndoe@example.com', 2)
        self.assertEqual(user.user_id, 1)
        self.assertIsNone(user.name)
        self.assertEqual(user.email, 'johndoe@example.com')
        self.assertEqual(user.role_id, 2)

    def test_user_initialization_none_email(self):
        with self.assertRaises(TypeError):
            user = User(1, 'John Doe', None, 2)

    def test_user_initialization_none_role_id(self):
        with self.assertRaises(TypeError):
            user = User(1, 'John Doe', 'johndoe@example.com', None)


if __name__ == '__main__':
    unittest.main()