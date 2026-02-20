import pytest
from backend.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_account_creation(client):
    response = client.post('/create_account', data=dict(name='John Doe', initial_deposit=1000))
    assert response.status_code == 200
    assert b"Account created successfully" in response.data


def test_account_balance(client):
    response = client.get('/balance?account_id=1')
    assert response.status_code == 200
    assert b"1000" in response.data


def test_account_deposit(client):
    response = client.post('/deposit', data=dict(account_id=1, amount=500))
    assert response.status_code == 200
    assert b"Deposit successful" in response.data


def test_account_withdrawal(client):
    response = client.post('/withdraw', data=dict(account_id=1, amount=200))
    assert response.status_code == 200
    assert b"Withdrawal successful" in response.data
