SELECT Countries.name, COUNT(cities.id)  
FROM countries
JOIN cities 
ON cities.country_id=countries.id
Group By countries.name
ORDER By Count(cities.id) DESC