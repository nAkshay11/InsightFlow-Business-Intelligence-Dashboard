CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role_id INT NOT NULL,
    status VARCHAR(20) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
);

INSERT INTO users (full_name, email, password_hash, role_id)
VALUES
('Admin User', 'admin@insightflow.com', 'admin123', 1),
('Akshay Chandra', 'akshay@insightflow.com', 'akshay123', 2),
('Business Manager', 'manager@insightflow.com', 'manager123', 4);