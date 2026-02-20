import pytest
from app import create_app, db
from app.models import User

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            yield testing_client  # this is where the testing happens!

            db.drop_all()

@pytest.fixture(scope='module')
def new_user():
    user = User(username='testuser', email='testuser@example.com', password='password')
    return user

def test_register_user(test_client, new_user):
    response = test_client.post('/register', data={
        'username': new_user.username,
        'email': new_user.email,
        'password': new_user.password
    })
    assert response.status_code == 200
    assert b'Registration successful' in response.data

def test_login_user(test_client, new_user):
    response = test_client.post('/login', data={
        'email': new_user.email,
        'password': new_user.password
    })
    assert response.status_code == 200
    assert b'Login successful' in response.data
