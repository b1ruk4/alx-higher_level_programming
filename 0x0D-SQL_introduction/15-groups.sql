-- lists the number of records with the same score
-- and list them in decs order 
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BT `number` DESC;
