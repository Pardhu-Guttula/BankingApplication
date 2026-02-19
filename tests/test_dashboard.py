import pytest

from app import create_dashboard


def test_create_dashboard():
    user_data = {'username': 'test_user', 'preferences': {'theme': 'dark'}}
    dashboard = create_dashboard(user_data)
    assert 'dashboard' in dashboard
    assert dashboard['username'] == 'test_user'
    assert dashboard['theme'] == 'dark'
