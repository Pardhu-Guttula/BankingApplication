# Epic Title: Generate detailed e-commerce performance reports

CREATE TABLE IF NOT EXISTS performance_metrics (
    metric_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    sales_quantity INT NOT NULL,
    total_revenue FLOAT NOT NULL,
    avg_session_duration FLOAT NOT NULL,
    total_page_views INT NOT NULL,
    click_through_rate FLOAT NOT NULL
);