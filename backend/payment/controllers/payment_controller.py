# Epic Title: Integrate payment gateway (Stripe) for processing payments

from flask import Blueprint, jsonify, request
import stripe
from backend.payment.repositories.transaction_repository import TransactionRepository
from backend.payment.models.transaction import Transaction
import datetime

payment_bp = Blueprint('payment', __name__)
stripe.api_key = 'your_stripe_api_key_here'
transaction_repository = TransactionRepository(db_config={'host': 'localhost', 'user': 'root', 'password': '', 'database': 'ecommerce'})

@payment_bp.route('/checkout', methods=['POST'])
def process_payment():
    try:
        amount = request.json.get('amount')
        currency = request.json.get('currency', 'usd')
        source = request.json.get('source')
        
        if not amount or not source:
            return jsonify({'error': 'Invalid payment details'}), 400
        
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # Stripe expects amount in cents
            currency=currency,
            source=source,
            description='E-commerce payment'
        )
        
        transaction = Transaction(
            id=charge.id,
            amount=amount,
            currency=currency,
            status=charge.status,
            created_at=datetime.datetime.now()
        )
        transaction_repository.save_transaction(transaction)
        
        return jsonify({'transaction_id': transaction.id, 'status': transaction.status}), 200
    except stripe.error.CardError as e:
        return jsonify({'error': str(e)}), 400