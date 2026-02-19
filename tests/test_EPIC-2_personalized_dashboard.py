import pytest


def test_personalized_dashboard_creation():
    # Test for successful creation of a personalized dashboard
    response = client.post('/dashboard', json={"user_id": 1, "preferences": {"theme": "dark", "layout": "grid"}})
    assert response.status_code == 201
    assert response.json == {"message": "Dashboard created successfully"}


def test_personalized_dashboard_retrieval():
    # Test for retrieving an existing personalized dashboard
    response = client.get('/dashboard/1')
    assert response.status_code == 200
    assert response.json == {"user_id": 1, "preferences": {"theme": "dark", "layout": "grid"}}


def test_personalized_dashboard_update():
    # Test for updating personalized dashboard settings
    response = client.put('/dashboard/1', json={"preferences": {"theme": "light", "layout": "list"}})
    assert response.status_code == 200
    assert response.json == {"message": "Dashboard updated successfully"}


def test_personalized_dashboard_deletion():
    # Test for deleting an existing personalized dashboard
    response = client.delete('/dashboard/1')
    assert response.status_code == 204
    assert response.data == b''
