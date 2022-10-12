from sqlalchemy.orm import sessionmaker
# from hw_spyder.models import AuthorData, Keyword, Details, db_connect, create_table
from hw_spyder.models import AuthorToKey, AuthorData, Keyword, Details, db_connect, create_table


class HwSpyderPipeline(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        author_data = AuthorData()
        author_data.author = item["author"]
        author_data.quote = item["quote"]
        author_data.about = item["about"]

        try:
            session.add(author_data)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item


class HwSpyderPipelineKeyword(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        author_keyword = Keyword()
        author_keyword.keywords = item["keywords"]

        try:
            session.add(author_keyword)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item


# class HwSpyderPipelineAuthorToKey(object):
#
#     def __init__(self):
#         """
#         Initializes database connection and sessionmaker.
#         Creates deals table.
#         """
#         engine = db_connect()
#         create_table(engine)
#         self.Session = sessionmaker(bind=engine)
#
#     def process_item(self, item, spider):
#         """Save deals in the database.
#
#         This method is called for every item pipeline component.
#         """
#         session = self.Session()
#         author_to_keyword = AuthorToKey()
#         author_to_keyword.id_author = item["id_author"]
#         author_to_keyword.id_keywords = item["id_keywords"]
#
#         try:
#             session.add(author_to_keyword)
#             session.commit()
#         except:
#             session.rollback()
#             raise
#         finally:
#             session.close()
#
#         return item


class HwSpyderPipelineDetails(object):
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        details_data = Details()

        details_data.title = item["title"]
        details_data.born_date = item["born_date"]
        details_data.born_year = item["born_year"]
        details_data.born_location = item["born_location"]
        details_data.description = item["description"]

        try:
            session.add(details_data)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item