import pytest
import requests

BASE_URL = "http://localhost:5000/behavior_metrics"

@pytest.fixture
def get_user_id():
    return 1

@pytest.fixture
def metric_payload():
    return {
        "user_id": 1,
        "session_duration": 120.5,
        "page_views": 15,
        "click_through_rate": 0.35
    }


def test_get_metrics_by_user_id_success(get_user_id):
    response = requests.get(f"{BASE_URL}/user/{get_user_id}")
    assert response.status_code == 200
    assert "average_session_duration" in response.json()
    assert "total_page_views" in response.json()
    assert "average_click_through_rate" in response.json()


def test_get_metrics_by_user_id_failure_invalid_user_id():
    response = requests.get(f"{BASE_URL}/user/99999")
    assert response.status_code == 200  # status code inferred 
    assert response.json() == []


def test_create_metric_success(metric_payload):
    response = requests.post(f"{BASE_URL}/create", json=metric_payload)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["user_id"] == metric_payload["user_id"]


def test_create_metric_failure_missing_fields():
    incomplete_payload = {"user_id": 1, "session_duration": 120.5}
    response = requests.post(f"{BASE_URL}/create", json=incomplete_payload)
    assert response.status_code == 400
    assert "error" in response.json()


def test_create_metric_failure_invalid_data():
    invalid_payload = {"user_id": "abc", "session_duration": -120.5, "page_views": "NaN", "click_through_rate": "none"}
    response = requests.post(f"{BASE_URL}/create", json=invalid_payload)
    assert response.status_code == 500
    assert "error" in response.json()


def test_create_metric_failure_server_error():
    payload_causing_error = {"user_id": 1, "session_duration": 120.5, "page_views": 15, "click_through_rate": 0.35}
    # Simulate server error by adding unrealistic high values (assuming validation in service layer)
    payload_causing_error["page_views"] = 10**6
    response = requests.post(f"{BASE_URL}/create", json=payload_causing_error)
    assert response.status_code == 500
    assert "error" in response.json()