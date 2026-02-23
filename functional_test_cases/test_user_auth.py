import pytest
from flask import Flask
from backend.authentication.services.authentication_service import AuthenticationService
from backend.authentication.repositories.user_repository import UserRepository


def create_app():
    app = Flask(__name__)
    user_repository = UserRepository()
    auth_service = AuthenticationService(user_repository)

    @app.route('/register', methods=['POST'])
    def register():
        data = request.json
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        if not name or not email or not password:
            return jsonify({'error': 'All fields are required'}), 400
        if not validate_email(email):
            return jsonify({'error': 'Invalid email format'}), 400
        if not validate_password(password):
            return jsonify({'error': 'Password does not meet security criteria'}), 400
        if user_repository.find_by_email(email):
            return jsonify({'error': 'Email already registered'}), 409
        user = auth_service.register(name, email, password)
        send_confirmation_email(user)
        return jsonify({'message': 'User registered successfully'}), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        email = data.get('email')
        password = data.get('password')
        if auth_service.is_account_locked(email):
            return jsonify({'error': 'Account is locked due to multiple invalid login attempts'}), 403
        session = auth_service.login(email, password)
        if session:
            return jsonify({'token': session.token}), 200
        auth_service.record_invalid_attempt(email)
        return jsonify({'error': 'Invalid credentials'}), 401

    @app.route('/logout', methods=['POST'])
    def logout():
        token = request.headers.get('Authorization').split(' ')[1]
        if auth_service.logout(token):
            return jsonify({'message': 'Logged out successfully'}), 200
        return jsonify({'error': 'Invalid token'}), 401

    @app.route('/assign-role', methods=['POST'])
    def assign_role():
        data = request.json
        user_id = data.get('user_id')
        role = data.get('role')
        if not auth_service.is_admin(request.headers.get('Authorization').split(' ')[1]):
            return jsonify({'error': 'Admin privileges required'}), 403
        if auth_service.assign_role(user_id, role):
            return jsonify({'message': 'Role assigned successfully'}), 200
        return jsonify({'error': 'Unable to assign role'}), 400

    return app

@pytest.fixture
    def app():
    app = create_app()
    app.config.update({
        'TESTING': True,
    })
    yield app

@pytest.fixture
    def client(app):
    return app.test_client() 

@pytest.fixture
    def runner(app):
    return app.test_cli_runner()

# Tests for registration

def test_successful_registration(client):
    response = client.post('/register', json={
        'name': 'Jane Doe',
        'email': 'jane@example.com',
        'password': 'StrongPass123'
    })
    assert response.status_code == 201
    assert response.json == {'message': 'User registered successfully'}

# Add more tests for invalid email, existing email, invalid password

def test_registration_with_existing_email(client):
    response = client.post('/register', json={
        'name': 'Jane Doe',
        'email': 'john@example.com',
        'password': 'AnotherStrongPass123'
    })
    assert response.status_code == 409
    assert response.json == {'error': 'Email already registered'}


def test_registration_with_invalid_data(client):
    response = client.post('/register', json={
        'name': '',
        'email': 'invalid-email',
        'password': 'weak'
    })
    assert response.status_code == 400
    # Check for all relevant error messages in response.json

# Tests for login

def test_successful_login(client):
    response = client.post('/login', json={
        'email': 'john@example.com',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'token' in response.json


def test_login_with_invalid_credentials(client):
    response = client.post('/login', json={
        'email': 'john@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert response.json == {'error': 'Invalid credentials'}


def test_login_account_locked(client):
    # First, trigger account lock by multiple invalid attempts
    for _ in range(5):
        client.post('/login', json={
            'email': 'john@example.com',
            'password': 'wrongpassword'
        })
    response = client.post('/login', json={
        'email': 'john@example.com',
        'password': 'password123'
    })
    assert response.status_code == 403
    assert response.json == {'error': 'Account is locked due to multiple invalid login attempts'}

# Tests for logout

def test_successful_logout(client):
    # Assuming the client has a valid token
    client.post('/login', json={
        'email': 'john@example.com',
        'password': 'password123'
    })
    response = client.post('/logout', headers={
        'Authorization': 'Bearer VALID_TOKEN'
    })
    assert response.status_code == 200
    assert response.json == {'message': 'Logged out successfully'}


def test_logout_with_invalid_token(client):
    response = client.post('/logout', headers={
        'Authorization': 'Bearer INVALID_TOKEN'
    })
    assert response.status_code == 401
    assert response.json == {'error': 'Invalid token'}

# Tests for role assignment

def test_assign_role_successfully(client):
    # Assuming the client has a valid admin token
    response = client.post('/assign-role', json={
        'email': 'jane@example.com',
        'role': 'admin'
    }, headers={
        'Authorization': 'Bearer ADMIN_TOKEN'
    })
    assert response.status_code == 200
    assert response.json == {'message': 'Role assigned successfully'}


def test_assign_role_without_admin_privileges(client):
    # Assuming the client does not have admin token
    response = client.post('/assign-role', json={
        'email': 'jane@example.com',
        'role': 'admin'
    }, headers={
        'Authorization': 'Bearer USER_TOKEN'
    })
    assert response.status_code == 403
    assert response.json == {'error': 'Admin privileges required'}
