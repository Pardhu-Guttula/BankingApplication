# File: tests/test_user_behavior_metrics.py
import datetime
import unittest
from user_behavior_metrics import UserSession, PageView, ClickThroughRate

class TestUserSession(unittest.TestCase):
    def test_user_session_creation(self):
        session = UserSession(1, 1, datetime.datetime(2023, 1, 1, 12, 0), datetime.datetime(2023, 1, 1, 13, 0))
        self.assertEqual(session.session_id, 1)
        self.assertEqual(session.user_id, 1)
        self.assertEqual(session.start_time, datetime.datetime(2023, 1, 1, 12, 0))
        self.assertEqual(session.end_time, datetime.datetime(2023, 1, 1, 13, 0))

    def test_user_session_invalid_date(self):
        with self.assertRaises(TypeError):
            UserSession(1, 1, '2023-01-01 12:00', datetime.datetime(2023, 1, 1, 13, 0))

class TestPageView(unittest.TestCase):
    def test_page_view_creation(self):
        view = PageView(1, 1, 'http://example.com', datetime.datetime(2023, 1, 1, 12: 30))
        self.assertEqual(view.view_id, 1)
        self.assertEqual(view.user_id, 1)
        self.assertEqual(view.page_url, 'http://example.com')
        self.assertEqual(view.timestamp, datetime.datetime(2023, 1, 1, 12:30))

    def test_page_view_invalid_url(self):
        with self.assertRaises(TypeError):
            PageView(1, 1, 12345, datetime.datetime(2023, 1, 1, 12:30))

class TestClickThroughRate(unittest.TestCase):
    def test_click_through_rate_creation(self):
        click = ClickThroughRate(1, 1, 'button123', datetime.datetime(2023, 1, 1, 12:45), True)
        self.assertEqual(click.click_id, 1)
        self.assertEqual(click.user_id, 1)
        self.assertEqual(click.element_id, 'button123')
        self.assertEqual(click.timestamp, datetime.datetime(2023, 1, 1, 12:45))
        self.assertTrue(click.clicked)

    def test_click_through_rate_invalid_clicked(self):
        with self.assertRaises(TypeError):
            ClickThroughRate(1, 1, 'button123', datetime.datetime(2023, 1, 1, 12:45), 'yes')

if __name__ == '__main__':
    unittest.main()
