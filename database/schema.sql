# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS interactions (
    interaction_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50),
    interaction_type VARCHAR(50),
    timestamp TIMESTAMP
);