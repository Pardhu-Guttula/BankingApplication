# File: tests/test_role_controller.py

import unittest
from unittest.mock import patch, MagicMock
from role_controller import app

class TestRoleController(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('backend.access_control.services.role_service.RoleService.assign_role')
    def test_assign_role_success(self, mock_assign_role):
        mock_assign_role.return_value = True
        response = self.app.post('/assign-role', json={"email": "test@example.com", "role": "admin"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Role assigned successfully"})

    @patch('backend.access_control.services.role_service.RoleService.assign_role')
    def test_assign_role_failure(self, mock_assign_role):
        mock_assign_role.return_value = False
        response = self.app.post('/assign-role', json={"email": "test@example.com", "role": "admin"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Failed to assign role"})

    @patch('backend.access_control.services.role_service.RoleService.assign_role')
    def test_assign_role_missing_email(self, mock_assign_role):
        response = self.app.post('/assign-role', json={"role": "admin"})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    @patch('backend.access_control.services.role_service.RoleService.assign_role')
    def test_assign_role_missing_role(self, mock_assign_role):
        response = self.app.post('/assign-role', json={"email": "test@example.com"})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    @patch('backend.access_control.services.role_service.RoleService.get_permissions')
    def test_get_permissions_success(self, mock_get_permissions):
        mock_get_permissions.return_value = ['read', 'write']
        response = self.app.get('/permissions?email=test@example.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"permissions": ['read', 'write']})

    @patch('backend.access_control.services.role_service.RoleService.get_permissions')
    def test_get_permissions_no_email(self, mock_get_permissions):
        response = self.app.get('/permissions')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    @patch('backend.access_control.services.role_service.RoleService.get_permissions')
    def test_get_permissions_empty_permissions(self, mock_get_permissions):
        mock_get_permissions.return_value = []
        response = self.app.get('/permissions?email=test@example.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"permissions": []})

    @patch('backend.access_control.services.role_service.RoleService.get_permissions')
    def test_get_permissions_error(self, mock_get_permissions):
        mock_get_permissions.side_effect = Exception('Unexpected Error')
        response = self.app.get('/permissions?email=test@example.com')
        self.assertEqual(response.status_code, 500)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()
