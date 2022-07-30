# Simle ETL workflow
---

The workflow brings the data into an PostgresSQL database.

## Approaching the workflow
The workflow requires the following steps:
1. Create the database.
2. Create the tables. Four tables are created in the database: `continents`, `countries`, `cities`, and `airports`.	
3. Load the data into the tables.
4. Generate the reports.

### Creating the database
The database is created using the `psql` with the following command:

```
psql -U user -d password -c "CREATE DATABASE dbname;"
```

### Creating the tables
The tables are created by describing the database tables and then by defining classes which will be mapped to those tables.

```sql
class Class(Base):
    __tablename__ = 'table_name'
    
    id = Column(Integer, primary_key = True)
    col1 = Column(2String)
    col2 = Column(String)
    col3 = Column(String)
```
Finally, pass the classes to the `Base.metadata.create_all` method.

### Load the tables
The json files are parsed and the data is loaded into the tables.

```python
with open('data/continents.json') as f:
    continents = json.load(f)
    for continent in continents:
        session.add(Continent(**continent))

The data is loaded into the tables by using the `session.add` method.

```sql
session.add(Class(col1 = 'value1', col2 = 'value2', col3 = 'value3'))
```



### Generating the reports
The reports are generated with SQL statements. You can use the following code to generate the reports:

1. List all the continents and the total number of countries in each—for example, Africa 100, Europe 10, etc. The continent's name and country count should be in a different column.
```sql
SELECT continents.name AS Continent, COUNT(*) AS "Country Count"
FROM countries
JOIN continents
ON countries.continent = continents.name
GROUP BY continents.name
```
2. List all the languages and commas separated countries that speak the language. 
```sql
SELECT l.name Language, array_to_string(array_agg(c.name), ', ') Countries
FROM languages l JOIN countries c
ON l.code = ANY (c.languages)
GROUP BY 1
ORDER BY 1;
```
3. List all the countries and the total number of languages spoken.
```sql
SELECT name AS Country, COUNT(languages) AS "Lng Count"
FROM countries c,
UNNEST(c.languages)
GROUP BY name;
```
