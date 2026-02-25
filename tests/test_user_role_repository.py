# File: tests/test_user_role_repository.py

import unittest
from unittest.mock import MagicMock, create_autospec
from sqlalchemy.orm import Session
from backend.access_control.models.user_role import UserRole
from backend.access_control.repositories.user_role_repository import UserRoleRepository

class TestUserRoleRepository(unittest.TestCase):
    def setUp(self):
        self.db = create_autospec(Session)
        self.user_role_repository = UserRoleRepository(self.db)

    def test_assign_role_to_user_success(self):
        user_id = 1
        role_id = 2
        user_role = UserRole(user_id=user_id, role_id=role_id)

        self.db.add.return_value = None
        self.db.commit.return_value = None
        self.db.refresh.return_value = None

        result = self.user_role_repository.assign_role_to_user(user_id, role_id)

        self.db.add.assert_called_once_with(user_role)
        self.db.commit.assert_called_once()
        self.db.refresh.assert_called_once_with(user_role)
        self.assertEqual(result.user_id, user_id)
        self.assertEqual(result.role_id, role_id)

    def test_assign_role_to_user_failure(self):
        user_id = 1
        role_id = 2

        self.db.add.side_effect = Exception("DB Error")

        with self.assertRaises(Exception) as context:
            self.user_role_repository.assign_role_to_user(user_id, role_id)

        self.assertTrue('DB Error' in str(context.exception))
        self.db.commit.assert_not_called()
        self.db.refresh.assert_not_called()

    def test_get_user_role_exists(self):
        user_id = 1
        user_role = UserRole(user_id=user_id, role_id=2)

        self.db.query().filter().first.return_value = user_role

        result = self.user_role_repository.get_user_role(user_id)

        self.db.query().filter.assert_called_once_with(UserRole.user_id == user_id)
        self.assertEqual(result, user_role)

    def test_get_user_role_not_exists(self):
        user_id = 1

        self.db.query().filter().first.return_value = None

        result = self.user_role_repository.get_user_role(user_id)

        self.db.query().filter.assert_called_once_with(UserRole.user_id == user_id)
        self.assertIsNone(result)

    def test_change_user_role_success(self):
        user_id = 1
        new_role_id = 3
        user_role = UserRole(user_id=user_id, role_id=2)

        self.user_role_repository.get_user_role = MagicMock(return_value=user_role)
        self.db.commit.return_value = None
        self.db.refresh.return_value = None

        result = self.user_role_repository.change_user_role(user_id, new_role_id)

        self.user_role_repository.get_user_role.assert_called_once_with(user_id)
        self.db.commit.assert_called_once()
        self.db.refresh.assert_called_once_with(user_role)
        self.assertEqual(result.role_id, new_role_id)

    def test_change_user_role_not_exists(self):
        user_id = 1
        new_role_id = 3

        self.user_role_repository.get_user_role = MagicMock(return_value=None)

        result = self.user_role_repository.change_user_role(user_id, new_role_id)

        self.user_role_repository.get_user_role.assert_called_once_with(user_id)
        self.db.commit.assert_not_called()
        self.db.refresh.assert_not_called()
        self.assertIsNone(result)

    def test_change_user_role_db_failure(self):
        user_id = 1
        new_role_id = 3
        user_role = UserRole(user_id=user_id, role_id=2)

        self.user_role_repository.get_user_role = MagicMock(return_value=user_role)
        self.db.commit.side_effect = Exception("DB Error")

        with self.assertRaises(Exception) as context:
            self.user_role_repository.change_user_role(user_id, new_role_id)

        self.user_role_repository.get_user_role.assert_called_once_with(user_id)
        self.db.commit.assert_called_once()
        self.assertTrue('DB Error' in str(context.exception))
        self.db.refresh.assert_not_called()

if __name__ == '__main__':
    unittest.main()