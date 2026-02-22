# Epic Title: Persist shopping cart state in PostgreSQL

from dataclasses import dataclass
from backend.shopping_cart.models.product import Product

@dataclass
class CartItem:
    product: Product
    quantity: int