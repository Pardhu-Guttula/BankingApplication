# Epic Title: Remove products from the shopping cart

from dataclasses import dataclass
from typing import List
from backend.shopping_cart.models.cart_item import CartItem
from backend.user_profile.models.user import User

@dataclass
class ShoppingCart:
    user: User
    items: List[CartItem]