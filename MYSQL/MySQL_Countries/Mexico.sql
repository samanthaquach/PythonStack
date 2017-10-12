SELECT * FROM Countries
JOIN cities
ON cities.country_id=countries.id
WHERE countries.name = "Mexico" AND cities.population > 500000
ORDER BY cities.population desc