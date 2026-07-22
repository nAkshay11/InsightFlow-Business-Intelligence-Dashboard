CREATE TABLE roles (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(50) UNIQUE NOT NULL,
    role_description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO roles (role_name, role_description)
VALUES
('Admin', 'Full access to the platform'),
('Data Analyst', 'Can analyze and generate reports'),
('Business Analyst', 'Can view dashboards and insights'),
('Manager', 'Can monitor business performance');