import pytest
from backend import app

@pytest.fixture

def client():
    with app.test_client() as client:
        yield client


def test_save_applications(client):
    # Assuming we have a route to save applications
    response = client.post('/save_application', json={'data': 'test_data'})
    assert response.status_code == 200
    assert response.json == {'message': 'Application saved successfully'}


def test_resume_applications(client):
    # Assuming we have a route to resume applications
    response = client.get('/resume_application', query_string={'app_id': 1})
    assert response.status_code == 200
    assert response.json == {'data': 'test_data'}