# Epic Title: Add Products to the Shopping Cart

from sqlalchemy.orm import Session
from backend.shopping_cart.repositories.cart_repository import CartRepository
from backend.product_catalog.repositories.product_repository import ProductRepository

class CartService:
    def __init__(self, cart_repository: CartRepository, product_repository: ProductRepository):
        self.cart_repository = cart_repository
        self.product_repository = product_repository

    def add_product_to_cart(self, db: Session, user_id: int, product_id: int, quantity: int):
        cart = self.cart_repository.get_cart_by_user_id(user_id)
        product = self.product_repository.get_product_by_id(product_id)

        if not cart:
            cart = Cart(user_id=user_id)
            db.add(cart)
            db.commit()
            db.refresh(cart)

        if product:
            self.cart_repository.add_item_to_cart(cart.id, product_id, quantity)
            return self.cart_repository.get_cart_items(cart.id)
        return "Product is unavailable in inventory"