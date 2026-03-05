import pytest
from flask import jsonify
from backend.account_requests.controllers.service_modification_controller import service_modification_controller

@pytest.fixture
def client():
    from app import app
    app.register_blueprint(service_modification_controller)
    with app.test_client() as client:
        yield client

def test_modify_service_success(client):
    response = client.post('/service/modify', json={
        'user_id': 'test_user',
        'service_id': 'test_service',
        'modification_type': 'upgrade'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Service modification request submitted successfully'
    assert 'request_id' in data
    assert 'status' in data

def test_modify_service_failure_missing_fields(client):
    response = client.post('/service/modify', json={'user_id': 'test_user'})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'User ID, service ID and modification type are required'

def test_modify_service_failure_empty_payload(client):
    response = client.post('/service/modify', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert data['error'] == 'User ID, service ID and modification type are required'
