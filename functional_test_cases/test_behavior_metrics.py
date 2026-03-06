import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.analytics.controllers.behavior_metric_controller import behavior_metric_bp
import json

@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(behavior_metric_bp)
    return app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()

# Test cases for GET /behavior_metrics/user/<user_id>

def test_get_metrics_by_user_id_success(client: FlaskClient):
    response = client.get('/behavior_metrics/user/1')
    assert response.status_code == 200
    assert 'average_session_duration' in response.json
    assert 'total_page_views' in response.json
    assert 'average_click_through_rate' in response.json
    assert 'metrics' in response.json

@pytest.mark.parametrize("user_id", [999, 'string_value'])
def test_get_metrics_by_user_id_failure(client: FlaskClient, user_id):
    response = client.get(f'/behavior_metrics/user/{user_id}')
    assert response.status_code == 500
    assert 'error' in response.json

# Test cases for POST /behavior_metrics/create

def test_create_metric_success(client: FlaskClient):
    data = {
        "user_id": 1,
        "session_duration": 120.5,
        "page_views": 10,
        "click_through_rate": 0.5
    }
    response = client.post('/behavior_metrics/create', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    response_json = response.json
    assert 'id' in response_json
    assert response_json['user_id'] == data['user_id']
    assert response_json['session_duration'] == data['session_duration']
    assert response_json['page_views'] == data['page_views']
    assert response_json['click_through_rate'] == data['click_through_rate']
    assert 'created_at' in response_json
    assert 'updated_at' in response_json

@pytest.mark.parametrize("data", [
    {},
    {"user_id": 1},
    {"user_id": 1, "session_duration": "string_value"},
])
def test_create_metric_failure(client: FlaskClient, data):
    response = client.post('/behavior_metrics/create', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert 'error' in response.json

def test_create_metric_server_error(client: FlaskClient):
    data = {
        "user_id": 1,
        "session_duration": 120.5,
        "page_views": 10,
        "click_through_rate": 0.5
    }
    response = client.post('/behavior_metrics/create', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 500
    assert 'error' in response.json
