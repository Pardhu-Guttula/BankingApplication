# Epic Title: Banking Platform — Core API

-- Side Navigation table
CREATE TABLE IF NOT EXISTS side_navigation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    collapsed BOOLEAN NOT NULL
);

-- MenuItem table
CREATE TABLE IF NOT EXISTS menu_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    side_navigation_id INT,
    FOREIGN KEY (side_navigation_id) REFERENCES side_navigation(id)
);

-- SubMenuItem table
CREATE TABLE IF NOT EXISTS sub_menu_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parent_id INT,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    FOREIGN KEY (parent_id) REFERENCES menu_item(id)
);