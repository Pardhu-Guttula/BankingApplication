import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Additional test for account management

def test_account_creation(client):
    # Assuming '/create_account' is the route for account creation
    response = client.post('/create_account', data=dict(account_name='testaccount', initial_deposit=1000))
    assert response.status_code == 200
    assert b'Account Created Successfully' in response.data

# Test for account deletion

def test_account_deletion(client):
    # Create account first
    client.post('/create_account', data=dict(account_name='testaccount', initial_deposit=1000))
    # Assuming '/delete_account' is the route for account deletion
    response = client.post('/delete_account', data=dict(account_name='testaccount'))
    assert response.status_code == 200
    assert b'Account Deleted Successfully' in response.data
