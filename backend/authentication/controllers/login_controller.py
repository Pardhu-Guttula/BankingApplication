# Epic Title: Implement user authentication and authorization features

from flask import Flask, request, jsonify
from backend.authentication.services.authentication_service import AuthenticationService
from backend.authentication.repositories.user_repository import UserRepository

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

# Helper functions

def validate_email(email):
    import re
    email_regex = r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    return re.match(email_regex, email)

def validate_password(password):
    import re
    password_regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return re.match(password_regex, password)

def send_confirmation_email(user):
    # Simulate sending a confirmation email
    print(f'Sending confirmation email to {user.email}')