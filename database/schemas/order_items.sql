# Epic Title: View Order History

CREATE TABLE IF NOT EXISTS order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    item_id INT,
    name VARCHAR(255),
    price DECIMAL(10, 2),
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);