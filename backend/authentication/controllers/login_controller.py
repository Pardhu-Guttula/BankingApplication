# Epic Title: Implement user authentication and authorization features

from flask import Flask, request, jsonify
from backend.authentication.services.authentication_service import AuthenticationService
from backend.authentication.repositories.user_repository import UserRepository

app = Flask(__name__)
user_repository = UserRepository()
auth_service = AuthenticationService(user_repository)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    session = auth_service.login(email, password)
    if session:
        return jsonify({"token": session.token}), 200
    return jsonify({"error": "Invalid credentials"}), 401