SELECT employee.id, employee.name, 
COUNT(sales.price) AS sales_c,
rank() over (order by COUNT(sales.price) desc) sales_rank_c,
SUM(sales.price) AS sales_s,
rank() over (order by SUM(sales.price) desc) sales_rank_s
FROM employee INNER JOIN sales ON employee.id = sales.employee_id
GROUP BY employee.id, employee.name