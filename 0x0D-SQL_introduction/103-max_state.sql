-- the  last advadced
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state;