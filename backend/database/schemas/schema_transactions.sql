# Epic Title: Integrate Payment Gateway (Stripe) for Processing Payments

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    transaction_id VARCHAR NOT NULL UNIQUE,
    amount FLOAT NOT NULL,
    status VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);