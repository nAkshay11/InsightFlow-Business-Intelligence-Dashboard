CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    payment_method VARCHAR(30) NOT NULL,
    payment_date DATE NOT NULL,
    payment_status VARCHAR(30) NOT NULL,
    transaction_reference VARCHAR(100) UNIQUE,
    amount DECIMAL(12,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

INSERT INTO payments
(order_id, payment_method, payment_date, payment_status, transaction_reference, amount)
VALUES
(1,'Credit Card','2026-01-15','Paid','TXN100001',86200.00),
(2,'UPI','2026-01-18','Paid','TXN100002',1200.00),
(3,'Net Banking','2026-01-22','Pending','TXN100003',65000.00),
(4,'Debit Card','2026-02-02','Paid','TXN100004',8500.00),
(5,'UPI','2026-02-05','Refunded','TXN100005',3200.00);