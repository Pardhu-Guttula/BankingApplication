# File: tests/test_logout_service.py

import unittest
from backend.authentication.models.session import Session
from logout_service import LogoutService

class TestLogoutService(unittest.TestCase):

    def setUp(self):
        self.sessions = [Session(token='token1'), Session(token='token2')]
        self.logout_service = LogoutService(active_sessions=self.sessions)

    def test_logout_valid_token(self):
        result = self.logout_service.logout('token1')
        self.assertTrue(result)
        self.assertEqual(len(self.logout_service.active_sessions), 1)

    def test_logout_invalid_token(self):
        result = self.logout_service.logout('invalid_token')
        self.assertFalse(result)
        self.assertEqual(len(self.logout_service.active_sessions), 2)

    def test_logout_empty_token(self):
        result = self.logout_service.logout('')
        self.assertFalse(result)
        self.assertEqual(len(self.logout_service.active_sessions), 2)

    def test_logout_none_token(self):
        result = self.logout_service.logout(None)
        self.assertFalse(result)
        self.assertEqual(len(self.logout_service.active_sessions), 2)

    def test_logout_last_session(self):
        self.logout_service.logout('token1')
        result = self.logout_service.logout('token2')
        self.assertTrue(result)
        self.assertEqual(len(self.logout_service.active_sessions), 0)

if __name__ == '__main__':
    unittest.main()