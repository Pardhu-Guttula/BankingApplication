# File: tests/test_session.py

import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from session import Session

class TestSession(unittest.TestCase):

    def setUp(self):
        self.valid_until = datetime.now() + timedelta(days=1)
        self.session = Session(session_id="12345", user_id=1, token="token123", valid_until=self.valid_until)

    def test_is_valid_when_session_is_valid(self):
        self.assertTrue(self.session.is_valid())

    def test_is_valid_when_session_is_expired(self):
        self.session.valid_until = datetime.now() - timedelta(days=1)
        self.assertFalse(self.session.is_valid())

    def test_is_valid_right_before_expiry(self):
        self.session.valid_until = datetime.now() + timedelta(seconds=1)
        self.assertTrue(self.session.is_valid())

    def test_is_valid_right_after_expiry(self):
        self.session.valid_until = datetime.now() - timedelta(seconds=1)
        self.assertFalse(self.session.is_valid())

if __name__ == '__main__':
    unittest.main()