import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.analytics.controllers.user_behavior_controller import behavior_bp
import json

@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(behavior_bp)
    return app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()

# Test cases for GET /user/session-duration

def test_get_session_duration_success(client: FlaskClient):
    response = client.get('/user/session-duration')
    assert response.status_code == 200
    assert 'average_session_duration' in response.json

# Test cases for GET /user/page-views

def test_get_page_views_success(client: FlaskClient):
    response = client.get('/user/page-views')
    assert response.status_code == 200
    assert 'total_page_views' in response.json

# Test cases for GET /user/click-through-rates

def test_get_click_rates_success(client: FlaskClient):
    response = client.get('/user/click-through-rates')
    assert response.status_code == 200
    assert 'click_through_rates' in response.json
