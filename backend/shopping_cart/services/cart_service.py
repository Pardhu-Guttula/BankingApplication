# Epic Title: Remove Products from the Shopping Cart

from sqlalchemy.orm import Session
from backend.shopping_cart.repositories.cart_repository import CartRepository
from backend.product_catalog.repositories.product_repository import ProductRepository

class CartService:
    def __init__(self, cart_repository: CartRepository, product_repository: ProductRepository):
        self.cart_repository = cart_repository
        self.product_repository = product_repository

    def remove_product_from_cart(self, db: Session, user_id: int, product_id: int):
        cart = self.cart_repository.get_cart_by_user_id(user_id)

        if not cart:
            return "Cart not found for the user"

        removed = self.cart_repository.remove_cart_item(cart.id, product_id)
        if removed:
            return self.cart_repository.get_cart_items(cart.id)
        return "Product is not in the cart"