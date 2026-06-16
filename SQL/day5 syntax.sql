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
