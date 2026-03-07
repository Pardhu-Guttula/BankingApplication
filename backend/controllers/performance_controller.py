# Epic Title: Banking Platform — Core API

from flask import Blueprint, request, jsonify
from backend.services.transaction_service import TransactionService
from backend.services.performance_metrics_service import PerformanceMetricsService
from backend.services.user_request_service import UserRequestService

performance_bp = Blueprint('performance_bp', __name__)

@performance_bp.route('/log_transaction', methods=['POST'])
def log_transaction():
    data = request.json
    service = TransactionService()
    transaction = service.create_transaction(data['transaction_id'], data['user_id'], data['amount'])
    return jsonify({"message": "Transaction logged successfully", "transaction": transaction.__dict__})

@performance_bp.route('/transactions', methods=['GET'])
def get_transactions():
    service = TransactionService()
    transactions = service.get_all_transactions()
    return jsonify([t.__dict__ for t in transactions])

@performance_bp.route('/log_metrics', methods=['POST'])
def log_metrics():
    data = request.json
    service = PerformanceMetricsService()
    metrics = service.log_metrics(data['metrics_id'], data['operation'], data['duration'])
    return jsonify({"message": "Performance metrics logged successfully", "metrics": metrics.__dict__})

@performance_bp.route('/performance_metrics', methods=['GET'])
def get_performance_metrics():
    service = PerformanceMetricsService()
    metrics = service.get_all_metrics()
    return jsonify([m.__dict__ for m in metrics])

@performance_bp.route('/log_user_request', methods=['POST'])
def log_user_request():
    data = request.json
    service = UserRequestService()
    user_request = service.log_user_request(data['request_id'], data['user_id'], data['operation'])
    return jsonify({"message": "User request logged successfully", "user_request": user_request.__dict__})

@performance_bp.route('/user_requests', methods=['GET'])
def get_user_requests():
    service = UserRequestService()
    user_requests = service.get_all_user_requests()
    return jsonify([r.__dict__ for r in user_requests])