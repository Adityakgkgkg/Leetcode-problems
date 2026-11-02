# Write your MySQL query statement below
select distinct num AS ConsecutiveNums
from (
    SELECT 
        num,
        LEAD(num, 1) OVER (ORDER BY id) AS next_1,
        LEAD(num, 2) OVER (ORDER BY id) AS next_2
        from logs  
) AS consecutive_table
WHERE num = next_1 
  AND num = next_2;


