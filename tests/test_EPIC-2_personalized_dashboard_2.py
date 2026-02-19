import pytest
from app import create_app
from flask import json

def test_dashboard_personalization():
    app = create_app()
    client = app.test_client()

    # Simulate login
    with client.session_transaction() as sess:
        sess['user_id'] = 1

    # Make request to personalized dashboard
    response = client.get('/dashboard')

    # Verify user-specific content in dashboard
    assert response.status_code == 200
    data = json.loads(response.data.decode('utf-8'))
    assert 'Welcome, User 1!' in data['message']
    assert 'Your account balance is' in data['content']