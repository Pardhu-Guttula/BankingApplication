-- Epic Title: Implement user authentication and authorization features

CREATE TABLE roles (
    role_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    permissions JSON NOT NULL
);