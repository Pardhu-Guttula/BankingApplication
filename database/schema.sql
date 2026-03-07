# Epic Title: Banking Platform — Core API

-- Header table
CREATE TABLE IF NOT EXISTS header (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL UNIQUE
);

-- NavigationLink table
CREATE TABLE IF NOT EXISTS navigation_link (
    id INT AUTO_INCREMENT PRIMARY KEY,
    header_id INT,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    FOREIGN KEY (header_id) REFERENCES header(id)
);