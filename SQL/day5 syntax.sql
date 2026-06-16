-- Subquery template
SELECT column
FROM table
WHERE column > (SELECT AVG(column) FROM table);

-- Window function template
SELECT column,
       RANK() OVER (ORDER BY column DESC) AS rank
FROM table;

-- Window with PARTITION
SELECT column,
       AVG(column) OVER (PARTITION BY group_column) AS group_avg
FROM table;



-- RANK customers by spending
RANK() OVER (ORDER BY total_spent DESC)

-- Running total
SUM(amount) OVER (ORDER BY order_date)

-- Average per group without collapsing
AVG(total_spent) OVER (PARTITION BY country)

-- Row number
ROW_NUMBER() OVER (ORDER BY total_spent DESC)
