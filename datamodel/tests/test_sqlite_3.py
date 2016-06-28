import sqlite3
import pytest
from datamodel.nodes import db
from datamodel.nodes.quick.dbs import sqlite_3


def clean_test_db(filepath):
    open(filepath, 'wb').close()


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


def test_db_connection():
    conn = sqlite_3.Sqlite3Connection('database.db')
    assert isinstance(conn, db.FileDatabaseConnection)


def test_requirements():
    expected = ['db_connection', 'query']
    instance = sqlite_3.Sqlite3()
    assert instance.requirements == expected


def test_output():
    clean_test_db('database.db')
    query = '''CREATE TABLE COMPANY(
        ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);'''
    conn = sqlite_3.Sqlite3Connection('database.db')
    instance = sqlite_3.Sqlite3(db_connection=conn, query=query)
    instance.output()

    # Check
    tables = fetch_all_databases('database.db')
    assert len(tables) == 1
    assert tables[0][0] == 'COMPANY'


def test_data_writing():
    clean_test_db('database.db')

    # create schema
    query_create = '''CREATE TABLE COMPANY(
        ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);'''
    conn = sqlite_3.Sqlite3Connection('database.db')
    instance = sqlite_3.Sqlite3(db_connection=conn, query=query_create)
    instance.output()

    # insert data
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
    clean_test_db('database.db')

    # create schema
    query_create = '''CREATE TABLE COMPANY(
        ID INT PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        AGE            INT     NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);'''
    conn = sqlite_3.Sqlite3Connection('database.db')
    instance = sqlite_3.Sqlite3(db_connection=conn, query=query_create)
    instance.output()

    # insert data
    query_insert = '''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES
        (1, 'Paul', 32, 'California', 20000.00 );'''
    instance.reset()
    instance.input(dict(db_connection=conn, query=query_insert))
    instance.output()

    # modify data
    query_modify = '''UPDATE COMPANY SET ADDRESS = 'Texas' WHERE ID = 1;'''
    instance.reset()
    instance.input(dict(db_connection=conn, query=query_modify))
    instance.output()
    rows = fetch_all_rows('database.db')
    assert len(rows) == 1
    assert rows[0][3] == 'Texas'

    # delete data
    query_modify = '''DELETE FROM COMPANY;'''
    instance.reset()
    instance.input(dict(db_connection=conn, query=query_modify))
    instance.output()
    rows = fetch_all_rows('database.db')
    assert len(rows) == 0
