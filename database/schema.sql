# Epic Title: Display Personalized Banking Products

CREATE TABLE user_profiles (
    user_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    income FLOAT NOT NULL,
    risk_tolerance VARCHAR(20) NOT NULL
);

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description VARCHAR(255) NOT NULL,
    eligibility_criteria TEXT NOT NULL
);