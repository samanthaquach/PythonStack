SELECT countries.name AS country_name, cities.name AS city_name, cities.district, cities.population
FROM cities
JOIN countries ON cities.country_id = countries.id 
WHERE countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population > 500000