# File: tests/test_user_role_repository.py

import pytest
from unittest.mock import Mock
from backend.access_control.models.user_role import UserRole
from backend.access_control.repositories.user_role_repository import UserRoleRepository

@pytest.fixture
def db_session():
    return Mock(spec=Session)

@pytest.fixture
def user_role_repository(db_session):
    return UserRoleRepository(db_session)

class TestUserRoleRepository:

    def test_assign_role_to_user_success(self, user_role_repository, db_session):
        db_session.commit.return_value = None
        db_session.refresh.return_value = None
        user_role = user_role_repository.assign_role_to_user(user_id=1, role_id=2)
        assert user_role.user_id == 1
        assert user_role.role_id == 2
        db_session.add.assert_called_once()
        db_session.commit.assert_called_once()
        db_session.refresh.assert_called_once()

    def test_assign_role_to_user_db_error(self, user_role_repository, db_session):
        db_session.commit.side_effect = Exception("DB Error")
        with pytest.raises(Exception) as excinfo:
            user_role_repository.assign_role_to_user(user_id=1, role_id=2)
        assert "DB Error" in str(excinfo.value)
        db_session.add.assert_called_once()
        db_session.commit.assert_called_once()

    def test_get_user_role_success(self, user_role_repository, db_session):
        mock_user_role = Mock(spec=UserRole)
        db_session.query().filter().first.return_value = mock_user_role
        user_role = user_role_repository.get_user_role(user_id=1)
        assert user_role == mock_user_role
        db_session.query.assert_called_once_with(UserRole)
        db_session.query().filter.assert_called_once()
        db_session.query().filter().first.assert_called_once()

    def test_get_user_role_not_found(self, user_role_repository, db_session):
        db_session.query().filter().first.return_value = None
        user_role = user_role_repository.get_user_role(user_id=1)
        assert user_role is None
        db_session.query.assert_called_once_with(UserRole)
        db_session.query().filter.assert_called_once()
        db_session.query().filter().first.assert_called_once()

    def test_change_user_role_success(self, user_role_repository, db_session):
        mock_user_role = Mock(spec=UserRole, user_id=1, role_id=2)
        db_session.query().filter().first.return_value = mock_user_role
        db_session.commit.return_value = None
        db_session.refresh.return_value = None
        user_role = user_role_repository.change_user_role(user_id=1, new_role_id=3)
        assert user_role == mock_user_role
        assert user_role.role_id == 3
        db_session.commit.assert_called_once()
        db_session.refresh.assert_called_once()

    def test_change_user_role_not_found(self, user_role_repository, db_session):
        db_session.query().filter().first.return_value = None
        user_role = user_role_repository.change_user_role(user_id=1, new_role_id=3)
        assert user_role is None
        db_session.query.assert_called_once_with(UserRole)
        db_session.query().filter.assert_called_once()