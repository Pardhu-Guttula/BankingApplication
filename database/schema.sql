# Epic Title: Banking Platform — Core API

-- Layout table
CREATE TABLE IF NOT EXISTS layout (
    name VARCHAR(255) PRIMARY KEY
);

-- Component table
CREATE TABLE IF NOT EXISTS component (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position INT NOT NULL,
    margin VARCHAR(50) NOT NULL,
    padding VARCHAR(50) NOT NULL,
    font_style VARCHAR(255) NOT NULL,
    layout_name VARCHAR(255),
    FOREIGN KEY (layout_name) REFERENCES layout(name)
);

-- Breakpoint table
CREATE TABLE IF NOT EXISTS breakpoint (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    min_width INT NOT NULL,
    max_width INT NOT NULL,
    layout_name VARCHAR(255),
    FOREIGN KEY (layout_name) REFERENCES layout(name)
);

-- Browser table
CREATE TABLE IF NOT EXISTS browser (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    version VARCHAR(255) NOT NULL
);