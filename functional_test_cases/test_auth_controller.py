import pytest
from flask import Flask, jsonify
from flask.testing import FlaskClient
from backend.authentication.controllers.auth_controller import auth_controller

@pytest.fixture
 def client() -> FlaskClient:
     app = Flask(__name__)
     app.register_blueprint(auth_controller)
     app.config['TESTING'] = True
     with app.test_client() as client:
         yield client

 def test_login_success(client: FlaskClient):
     data = {'username': 'john@example.com', 'password': 'securepassword'}
     response = client.post('/login', json=data)
     assert response.status_code == 200
     assert response.get_json() == {'message': 'Login successful'}

 def test_login_failure_invalid_credentials(client: FlaskClient):
     data = {'username': 'john@example.com', 'password': 'wrongpassword'}
     response = client.post('/login', json=data)
     assert response.status_code == 401
     assert response.get_json() == {'message': 'Invalid credentials'}

 def test_register_success(client: FlaskClient):
     data = {'name': 'Jane Doe', 'email': 'jane@example.com', 'password': 'securepassword'}
     response = client.post('/register', json=data)
     assert response.status_code == 201
     assert response.get_json() == {'message': 'Registration successful. Please check your email for confirmation.'}

 def test_register_failure_existing_email(client: FlaskClient):
     data = {'name': 'John Doe', 'email': 'john@example.com', 'password': 'securepassword'}
     response = client.post('/register', json=data)
     assert response.status_code == 400
     assert response.get_json() == {'message': 'Registration failed, email may already be in use.'}

 def test_logout_success(client: FlaskClient):
     response = client.post('/logout')
     assert response.status_code == 200
     assert response.get_json() == {'message': 'Logout successful'}