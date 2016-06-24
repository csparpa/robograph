from datamodel.base import node


class UnsupportedDatabaseException(Exception):
    """
    This exception marks the fact that support for a DB is not yet operational.
    """
    pass


class DatabaseConnection:
    """
    Abstract parent class for DB connections
    """
    def get_connection(self):
        pass


class FileDatabaseConnection(DatabaseConnection):
    """
    This class abstracts a connection to a DB server
    """

    def __init__(self, filepath):
        DatabaseConnection.__init__()
        self._filepath = filepath


class ServerDatabaseConnection(DatabaseConnection):
    """
    This class abstracts a connection to a DB server
    """

    def __init__(self, host, port, username, password):
        DatabaseConnection.__init__()
        self._host = host
        self._port = port
        self._username = username
        self._password = password


class Database(node.Node):
    """
    Abstract parent node for Databases.
    Requirements:
      db_connection --> instance of a datamodel.db.DatabaseConnection subclass
      db_name --> name of the database
      query --> the query you want to run on the database
    Eg:
      Database(db_connection=conn, db_name='my_db', query='SELECT * from my_table')
    """

    _reqs = ['db_connection', 'db_name', 'query']

    def output(self):
        pass

