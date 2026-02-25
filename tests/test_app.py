# File: tests/test_app.py
import unittest
from unittest import mock
from flask import json
from app import app, role_service

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test assign_role positive scenario
    @mock.patch('app.role_service.assign_role')
    def test_assign_role_success(self, mock_assign_role):
        mock_assign_role.return_value = True
        response = self.app.post('/assign-role', 
                                 data=json.dumps({"email": "user1@example.com", "role": "admin"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Role assigned successfully"})

    # Test assign_role negative scenario
    @mock.patch('app.role_service.assign_role')
    def test_assign_role_failure(self, mock_assign_role):
        mock_assign_role.return_value = False
        response = self.app.post('/assign-role', 
                                 data=json.dumps({"email": "user1@example.com", "role": "admin"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Failed to assign role"})

    # Test assign_role with missing email
    def test_assign_role_missing_email(self):
        response = self.app.post('/assign-role', 
                                 data=json.dumps({"role": "admin"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # Test assign_role with missing role
    def test_assign_role_missing_role(self):
        response = self.app.post('/assign-role', 
                                 data=json.dumps({"email": "user1@example.com"}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # Test assign_role with invalid json
    def test_assign_role_invalid_json(self):
        response = self.app.post('/assign-role', 
                                 data="invalid json",
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    # Test get_permissions positive scenario
    @mock.patch('app.role_service.get_permissions')
    def test_get_permissions_success(self, mock_get_permissions):
        mock_get_permissions.return_value = ["read", "write"]
        response = self.app.get('/permissions?email=user1@example.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"permissions": ["read", "write"]})

    # Test get_permissions with missing email
    def test_get_permissions_missing_email(self):
        response = self.app.get('/permissions')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"permissions": []})

if __name__ == '__main__':
    unittest.main()