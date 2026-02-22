# Epic Title: Persist shopping cart state in PostgreSQL

CREATE TABLE IF NOT EXISTS shopping_carts (
    user_id INT PRIMARY KEY,
    FOREIGN KEY (user_id) REFERENCES users(id)
);