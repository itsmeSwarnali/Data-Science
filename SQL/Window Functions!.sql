customers    → customer_id, full_name, country, age, gender, total_spent
orders       → order_id, customer_id, order_date, amount, status
order_items  → item_id, order_id, product_id, quantity, unit_price
products     → product_id, product_name, category, price, stock



--Q1 — RANK with PARTITION BY
--Rank all products by their price, but rank them
--separately within each category (each category gets its own #1, #2, #3...).
--Show: product_name, category, price, rank_in_category.
select p.product_name, p.category, p.price,
RANK() over (PARTITION BY p.category order BY p.price DESC) as rank_in_category
from products p;


-- Q2 RANK with PARTITION BY (same pattern, new table)
--Rank all customers by their total_spent, but rank them separately within each country.
--Show: full_name, country, total_spent, rank_in_country.
select c.full_name, c.country, c.total_spent,
RANK() over (Partition by country  order by c.total_spent desc) as rank_in_country
from customers c;

-- Q3 — Window Function + CASE WHEN (same pattern as yesterday's Q3)
--For each customer, show:vfull_name, country, total_spent
--The average total_spent for their country (PARTITION BY country)
--A column saying 'Above Country Avg' or 'Below Country Avg'
select c.full_name, c.country, c.total_spent,
  avg(c.total_spent) over (partition by c.country) as avg_spent,
  case
      when c.total_spent>avg(c.total_spent) over (partition by c.country) then "Above Country Avg"
      else "Below Country Avg"
  end as spending_status
from customers c;



-- Q4 — DENSE_RANK practice
-- Using the same product ranking as Q1, but this time use DENSE_RANK() instead of RANK().
-- Show: product_name, category, price, rank_in_category, dense_rank_in_category (both columns side by side, so you can see the difference).
select p.product_name, p.category, p.price, 
DENSE_RANK() over (partition by category order by p.price) as dense_rank_in_category, 
RANK() over (partition by category order by p.price) as rank_in_category
from products p;

  
  --Q5 — JOIN + GROUP BY + Subquery + HAVING (yesterday's hardest type!)
--Find customers whose total completed order amount is above the average total completed order amount (averaged across all customers who have completed orders).
--Show: full name, country, total order amount.


