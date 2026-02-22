# Epic Title: Track sales performance metrics

CREATE TABLE IF NOT EXISTS sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    total_price FLOAT NOT NULL,
    sale_date DATE NOT NULL
);