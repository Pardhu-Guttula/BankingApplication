# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS banking_product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id VARCHAR(50) UNIQUE,
    name VARCHAR(255),
    description TEXT,
    eligibility_criteria VARCHAR(255)
);