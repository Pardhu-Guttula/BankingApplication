import pytest
from flask import url_for
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

class TestUserAuthenticationAndSecurity:

    def test_users_login_success(self, client):
        response = client.post(url_for('auth_controller.login'), json={
            'username': 'valid_user',
            'password': 'valid_password'
        })
        assert response.status_code == 200
        assert response.json['message'] == 'Login successful'

    def test_users_login_invalid_credentials(self, client):
        response = client.post(url_for('auth_controller.login'), json={
            'username': 'invalid_user',
            'password': 'invalid_password'
        })
        assert response.status_code == 401
        assert response.json['message'] == 'Invalid credentials'

    def test_users_login_fail_exception(self, client):
        response = client.post(url_for('auth_controller.login'), json={
            'username': 'error_user',
            'password': 'error_password'
        })
        assert response.status_code == 500
        assert response.json['message'] == 'Login failed'
