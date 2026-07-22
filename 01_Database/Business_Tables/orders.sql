CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    employee_id INT NOT NULL,
    order_date DATE NOT NULL,
    order_status VARCHAR(30) DEFAULT 'Pending',
    payment_status VARCHAR(30) DEFAULT 'Pending',
    shipping_address VARCHAR(255),
    total_amount DECIMAL(12,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
);

INSERT INTO orders
(customer_id, employee_id, order_date, order_status, payment_status, shipping_address, total_amount)
VALUES
(1,1,'2026-01-15','Delivered','Paid','Bangalore',86200.00),

(2,2,'2026-01-18','Shipped','Paid','Ahmedabad',1200.00),

(3,3,'2026-01-22','Processing','Pending','Hyderabad',65000.00),

(4,4,'2026-02-02','Delivered','Paid','Kochi',8500.00),

(5,5,'2026-02-05','Cancelled','Refunded','Delhi',3200.00);