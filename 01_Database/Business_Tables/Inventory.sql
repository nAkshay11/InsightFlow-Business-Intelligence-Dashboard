CREATE TABLE inventory (
    inventory_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    warehouse_id INT NOT NULL,
    available_stock INT NOT NULL,
    reserved_stock INT DEFAULT 0,
    damaged_stock INT DEFAULT 0,
    reorder_level INT DEFAULT 20,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (product_id)
        REFERENCES products(product_id),

    FOREIGN KEY (warehouse_id)
        REFERENCES warehouses(warehouse_id)
);

INSERT INTO inventory
(product_id, warehouse_id, available_stock, reserved_stock, damaged_stock, reorder_level)
VALUES
(1,1,120,10,2,20),
(2,1,450,15,1,50),
(3,2,180,12,3,30),
(4,3,95,8,0,15),
(5,4,75,5,1,10);