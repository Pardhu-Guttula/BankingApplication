# Epic Title: Create Orders Table in PostgreSQL

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    total_amount FLOAT NOT NULL CHECK(total_amount > 0),
    FOREIGN KEY (user_id) REFERENCES users(id)
);