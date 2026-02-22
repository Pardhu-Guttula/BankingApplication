import pytest
from flask import Flask
from flask.testing import FlaskClient

from backend.authentication.controllers.auth_controller import auth_controller

@pytest.fixture()
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(auth_controller)
    return app

@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()

def test_successful_login(client: FlaskClient):
    response = client.post('/login', json={
        "username": "valid_user",
        "password": "valid_password"
    })
    assert response.status_code == 200
    assert response.json == {"message": "Login successful"}


def test_invalid_login(client: FlaskClient):
    response = client.post('/login', json={
        "username": "invalid_user",
        "password": "invalid_password"
    })
    assert response.status_code == 401
    assert response.json == {"message": "Invalid credentials"}


def test_login_missing_fields(client: FlaskClient):
    response = client.post('/login', json={})
    assert response.status_code == 500
    assert response.json == {"message": "Login failed"}
