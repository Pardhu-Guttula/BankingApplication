# File: tests/test_app.py

import unittest
from unittest.mock import patch, MagicMock
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.role_service.assign_role')
    def test_assign_role_success(self, mock_assign_role):
        mock_assign_role.return_value = True
        response = self.app.post('/assign-role', json={"email": "user@example.com", "role": "admin"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Role assigned successfully"})

    @patch('app.role_service.assign_role')
    def test_assign_role_failure(self, mock_assign_role):
        mock_assign_role.return_value = False
        response = self.app.post('/assign-role', json={"email": "user@example.com", "role": "admin"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Failed to assign role"})

    @patch('app.role_service.assign_role')
    def test_assign_role_no_data(self, mock_assign_role):
        response = self.app.post('/assign-role', json={})
        self.assertEqual(response.status_code, 400)

    @patch('app.role_service.get_permissions')
    def test_get_permissions_success(self, mock_get_permissions):
        mock_get_permissions.return_value = ["read", "write"]
        response = self.app.get('/permissions?email=user@example.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"permissions": ["read", "write"]})

    @patch('app.role_service.get_permissions')
    def test_get_permissions_no_email(self, mock_get_permissions):
        response = self.app.get('/permissions')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"permissions": []})

    @patch('app.role_service.get_permissions')
    def test_get_permissions_invalid_email(self, mock_get_permissions):
        mock_get_permissions.return_value = []
        response = self.app.get('/permissions?email=invalid@example.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"permissions": []})

if __name__ == '__main__':
    unittest.main()
