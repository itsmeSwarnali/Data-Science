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

--Q1--For each order status (completed, pending, cancelled), show the count of orders and the total amount of orders in that status.
--Show: status, order_count, total_amount.
--Sort by total_amount descending.
select o.status, count(status) as order_count, sum(o.amount) as total_amount
from orders o
group by o.status
order by total_amount desc;

-- Q2 Find all customers who have placed at least one order, but show their info 
--from the customers table along with the 
--number of distinct order statuses they've experienced (e.g., a customer with one completed and one cancelled order = 2 distinct statuses).
--Show: full_name, country, distinct_status_count.
select c.full_name, c.country, count(distinct o.status) as distinct_status_count 
from customers c 
inner join orders o 
on c.customer_id = o.customer_id
group by c.full_name, c.country;


--Q3 Calculate the order completion rate per country — meaning, of all orders placed by customers in that country, what percentage were completed?
--Show: country, total_orders, completed_orders, completion_rate (as a percentage, rounded to 1 decimal).
--(Hint: you'll need conditional counting — think CASE WHEN inside SUM or COUNT)
select c.country, count(*) as total_orders, 
sum(case when o.status = "completed" then 1 else 0 end) as completed_orders, 
round(100.0* sum(case when o.status = "completed" then 1 else 0 end) / count(*),1) as completion_rate
from orders o
left join customers c on c.customer_id= o.customer_id
group by c.country;


--Q4 customers who have exactly 1 completed order AND that order amount is below the overall average order amount (across completed orders).
--Show: full_name, country, order_amount.
select c.full_name, c.country, sum(o.amount) as order_amount
from customers c
left join orders o 
on c.customer_id = o.customer_id
WHERE o.status = 'completed'
group by c.full_name, c.country
having count(*) = 1 and 
sum(o.amount)<(select avg(o.amount) from orders o where o.status = "completed");



--Q5 (Same pattern as yesterday — more reps!)
--Find customers whose total completed order amount is above the average total completed order amount, 
--Show: full_name, country, total_order_amount.

WITH completed_orders AS (
    SELECT 
        c.customer_id,
        c.full_name,
        c.country,
        SUM(o.amount) AS total_completed_order_amount
    FROM customers c
    INNER JOIN orders o
        ON c.customer_id = o.customer_id
    WHERE o.status = 'completed'
    GROUP BY c.customer_id, c.full_name, c.country
)

SELECT *
FROM completed_orders
WHERE total_completed_order_amount > (
    SELECT AVG(total_completed_order_amount)
    FROM completed_orders
);

