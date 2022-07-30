# Simle ETL workflow
---

The workflow brings the data into an PostgreSQL database.

## Approaching the workflow
The workflow requires the following steps:
1. Create the database and the tables.
2. Load the data into the tables.
3. Generate the reports.

### Creating the database and the tables
The database with the following SQL commands:

```sql
CREATE DATABASE IF NOT EXISTS database_name;
USE database_name;
```
The tables are created in the database with pandas.

```sql
df.head(n=0).to_sql(table_name, con=engine, if_exists='replace', index=True)
```
This will create the table with the appropriate schema and columns. You can also specify the schema and columns in the following way:

```sql
df.head(n=0).to_sql(table_name, con=engine, if_exists='replace', index=True, schema='schema_name', dtype={'column_name': 'data_type'})
```

### Loading the data into the tables
The data is loaded into the tables with pandas.

```sql
df.to_sql(table_name, con=engine, if_exists='replace', index=True)
```

The data is loaded into a pandas dataframe. The dataframe is then converted to a PostgreSQL table. 
The following steps are performed on an dataframe database object:
1. Convert the dataframe to a PostgreSQL table.
2. Create a database connection.
3. Create a cursor.
4. Write the dataframe to the database.
5. Close the database connection.


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
