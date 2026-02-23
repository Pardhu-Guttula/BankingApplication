# Epic Title: Persist Shopping Cart State in PostgreSQL

CREATE TABLE carts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL
);