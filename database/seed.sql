INSERT INTO customers (name, email, company_name)
VALUES
('Bob Alex', 'bob@example.com', 'Bob Designs'),
('Omar Ali', 'omar@example.com', 'Omar Retail Co.'),
('Sara John', 'sara@example.com', NULL);

INSERT INTO products (name, description, base_price, stock_quantity, image_path)
VALUES
('Custom Mug', 'Personalized ceramic mug with custom text.', 12.99, 50, 'images/mug.jpg'),
('Custom T-Shirt', 'Cotton t-shirt with printed custom design.', 24.99, 30, 'images/tshirt.jpg'),
('Custom Notebook', 'Personalized notebook for school or office use.', 9.99, 100, 'images/notebook.jpg');

INSERT INTO orders (customer_id, product_id, custom_text, quantity, special_instructions, status)
VALUES
(1, 1, 'Best Teacher Ever', 2, 'Use blue text if possible.', 'Pending'),
(2, 2, 'Omar Retail Team', 5, 'Need all shirts in size medium.', 'Processing'),
(3, 3, 'Sara Notes', 3, NULL, 'Completed');