-- Epic Title: Implement user authentication and authorization features

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    role_id INT NOT NULL,
    FOREIGN KEY(role_id) REFERENCES roles(role_id)
);