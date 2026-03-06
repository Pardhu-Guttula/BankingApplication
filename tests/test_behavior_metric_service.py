# File: tests/test_behavior_metric_service.py

import unittest
from unittest.mock import MagicMock, create_autospec
from sqlalchemy.orm import Session
from backend.analytics.repositories.behavior_metric_repository import BehaviorMetricRepository
from backend.analytics.services.behavior_metric_service import BehaviorMetricService

class TestBehaviorMetricService(unittest.TestCase):

    def setUp(self):
        self.mock_repository = create_autospec(BehaviorMetricRepository)
        self.service = BehaviorMetricService(self.mock_repository)
        self.mock_db = create_autospec(Session)

    def test_get_metrics_by_user_id_with_metrics(self):
        mock_metrics = [
            MagicMock(session_duration=10, page_views=5, click_through_rate=0.5),
            MagicMock(session_duration=20, page_views=10, click_through_rate=0.8)
        ]
        self.mock_repository.get_metrics_by_user_id.return_value = mock_metrics

        result = self.service.get_metrics_by_user_id(self.mock_db, 1)

        self.assertEqual(result['average_session_duration'], 15)
        self.assertEqual(result['total_page_views'], 15)
        self.assertEqual(result['average_click_through_rate'], 0.65)
        self.assertEqual(result['metrics'], mock_metrics)

    def test_get_metrics_by_user_id_no_metrics(self):
        self.mock_repository.get_metrics_by_user_id.return_value = []

        result = self.service.get_metrics_by_user_id(self.mock_db, 1)

        self.assertEqual(result['average_session_duration'], 0)
        self.assertEqual(result['total_page_views'], 0)
        self.assertEqual(result['average_click_through_rate'], 0)
        self.assertEqual(result['metrics'], [])

    def test_create_metric_success(self):
        mock_metric = MagicMock()
        self.mock_repository.create_metric.return_value = mock_metric

        result = self.service.create_metric(self.mock_db, 1, 30.0, 20, 0.9)

        self.assertTrue(result['success'])
        self.assertEqual(result['metric'], mock_metric)

    def test_create_metric_failure(self):
        self.mock_repository.create_metric.side_effect = Exception('Database error')

        with self.assertRaises(Exception) as context:
            self.service.create_metric(self.mock_db, 1, 30.0, 20, 0.9)

        self.assertTrue('Database error' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
