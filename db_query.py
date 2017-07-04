#_*_ coding:utf-8 _*_

import db_config
import sys
import warnings


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

# INSERT VALUES

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

# UPDATE ROW
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


# DELETE ROW

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

# ADD COlUMN IN THE TABLE

    def addColumn(self, *args):
        colname = args[0]
        cur = self.conn.cursor()
        cur.execute("ALTER TABLE StudentDetail ADD colname VARCHAR(15) ;")
        self.conn.commit()
        print "Column is added"

# DELETE COLUMN IN THE TABLE

    def deleteCol(self, *args):
        col_name = args[0]
        cur = self.conn.cursor()
        cur.execute("describe StudentDetail;")
        cur.execute("ALTER TABLE StudentDetail DROP COLUMN col_name;")
        self.conn.commit()
        print "Column is deleted"

# SHOW TABLES

    def listTable_mysql(self):
        self.conn = db_config.createdb_mysql()
        cur = self.db.cursor()
        cur.execute('SHOW TABLES')
        rows = cur.fetchall()
        for row in rows:
            print row

    def listTable_Postgresql(self):
        self.conn = db_config.creatdb_postgres()
        cur = self.conn.cursor()
        cur.execute(
            "SELECT * FROM information_schema.tables WHERE table_type = 'BASE TABLE' AND table_schema = 'public' ORDER BY table_type, table_name")
        rows = self.cur.fetchall()
        for row in rows:
            print row[2]

    def listTable_sqlite(self):
        self.conn = db_config.creatdb_sqlite()
        cur = self.conn.cursor()
        cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table'")
        rows = self.cur.fetchall()
        for row in rows:
            row


# SHOW DATABASE
def listDb(self):

    if self.db == '1':
        self.cur.execute('SHOW DATABASES')
        rows = self.cur.fetchall()
        for row in rows:
            print row
    elif self.db == '2':
        self.cur.execute('PRAGMA database_list;')
        rows = self.cur.fetchall()
        print rows
        for row in rows:
            print row[2]
    else:
        self.cur.execute(
            'SELECT datname FROM pg_database WHERE datistemplate = false;')
        rows = self.cur.fetchall()
        for row in rows:
            print row
