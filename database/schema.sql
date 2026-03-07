# Epic Title: Banking Platform — Core API

-- User table
CREATE TABLE IF NOT EXISTS user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    INDEX idx_username (username),
    INDEX idx_role (role)
);

-- Account table
CREATE TABLE IF NOT EXISTS account (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    balance DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    INDEX idx_user_id (user_id)
);

-- Service Request table
CREATE TABLE IF NOT EXISTS service_request (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    description TEXT NOT NULL,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    INDEX idx_user_id (user_id),
    INDEX idx_status (status)
);

-- Interaction History table
CREATE TABLE IF NOT EXISTS interaction_history (
    interaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    details TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    INDEX idx_user_id (user_id)
);