import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test for user authentication

def test_user_login(client):
    # Assuming '/login' is the route for logging in
    response = client.post('/login', data=dict(username='testuser', password='testpass'))
    assert response.status_code == 200
    assert b'Login Successful' in response.data

# Test for user logout

def test_user_logout(client):
    # Assuming '/logout' is the route for logging out
    response = client.get('/logout')
    assert response.status_code == 200
    assert b'Logout Successful' in response.data

# Test for accessing a protected route

def test_protected_route(client):
    # Assuming '/protected' is a protected route
    response = client.get('/protected')
    assert response.status_code == 401  # Unauthorized before login

    # Now login
    client.post('/login', data=dict(username='testuser', password='testpass'))

    # Accessing the protected route after login
    response = client.get('/protected')
    assert response.status_code == 200
    assert b'Welcome to the protected route' in response.data

# Additional test: Personalized Dashboard access

def test_dashboard_access(client):
    # Assuming '/dashboard' is the personalized dashboard route
    response = client.get('/dashboard')
    assert response.status_code == 401  # Unauthorized before login

    # Now login
    client.post('/login', data=dict(username='testuser', password='testpass'))

    # Accessing the personalized dashboard after login
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Welcome to your personalized dashboard' in response.data
