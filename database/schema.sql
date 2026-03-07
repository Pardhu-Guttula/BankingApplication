# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id VARCHAR(50) UNIQUE,
    user_id VARCHAR(50),
    amount FLOAT,
    timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS performance_metrics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    metrics_id VARCHAR(50) UNIQUE,
    operation VARCHAR(255),
    duration FLOAT,
    timestamp TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_request (
    id INT AUTO_INCREMENT PRIMARY KEY,
    request_id VARCHAR(50) UNIQUE,
    user_id VARCHAR(50),
    operation VARCHAR(255),
    timestamp TIMESTAMP
);