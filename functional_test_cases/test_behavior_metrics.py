import pytest
import json
from flask import Flask
from backend.analytics.controllers.behavior_metric_controller import behavior_metric_bp
from flask.testing import FlaskClient

@pytest.fixture
def app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(behavior_metric_bp)
    return app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_get_metrics_by_user_id_success(client: FlaskClient, mocker):
    user_id = 1
    expected_response = {
        "average_session_duration": 30,
        "total_page_views": 15,
        "average_click_through_rate": 0.5,
        "metrics": [
            {
                "session_duration": 30,
                "page_views": 15,
                "click_through_rate": 0.5
            }
        ]
    }

    mock_service = mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.get_metrics_by_user_id', return_value=expected_response)

    response = client.get(f'/behavior_metrics/user/{user_id}')
    assert response.status_code == 200
    assert response.json == expected_response


def test_get_metrics_by_user_id_failure(client: FlaskClient, mocker):
    user_id = 1
    expected_response = {"error": "Unable to process your request"}

    mock_service = mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.get_metrics_by_user_id', side_effect=Exception)

    response = client.get(f'/behavior_metrics/user/{user_id}')
    assert response.status_code == 500
    assert response.json == expected_response


def test_create_metric_success(client: FlaskClient, mocker):
    metric_data = {
        "user_id": 1,
        "session_duration": 30,
        "page_views": 15,
        "click_through_rate": 0.5
    }

    expected_response = {
        "id": 1,
        "user_id": 1,
        "session_duration": 30,
        "page_views": 15,
        "click_through_rate": 0.5,
        "created_at": "2023-10-01T00:00:00",
        "updated_at": "2023-10-01T00:00:00"
    }

    mock_service = mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.create_metric', return_value={"success": True, "metric": metric_data})

    response = client.post('/behavior_metrics/create', data=json.dumps(metric_data), content_type='application/json')
    assert response.status_code == 201
    assert response.json == expected_response


def test_create_metric_failure(client: FlaskClient, mocker):
    metric_data = {
        "user_id": 1,
        "session_duration": 30,
        "page_views": 15,
        "click_through_rate": 0.5
    }

    expected_response = {"error": "Metric creation failed"}

    mock_service = mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.create_metric', return_value={"success": False})

    response = client.post('/behavior_metrics/create', data=json.dumps(metric_data), content_type='application/json')
    assert response.status_code == 400
    assert response.json == expected_response


def test_create_metric_exception(client: FlaskClient, mocker):
    metric_data = {
        "user_id": 1,
        "session_duration": 30,
        "page_views": 15,
        "click_through_rate": 0.5
    }

    expected_response = {"error": "Unable to process your request"}

    mock_service = mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.create_metric', side_effect=Exception)

    response = client.post('/behavior_metrics/create', data=json.dumps(metric_data), content_type='application/json')
    assert response.status_code == 500
    assert response.json == expected_response
