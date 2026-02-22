import pytest
from flask import jsonify
from backend.authentication.controllers.auth_controller import auth_controller



class TestAuthController:
    @pytest.fixture
    def client(self, app):
        return app.test_client()

    @pytest.fixture
    def app(self):
        from backend.app import create_app
        app = create_app()
        app.testing = True
        return app

    def test_login_success(self, client, mocker):
        mocker.patch('backend.authentication.services.auth_service.AuthService.authenticate', return_value=True)
        response = client.post('/login', json={'username': 'valid_user', 'password': 'valid_password'})
        assert response.status_code == 200
        assert response.json == {"message": "Login successful"}

    def test_login_invalid_credentials(self, client, mocker):
        mocker.patch('backend.authentication.services.auth_service.AuthService.authenticate', return_value=False)
        response = client.post('/login', json={'username': 'invalid_user', 'password': 'invalid_password'})
        assert response.status_code == 401
        assert response.json == {"message": "Invalid credentials"}

    def test_login_failure(self, client, mocker):
        mocker.patch('backend.authentication.services.auth_service.AuthService.authenticate', side_effect=Exception('Unexpected error'))
        response = client.post('/login', json={'username': 'test', 'password': 'test'})
        assert response.status_code == 500
        assert response.json == {"message": "Login failed"}
    
