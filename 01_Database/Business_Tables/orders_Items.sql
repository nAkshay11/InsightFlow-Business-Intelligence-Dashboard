CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    discount DECIMAL(10,2) DEFAULT 0,
    total_price DECIMAL(12,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO order_items
(order_id, product_id, quantity, unit_price, discount, total_price)
VALUES
(1,1,1,85000,0,85000),
(1,2,1,1200,0,1200),
(2,2,1,1200,0,1200),
(3,4,1,65000,0,65000),
(4,5,1,8500,0,8500),
(5,3,1,3200,0,3200);