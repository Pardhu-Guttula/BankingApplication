import pytest
from flask import Flask
from backend.account_requests.controllers.service_modification_controller import modify_service

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(service_modification_controller)
    return app

@pytest.fixture

def client(app):
    return app.test_client()

def test_modify_service_success(client, monkeypatch):
    test_data = {'user_id': '1', 'service_id': '1', 'modification_type': 'upgrade'}

    class MockServiceModificationRequest:
        def __init__(self):
            self.id = '123'
            self.status = 'submitted'

def mock_create_modification_request(user_id, service_id, modification_type):
        return MockServiceModificationRequest()

    monkeypatch.setattr('backend.account_requests.services.service_modification_service.ServiceModificationService.create_modification_request', mock_create_modification_request)
    response = client.post('/service/modify', json=test_data)
    assert response.status_code == 200
    assert response.json == {
        'message': 'Service modification request submitted successfully',
        'request_id': '123',
        'status': 'submitted'
    }

def test_modify_service_missing_field(client):
    test_data = {'user_id': '1', 'service_id': '1'}  # Missing modification_type
    response = client.post('/service/modify', json=test_data)
    assert response.status_code == 400
    assert response.json == {'error': 'User ID, service ID and modification type are required'}

def test_modify_service_empty_body(client):
    response = client.post('/service/modify', json={})  # Empty body
    assert response.status_code == 400
    assert response.json == {'error': 'User ID, service ID and modification type are required'}

def test_modify_service_invalid_json(client):
    response = client.post('/service/modify', data='Invalid JSON', content_type='application/json')  # Invalid JSON
    assert response.status_code == 400
    assert response.json == {'error': 'User ID, service ID and modification type are required'}