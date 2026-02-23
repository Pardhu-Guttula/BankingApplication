# Epic Title: Integrate Payment Gateway (Stripe) for Processing Payments

from sqlalchemy.orm import Session
from backend.payment.models.transaction import Transaction

class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_transaction(self, user_id: int, transaction_id: str, amount: float, status: str) -> Transaction:
        transaction = Transaction(
            user_id=user_id,
            transaction_id=transaction_id,
            amount=amount,
            status=status,
        )
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def get_transaction_by_id(self, transaction_id: str) -> Transaction:
        return self.db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()