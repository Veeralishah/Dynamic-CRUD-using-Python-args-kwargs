#_*_ coding:utf-8 _*_

import db_config
import sqlite3
import sys
import warnings
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Base File that contain class for CURD operation in Database


class DBwrapper:
    con = 0

    def __init__(self, user):
        if user == "1":
            self.conn = db_config.createdb_mysql()
        elif user == "2":
            self.conn = db_config.creatdb_postgres()
        elif user == "3":
            self.conn = db_config.creatdb_sqlite()

# CREATE A NEW TABLE

    def createTable(self):
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            warnings.filterwarnings('ignore', 'unknown table')
            cur = self.conn.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS StudentDetail (sid INT NOT NULL, sname VARCHAR(25) NOT NULL, sage INT, scourse TEXT, scity TEXT)")
            print 'Student Details Table created'
            self.conn.commit()

# INSERT TABLE ROW VALUES

    def insertTable(self, *args):
        cur = self.conn.cursor()
        Id = args[0]
        name = args[1]
        age = args[2]
        course = args[3]
        city = args[4]
        cur.execute("""INSERT INTO StudentDetail VALUES (%s, '%s', %s, '%s', '%s');""" % (
            Id, name, age, course, city))
        print "Record Inserted"
        self.conn.commit()

# RETRIEVE TABLE ROWS

    def retrieveTable(self, *args):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM StudentDetail")
        rows = cur.fetchall()
        if len(rows) == 0:
            print "No records found"
        else:
            print rows

# UPDATE TABLE ROW

    def updateRow(self, *args):
        cur = self.conn.cursor()
        u_id = args[0]
        name = args[1]
        age = args[2]
        course = args[3]
        city = args[4]

        cur.execute("UPDATE StudentDetail SET sname = %s, sage = %s, scourse = %s, scity = %s WHERE sid = %s",
                    (name, age, course, city, u_id))
        print "Number of rows updated:",  cur.rowcount
        self.conn.commit()
        if cur.rowcount == 0:
            print 'Record Not Updated'


# DELETE TABLE ROW

    def deleteRow(self, *args):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM StudentDetail")
        rows = cur.fetchall()
        print rows
        no = raw_input("Enter ID for Delete Record")
        try:
            cur.execute("DELETE FROM StudentDetail WHERE sid = %s", (no,))
            print "Record deleted", cur.rowcount
        except Exception as e:
            print "Record with the given id not found"

# CREATE DATABASE

    def addDb_mysql(self):
        self.conn = db_config.createdb_mysql()
        cur = self.conn.cursor()
        name = raw_input("Enter Name For Databse")
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            cur.execute("SET sql_notes = 0; ")
            cur.execute("CREATE DATABASE IF NOT EXISTS " + name + ";")
            print "Database Created Successfully"
            self.conn.commit()

    def addDb_postgresql(self):
        cur = self.conn.cursor()
        name = raw_input("Enter Name For Databse")
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur.execute('CREATE DATABASE ' + name)
        print "Database Created Successfully"
        self.conn.commit()

    def addDb_sqlite(self):
        self.conn = db_config.createdb_sqlite()
        name_db = raw_input("Enter Name For Databse")
        try:
            sqlite3.connect(name_db + '.db')
            print "Database Created Successfully"
            self.conn.commit()
        except Exception as e:
            print e


# ADD COlUMN IN THE TABLE

    def addColumn(self, *args):
        colname = args[0]
        cur = self.conn.cursor()
        cur.execute("ALTER TABLE StudentDetail ADD COLUMN " +
                    args[0] + " VARCHAR(15) ;")
        self.conn.commit()
        print "Column is added"

# DELETE COLUMN IN THE TABLE

    def deleteCol(self, *args):
        col_name = args[0]
        cur = self.conn.cursor()
        cur.execute("ALTER TABLE StudentDetail DROP COLUMN " + args[0])
        self.conn.commit()
        print "Column is deleted"

# DELETE TABLE FROM DATABASE

    def deleteTable(self, *args):
        cur = self.conn.cursor()
        tbname = args[0]
        cur.execute("DROP TABLE " + args[0])
        self.conn.commit()
        print "table is deleted"

# SHOW TABLES

    def listTable_mysql(self):
        self.conn = db_config.createdb_mysql()
        cur = self.conn.cursor()
        cur.execute('SHOW TABLES')
        rows = cur.fetchall()
        for row in rows:
            print row

    def listTable_Postgresql(self):
        self.conn = db_config.creatdb_postgres()
        cur = self.conn.cursor()
        cur.execute(
            "SELECT * FROM information_schema.tables WHERE table_type = 'BASE TABLE' AND table_schema = 'public' ORDER BY table_type, table_name")
        rows = cur.fetchall()
        for row in rows:
            print row[2]

    def listTable_sqlite(self):
        self.conn = db_config.creatdb_sqlite()
        cur = self.conn.cursor()
        cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table'")
        rows = cur.fetchall()
        for row in rows:
            print row


# SHOW DATABASE

    def listDb_mysql(self):
        self.conn = db_config.createdb_mysql()
        cur = self.conn.cursor()
        cur.execute('SHOW DATABASES')
        rows = cur.fetchall()
        for row in rows:
            print row

    def listDb_Postgresql(self):
        self.conn = db_config.creatdb_postgres()
        cur = self.conn.cursor()
        cur.execute(
            'SELECT datname FROM pg_database WHERE datistemplate = false;')
        rows = cur.fetchall()
        for row in rows:
            print row

    def listDb_sqlite(self):
        self.conn = db_config.creatdb_sqlite()
        cur = self.conn.cursor()
        cur.execute('PRAGMA database_list;')
        rows = cur.fetchall()
        for row in rows:
            print row
            print "SQLite can not show All Databases using Python"
