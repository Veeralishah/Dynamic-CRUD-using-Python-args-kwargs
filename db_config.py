#!/usr/bin/python
# -*- coding: utf-8 -*-

# Configuration File to Connect Databases


import MySQLdb
import sqlite3
import psycopg2
import warnings
import sys

# Mysql database


def createdb_mysql():
    try:
        con = MySQLdb.connect("localhost", "USER", "PASSWORD", "Student")
        cursor = con.cursor()
        cursor.execute("SELECT VERSION()")
        ver = cursor.fetchone()
        print "Database version : %s " % ver
        print "Connected with MYSQL DB"
        return con
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

# Postgresql database


def creatdb_postgres():

    try:
        con = psycopg2.connect(database="testdb", user="USER",
                               password="PASSWORD", host="127.0.0.1", port="5432")
        cursor = con.cursor()
        cursor.execute('SELECT version()')
        ver = cursor.fetchone()
        print "Database version : %s " % ver
        print "Connected with PostgreSQL DB"
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
        cursor.execute('SELECT SQLITE_VERSION()')
        data = cursor.fetchone()
        print "SQLite version: %s" % data
        print("Connected with sqlite database Student")
        return con
    except sqlite3.Error as e:
        print(e)
