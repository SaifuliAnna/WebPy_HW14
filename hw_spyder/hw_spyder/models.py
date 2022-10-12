from sqlalchemy import create_engine, Column, Table, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from sqlalchemy.orm import declarative_base, relationship

from scrapy.utils.project import get_project_settings

Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)


class AuthorToKey(Base):
    __tablename__ = "author_to_keywords"
    id = Column(Integer, primary_key=True)
    id_author = Column(Integer, ForeignKey('data_table.id', ondelete='CASCADE'), primary_key=True)
    id_keywords = Column(Integer, ForeignKey('data_keywords.id', ondelete='CASCADE'), primary_key=True)
    auth = relationship('AuthorData', back_populates="keyword_r")
    key = relationship('Keyword', back_populates="author_r")


class AuthorData(Base):
    __tablename__ = "data_table"
    id = Column(Integer, primary_key=True)
    author = Column('author', Text())
    quote = Column('quote', Text())
    about = Column('about', Text())
    keyword_r = relationship('AuthorToKey', back_populates='auth')


class Keyword(Base):
    __tablename__ = "data_keywords"
    id = Column(Integer, primary_key=True)
    keywords = Column('keywords', Text())
    author_r = relationship('AuthorToKey', back_populates='key')


class Details(Base):
    __tablename__ = "details_data"
    id = Column(Integer, primary_key=True)
    title = Column('title', Text())
    born_date = Column('born_date', Text())
    born_year = Column('born_year', Text())
    born_location = Column('born_location', Text())
    description = Column('description', Text())

