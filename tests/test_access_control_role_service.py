# File: tests/test_access_control_role_service.py

import pytest
from unittest.mock import MagicMock, create_autospec
from backend.access_control.services.role_service import RoleService
from backend.access_control.repositories.role_repository import RoleRepository
from backend.access_control.repositories.user_repository import UserRepository

@pytest.fixture
def role_repository():
    return create_autospec(RoleRepository)

@pytest.fixture
def user_repository():
    return create_autospec(UserRepository)

@pytest.fixture
def role_service(role_repository, user_repository):
    return RoleService(role_repository, user_repository)

class TestRoleService:

    def test_assign_role_success(self, role_service, role_repository, user_repository):
        user_repository.find_by_email.return_value = MagicMock(user_id=1, role_id=1)
        role_repository.get_role_by_name.return_value = MagicMock(role_id=2)
        
        assert role_service.assign_role('user@example.com', 'admin') is True
        user_repository.update_role.assert_called_once_with(1, 2)

    def test_assign_role_user_not_found(self, role_service, role_repository, user_repository):
        user_repository.find_by_email.return_value = None
        role_repository.get_role_by_name.return_value = MagicMock(role_id=2)
        
        assert role_service.assign_role('user@example.com', 'admin') is False
        user_repository.update_role.assert_not_called()

    def test_assign_role_role_not_found(self, role_service, role_repository, user_repository):
        user_repository.find_by_email.return_value = MagicMock(user_id=1, role_id=1)
        role_repository.get_role_by_name.return_value = None
        
        assert role_service.assign_role('user@example.com', 'admin') is False
        user_repository.update_role.assert_not_called()

    def test_assign_role_user_and_role_not_found(self, role_service, role_repository, user_repository):
        user_repository.find_by_email.return_value = None
        role_repository.get_role_by_name.return_value = None
        
        assert role_service.assign_role('user@example.com', 'admin') is False
        user_repository.update_role.assert_not_called()

    def test_get_permissions_success(self, role_service, role_repository, user_repository):
        user_repository.find_by_email.return_value = MagicMock(user_id=1, role_id='admin')
        role_repository.get_role_by_name.return_value = MagicMock(permissions=['read', 'write'])
        
        assert role_service.get_permissions('user@example.com') == ['read', 'write']

    def test_get_permissions_user_not_found(self, role_service, role_repository, user_repository):
        user_repository.find_by_email.return_value = None
        
        assert role_service.get_permissions('user@example.com') == []

    def test_get_permissions_role_not_found(self, role_service, role_repository, user_repository):
        user_repository.find_by_email.return_value = MagicMock(user_id=1, role_id='admin')
        role_repository.get_role_by_name.return_value = None
        
        assert role_service.get_permissions('user@example.com') == []
