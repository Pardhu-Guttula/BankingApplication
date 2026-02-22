# File: tests/test_user.py
import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.valid_user = User(user_id=1, name='John Doe', email='john.doe@example.com', hashed_password='hashed_password')

    def test_user_initialization(self):
        user = User(user_id=2, name='Jane Doe', email='jane.doe@example.com', hashed_password='hashed_password2')
        self.assertEqual(user.user_id, 2)
        self.assertEqual(user.name, 'Jane Doe')
        self.assertEqual(user.email, 'jane.doe@example.com')
        self.assertEqual(user.hashed_password, 'hashed_password2')

    def test_validate_email_valid(self):
        valid_email = 'test@example.com'
        self.assertTrue(User.validate_email(valid_email))

    def test_validate_email_invalid(self):
        invalid_email = 'invalid-email'
        self.assertFalse(User.validate_email(invalid_email))

    def test_hash_password(self):
        password = 'password123'
        hashed = User.hash_password(password)
        self.assertEqual(hashed, 'hashed_password')

    def test_invalid_email_on_initialization(self):
        with self.assertRaises(ValueError):
            User(user_id=3, name='Bad Email', email='bad-email', hashed_password='hashed_password3')

    def test_null_email_on_initialization(self):
        with self.assertRaises(ValueError):
            User(user_id=4, name='Null Email', email=None, hashed_password='hashed_password4')

    def test_null_name_on_initialization(self):
        with self.assertRaises(ValueError):
            User(user_id=5, name=None, email='null.name@example.com', hashed_password='hashed_password5')

    def test_empty_password_on_initialization(self):
        with self.assertRaises(ValueError):
            User(user_id=6, name='Empty Password', email='empty.password@example.com', hashed_password='')

if __name__ == '__main__':
    unittest.main()