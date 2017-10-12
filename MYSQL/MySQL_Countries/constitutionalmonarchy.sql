SELECT name, government_form, capital, life_expectancy
FROM Countries
WHERE government_form = 'Constitutional Monarchy' and capital > 200 and life_expectancy > 75