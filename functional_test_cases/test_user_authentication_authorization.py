import pytest
from flask import Flask
from flask_testing import TestCase
from backend.authentication.controllers.auth_controller import auth_controller
from backend.access_control.controllers.role_controller import assign_role, get_permissions
from backend.database.schemas.users import users
from backend.database.schemas.roles import roles
from backend.database.schemas.sessions import sessions

class TestUserAuthenticationAuthorization(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.register_blueprint(auth_controller, url_prefix='/auth')
        app.add_url_rule('/assign-role', view_func=assign_role, methods=['POST'])
        app.add_url_rule('/permissions', view_func=get_permissions, methods=['GET'])
        return app

    def test_successful_registration(self):
        response = self.client.post('/auth/register', json={
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'Password123!'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.json)
        self.assertEqual(response.json['message'], 'Registration successful. Please check your email for confirmation.')

    def test_registration_with_existing_email(self):
        self.client.post('/auth/register', json={
            'name': 'Existing User',
            'email': 'existing@example.com',
            'password': 'Password123!'
        })
        response = self.client.post('/auth/register', json={
            'name': 'New User',
            'email': 'existing@example.com',
            'password': 'Password123!'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('message', response.json)
        self.assertEqual(response.json['message'], 'Registration failed, email may already be in use.')

    def test_registration_with_invalid_data(self):
        response = self.client.post('/auth/register', json={
            'name': '',
            'email': 'invalid-email',
            'password': 'short'
        })
        self.assertEqual(response.status_code, 500)
        self.assertIn('message', response.json)
        self.assertEqual(response.json['message'], 'Registration failed')

    def test_successful_login(self):
        self.client.post('/auth/register', json={
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'Password123!'
        })
        response = self.client.post('/auth/login', json={
            'username': 'test@example.com',
            'password': 'Password123!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json)
        self.assertEqual(response.json['message'], 'Login successful')

    def test_login_with_invalid_credentials(self):
        response = self.client.post('/auth/login', json={
            'username': 'nonexistent@example.com',
            'password': 'WrongPassword123!'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn('message', response.json)
        self.assertEqual(response.json['message'], 'Invalid credentials')

    def test_account_lockout(self):
        for _ in range(5):
            response = self.client.post('/login', json={
                'user_id': 1,
                'password': 'WrongPassword123!'
            })
            self.assertEqual(response.status_code, 400)
        response = self.client.post('/login', json={
            'user_id': 1,
            'password': 'WrongPassword123!'
        })
        self.assertEqual(response.status_code, 423)

    def test_successful_logout(self):
        self.client.post('/auth/register', json={
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'Password123!'
        })
        self.client.post('/auth/login', json={
            'username': 'test@example.com',
            'password': 'Password123!'
        })
        response = self.client.post('/auth/logout')
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json)
        self.assertEqual(response.json['message'], 'Logout successful')

    def test_session_invalidation_on_logout(self):
        self.client.post('/auth/register', json={
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'Password123!'
        })
        self.client.post('/auth/login', json={
            'username': 'test@example.com',
            'password': 'Password123!'
        })
        self.client.post('/auth/logout')
        response = self.client.post('/auth/logout')
        self.assertEqual(response.status_code, 500)
        self.assertIn('message', response.json)
        self.assertEqual(response.json['message'], 'Logout failed')

    def test_assign_role_to_user(self):
        self.client.post('/auth/register', json={
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'Password123!'
        })
        response = self.client.post('/assign-role', json={
            'email': 'test@example.com',
            'role': 'admin'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json)
        self.assertEqual(response.json['message'], 'Role assigned successfully')

    def test_access_control_based_on_role(self):
        self.client.post('/auth/register', json={
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'Password123!'
        })
        self.client.post('/assign-role', json={
            'email': 'test@example.com',
            'role': 'admin'
        })
        response = self.client.get('/permissions', query_string={
            'email': 'test@example.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('permissions', response.json)
        self.assertEqual(response.json['permissions'], ['manage_users', 'view_reports', 'edit_content'])

    def test_change_user_role(self):
        self.client.post('/auth/register', json={
            'name': 'Test User',
            'email': 'test@example.com',
            'password': 'Password123!'
        })
        self.client.post('/assign-role', json={
            'email': 'test@example.com',
            'role': 'user'
        })
        response = self.client.post('/assign-role', json={
            'email': 'test@example.com',
            'role': 'admin'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json)
        self.assertEqual(response.json['message'], 'Role assigned successfully')

if __name__ == '__main__':
    pytest.main()