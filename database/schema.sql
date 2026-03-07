# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS realtime_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_id VARCHAR(50) UNIQUE,
    content TEXT,
    timestamp TIMESTAMP
);