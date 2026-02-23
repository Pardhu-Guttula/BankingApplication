# Epic Title: Track Sales Performance Metrics

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    amount FLOAT NOT NULL,
    category VARCHAR NOT NULL,
    product_id INTEGER NOT NULL
);