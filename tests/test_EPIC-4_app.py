import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test for fetching user interaction history
def test_user_interaction_history(client):
    # Assuming '/interaction-history' is the route for fetching interaction history
    response = client.get('/interaction-history')
    assert response.status_code == 200
    assert b'Interaction History' in response.data

# Test for adding a new interaction
def test_add_new_interaction(client):
    # Assuming '/add-interaction' is the route for adding a new interaction
    response = client.post('/add-interaction', data=dict(detail='User viewed account details'))
    assert response.status_code == 201
    assert b'Interaction Added' in response.data
