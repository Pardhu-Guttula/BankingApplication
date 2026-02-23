# Epic Title: Manage and Update Order Statuses

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    order_id VARCHAR NOT NULL UNIQUE,
    user_id INTEGER NOT NULL,
    total_amount FLOAT NOT NULL,
    transaction_id VARCHAR NOT NULL UNIQUE,
    status VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);