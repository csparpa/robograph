from datamodel.base import node


class UnsupportedDatabaseException(Exception):
    """
    This exception marks the fact that support for a DB is not yet operational.
    """
    pass


class IntegrityException(Exception):
    """
    This exception marks attempts to jeopardise the integrity of the database
    """
    pass


class DatabaseConnection:
    """
    Abstract parent class for DB connections
    """
    def __init__(self):
        pass

    def get_connection(self):
        pass


class FileDatabaseConnection(DatabaseConnection):
    """
    This class abstracts a connection to a DB server
    """

    def __init__(self, filepath):
        DatabaseConnection.__init__(self)
        self._filepath = filepath


class ServerDatabaseConnection(DatabaseConnection):
    """
    This class abstracts a connection to a DB server
    """

    def __init__(self, host, port, username, password, db_name):
        DatabaseConnection.__init__(self)
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._db_name = db_name


class Database(node.Node):
    """
    Abstract parent node for Databases.
    Requirements:
      db_connection --> instance of a datamodel.db.DatabaseConnection subclass
      query --> the query you want to run on the database
    Eg:
      Database(db_connection=conn, query='SELECT * from my_table')
    """

    _reqs = ['db_connection', 'query']

