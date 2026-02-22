# Epic Title: Monitor user behavior metrics

CREATE TABLE IF NOT EXISTS click_through_rates (
    click_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    element_id VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    clicked BOOLEAN NOT NULL
);