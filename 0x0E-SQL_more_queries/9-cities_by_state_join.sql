-- my first join
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.id=states.id ORDER BY id ASC;