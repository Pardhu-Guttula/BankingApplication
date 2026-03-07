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
    layout_name VARCHAR(255),
    FOREIGN KEY (layout_name) REFERENCES layout(name)
);