# File: tests/test_behavior_metric.py

import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from backend.database.config import Base
from datetime import datetime, timedelta
from source_code_module import BehaviorMetric

class TestBehaviorMetric(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        self.session = self.Session()

    def tearDown(self):
        self.session.close()

    def test_create_behavior_metric(self):
        metric = BehaviorMetric(
            user_id=1,
            session_duration=120.5,
            page_views=10,
            click_through_rate=0.5
        )
        self.session.add(metric)
        self.session.commit()
        self.assertIsNotNone(metric.id)
        self.assertEqual(metric.session_duration, 120.5)
        self.assertEqual(metric.page_views, 10)
        self.assertEqual(metric.click_through_rate, 0.5)

    def test_create_behavior_metric_min_values(self):
        metric = BehaviorMetric(user_id=1)
        self.session.add(metric)
        self.session.commit()
        self.assertIsNotNone(metric.id)
        self.assertIsNone(metric.session_duration)
        self.assertIsNone(metric.page_views)
        self.assertIsNone(metric.click_through_rate)

    def test_create_behavior_metric_edge_values(self):
        metric = BehaviorMetric(
            user_id=0,
            session_duration=0.0,
            page_views=0,
            click_through_rate=0.0
        )
        self.session.add(metric)
        self.session.commit()
        self.assertIsNotNone(metric.id)
        self.assertEqual(metric.user_id, 0)
        self.assertEqual(metric.session_duration, 0.0)
        self.assertEqual(metric.page_views, 0)
        self.assertEqual(metric.click_through_rate, 0.0)

    def test_create_behavior_metric_high_values(self):
        metric = BehaviorMetric(
            user_id=2147483647,
            session_duration=float('inf'),
            page_views=2147483647,
            click_through_rate=1.0
        )
        self.session.add(metric)
        self.session.commit()
        self.assertIsNotNone(metric.id)
        self.assertEqual(metric.user_id, 2147483647)
        self.assertEqual(metric.session_duration, float('inf'))
        self.assertEqual(metric.page_views, 2147483647)
        self.assertEqual(metric.click_through_rate, 1.0)

    def test_create_behavior_metric_invalid_user_id(self):
        with self.assertRaises(Exception):
            metric = BehaviorMetric(user_id=None)
            self.session.add(metric)
            self.session.commit()

    def test_default_timestamps(self):
        metric = BehaviorMetric(user_id=1)
        self.session.add(metric)
        self.session.commit()
        self.assertIsInstance(metric.created_at, datetime)
        self.assertIsInstance(metric.updated_at, datetime)

    def test_auto_update_timestamp(self):
        metric = BehaviorMetric(user_id=1)
        self.session.add(metric)
        self.session.commit()

        created_at = metric.created_at
        updated_at = metric.updated_at

        # Simulate update
        metric.session_duration = 300.0
        self.session.commit()

        self.assertEqual(metric.created_at, created_at)
        self.assertNotEqual(metric.updated_at, updated_at)
        self.assertGreater(metric.updated_at, updated_at)

if __name__ == '__main__':
    unittest.main()