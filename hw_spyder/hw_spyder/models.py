from sqlalchemy import create_engine, Column, Table, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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


association_table = Table(
    "association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("data_table_id", Integer, ForeignKey("data_table.id"), primary_key=True),
    Column("data_keywords_id", Integer, ForeignKey("data_keywords.id"), primary_key=True)
)


class AuthorData(Base):
    __tablename__ = "data_table"
    id = Column(Integer, primary_key=True)
    author = Column('author', Text())
    quote = Column('quote', Text())
    about = Column('about', Text())
    keyword = relationship('Keyword', secondary=association_table, back_populates="quotes")


class Keyword(Base):
    __tablename__ = "data_keywords"
    id = Column(Integer, primary_key=True)
    keywords = Column('keywords', Text())
    quotes = relationship("AuthorData", secondary=association_table, back_populates="keyword")


class Details(Base):
    __tablename__ = "details_data"
    id = Column(Integer, primary_key=True)
    title = Column('title', Text())
    born_date = Column('born_date', Text())
    born_year = Column('born_year', Text())
    born_location = Column('born_location', Text())
    description = Column('description', Text())
