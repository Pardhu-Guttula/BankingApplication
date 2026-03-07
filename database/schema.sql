# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS interactions (
    interaction_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50),
    interaction_type VARCHAR(50),
    timestamp TIMESTAMP,
    location VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS notifications (
    user_id VARCHAR(50),
    notification_type VARCHAR(50),
    message TEXT,
    timestamp TIMESTAMP
);