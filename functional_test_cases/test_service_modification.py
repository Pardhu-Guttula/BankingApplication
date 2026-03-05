import pytest
import json
from flask import Flask
from backend.account_requests.controllers.service_modification_controller import service_modification_controller

@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(service_modification_controller)
    app.testing = True
    client = app.test_client()
    yield client


def test_modify_service_success(client):
    payload = {
        'user_id': '123',
        'service_id': '456',
        'modification_type': 'upgrade'
    }
    response = client.post('/service/modify', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['message'] == 'Service modification request submitted successfully'
    assert 'request_id' in response_data
    assert 'status' in response_data


def test_modify_service_missing_fields(client):
    payload = {
        'user_id': '123',
        'service_id': '456'
    }
    response = client.post('/service/modify', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 400
    response_data = json.loads(response.data)
    assert response_data['error'] == 'User ID, service ID and modification type are required'


def test_modify_service_empty_fields(client):
    payload = {
        'user_id': '',
        'service_id': '',
        'modification_type': ''
    }
    response = client.post('/service/modify', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 400
    response_data = json.loads(response.data)
    assert response_data['error'] == 'User ID, service ID and modification type are required'


def test_modify_service_invalid_fields(client):
    payload = {
        'user_id': 123,
        'service_id': 456,
        'modification_type': True
    }
    response = client.post('/service/modify', data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 400
    response_data = json.loads(response.data)
    assert response_data['error'] == 'User ID, service ID and modification type are required'
