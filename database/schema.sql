# Epic Title: Display Personalized Banking Products

CREATE TABLE user_profiles (
    user_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT NOT NULL,
    income_bracket VARCHAR(50) NOT NULL,
    preferences VARCHAR(255)
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    eligibility_criteria VARCHAR(255) NOT NULL,
    recommended_for VARCHAR(255)
);