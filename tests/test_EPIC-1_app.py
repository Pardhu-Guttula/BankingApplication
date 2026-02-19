import pytest
from app import create_dashboard

def test_create_dashboard():
    user_id = 1
    dashboard = create_dashboard(user_id)
    assert dashboard['user_id'] == user_id
    assert 'widgets' in dashboard