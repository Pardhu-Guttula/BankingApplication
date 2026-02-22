# Epic Title: Integrate payment gateway (Stripe) for processing payments

from dataclasses import dataclass
import datetime

@dataclass
class Transaction:
    id: str
    amount: float
    currency: str
    status: str
    created_at: datetime.datetime