# Epic Title: Change Password

CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    hashed_password VARCHAR(255) NOT NULL
);