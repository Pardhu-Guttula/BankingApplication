# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_id VARCHAR(50),
    status VARCHAR(50),
    message TEXT
);