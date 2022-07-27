import os
import configparser
import sqlalchemy
from sqlalchemy.exc import DontWrapMixin

from sqlalchemy import create_engine


base = os.path.dirname(os.path.realpath(__file__)) + "../../dependencies"
config = configparser.ConfigParser()
config.read(base+'/env.cfg')

user = config.get('POSTGRES', 'POSTGRES_USER'),
password = config.get('POSTGRES', 'POSTGRES_PASSWORD'),
database = config.get('POSTGRES', 'POSTGRES_DB')


# connect to postgres database
def connect():
    """
    Connect to the PostgreSQL database
    """
    try:
        engine = create_engine(f'postgresql://{user}:{password}@localhost:5432/{database}')
        print("Database connection established successfully")
        return engine
    except (Exception, sqlalchemy.exc.DatabaseError) as error:
        print(f"Error: Unable to connect to the database {error}")

