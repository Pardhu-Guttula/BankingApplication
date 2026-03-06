# File: tests/test_behavior_metric_api.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.api.behavior_metric_api import behavior_metric_bp
from flask.testing import FlaskClient
import sqlalchemy.exc

class TestBehaviorMetricAPI(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(behavior_metric_bp)
        self.client: FlaskClient = self.app.test_client()

    @patch('backend.api.behavior_metric_api.get_db')
    @patch('backend.analytics.repositories.behavior_metric_repository.BehaviorMetricRepository')
    @patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService')
    def test_get_metrics_by_user_id_success(self, MockService, MockRepository, MockDB):
        mock_db = MagicMock()
        MockDB.return_value = iter([mock_db])
        mock_service = MockService.return_value
        mock_service.get_metrics_by_user_id.return_value = {
            'user_id': 1,
            'metrics': []
        }

        response = self.client.get('/behavior_metrics/user/1')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'user_id': 1, 'metrics': []})

    @patch('backend.api.behavior_metric_api.get_db')
    @patch('backend.analytics.repositories.behavior_metric_repository.BehaviorMetricRepository')
    @patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService')
    def test_get_metrics_by_user_id_sqlalchemy_error(self, MockService, MockRepository, MockDB):
        mock_db = MagicMock()
        MockDB.return_value = iter([mock_db])
        MockService.return_value.get_metrics_by_user_id.side_effect = sqlalchemy.exc.SQLAlchemyError

        response = self.client.get('/behavior_metrics/user/1')

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'error': 'Unable to process your request'})

    @patch('backend.api.behavior_metric_api.get_db')
    @patch('backend.analytics.repositories.behavior_metric_repository.BehaviorMetricRepository')
    @patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService')
    def test_create_metric_success(self, MockService, MockRepository, MockDB):
        mock_db = MagicMock()
        MockDB.return_value = iter([mock_db])
        mock_service = MockService.return_value
        mock_service.create_metric.return_value = {
            'success': True,
            'metric': MagicMock(id=1, user_id=101, session_duration=300, page_views=5, click_through_rate=0.2, created_at='2023-10-01T12:00:00Z', updated_at='2023-10-01T12:00:00Z')
        }

        payload = {
            'user_id': 101,
            'session_duration': 300,
            'page_views': 5,
            'click_through_rate': 0.2
        }

        response = self.client.post('/behavior_metrics/create', json=payload)

        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['user_id'], 101)
        self.assertEqual(response.json['session_duration'], 300)

    @patch('backend.api.behavior_metric_api.get_db')
    @patch('backend.analytics.repositories.behavior_metric_repository.BehaviorMetricRepository')
    @patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService')
    def test_create_metric_failure(self, MockService, MockRepository, MockDB):
        mock_db = MagicMock()
        MockDB.return_value = iter([mock_db])
        mock_service = MockService.return_value
        mock_service.create_metric.return_value = {
            'success': False
        }

        payload = {
            'user_id': 101,
            'session_duration': 300,
            'page_views': 5,
            'click_through_rate': 0.2
        }

        response = self.client.post('/behavior_metrics/create', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Metric creation failed'})

    @patch('backend.api.behavior_metric_api.get_db')
    @patch('backend.analytics.repositories.behavior_metric_repository.BehaviorMetricRepository')
    @patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService')
    def test_create_metric_sqlalchemy_error(self, MockService, MockRepository, MockDB):
        mock_db = MagicMock()
        MockDB.return_value = iter([mock_db])
        MockService.return_value.create_metric.side_effect = sqlalchemy.exc.SQLAlchemyError

        payload = {
            'user_id': 101,
            'session_duration': 300,
            'page_views': 5,
            'click_through_rate': 0.2
        }

        response = self.client.post('/behavior_metrics/create', json=payload)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'error': 'Unable to process your request'})

    def test_create_metric_no_payload(self):
        response = self.client.post('/behavior_metrics/create', json=None)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid input'})

if __name__ == '__main__':
    unittest.main()
