# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS dashboard (
    id INT AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS main_content_area (
    id INT AUTO_INCREMENT PRIMARY KEY,
    current_view VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS main_content_view (
    id INT AUTO_INCREMENT PRIMARY KEY,
    main_content_area_id INT,
    name VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (main_content_area_id) REFERENCES main_content_area(id)
);

CREATE TABLE IF NOT EXISTS side_navigation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    collapsed BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS menu_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    side_navigation_id INT,
    FOREIGN KEY (side_navigation_id) REFERENCES side_navigation(id)
);

CREATE TABLE IF NOT EXISTS sub_menu_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parent_id INT,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    FOREIGN KEY (parent_id) REFERENCES menu_item(id)
);

CREATE TABLE IF NOT EXISTS header (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS navigation_link (
    id INT AUTO_INCREMENT PRIMARY KEY,
    header_id INT,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    FOREIGN KEY (header_id) REFERENCES header(id)
);