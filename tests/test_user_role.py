# File: tests/test_user_role.py

import unittest
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database.config import Base
from backend.models.user_role import UserRole

class TestUserRole(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Use an in-memory SQLite database for testing
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.session = self.Session()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_create_user_role_happy_path(self):
        user_role = UserRole(user_id=1, role_id=1)
        self.session.add(user_role)
        self.session.commit()
        self.assertIsNotNone(user_role.id)

    def test_create_user_role_missing_user_id(self):
        user_role = UserRole(role_id=1)
        self.session.add(user_role)
        with self.assertRaises(IntegrityError):
            self.session.commit()

    def test_create_user_role_missing_role_id(self):
        user_role = UserRole(user_id=1)
        self.session.add(user_role)
        with self.assertRaises(IntegrityError):
            self.session.commit()

    def test_create_user_role_duplicate_entry(self):
        user_role1 = UserRole(user_id=1, role_id=1)
        user_role2 = UserRole(user_id=1, role_id=1)
        self.session.add(user_role1)
        self.session.add(user_role2)
        self.session.commit()
        result = self.session.query(UserRole).filter_by(user_id=1, role_id=1).all()
        self.assertEqual(len(result), 2)

    def test_create_user_role_no_duplicate_constraint(self):
        user_role1 = UserRole(user_id=1, role_id=1)
        user_role2 = UserRole(user_id=1, role_id=2)
        self.session.add(user_role1)
        self.session.add(user_role2)
        self.session.commit()
        result = self.session.query(UserRole).filter_by(user_id=1).all()
        self.assertEqual(len(result), 2)

    def test_create_user_role_edge_case_zero_user_id(self):
        user_role = UserRole(user_id=0, role_id=1)
        self.session.add(user_role)
        self.session.commit()
        self.assertIsNotNone(user_role.id)

    def test_create_user_role_edge_case_zero_role_id(self):
        user_role = UserRole(user_id=1, role_id=0)
        self.session.add(user_role)
        self.session.commit()
        self.assertIsNotNone(user_role.id)

    def test_create_user_role_negative_user_id(self):
        user_role = UserRole(user_id=-1, role_id=1)
        self.session.add(user_role)
        with self.assertRaises(IntegrityError):
            self.session.commit()

    def test_create_user_role_negative_role_id(self):
        user_role = UserRole(user_id=1, role_id=-1)
        self.session.add(user_role)
        with self.assertRaises(IntegrityError):
            self.session.commit()

    def test_create_user_role_str_user_id(self):
        with self.assertRaises(TypeError):
            user_role = UserRole(user_id='string', role_id=1)
            self.session.add(user_role)
            self.session.commit()

    def test_create_user_role_str_role_id(self):
        with self.assertRaises(TypeError):
            user_role = UserRole(user_id=1, role_id='string')
            self.session.add(user_role)
            self.session.commit()

    def test_create_user_role_none_user_id(self):
        user_role = UserRole(user_id=None, role_id=1)
        self.session.add(user_role)
        with self.assertRaises(IntegrityError):
            self.session.commit()

    def test_create_user_role_none_role_id(self):
        user_role = UserRole(user_id=1, role_id=None)
        self.session.add(user_role)
        with self.assertRaises(IntegrityError):
            self.session.commit()

if __name__ == '__main__':
    unittest.main()