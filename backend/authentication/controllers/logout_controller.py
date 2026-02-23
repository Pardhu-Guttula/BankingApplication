# Epic Title: Develop User Logout Capability

from flask import Blueprint, request, jsonify
from backend.database.config import get_db
from backend.authentication.repositories.session_repository import SessionRepository

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/logout', methods=['POST'])
def logout_user():
    db = next(get_db())
    session_repository = SessionRepository(db)

    try:
        token = request.headers.get('Authorization').split(" ")[1]
        session_repository.invalidate_session_by_token(token)
        return jsonify({"message": "User logged out successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400