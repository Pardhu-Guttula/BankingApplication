import pytest
from flask import Flask
from backend.analytics.controllers.behavior_metric_controller import behavior_metric_bp

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(behavior_metric_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()


def test_get_metrics_by_user_id_success(client, mocker):
    mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.get_metrics_by_user_id', return_value={
        "average_session_duration": 120.5,
        "total_page_views": 25,
        "average_click_through_rate": 0.05,
        "metrics": []
    })

    response = client.get('/behavior_metrics/user/1')
    assert response.status_code == 200
    assert response.json == {
        "average_session_duration": 120.5,
        "total_page_views": 25,
        "average_click_through_rate": 0.05,
        "metrics": []
    }


def test_get_metrics_by_user_id_error(client, mocker):
    mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.get_metrics_by_user_id', side_effect=Exception('DB Error'))

    response = client.get('/behavior_metrics/user/1')
    assert response.status_code == 500
    assert response.json == {"error": "Unable to process your request"}


def test_create_metric_success(client, mocker):
    mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.create_metric', return_value={
        "success": True,
        "metric": {
            "id": 1,
            "user_id": 1,
            "session_duration": 120.5,
            "page_views": 25,
            "click_through_rate": 0.05,
            "created_at": "2023-10-01T00:00:00",
            "updated_at": "2023-10-01T00:00:00"
        }
    })

    response = client.post('/behavior_metrics/create', json={
        "user_id": 1,
        "session_duration": 120.5,
        "page_views": 25,
        "click_through_rate": 0.05
    })
    assert response.status_code == 201
    assert response.json == {
        "id": 1,
        "user_id": 1,
        "session_duration": 120.5,
        "page_views": 25,
        "click_through_rate": 0.05,
        "created_at": "2023-10-01T00:00:00",
        "updated_at": "2023-10-01T00:00:00"
    }


def test_create_metric_failure(client, mocker):
    mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.create_metric', return_value={"success": False})

    response = client.post('/behavior_metrics/create', json={
        "user_id": 1,
        "session_duration": 120.5,
        "page_views": 25,
        "click_through_rate": 0.05
    })
    assert response.status_code == 400
    assert response.json == {"error": "Metric creation failed"}


def test_create_metric_error(client, mocker):
    mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.create_metric', side_effect=Exception('DB Error'))

    response = client.post('/behavior_metrics/create', json={
        "user_id": 1,
        "session_duration": 120.5,
        "page_views": 25,
        "click_through_rate": 0.05
    })
    assert response.status_code == 500
    assert response.json == {"error": "Unable to process your request"}
