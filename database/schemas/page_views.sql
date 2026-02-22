# Epic Title: Monitor user behavior metrics

CREATE TABLE IF NOT EXISTS page_views (
    view_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    page_url VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP NOT NULL
);