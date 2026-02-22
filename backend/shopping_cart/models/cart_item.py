# Epic Title: Add products to the shopping cart

from dataclasses import dataclass
from backend.shopping_cart.models.product import Product

@dataclass
class CartItem:
    product: Product
    quantity: int