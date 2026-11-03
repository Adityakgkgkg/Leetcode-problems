# Write your MySQL query statement below
select distinct l1.num AS ConsecutiveNums
from logs l1
join logs l2 
ON l1.id = l2.id-1
join logs l3
ON l2.id = l3.id-1
where l1.num = l2.num AND l2.num = l3.num;



