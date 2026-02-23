# Epic Title: Integrate Payment Gateway (Stripe) for Processing Payments

import stripe
from sqlalchemy.orm import Session
from backend.payment.repositories.transaction_repository import TransactionRepository

class PaymentService:
    def __init__(self, transaction_repository: TransactionRepository, stripe_api_key: str):
        self.transaction_repository = transaction_repository
        stripe.api_key = stripe_api_key

    def process_payment(self, db: Session, user_id: int, amount: float, currency: str = "usd"):
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),
                currency=currency,
                payment_method_types=["card"],
            )
            transaction = self.transaction_repository.create_transaction(
                user_id=user_id,
                transaction_id=payment_intent['id'],
                amount=amount,
                status='pending',
            )
            return {"transaction_id": transaction.transaction_id, "client_secret": payment_intent['client_secret']}
        except stripe.error.StripeError as e:
            return {"error": str(e)}

    def confirm_payment(self, db: Session, transaction_id: str):
        try:
            payment_intent = stripe.PaymentIntent.retrieve(transaction_id)
            if payment_intent['status'] == 'succeeded':
                transaction = self.transaction_repository.get_transaction_by_id(transaction_id)
                transaction.status = 'succeeded'
                db.commit()
                return {"message": "Payment successful"}
            else:
                return {"error": "Payment not successful"}
        except stripe.error.StripeError as e:
            return {"error": str(e)}