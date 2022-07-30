import json
import os

from database import Base, engine
from database import SessionLocal
from model import Country, Continent, Language, Currency


def insert_country(json_file, session):
    """Insert data from json file into the database.
    
    Args:
        json_file (str): path to json file
        session (SessionLocal): database session
        
        Returns:
            bool: True if data is inserted, False if data is not inserted
    """
    with open(json_file, encoding='utf-8') as json_file:
        data = json.load(json_file)
        for country in data:
            if session.query(Country).filter(Country.code == country).first():
                country_obj = session.query(Country).filter(Country.code == country).first()
                country_obj.name = data[country]['name']
                country_obj.native = data[country]['native']
                country_obj.phone = data[country]['phone']
                country_obj.continent = data[country]['continent']
                country_obj.capital = data[country]['capital']
                country_obj.languages = data[country]['languages']
                session.commit()
                print(f"Data updated in table: {Country.__tablename__}")
            else:
                country_obj = Country(
                    code=country,
                    name=data[country]['name'],
                    native=data[country]['native'],
                    phone=data[country]['phone'],
                    continent=data[country]['continent'],
                    capital=data[country]['capital'],
                    languages=data[country]['languages']
                )
                session.add(country_obj)
            session.add(country_obj)
        session.commit()
        print(f"Data inserted into table: {Country.__tablename__}")
        return True


def insert_continent(json_file, session):
    """Insert data from json file into the database

    Args:
        json_file (str): path to json file
        session (SessionLocal): database session

    Returns:
        bool: True if data is inserted, False if data is not inserted
    """
    with open(json_file, encoding='utf-8') as json_file:
        data = json.load(json_file)
        for continent in data:
            continent_obj = Continent(
                name=continent,
                code=data[continent]
            )
            session.add(continent_obj)
        session.commit()
        print(f"Data inserted into table: {Continent.__tablename__}")
        return True


def insert_language(json_file, session):
    """Insert data from json file into the database.
    
    Args:
        json_file (str): path to json file
        session (SessionLocal): database session
        
        Returns:
            bool: True if data is inserted, False if data is not inserted
    """
    with open(json_file, encoding='utf-8') as json_file:
        data = json.load(json_file)
        for language in data:
            # if code exists, update the language name and code instead of inserting a new language
            if session.query(Language).filter(Language.code == language).first():
                language_obj = session.query(Language).filter(Language.code == language).first()
                language_obj.name = data[language]['name']
                language_obj.code = data[language]['native']
            else:
                language_obj = Language(
                    name=data[language]['name'],
                    native=data[language]['native'],
                    code=language
                )
                session.add(language_obj)
        session.commit()
        print(f"Data updated in table: {Language.__tablename__}")
        return True


def insert_currency(json_file, session):
    """Insert data from json file into the database.
    
    Args:
        json_file (str): path to json file
        session (SessionLocal): database session
        
        Returns:
            bool: True if data is inserted, False if data is not inserted
        """
    with open(json_file, encoding='utf-8') as json_file:
        data = json.load(json_file)
        for currency in data:
            if session.query(Currency).filter(Currency.country_code == currency).first():
                currency_obj = session.query(Currency).filter(
                    Currency.country_code == currency).first()
                currency_obj.name = data[currency]['currency']
                currency_obj.country = data[currency]['name']
                session.commit()
                print(f"Data updated in table: {Currency.__tablename__}")
            else:
                currency_obj = Currency(
                    country_code=currency,
                    name=data[currency]['currency'],
                    country=data[currency]['name']
                )
                session.add(currency_obj)
            session.add(currency_obj)
        session.commit()
        print(f"Data inserted into table: {Currency.__tablename__}")
        return True


# create tables
def main():
# if __name__ == '__main__':
    """
    Create tables in the database and insert data from json files
    """
    # get .env file path
    base_path = os.path.abspath(__file__)
    dir_path = os.path.join(base_path, '../../data')

    countries = os.path.join(dir_path, 'countries.json')
    continents = os.path.join(dir_path, 'continents.json')
    languages = os.path.join(dir_path, 'languages.json')

    # create session
    session = SessionLocal()

    # drop tables if they exist
    Base.metadata.drop_all(engine)
    print(f"Dropped tables: {Base.metadata.tables.keys()}")

    # create tables
    print("Creating tables...")
    Base.metadata.create_all(engine)
    print(f"Created tables: {Base.metadata.tables.keys()}")

    # insert data into tables
    print("Inserting data into tables...")
    print("Inserting data into countries table...")
    insert_country(countries, session)
    print("Inserting data into currencies table...")
    insert_currency(countries, session)
    print("Inserting data into continents table...")
    insert_continent(continents, session)
    print("Inserting data into languages table...")
    insert_language(languages, session)

    # close session
    session.close()
    print("Session closed")
    print("Done!")

# parent working directory
