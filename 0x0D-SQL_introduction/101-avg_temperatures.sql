-- count commands that count the once that are the words in specific in table of a databases
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;