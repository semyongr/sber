WITH union_transfers(id_from, id_to) AS (
SELECT id_from, (0-amount) FROM transfers
UNION
SELECT id_to, amount FROM transfers)

SELECT id_from AS acc, SUM(id_to) AS balance FROM union_transfers
GROUP BY id_from


