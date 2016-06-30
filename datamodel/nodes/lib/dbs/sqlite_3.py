import sqlite3

from datamodel.nodes.lib import db


class Sqlite3Connection(db.FileDatabaseConnection):
    """
    Connection object ti a SQLite3 database
    """
    def get_connection(self):
        return sqlite3.connect(self._filepath)


class Sqlite3Writer(db.Database):
    """
    This node performs one single write operation on a SQLite3 database
    """

    def output(self):
        conn = self._params['db_connection'].get_connection()
        try:
            with conn:
                conn.execute(self._params['query'])
        except sqlite3.IntegrityError as e:
            raise db.IntegrityException(e.message)


class Sqlite3BulkWriter(db.Database):
    """
    This node performs multiple times the same write operation on a SQLite3 database
    Requirements:
      parameters --> list of tuples, the parameters to be feed into the statements
    Eg:
      Sqlite3BulkWriter(db_connection=conn,
        query="INSERT INTO users (user, password) VALUES (?, ?)",
        parameters=[("Laura", "xyz"), ("Tom", "abc")])
    """
    _reqs = db.Database._reqs + ['parameters']

    def output(self):
        conn = self._params['db_connection'].get_connection()
        try:
            with conn:
                conn.executemany(self._params['query'], self._params['parameters'])
        except sqlite3.IntegrityError as e:
            raise db.IntegrityException(e.message)


class Sqlite3Reader(db.Database):
    """
    This node performs one single read operation on a SQLite3 database. The
    output is a list of tuples.
    """

    def output(self):
        conn = self._params['db_connection'].get_connection()
        try:
            with conn:
                cur = conn.cursor()
                cur.execute(self._params['query'])
                return cur.fetchall()
        except sqlite3.IntegrityError as e:
            raise db.IntegrityException(e.message)
