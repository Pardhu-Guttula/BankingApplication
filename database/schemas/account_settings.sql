# Epic Title: Manage Account

CREATE TABLE IF NOT EXISTS account_settings (
    user_id INT PRIMARY KEY,
    preferences TEXT NOT NULL,
    privacy_settings TEXT NOT NULL,
    updated_at TIMESTAMP NOT NULL
);