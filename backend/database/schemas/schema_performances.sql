# Epic Title: Generate Detailed E-commerce Performance Reports

CREATE TABLE performances (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP NOT NULL,
    metric_name VARCHAR NOT NULL,
    metric_value FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);