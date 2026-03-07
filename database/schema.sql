# Epic Title: Banking Platform — Core API

CREATE TABLE IF NOT EXISTS monitoring_alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    alert TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS monitoring_reports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    report TEXT NOT NULL
);