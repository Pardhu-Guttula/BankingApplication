# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS navigation_menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    expanded BOOLEAN
);

CREATE TABLE IF NOT EXISTS navigation_link (
    id INT AUTO_INCREMENT PRIMARY KEY,
    navigation_menu_id INT,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    icon VARCHAR(255),
    FOREIGN KEY (navigation_menu_id) REFERENCES navigation_menu(id)
);

CREATE TABLE IF NOT EXISTS header_menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS header_link (
    id INT AUTO_INCREMENT PRIMARY KEY,
    header_menu_id INT,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    FOREIGN KEY (header_menu_id) REFERENCES header_menu(id)
);