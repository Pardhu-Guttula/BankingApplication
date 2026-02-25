# File: tests/test_user_repository.py

import unittest
from backend.access_control.models.user import User
from backend.access_control.repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.repo = UserRepository()

    def test_find_by_email_exists(self):
        user = self.repo.find_by_email("john@example.com")
        self.assertIsNotNone(user)
        self.assertEqual(user.email, "john@example.com")

    def test_find_by_email_not_exists(self):
        user = self.repo.find_by_email("notfound@example.com")
        self.assertIsNone(user)

    def test_update_role_valid_user(self):
        result = self.repo.update_role(1, 3)
        self.assertTrue(result)
        user = self.repo.find_by_email("john@example.com")
        self.assertEqual(user.role_id, 3)

    def test_update_role_invalid_user(self):
        result = self.repo.update_role(99, 3)
        self.assertFalse(result)

    def test_update_role_invalid_role_id(self):
        with self.assertRaises(ValueError):
            self.repo.update_role(1, -1)

if __name__ == "__main__":
    unittest.main()