# Epic Title: Store Order Information in PostgreSQL Database

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    order_id VARCHAR NOT NULL UNIQUE,
    user_id INTEGER NOT NULL,
    total_amount FLOAT NOT NULL,
    transaction_id VARCHAR NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);