# Write your MySQL query statement below
select email
From Person 
GROUP BY email
HAVING COUNT(*)>1 