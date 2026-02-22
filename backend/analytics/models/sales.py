# Epic Title: Track sales performance metrics

from dataclasses import dataclass
import datetime

@dataclass
class Sales:
    sale_id: int
    product_id: int
    quantity: int
    total_price: float
    sale_date: datetime.date