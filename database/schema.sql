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

CREATE TABLE IF NOT EXISTS roles (
    role_name VARCHAR(100) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS permissions (
    permission_name VARCHAR(100) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS role_permissions (
    role_name VARCHAR(100),
    permission_name VARCHAR(100),
    PRIMARY KEY (role_name, permission_name),
    FOREIGN KEY (role_name) REFERENCES roles (role_name),
    FOREIGN KEY (permission_name) REFERENCES permissions (permission_name)
);