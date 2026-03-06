# File: tests/test_behavior_metric_repository.py

import unittest
from unittest.mock import Mock
from sqlalchemy.orm import Session
from backend.analytics.models.behavior_metric import BehaviorMetric
from backend.analytics.repositories.behavior_metric_repository import BehaviorMetricRepository

class TestBehaviorMetricRepository(unittest.TestCase):
    def setUp(self):
        self.mock_session = Mock(spec=Session)
        self.repo = BehaviorMetricRepository(self.mock_session)
        self.user_id = 1
        self.session_duration = 300.5
        self.page_views = 10
        self.click_through_rate = 0.25

    def test_get_metrics_by_user_id_returns_metrics(self):
        # Mock behavior
        mock_metric = Mock(spec=BehaviorMetric)
        self.mock_session.query.return_value.filter.return_value.all.return_value = [mock_metric]

        result = self.repo.get_metrics_by_user_id(self.user_id)

        self.mock_session.query.assert_called_with(BehaviorMetric)
        self.mock_session.query.return_value.filter.assert_called_with(BehaviorMetric.user_id == self.user_id)
        self.assertEqual(result, [mock_metric])

    def test_get_metrics_by_user_id_no_metrics(self):
        # Mock behavior for no results
        self.mock_session.query.return_value.filter.return_value.all.return_value = []

        result = self.repo.get_metrics_by_user_id(self.user_id)

        self.mock_session.query.assert_called_with(BehaviorMetric)
        self.mock_session.query.return_value.filter.assert_called_with(BehaviorMetric.user_id == self.user_id)
        self.assertEqual(result, [])

    def test_create_metric_successful(self):
        # Mock behavior
        mock_metric = Mock(spec=BehaviorMetric)
        self.mock_session.add.return_value = None
        self.mock_session.commit.return_value = None
        self.mock_session.refresh.return_value = None

        result = self.repo.create_metric(self.user_id, self.session_duration, self.page_views, self.click_through_rate)

        self.mock_session.add.assert_called_once()
        self.mock_session.commit.assert_called_once()
        self.mock_session.refresh.assert_called_once_with(result)

    def test_create_metric_with_invalid_input(self):
        invalid_user_id = None
        with self.assertRaises(TypeError):
            self.repo.create_metric(invalid_user_id, self.session_duration, self.page_views, self.click_through_rate)

        invalid_session_duration = "not a float"
        with self.assertRaises(TypeError):
            self.repo.create_metric(self.user_id, invalid_session_duration, self.page_views, self.click_through_rate)

        invalid_page_views = "not an int"
        with self.assertRaises(TypeError):
            self.repo.create_metric(self.user_id, self.session_duration, invalid_page_views, self.click_through_rate)

        invalid_click_through_rate = "not a float"
        with self.assertRaises(TypeError):
            self.repo.create_metric(self.user_id, self.session_duration, self.page_views, invalid_click_through_rate)

    def test_create_metric_boundary_values(self):
        boundary_user_id = 0
        boundary_session_duration = 0.0
        boundary_page_views = 0
        boundary_click_through_rate = 0.0

        result = self.repo.create_metric(boundary_user_id, boundary_session_duration, boundary_page_views, boundary_click_through_rate)

        self.mock_session.add.assert_called_once()
        self.mock_session.commit.assert_called_once()
        self.mock_session.refresh.assert_called_once_with(result)

if __name__ == '__main__':
    unittest.main()
