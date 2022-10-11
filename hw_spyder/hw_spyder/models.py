from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, SmallInteger, String, Text

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class AuthorData(DeclarativeBase):
    __tablename__ = "data_table"

    id = Column(Integer, primary_key=True)
    author = Column('author', Text())
    quote = Column('quote', Text())
    keywords = Column('keywords', Text())
    about = Column('about', Text())


class Details(DeclarativeBase):
    __tablename__ = "details_data"
    id = Column(Integer, primary_key=True)
    title = Column('title', Text())
    born_date = Column('born_date', Text())
    born_year = Column('born_year', Text())
    born_location = Column('born_location', Text())
    description = Column('description', Text())

