# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS email_statuses (
    email_id VARCHAR(50) PRIMARY KEY,
    status VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS delivery_receipts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    receipt_id VARCHAR(50),
    email VARCHAR(100),
    status VARCHAR(50)
);