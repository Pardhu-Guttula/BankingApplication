# File: tests/test_user_repository.py

import unittest
from backend.access_control.models.user import User
from backend.access_control.repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repo = UserRepository()
        self.existing_user = self.user_repo.users[0]

    # Positive scenarios
    def test_find_by_email_existing_user(self):
        user = self.user_repo.find_by_email(self.existing_user.email)
        self.assertIsNotNone(user)
        self.assertEqual(user.email, self.existing_user.email)

    def test_update_role_existing_user(self):
        result = self.user_repo.update_role(self.existing_user.user_id, 1)
        self.assertTrue(result)
        self.assertEqual(self.existing_user.role_id, 1)

    # Negative scenarios
    def test_find_by_email_non_existent_user(self):
        user = self.user_repo.find_by_email("nonexistent@example.com")
        self.assertIsNone(user)

    def test_update_role_non_existent_user(self):
        result = self.user_repo.update_role(999, 1)
        self.assertFalse(result)

    # Edge cases
    def test_find_by_email_empty_string(self):
        user = self.user_repo.find_by_email("")
        self.assertIsNone(user)

    def test_find_by_email_invalid_email(self):
        user = self.user_repo.find_by_email("invalid-email")
        self.assertIsNone(user)

    def test_update_role_with_zero_role_id(self):
        result = self.user_repo.update_role(self.existing_user.user_id, 0)
        self.assertTrue(result)
        self.assertEqual(self.existing_user.role_id, 0)

    def test_update_role_with_negative_role_id(self):
        result = self.user_repo.update_role(self.existing_user.user_id, -1)
        self.assertTrue(result)
        self.assertEqual(self.existing_user.role_id, -1)

if __name__ == '__main__':
    unittest.main()