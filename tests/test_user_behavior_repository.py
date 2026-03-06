# File: tests/test_user_behavior_repository.py

import unittest
from unittest.mock import patch, MagicMock
from backend.analytics.models.user_session import UserBehaviorRepository
import mysql.connector

class TestUserBehaviorRepository(unittest.TestCase):

    def setUp(self):
        self.db_config = {'user': 'testuser', 'password': 'password', 'host': '127.0.0.1', 'database': 'testdb'}
        self.repo = UserBehaviorRepository(self.db_config)

    @patch('mysql.connector.connect')
    def test_get_average_session_duration(self, mock_connect):
        # Mock the cursor and connection
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = [3600.0]

        # Positive test
        avg_duration = self.repo.get_average_session_duration()
        self.assertEqual(avg_duration, 3600.0)

        # Test empty result set
        mock_cursor.fetchone.return_value = None
        avg_duration = self.repo.get_average_session_duration()
        self.assertEqual(avg_duration, 0.0)

        # Test exception path
        mock_cursor.execute.side_effect = mysql.connector.Error
        avg_duration = self.repo.get_average_session_duration()
        self.assertEqual(avg_duration, 0.0)
        mock_cursor.execute.side_effect = None

    @patch('mysql.connector.connect')
    def test_get_total_page_views(self, mock_connect):
        # Mock the cursor and connection
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = [100]

        # Positive test
        total_views = self.repo.get_total_page_views()
        self.assertEqual(total_views, 100)

        # Test empty result set
        mock_cursor.fetchone.return_value = None
        total_views = self.repo.get_total_page_views()
        self.assertEqual(total_views, 0)

        # Test exception path
        mock_cursor.execute.side_effect = mysql.connector.Error
        total_views = self.repo.get_total_page_views()
        self.assertEqual(total_views, 0)
        mock_cursor.execute.side_effect = None

    @patch('mysql.connector.connect')
    def test_get_click_through_rates(self, mock_connect):
        # Mock the cursor and connection
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(1, 10), (2, 20)]

        # Positive test
        click_rates = self.repo.get_click_through_rates()
        self.assertEqual(click_rates, [{'element_id': 1, 'total_clicks': 10}, {'element_id': 2, 'total_clicks': 20}])

        # Test empty result set
        mock_cursor.fetchall.return_value = []
        click_rates = self.repo.get_click_through_rates()
        self.assertEqual(click_rates, [])

        # Test exception path
        mock_cursor.execute.side_effect = mysql.connector.Error
        click_rates = self.repo.get_click_through_rates()
        self.assertEqual(click_rates, [])
        mock_cursor.execute.side_effect = None

if __name__ == '__main__':
    unittest.main()