CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    department VARCHAR(50),
    designation VARCHAR(50),
    hire_date DATE,
    salary DECIMAL(10,2),
    city VARCHAR(50),
    state VARCHAR(50),
    status VARCHAR(20) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO employees (
    first_name,
    last_name,
    email,
    phone,
    department,
    designation,
    hire_date,
    salary,
    city,
    state
)
VALUES
('Akshay','Chandra','akshay@insightflow.com','9876543210','Analytics','Data Analyst','2025-01-15',65000,'Bangalore','Karnataka'),

('Rahul','Kumar','rahul@insightflow.com','9876501234','Sales','Sales Manager','2023-05-10',85000,'Hyderabad','Telangana'),

('Priya','Sharma','priya@insightflow.com','9988776655','Finance','Finance Analyst','2024-03-18',72000,'Mumbai','Maharashtra'),

('Arjun','Reddy','arjun@insightflow.com','9011223344','Operations','Operations Manager','2022-08-22',92000,'Chennai','Tamil Nadu'),

('Sneha','Patel','sneha@insightflow.com','9123456789','HR','HR Executive','2024-07-12',58000,'Ahmedabad','Gujarat');