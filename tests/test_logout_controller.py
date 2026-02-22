# File: tests/test_logout_controller.py

import unittest
from unittest.mock import patch, MagicMock
from logout_controller import app, active_sessions

class LogoutControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('logout_controller.logout_service.logout')
    def test_logout_success(self, mock_logout):
        mock_logout.return_value = True
        response = self.app.post('/logout', headers={'Authorization': 'valid_token'})
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login', response.location)

    @patch('logout_controller.logout_service.logout')
    def test_logout_invalid_token(self, mock_logout):
        mock_logout.return_value = False
        response = self.app.post('/logout', headers={'Authorization': 'invalid_token'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'error': 'Invalid token'})

    @patch('logout_controller.logout_service.logout')
    def test_logout_missing_token(self, mock_logout):
        response = self.app.post('/logout')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'error': 'Invalid token'})

if __name__ == '__main__':
    unittest.main()