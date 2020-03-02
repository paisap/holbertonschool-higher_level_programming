-- Number by score
SELECT score, COUNT(score) as number from second_table GROUP BY score ORDER BY score desc;