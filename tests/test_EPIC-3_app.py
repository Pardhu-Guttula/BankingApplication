import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test for creating a new account
def test_create_account(client):
    response = client.post('/create_account', data=dict(account_name='testaccount', initial_deposit=100))
    assert response.status_code == 200
    assert b'Account created successfully' in response.data

# Test for retrieving account information
def test_get_account_info(client):
    response = client.get('/account_info?account_name=testaccount')
    assert response.status_code == 200
    assert b'testaccount' in response.data

# Test for deleting an account
def test_delete_account(client):
    response = client.post('/delete_account', data=dict(account_name='testaccount'))
    assert response.status_code == 200
    assert b'Account deleted successfully' in response.data
