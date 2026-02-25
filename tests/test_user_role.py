# File: tests/test_user_role.py

import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from backend.database.config import Base
from backend.models import UserRole, User

class UserRoleTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create an in-memory SQLite database and bind the Base
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        # Each test gets a fresh session
        self.session = self.Session()

    def tearDown(self):
        # Roll back any changes to keep the tests isolated
        self.session.rollback()
        self.session.close()

    def test_create_user_role(self):
        # Happy path - Create a valid UserRole
        user_role = UserRole(user_id=1, role_id=1)
        self.session.add(user_role)
        self.session.commit()
        self.assertIsNotNone(user_role.id)

    def test_create_user_role_missing_user_id(self):
        # Negative scenario - UserRole with missing user_id
        user_role = UserRole(role_id=1)
        self.session.add(user_role)
        with self.assertRaises(IntegrityError):
            self.session.commit()

    def test_create_user_role_missing_role_id(self):
        # Negative scenario - UserRole with missing role_id
        user_role = UserRole(user_id=1)
        self.session.add(user_role)
        with self.assertRaises(IntegrityError):
            self.session.commit()

    def test_create_user_role_non_integer_user_id(self):
        # Edge case - UserRole with non-integer user_id
        user_role = UserRole(user_id='a', role_id=1)
        self.session.add(user_role)
        with self.assertRaises(IntegrityError):
            self.session.commit()

    def test_create_user_role_non_integer_role_id(self):
        # Edge case - UserRole with non-integer role_id
        user_role = UserRole(user_id=1, role_id='a')
        self.session.add(user_role)
        with self.assertRaises(IntegrityError):
            self.session.commit()

    def test_create_user_role_both_non_integer_ids(self):
        # Edge case - UserRole with both user_id and role_id as non-integer
        user_role = UserRole(user_id='a', role_id='b')
        self.session.add(user_role)
        with self.assertRaises(IntegrityError):
            self.session.commit()

    def test_create_user_role_null_user_id(self):
        # Edge case - UserRole with null user_id
        user_role = UserRole(user_id=None, role_id=1)
        self.session.add(user_role)
        self.assertIsNone(user_role.user_id)
        with self.assertRaises(IntegrityError):
            self.session.commit()

    def test_create_user_role_null_role_id(self):
        # Edge case - UserRole with null role_id
        user_role = UserRole(user_id=1, role_id=None)
        self.session.add(user_role)
        self.assertIsNone(user_role.role_id)
        with self.assertRaises(IntegrityError):
            self.session.commit()

    def test_create_user_role_null_both_ids(self):
        # Edge case - UserRole with both user_id and role_id as null
        user_role = UserRole(user_id=None, role_id=None)
        self.session.add(user_role)
        self.assertIsNone(user_role.user_id)
        self.assertIsNone(user_role.role_id)
        with self.assertRaises(IntegrityError):
            self.session.commit()

if __name__ == '__main__':
    unittest.main()