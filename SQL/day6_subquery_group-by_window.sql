-- Table 1: customers
CREATE TABLE customers (
  customer_id  INT,
  full_name    VARCHAR(100),
  city         VARCHAR(50),
  country      VARCHAR(50),
  age          INT,
  gender       VARCHAR(10),
  signup_date  DATE,
  total_spent  DECIMAL(10,2)
);

INSERT INTO customers VALUES
(1,  'Sofia Ricci',       'Rome',    'Italy',   28, 'Female', '2022-01-15', 820.00),
(2,  'Marco Bianchi',     'Milan',   'Italy',   35, 'Male',   '2021-06-10', 450.00),
(3,  'Anna Müller',       'Berlin',  'Germany', 42, 'Female', '2020-03-22', 310.00),
(4,  'Hans Weber',        'Munich',  'Germany', 55, 'Male',   '2019-11-05', 980.00),
(5,  'Claire Dupont',     'Paris',   'France',  30, 'Female', '2023-02-18', 150.00),
(6,  'Lucas Martin',      'Lyon',    'France',  47, 'Male',   '2021-08-30', 620.00),
(7,  'Elena Greco',       'Naples',  'Italy',   22, 'Female', '2023-05-01', 200.00),
(8,  'Lena Braun',        'Berlin',  'Germany', 26, 'Female', '2022-09-14', 530.00),
(9,  'Carlos Ruiz',       'Madrid',  'Spain',   38, 'Male',   '2020-07-19', 410.00),
(10, 'Maria Garcia',      'Madrid',  'Spain',   31, 'Female', '2022-12-01', 760.00),
(11, 'Giuseppe Esposito', 'Rome',    'Italy',   60, 'Male',   '2018-04-25', 1200.00),
(12, 'Nina Schmidt',      'Munich',  'Germany', 24, 'Female', '2023-03-10', 275.00),
(13, 'Emilie Bernard',    'Paris',   'France',  52, 'Female', '2019-10-08', 890.00),
(14, 'Yuki Tanaka',       'Rome',    'Italy',   29, 'Female', '2023-01-20', 340.00),
(15, 'Pedro Alves',       'Madrid',  'Spain',   44, 'Male',   '2021-05-17', 505.00);

-- Table 2: orders
CREATE TABLE orders (
  order_id    INT,
  customer_id INT,
  order_date  DATE,
  amount      DECIMAL(10,2),
  status      VARCHAR(20)
);

INSERT INTO orders VALUES
(1,  1,  '2023-01-10', 250.00, 'completed'),
(2,  1,  '2023-03-15', 180.00, 'completed'),
(3,  2,  '2023-02-20', 450.00, 'completed'),
(4,  3,  '2023-01-25', 310.00, 'pending'),
(5,  4,  '2023-04-10', 980.00, 'completed'),
(6,  5,  '2023-05-01', 150.00, 'cancelled'),
(7,  6,  '2023-03-18', 620.00, 'completed'),
(8,  7,  '2023-06-22', 200.00, 'completed'),
(9,  8,  '2023-02-14', 530.00, 'completed'),
(10, 9,  '2023-07-30', 410.00, 'pending'),
(11, 11, '2023-08-05', 800.00, 'completed'),
(12, 11, '2023-09-12', 400.00, 'completed'),
(13, 13, '2023-04-28', 890.00, 'completed'),
(14, 14, '2023-05-15', 340.00, 'completed'),
(15, 15, '2023-06-20', 505.00, 'completed');

-- Table 3: products
CREATE TABLE products (
  product_id   INT,
  product_name VARCHAR(100),
  category     VARCHAR(50),
  price        DECIMAL(10,2),
  stock        INT
);

INSERT INTO products VALUES
(1,  'Laptop Pro',        'Electronics', 1200.00, 50),
(2,  'Wireless Mouse',    'Electronics',   25.00, 200),
(3,  'Python Book',       'Books',         45.00, 150),
(4,  'SQL Guide',         'Books',         35.00, 120),
(5,  'Running Shoes',     'Clothing',      90.00, 80),
(6,  'Winter Jacket',     'Clothing',     150.00, 60),
(7,  'Coffee Beans',      'Food',          20.00, 300),
(8,  'Olive Oil',         'Food',          15.00, 250),
(9,  'Headphones',        'Electronics',  200.00, 75),
(10, 'Data Science Book', 'Books',         55.00, 100);

-- Table 4: order_items
CREATE TABLE order_items (
  item_id    INT,
  order_id   INT,
  product_id INT,
  quantity   INT,
  unit_price DECIMAL(10,2)
);

INSERT INTO order_items VALUES
(1,  1,  1,  1, 1200.00),
(2,  1,  2,  2,   25.00),
(3,  2,  3,  1,   45.00),
(4,  3,  9,  1,  200.00),
(5,  4,  5,  2,   90.00),
(6,  5,  1,  1, 1200.00),
(7,  6,  7,  3,   20.00),
(8,  7,  6,  2,  150.00),
(9,  8,  4,  1,   35.00),
(10, 9,  2,  3,   25.00),
(11, 10, 8,  2,   15.00),
(12, 11, 9,  2,  200.00),
(13, 12, 10, 1,   55.00),
(14, 13, 1,  1, 1200.00),
(15, 14, 3,  2,   45.00);


-- Q1 — JOIN + GROUP BY + ORDER BY: For each product category, show the number of distinct customers who bought from that category and the total revenue generated.
--Show: category, distinct_customer_count, total_revenue.
--Sort by total_revenue descending.
select p.category, count(distinct c.customer_id) as number_of_distinct_customers, sum(oi.unit_price*oi.quantity) as total_revenue

from products p inner join order_items oi on p.product_id = oi.product_id

inner join orders o on oi.order_id = o.order_id

inner join  customers c on c.customer_id = o.customer_id

group by p.category

order by total_revenue desc;



--Q2 — Subquery: Find customers who have never bought anything from the 'Electronics' category (even if they've bought from other categories or placed no orders at all).
--Show: full_name, country.

select c.full_name, c.country, p.category, p.product_name

from customers c inner join orders o on o.customer_id = c.customer_id

inner join order_items oi on oi.order_id = o.order_id

inner join products p on p.product_id = oi.product_id

where p.category != "Electronics";


--Q3 — Window Function: For each order, show the order_id, customer_id, order_date, amount, and a running total of amount ordered by that same customer, ordered by order_date.
--Show: order_id, customer_id, order_date, amount, running_total.
--(Hint: SUM() OVER with PARTITION BY customer AND ORDER BY date)
select c.customer_id, o.order_id, o.order_date, o.amount, 
sum(o.amount) over (partition by c.customer_id order by o.order_date) as running_total
from customers c inner join orders o on c.customer_id = o.customer_id;



