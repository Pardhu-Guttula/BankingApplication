import pytest


def test_user_login():
    # Setup
    username = 'test_user'
    password = 'secure_password'

    # Exercise
    response = login(username, password)

    # Verify
    assert response.status_code == 200
    assert response.json()['username'] == username


def login(username, password):
    # This function simulates a login attempt. Replace it with actual implementation.
    class Response:
        def __init__(self):
            self.status_code = 200

        def json(self):
            return {'username': username}

    return Response()