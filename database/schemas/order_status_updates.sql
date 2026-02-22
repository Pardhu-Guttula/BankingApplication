# Epic Title: Manage and Update Order Statuses

CREATE TABLE IF NOT EXISTS order_status_updates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    status VARCHAR(50),
    updated_at TIMESTAMP,
    updated_by INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (updated_by) REFERENCES users(id)
);