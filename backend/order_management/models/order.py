# Epic Title: Display order confirmation to customers after successful payment

from dataclasses import dataclass
from typing import List

@dataclass
class OrderItem:
    id: int
    name: str
    price: float
    quantity: int

@dataclass
class Order:
    order_id: int
    transaction_id: str
    items: List[OrderItem]
    total_amount: float
    customer_email: str