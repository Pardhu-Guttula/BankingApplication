# Epic Title: Create Products Table in PostgreSQL

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price FLOAT CHECK(price > 0)
);