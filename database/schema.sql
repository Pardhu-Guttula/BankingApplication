# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS modification_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_id VARCHAR(50),
    user_id VARCHAR(50),
    modification_type VARCHAR(50),
    data TEXT
);