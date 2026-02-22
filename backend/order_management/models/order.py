# Epic Title: Manage and Update Order Statuses

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

@dataclass
class OrderStatus:
    order_id: int
    status: str
    updated_at: datetime.datetime
    updated_by: int  # administrator ID