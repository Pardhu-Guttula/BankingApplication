# File: tests/test_user_behavior.py

import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from backend.analytics.repositories.user_behavior_repository import UserBehaviorRepository
import behavior_bp

class BehaviorBlueprintTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(behavior_bp.behavior_bp)
        self.client = self.app.test_client()

    @patch.object(UserBehaviorRepository, 'get_average_session_duration')
    def test_get_session_duration_success(self, mock_get_average):
        mock_get_average.return_value = 125.0

        response = self.client.get('/user/session-duration')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'average_session_duration': 125.0})

    @patch.object(UserBehaviorRepository, 'get_average_session_duration')
    def test_get_session_duration_failure(self, mock_get_average):
        mock_get_average.side_effect = Exception('Database error')

        response = self.client.get('/user/session-duration')
        self.assertEqual(response.status_code, 500)

    @patch.object(UserBehaviorRepository, 'get_total_page_views')
    def test_get_page_views_success(self, mock_get_total_views):
        mock_get_total_views.return_value = 2500

        response = self.client.get('/user/page-views')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'total_page_views': 2500})

    @patch.object(UserBehaviorRepository, 'get_total_page_views')
    def test_get_page_views_failure(self, mock_get_total_views):
        mock_get_total_views.side_effect = Exception('Database error')

        response = self.client.get('/user/page-views')
        self.assertEqual(response.status_code, 500)

    @patch.object(UserBehaviorRepository, 'get_click_through_rates')
    def test_get_click_rates_success(self, mock_get_click_rates):
        mock_get_click_rates.return_value = {'home': 5.0, 'product': 7.2}

        response = self.client.get('/user/click-through-rates')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'click_through_rates': {'home': 5.0, 'product': 7.2}})

    @patch.object(UserBehaviorRepository, 'get_click_through_rates')
    def test_get_click_rates_failure(self, mock_get_click_rates):
        mock_get_click_rates.side_effect = Exception('Database error')

        response = self.client.get('/user/click-through-rates')
        self.assertEqual(response.status_code, 500)