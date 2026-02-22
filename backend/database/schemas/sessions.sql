-- Epic Title: Implement user authentication and authorization features

CREATE TABLE sessions (
    session_id VARCHAR(32) PRIMARY KEY,
    user_id INT NOT NULL,
    token VARCHAR(32) NOT NULL UNIQUE,
    valid_until DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);