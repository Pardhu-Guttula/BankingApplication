# File: tests/test_authentication_service.py

import datetime
import hashlib
import secrets
from unittest import TestCase
from unittest.mock import MagicMock
from backend.authentication.models.user import User
from backend.authentication.models.session import Session
from backend.authentication.repositories.user_repository import UserRepository
from authentication_service import AuthenticationService

class TestAuthenticationService(TestCase):
    def setUp(self):
        self.user_repository = MagicMock(spec=UserRepository)
        self.auth_service = AuthenticationService(self.user_repository)

    def test_login_success(self):
        user = User(user_id=1, email='test@example.com', hashed_password=self.auth_service.hash_password('password'))
        self.user_repository.find_by_email.return_value = user

        session = self.auth_service.login('test@example.com', 'password')

        self.assertIsNotNone(session)
        self.assertEqual(session.user_id, 1)
        self.assertEqual(len(session.token), 32)
        self.assertGreater(session.valid_until, datetime.datetime.now())

    def test_login_failure_wrong_password(self):
        user = User(user_id=1, email='test@example.com', hashed_password=self.auth_service.hash_password('password'))
        self.user_repository.find_by_email.return_value = user

        session = self.auth_service.login('test@example.com', 'wrongpassword')

        self.assertIsNone(session)

    def test_login_failure_user_not_found(self):
        self.user_repository.find_by_email.return_value = None

        session = self.auth_service.login('unknown@example.com', 'password')

        self.assertIsNone(session)

    def test_login_failure_null_email(self):
        session = self.auth_service.login(None, 'password')

        self.assertIsNone(session)

    def test_login_failure_null_password(self):
        self.user_repository.find_by_email.return_value = None

        session = self.auth_service.login('test@example.com', None)

        self.assertIsNone(session)

    def test_hash_password_consistency(self):
        password = 'password'
        hashed_password1 = self.auth_service.hash_password(password)
        hashed_password2 = self.auth_service.hash_password(password)

        self.assertEqual(hashed_password1, hashed_password2)

    def test_hash_password_different_inputs(self):
        password1 = 'password1'
        password2 = 'password2'
        hashed_password1 = self.auth_service.hash_password(password1)
        hashed_password2 = self.auth_service.hash_password(password2)

        self.assertNotEqual(hashed_password1, hashed_password2)

    def test_hash_password_not_empty(self):
        password = 'password'
        hashed_password = self.auth_service.hash_password(password)

        self.assertNotEqual(hashed_password, '')
        self.assertTrue(hashed_password)
