from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY

from database import Base


class Country(Base):
    """Create the tables for the database """
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    name = Column(String, unique=True, index=True)
    native = Column(String, unique=True, index=True)
    phone = Column(ARRAY(String), index=True)
    continent = Column(String, index=True)
    capital = Column(String, index=True)
    languages = Column(ARRAY(String), index=True)

    def __repr__(self):
        return f"<Country(code={self.code}, name={self.name}, native={self.native}, phone={self.phone}, continent={self.continent}, capital={self.capital}, languages={self.languages})"


class Continent(Base):
    """Create the continents' table for the database """
    __tablename__ = 'continents'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    code = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"<Continent(name='{self.name}', code='{self.code}')>"


class Language(Base):
    """Create the languages' table for the database """
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    native = Column(String, unique=True, index=True)
    code = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"<Language(name='{self.name}', native='{self.native}', code='{self.code}')>"


class Currency(Base):
    """Create the currencies' table for the database """
    __tablename__ = 'currencies'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(ARRAY(String), index=True)
    country_code = Column(String, unique=True, index=True)
    country = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"<Currency(name='{self.name}', country_code='{self.country_code}', country='{self.country}')>"
