import sqlite3
import pytest
from datamodel.nodes import db
from datamodel.nodes.quick.dbs import sqlite_3


DBFILE = 'datamodel/tests/database.db'


# Utilities

def clean_test_db(filepath):
    open(filepath, 'wb').close()


def create_test_database(filepath):
    conn = sqlite3.connect(filepath)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE COMPANY(
        ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);''')


def fetch_all_databases(filepath):
    conn = sqlite3.connect(filepath)
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return cur.fetchall()


def fetch_all_rows(filepath):
    conn = sqlite3.connect(filepath)
    cur = conn.cursor()
    cur.execute("SELECT * FROM COMPANY;")
    return cur.fetchall()


def insert_a_row(filepath, pk):
    conn = sqlite3.connect(filepath)
    cur = conn.cursor()
    cur.execute('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES
        (%d, 'Paul', 32, 'California', 20000.00 );''' % (pk,))
    conn.commit()


# Tests


def test_requirements():
    instance = sqlite_3.Sqlite3Writer()
    assert instance.requirements == ['db_connection', 'query']
    instance = sqlite_3.Sqlite3BulkWriter()
    assert instance.requirements == ['db_connection', 'query', 'parameters']


def test_output():
    clean_test_db(DBFILE)
    query = '''CREATE TABLE COMPANY(
        ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);'''
    conn = sqlite_3.Sqlite3Connection(DBFILE)
    instance = sqlite_3.Sqlite3Writer(db_connection=conn, query=query)
    instance.output()

    # Check
    tables = fetch_all_databases(DBFILE)
    assert len(tables) == 1
    assert tables[0][0] == 'COMPANY'


def test_data_creation():
    clean_test_db(DBFILE)
    create_test_database(DBFILE)

    # insert data
    instance = sqlite_3.Sqlite3Writer()
    conn = sqlite_3.Sqlite3Connection(DBFILE)
    query_insert = '''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES
        (1, 'Paul', 32, 'California', 20000.00 );'''
    instance.reset()
    instance.input(dict(db_connection=conn, query=query_insert))
    instance.output()

    # try to insert again the same PK and get an error
    instance.reset()
    instance.input(dict(db_connection=conn, query=query_insert))
    with pytest.raises(db.IntegrityException):
        instance.output()


def test_data_modification():
    clean_test_db(DBFILE)
    create_test_database(DBFILE)

    # insert data
    conn = sqlite_3.Sqlite3Connection(DBFILE)
    instance = sqlite_3.Sqlite3Writer()
    query_insert = '''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES
        (1, 'Paul', 32, 'California', 20000.00 );'''
    instance.input(dict(db_connection=conn, query=query_insert))
    instance.output()

    # modify data
    query_modify = '''UPDATE COMPANY SET ADDRESS = 'Texas' WHERE ID = 1;'''
    instance.reset()
    instance.input(dict(db_connection=conn, query=query_modify))
    instance.output()
    rows = fetch_all_rows(DBFILE)
    assert len(rows) == 1
    assert rows[0][3] == 'Texas'

    # delete data
    query_modify = '''DELETE FROM COMPANY;'''
    instance.reset()
    instance.input(dict(db_connection=conn, query=query_modify))
    instance.output()
    rows = fetch_all_rows(DBFILE)
    assert len(rows) == 0


def test_data_read():
    clean_test_db(DBFILE)
    create_test_database(DBFILE)
    insert_a_row(DBFILE, 1)
    insert_a_row(DBFILE, 2)
    insert_a_row(DBFILE, 3)

    expected_result = [(1, 'Paul', 32, 'California', 20000.00),
                       (2, 'Paul', 32, 'California', 20000.00),
                       (3, 'Paul', 32, 'California', 20000.00)]
    query_read = '''SELECT * FROM COMPANY;'''
    conn = sqlite_3.Sqlite3Connection(DBFILE)
    instance = sqlite_3.Sqlite3Reader(db_connection=conn, query=query_read)
    result = instance.output()
    assert len(result) == 3
    assert result == expected_result


def test_data_bulk_write():
    clean_test_db(DBFILE)
    create_test_database(DBFILE)

    rows = fetch_all_rows(DBFILE)
    assert len(rows) == 0

    query_insert = '''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES
        (?, ?, ?, ?, ?);'''
    parameters = [
        (1, 'Paul', 32, 'California', 20000.00),
        (2, 'Mark', 25, 'Florida', 10000.00),
        (3, 'Tom', 48, 'Utah', 60000.00)]

    conn = sqlite_3.Sqlite3Connection(DBFILE)
    instance = sqlite_3.Sqlite3BulkWriter(db_connection=conn,
                                          query=query_insert,
                                          parameters=parameters)
    instance.output()

    rows = fetch_all_rows(DBFILE)
    assert len(rows) == 3