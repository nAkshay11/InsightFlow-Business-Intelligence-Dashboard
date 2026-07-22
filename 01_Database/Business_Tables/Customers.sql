CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    gender VARCHAR(10),
    date_of_birth DATE,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    customer_segment VARCHAR(30),
    registration_date DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customers (
    first_name,
    last_name,
    email,
    phone,
    gender,
    date_of_birth,
    city,
    state,
    country,
    customer_segment
)
VALUES
('Rahul','Sharma','rahul.sharma@email.com','9876543210','Male','1995-06-15','Bangalore','Karnataka','India','Premium'),

('Priya','Patel','priya.patel@email.com','9123456780','Female','1998-11-20','Ahmedabad','Gujarat','India','Standard'),

('Arjun','Reddy','arjun.reddy@email.com','9988776655','Male','1993-04-10','Hyderabad','Telangana','India','Corporate'),

('Sneha','Nair','sneha.nair@email.com','9876501234','Female','1997-09-18','Kochi','Kerala','India','Premium'),

('Vikram','Singh','vikram.singh@email.com','9011223344','Male','1992-01-30','Delhi','Delhi','India','Standard');