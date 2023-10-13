SELECT employee.id, employee.name, 
COUNT(sales.price) AS sales_c,
RANK() OVER (ORDER BY COUNT(sales.price) DESC) sales_rank_c,
SUM(sales.price) AS sales_s,
RANK() OVER (ORDER BY SUM(sales.price) DESC) sales_rank_s
FROM employee INNER JOIN sales ON employee.id = sales.employee_id
GROUP BY employee.id, employee.name
