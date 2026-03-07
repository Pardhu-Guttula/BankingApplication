# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS user_sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    session_id VARCHAR(255),
    user_id VARCHAR(255),
    expires_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS auth_tokens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    token VARCHAR(255),
    user_id VARCHAR(255),
    expires_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES user_sessions(user_id)
);