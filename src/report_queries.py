

continent_query = """
SELECT continents.name AS Continent, COUNT(*) AS "Country Count"
FROM countries
JOIN continents
ON countries.continent = continents.name
GROUP BY continents.name
"""

country_query = """
SELECT l.name Language, array_to_string(array_agg(c.name), ', ') Countries
FROM languages l JOIN countries c
ON l.code = ANY (c.languages)
GROUP BY 1
ORDER BY 1;
"""

language_query = """
SELECT name AS Country, COUNT(languages) AS "Lng Count"
FROM countries c,
UNNEST(c.languages)
GROUP BY name;
"""
