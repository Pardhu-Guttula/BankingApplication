# File: tests/test_user_repository.py

import unittest
from backend.authentication.models.user import User
from backend.authentication.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.user_repository = UserRepository()

    def test_find_by_email_existing_user(self):
        # Happy path test
        user = self.user_repository.find_by_email("john@example.com")
        self.assertIsNotNone(user)
        self.assertEqual(user.email, "john@example.com")

    def test_find_by_email_non_existing_user(self):
        # Negative test path
        user = self.user_repository.find_by_email("nonexistent@example.com")
        self.assertIsNone(user)

    def test_find_by_email_empty_email(self):
        # Edge case: empty email
        user = self.user_repository.find_by_email("")
        self.assertIsNone(user)

    def test_find_by_email_invalid_email(self):
        # Edge case: invalid email format
        user = self.user_repository.find_by_email("invalid-email")
        self.assertIsNone(user)

    def test_find_by_email_case_insensitive(self):
        # Ensure email lookup is case-insensitive
        user = self.user_repository.find_by_email("JOHN@EXAMPLE.COM")
        self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()
