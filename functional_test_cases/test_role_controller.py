import pytest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from backend.access_control.controllers.role_controller import app

@pytest.fixture
 def client() -> FlaskClient:
     app.config['TESTING'] = True
     with app.test_client() as client:
         yield client

 def test_assign_role_success(client: FlaskClient):
     data = {'email': 'john@example.com', 'role': 'admin'}
     response = client.post('/assign-role', json=data)
     assert response.status_code == 200
     assert response.get_json() == {'message': 'Role assigned successfully'}

 def test_assign_role_failure(client: FlaskClient):
     data = {'email': 'jane@example.com', 'role': 'admin'}
     response = client.post('/assign-role', json=data)
     assert response.status_code == 400
     assert response.get_json() == {'error': 'Failed to assign role'}

 def test_get_permissions_success(client: FlaskClient):
     response = client.get('/permissions?email=john@example.com')
     assert response.status_code == 200
     assert response.get_json() == {'permissions': ['manage_users', 'view_reports', 'edit_content']}

 def test_get_permissions_failure(client: FlaskClient):
     response = client.get('/permissions?email=jane@example.com')
     assert response.status_code == 200
     assert response.get_json() == {'permissions': []}