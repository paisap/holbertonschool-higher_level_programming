-- number by score
SELECT score, count(score) as number from second_table GROUP BY score ORDER BY score DESC;