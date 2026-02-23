# Epic Title: Integrate Payment Gateway (Stripe) for Processing Payments

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from backend.database.config import get_db
from backend.payment.repositories.transaction_repository import TransactionRepository
from backend.payment.services.payment_service import PaymentService

payment_bp = Blueprint('payment', __name__)

STRIPE_API_KEY = "your_stripe_api_key"  # Replace with your actual Stripe API key

@payment_bp.route('/payment/process', methods=['POST'])
def process_payment():
    db = next(get_db())
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')
    currency = data.get('currency', 'usd')

    transaction_repository = TransactionRepository(db)
    payment_service = PaymentService(transaction_repository, STRIPE_API_KEY)

    try:
        response = payment_service.process_payment(db, user_id, amount, currency)
        if "error" in response:
            return jsonify(response), 400
        return jsonify(response)
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400

@payment_bp.route('/payment/confirm', methods=['POST'])
def confirm_payment():
    db = next(get_db())
    data = request.get_json()
    transaction_id = data.get('transaction_id')

    transaction_repository = TransactionRepository(db)
    payment_service = PaymentService(transaction_repository, STRIPE_API_KEY)

    try:
        response = payment_service.confirm_payment(db, transaction_id)
        if "error" in response:
            return jsonify(response), 400
        return jsonify(response)
    except SQLAlchemyError as e:
        return jsonify({"error": "Unable to process your request"}), 500
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400