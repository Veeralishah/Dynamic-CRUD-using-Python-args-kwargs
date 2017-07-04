#-*- coding: utf8 -*-

import MySQLdb
import sqlite3
import psycopg2
import warnings

# CREATE THE DATABASE


# Mysql database
def createdb_mysql():
    con = MySQLdb.connect("localhost", "root", "Drc@1234", "Student")
    cursor = con.cursor()
    print "Connected with mysql database"
    return con

# Postgresql database
def creatdb_postgres():

    try:
        con = psycopg2.connect(database="testdb", user="postgres",
                               password="Drc@1234", host="127.0.0.1", port="5432")
        cursor = con.cursor()
        print "Connected with postgresql database"
        return con
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
        sys.exit(1)

# Sqlite database
def creatdb_sqlite():
    con = None
    try:
        con = sqlite3.connect('Student.db')
        cursor = con.cursor()
        print("Connected with sqlite database Student")
        return con
    except sqlite3.Error as e:
        print(e)


# try:
#         db = mdb.connect(host="localhost", user="root", passwd="Drc@1234")
#         db1 = db.cursor()
#         with warnings.catch_warnings():
#             warnings.simplefilter('ignore')
#             db1.execute('CREATE DATABASE IF NOT EXISTS StudentDetails')
#             print('Create Database StudentDetails')
#             cur = db.cursor()
#             cur.execute("SELECT VERSION()")
#             ver = cur.fetchone()
#             print "Database version : %s " % ver
#     except mdb.Error, e:
#         print "Error %d: %s" % (e.args[0], e.args[1])
#         sys.exit(1)
