# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS banking_service (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service_id VARCHAR(50) UNIQUE,
    name VARCHAR(255),
    description TEXT,
    eligibility_criteria VARCHAR(255)
);