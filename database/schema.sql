# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(50) PRIMARY KEY,
    username VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS user_roles (
    user_id VARCHAR(50),
    role_name VARCHAR(100),
    PRIMARY KEY (user_id, role_name),
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);