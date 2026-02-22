# Epic Title: Persist shopping cart state in PostgreSQL

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price > 0),
    description TEXT,
    available INT NOT NULL CHECK (available >= 0)
);