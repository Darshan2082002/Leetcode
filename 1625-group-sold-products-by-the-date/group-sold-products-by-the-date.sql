# Write your MySQL query statement below
select sell_date,COUNT(DISTINCT product) as num_sold,GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
From Activities
GROUP BY sell_date
ORDER BY sell_date