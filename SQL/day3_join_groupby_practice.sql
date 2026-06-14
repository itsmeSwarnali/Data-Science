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


-- Step 1: Create customers table
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

-- Step 2: Insert 15 rows
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


-- Q1. Show each order with the customer's full name, country, order amount and status. Use INNER JOIN.
select c.full_name, c.country, o.amount, o.status 
from customers c 
inner join orders o 
on c.customer_id = o.customer_id;

-- Q2. Show all customers and their orders.Include customers who have no orders too. Show: full name, order date, amount.
select c.full_name, o.order_id, o.order_date, o.amount 
from customers c 
left join orders o 
on c.customer_id = o.customer_id;

-- Q3. How many completed orders does each customer have? Show: full name, number of completed orders. Only show customers with at least 1 completed order.
select c.full_name, count(*) as num_of_comple_order
from customers c
left join orders o
on c.customer_id = o.customer_id
where o.status = "completed"
group by c.full_name, c.customer_id
HAVING COUNT(*) >= 1; ;

-- Q4. For each country, what is the total revenue from completed orders? Show: country, total revenue. Sort by total revenue descending.
select c.country, sum(o.amount) as revenue
from customers c 
left join orders o
on c.customer_id = o.customer_id
where o.status='completed'
group by c.country
order by revenue desc;

-- Q5. Find customers who have never placed an order.Show their full name and country.
select c.full_name, c.country
from customers c left join orders o
on c.customer_id = o.customer_id
where o.order_id is null;
