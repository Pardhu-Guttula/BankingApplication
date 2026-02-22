# Epic Title: Display order confirmation to customers after successful payment

CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id VARCHAR(255) NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    customer_email VARCHAR(255) NOT NULL
);