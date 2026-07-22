CREATE TABLE warehouses (
    warehouse_id SERIAL PRIMARY KEY,
    warehouse_name VARCHAR(100) NOT NULL,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    manager_name VARCHAR(100),
    capacity INT,
    contact_number VARCHAR(20),
    status VARCHAR(20) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO warehouses (
    warehouse_name,
    city,
    state,
    country,
    manager_name,
    capacity,
    contact_number
)
VALUES
('Bangalore Central Warehouse','Bangalore','Karnataka','India','Rahul Kumar',50000,'9876543210'),

('Hyderabad Distribution Center','Hyderabad','Telangana','India','Priya Sharma',45000,'9988776655'),

('Mumbai Storage Hub','Mumbai','Maharashtra','India','Arjun Reddy',60000,'9011223344'),

('Chennai South Warehouse','Chennai','Tamil Nadu','India','Sneha Patel',35000,'9123456789'),

('Delhi North Warehouse','Delhi','Delhi','India','Vikram Singh',55000,'9876501234');