# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS navigation_links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    link_id VARCHAR(50),
    title VARCHAR(100),
    url VARCHAR(255)
);