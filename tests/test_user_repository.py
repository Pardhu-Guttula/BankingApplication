# File: tests/test_user_repository.py
import unittest
from backend.access_control.models.user import User
from user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.user_repo = UserRepository()

    def test_find_by_email_existing_user(self):
        user = self.user_repo.find_by_email("john@example.com")
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "John Doe")

    def test_find_by_email_non_existing_user(self):
        user = self.user_repo.find_by_email("jane@example.com")
        self.assertIsNone(user)

    def test_update_role_existing_user(self):
        result = self.user_repo.update_role(1, 5)
        self.assertTrue(result)
        user = self.user_repo.find_by_email("john@example.com")
        self.assertEqual(user.role_id, 5)

    def test_update_role_non_existing_user(self):
        result = self.user_repo.update_role(99, 5)
        self.assertFalse(result)

    def test_update_role_invalid_role_id(self):
        with self.assertRaises(TypeError):
            self.user_repo.update_role(1, "invalid_role")

if __name__ == '__main__':
    unittest.main()