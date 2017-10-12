SELECT region, COUNT(id) AS number_countries
FROM countries
GROUP BY region
ORDER BY COUNT(id) desc