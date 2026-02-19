import pytest
from backend.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_incomplete_application(client):
    response = client.post('/submit_application', data=dict(application_data='incomplete_data'), follow_redirects=True)
    assert response.status_code == 400
    assert b"Incomplete application data" in response.data
