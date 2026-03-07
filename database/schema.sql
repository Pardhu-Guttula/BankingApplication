# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS request_forms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50),
    account_type VARCHAR(50),
    initial_deposit FLOAT
);