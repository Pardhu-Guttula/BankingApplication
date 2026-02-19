import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_page_responsive(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Banking Application!" in response.data
    # Additional assertion to ensure the page is responsive
    assert b"viewport" in response.data


def test_login_page_responsive(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b"Please login" in response.data
    # Additional assertion to ensure the page is responsive
    assert b"viewport" in response.data


def test_login_responsive(client):
    response = client.post('/login', data=dict(username='user', password='pass'), follow_redirects=True)
    assert response.status_code == 200
    assert b"Login successful" in response.data
    # Additional assertion to ensure the page is responsive
    assert b"viewport" in response.data


def test_logout_responsive(client):
    client.post('/login', data=dict(username='user', password='pass'), follow_redirects=True)
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"You have been logged out" in response.data
    # Additional assertion to ensure the page is responsive
    assert b"viewport" in response.data
