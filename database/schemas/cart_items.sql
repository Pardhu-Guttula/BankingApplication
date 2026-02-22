# Epic Title: Update product quantities in the shopping cart

CREATE TABLE IF NOT EXISTS cart_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cart_user_id INT,
    product_id INT,
    quantity INT NOT NULL CHECK (quantity >= 0),
    FOREIGN KEY (cart_user_id) REFERENCES shopping_carts(user_id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);