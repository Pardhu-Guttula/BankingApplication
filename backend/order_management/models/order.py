# Epic Title: View Order History

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
    user_id: int
    items: List<OrderItem]
    total_amount: float
    status: str