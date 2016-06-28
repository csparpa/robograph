import sqlite3
from datamodel.nodes import db


class Sqlite3Connection(db.FileDatabaseConnection):
    """
    Connection object ti a SQLite3 database
    """
    def get_connection(self):
        return sqlite3.connect(self._filepath)


class Sqlite3(db.Database):
    """
    This node models a SQLite3 database
    """
    def output(self):
        if not isinstance(self._params['db_connection'], Sqlite3Connection):
            raise ValueError('Need a Sqlite3Connection object')
        conn = self._params['db_connection'].get_connection()
        try:
            with conn:
                conn.execute(self._params['query'])
        except sqlite3.IntegrityError as e:
            raise db.IntegrityException(e.message)


class Sqlite3Read(db.Database):
    pass