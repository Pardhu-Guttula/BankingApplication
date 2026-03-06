import pytest
from flask import Flask
from flask.testing import FlaskClient
from backend.analytics.controllers.behavior_metric_controller import behavior_metric_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(behavior_metric_bp)
    return app

@pytest.fixture
def client(app: Flask):
    return app.test_client()

# Test cases for get_metrics_by_user_id endpoint

def test_get_metrics_by_user_id(client: FlaskClient):
    response = client.get('/behavior_metrics/user/1')
    assert response.status_code == 200  # status code inferred - not explicit in source


def test_get_metrics_by_user_id_not_found(client: FlaskClient):
    response = client.get('/behavior_metrics/user/9999')
    assert response.status_code == 200  # status code inferred - not explicit in source

# Test cases for create_metric endpoint

def test_create_metric_success(client: FlaskClient):
    payload = {
        "user_id": 1,
        "session_duration": 120,
        "page_views": 8,
        "click_through_rate": 0.5
    }
    response = client.post('/behavior_metrics/create', json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data['user_id'] == 1
    assert data['session_duration'] == 120
    assert data['page_views'] == 8
    assert data['click_through_rate'] == 0.5


def test_create_metric_validation_error(client: FlaskClient):
    payload = {
        "user_id": None,
        "session_duration": "invalid",
        "page_views": "invalid",
        "click_through_rate": "invalid"
    }
    response = client.post('/behavior_metrics/create', json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == "Metric creation failed"


def test_create_metric_internal_error(client: FlaskClient, mocker):
    payload = {
        "user_id": 1,
        "session_duration": 120,
        "page_views": 8,
        "click_through_rate": 0.5
    }
    mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.create_metric', side_effect=Exception("DB Error"))
    response = client.post('/behavior_metrics/create', json=payload)
    assert response.status_code == 500
    data = response.get_json()
    assert data['error'] == "Unable to process your request"