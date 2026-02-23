# Epic Title: Persist Shopping Cart State in PostgreSQL

from sqlalchemy.orm import Session
from backend.shopping_cart.models.cart import Cart
from backend.shopping_cart.models.cart_item import CartItem

class CartRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_cart_by_user_id(self, user_id: int) -> Cart:
        return self.db.query(Cart).filter(Cart.user_id == user_id).first()

    def add_item_to_cart(self, cart_id: int, product_id: int, quantity: int):
        cart_item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
        self.db.add(cart_item)
        self.db.commit()
        self.db.refresh(cart_item)

    def update_cart_item_quantity(self, cart_id: int, product_id: int, quantity: int):
        cart_item = self.db.query(CartItem).filter(CartItem.cart_id == cart_id, CartItem.product_id == product_id).first()
        if cart_item:
            if quantity == 0:
                self.db.delete(cart_item)
            else:
                cart_item.quantity = quantity
            self.db.commit()
            self.db.refresh(cart_item)
            return cart_item
        return None

    def remove_cart_item(self, cart_id: int, product_id: int):
        cart_item = self.db.query(CartItem).filter(CartItem.cart_id == cart_id, CartItem.product_id == product_id).first()
        if cart_item:
            self.db.delete(cart_item)
            self.db.commit()
            return True
        return False

    def get_cart_items(self, cart_id: int):
        return self.db.query(CartItem).filter(CartItem.cart_id == cart_id).all()