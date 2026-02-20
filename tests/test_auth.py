import pytest
from app import create_app, db
from app.models import User
from flask_jwt_extended import create_access_token

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    db.create_all()

    # Insert user data
    user1 = User(username='testuser', email='testuser@example.com', password='testpassword')
    db.session.add(user1)
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()


def get_auth_token(client):
    response = client.post('/auth/login', json={'username': 'testuser', 'password': 'testpassword'})
    token = response.get_json()['access_token']
    return token


def test_register_user(test_client, init_database):
    response = test_client.post('/auth/register', json={'username': 'newuser', 'email': 'newuser@example.com', 'password': 'newpassword'})
    assert response.status_code == 201
    assert response.get_json()['message'] == 'User created successfully.'


def test_login_user(test_client, init_database):
    response = test_client.post('/auth/login', json={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 200
    assert 'access_token' in response.get_json()


def test_protected_route(test_client, init_database):
    token = get_auth_token(test_client)
    response = test_client.get('/protected', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert response.get_json() == {'logged_in_as': 'testuser'}
