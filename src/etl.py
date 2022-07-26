import os
import json
import pandas as pd

from dependencies.db import connect

data = os.path.dirname(os.path.realpath(__file__)) + "/data"

# dataframe for continents
df_continent = pd.read_json(data + '/continents.json', orient='index')

# dataframe for languages
df_lang = pd.read_json(data + '/languages.json', orient='index')
df_lang.drop(columns=['rtl'], inplace=True)

# dataframe for countries
df_country = pd.read_json(data + '/countries.json', orient='index')
df_country.drop(columns=['continents'], inplace=True)

# dataframe for countries2to3
df_country_code = pd.read_json(data + '/countries.2to3.json', orient='index')


def create_insert_table():
    """
    Create tables for continents, languages, countries, countries2to3, countries3to2
    """
    engine = connect()
    conn = engine.connect()
    with engine.connect() as conn:
        # continents table
        df_continent.head(n=0).to_sql('continents', con=conn,
                                      if_exists='append', index=True)
        df_continent.to_sql('continents', con=conn,
                            if_exists='append', index=True)

        # languages table
        df_lang.head(n=0).to_sql('languages', con=conn,
                                 if_exists='append', index=True)
        df_lang.to_sql('languages', con=conn,
                       if_exists='append', index=True)

        # countries table
        df_country.head(n=0).to_sql('countries', con=conn,
                                    if_exists='append', index=True)
        df_country.to_sql('countries', con=conn,
                          if_exists='append', index=True)

        # countries2to3 table
        df_country_code.head(n=0).to_sql('countries2to3', con=conn,
                                         if_exists='append', index=True)
        df_country_code.to_sql('countries2to3', con=conn,
                               if_exists='append', index=True)
        print("Tables created successfully")
        conn.close()
        engine.dispose()
        return conn


def main():
    """	Connect to the PostgresSQL database, run queries, and close connection """
    create_insert_table()


if __name__ == "__main__":
    main()
