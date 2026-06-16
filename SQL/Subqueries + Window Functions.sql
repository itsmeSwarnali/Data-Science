-- Customers (same as before)
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

-- Orders (same as before)
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

-- Products (NEW!)
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

-- Order Items (NEW! — links orders to products)
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


-- — Q1 — Subquery
--Find all customers whose total_spent is above the average total_spent of all customers.
--Show: full name, country, total spent. Sort by total spent descending.

select c.full_name, c.country, c.total_spent
from customers c
where c.total_spent > (select avg(c.total_spent) from customers c)
order by c.total_spent desc;



-- Q2 — Subquery -- Find all products whose price is above the average price of all products.
--Show: product name, category, price. Sort by price descending.
select p.product_name, p.category, p.price
from products p
where p.price > (select avg(p.price) from products p) 
order by p.price desc;


-- Q3 — Window Function
--For each customer show: Full name, Country, Total spent ,Average total spent of their country
--Difference between their spending and country average
select c.full_name, c.country, c.total_spent,
        avg(c.total_spent) over (partition by country) as avg_per_country,
        c.total_spent - avg(c.total_spent) over (partition by country) as difference
from customers c
order by country, total_spent desc;





-- Q4 — Window Function -- Rank all customers by their total_spent.
--Show: rank, full name, country, total spent. Highest spender = Rank 1.
--(Use RANK() window function)
select c.full_name, c.country, c.total_spent,
        rank() over (order by c.total_spent desc) as rank_cus
from customers c;



-- Q5 — Subquery + JOIN
--Find customers who have spent more than the average order amount in completed orders.
--Show: full name, country, their total order amount.
--(Hint: You need orders table + subquery for average)
select c.full_name, c.country, sum(o.amount) as sum_of_amount
from customers c
inner join orders o
on c.customer_id = o.customer_id
where o.status = 'completed'
group by c.full_name, c.country
having sum(o.amount) > (
  select avg(o.amount) from orders o
  where o.status='completed'
);
