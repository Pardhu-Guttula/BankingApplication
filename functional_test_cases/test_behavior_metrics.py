import pytest
import json
from flask import Flask
from backend.analytics.controllers.behavior_metric_controller import behavior_metric_bp

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(behavior_metric_bp)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test for getting metrics by user id

def test_get_metrics_by_user_id_success(client, mocker):
    mocker.patch('backend.database.config.get_db', return_value=(mocker.Mock(),))
    mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.get_metrics_by_user_id', return_value={
        "average_session_duration": 120.0,
        "total_page_views": 50,
        "average_click_through_rate": 0.5,
        "metrics": []
    })
    response = client.get('/behavior_metrics/user/1')
    assert response.status_code == 200
    assert response.json == {
        "average_session_duration": 120.0,
        "total_page_views": 50,
        "average_click_through_rate": 0.5,
        "metrics": []
    }

def test_get_metrics_by_user_id_failure(client, mocker):
    mocker.patch('backend.database.config.get_db', return_value=(mocker.Mock(),))
    mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.get_metrics_by_user_id', side_effect=Exception("Unable to process your request"))
    response = client.get('/behavior_metrics/user/1')
    assert response.status_code == 500
    assert response.json == {"error": "Unable to process your request"}

# Test for creating a metric

def test_create_metric_success(client, mocker):
    mocker.patch('backend.database.config.get_db', return_value=(mocker.Mock(),))
    mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.create_metric', return_value={
        "success": True,
        "metric": mocker.Mock(id=1, user_id=1, session_duration=120.0, page_views=50, click_through_rate=0.5, created_at="2023-10-10T00:00:00", updated_at="2023-10-10T00:00:00")
    })
    payload = {
        "user_id": 1,
        "session_duration": 120.0,
        "page_views": 50,
        "click_through_rate": 0.5
    }
    response = client.post('/behavior_metrics/create', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 201
    assert response.json == {
        "id": 1,
        "user_id": 1,
        "session_duration": 120.0,
        "page_views": 50,
        "click_through_rate": 0.5,
        "created_at": "2023-10-10T00:00:00",
        "updated_at": "2023-10-10T00:00:00"
    }

def test_create_metric_failure(client, mocker):
    mocker.patch('backend.database.config.get_db', return_value=(mocker.Mock(),))
    mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.create_metric', return_value={"success": False})
    payload = {
        "user_id": 1,
        "session_duration": 120.0,
        "page_views": 50,
        "click_through_rate": 0.5
    }
    response = client.post('/behavior_metrics/create', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 400
    assert response.json == {"error": "Metric creation failed"}

def test_create_metric_exception(client, mocker):
    mocker.patch('backend.database.config.get_db', return_value=(mocker.Mock(),))
    mocker.patch('backend.analytics.services.behavior_metric_service.BehaviorMetricService.create_metric', side_effect=Exception("Unable to process your request"))
    payload = {
        "user_id": 1,
        "session_duration": 120.0,
        "page_views": 50,
        "click_through_rate": 0.5
    }
    response = client.post('/behavior_metrics/create', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 500
    assert response.json == {"error": "Unable to process your request"}
