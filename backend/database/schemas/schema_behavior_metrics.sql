# Epic Title: Monitor User Behavior Metrics

CREATE TABLE behavior_metrics (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    session_duration FLOAT,
    page_views INTEGER,
    click_through_rate FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);