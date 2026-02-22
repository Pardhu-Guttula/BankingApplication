# Epic Title: Persist shopping cart state in PostgreSQL

CREATE TABLE IF NOT EXISTS cart_items (
    cart_user_id INT,
    product_id INT,
    quantity INT NOT NULL CHECK (quantity >= 0),
    PRIMARY KEY(cart_user_id, product_id),
    FOREIGN KEY (cart_user_id) REFERENCES shopping_carts(user_id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);