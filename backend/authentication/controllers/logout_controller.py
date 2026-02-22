# Epic Title: Implement user authentication and authorization features

from flask import Flask, request, jsonify, redirect, url_for
from backend.authentication.services.logout_service import LogoutService

app = Flask(__name__)
active_sessions = []  # This should be managed better in a real-world scenario
logout_service = LogoutService(active_sessions)

@app.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get("Authorization")
    if token and logout_service.logout(token):
        return redirect(url_for('login'))
    return jsonify({"error": "Invalid token"}), 401