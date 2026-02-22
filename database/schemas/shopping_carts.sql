# Epic Title: Add products to the shopping cart

CREATE TABLE IF NOT EXISTS shopping_carts (
    user_id INT PRIMARY KEY,
    FOREIGN KEY (user_id) REFERENCES users(id)
);