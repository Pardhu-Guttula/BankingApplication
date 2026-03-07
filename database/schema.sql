# Epic Title: Banking Platform — Core API

-- MainContentArea table
CREATE TABLE IF NOT EXISTS main_content_area (
    id INT AUTO_INCREMENT PRIMARY KEY,
    current_view VARCHAR(255)
);

-- MainContentView table
CREATE TABLE IF NOT EXISTS main_content_view (
    id INT AUTO_INCREMENT PRIMARY KEY,
    main_content_area_id INT,
    name VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (main_content_area_id) REFERENCES main_content_area(id)
);