SELECT * FROM languages
JOIN countries
ON languages.country_id=countries.id
WHERE languages.percentage > 89
ORDER BY languages.percentage desc