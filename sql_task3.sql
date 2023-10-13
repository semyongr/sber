
with who(id_from, id_to) as (
select id_from, (0-amount) from transfers
UNION
select id_to, amount from transfers)



select id_from as acc, SUM(id_to) as balance from who
group by id_from


