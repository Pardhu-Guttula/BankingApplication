# Epic Title: Banking Platform — Core API

from flask import Flask, jsonify, request
from backend.repositories.user_repository import UserRepository
from backend.repositories.account_repository import AccountRepository
from backend.repositories.service_request_repository import ServiceRequestRepository
from backend.repositories.interaction_history_repository import InteractionHistoryRepository

app = Flask(__name__)

user_repository = UserRepository()
account_repository = AccountRepository()
service_request_repository = ServiceRequestRepository()
interaction_history_repository = InteractionHistoryRepository()

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_repository.get_user_by_id(user_id)
    if user:
        return jsonify({
            "user_id": user.user_id,
            "username": user.username,
            "role": user.role
        })
    return jsonify({"error": "User not found"}), 404

@app.route('/account/<int:user_id>', methods=['GET'])
def get_account(user_id):
    account = account_repository.get_account_by_user_id(user_id)
    if account:
        return jsonify({
            "account_id": account.account_id,
            "user_id": account.user_id,
            "balance": account.balance
        })
    return jsonify({"error": "Account not found"}), 404

@app.route('/service-requests/<int:user_id>', methods=['GET'])
def get_service_requests(user_id):
    requests = service_request_repository.get_service_requests_by_user_id(user_id)
    return jsonify([{
        "request_id": request.request_id,
        "user_id": request.user_id,
        "description": request.description,
        "status": request.status
    } for request in requests])

@app.route('/interaction-history/<int:user_id>', methods=['GET'])
def get_interaction_history(user_id):
    interactions = interaction_history_repository.get_interactions_by_user_id(user_id)
    return jsonify([{
        "interaction_id": interaction.interaction_id,
        "user_id": interaction.user_id,
        "details": interaction.details
    } for interaction in interactions])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)