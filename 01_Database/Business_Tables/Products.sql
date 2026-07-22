CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    brand VARCHAR(50),
    unit_price DECIMAL(10,2) NOT NULL,
    cost_price DECIMAL(10,2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    reorder_level INT DEFAULT 20,
    status VARCHAR(20) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products (
    product_name,
    category,
    brand,
    unit_price,
    cost_price,
    stock_quantity,
    reorder_level
)
VALUES
('Laptop Pro 15','Electronics','Dell',85000,72000,120,20),

('Wireless Mouse','Accessories','Logitech',1200,750,450,50),

('Gaming Keyboard','Accessories','Redragon',3200,2200,180,30),

('Smartphone X','Electronics','Samsung',65000,55000,95,15),

('Office Chair','Furniture','Godrej',8500,6200,75,10);