#!/usr/bin/python
#_*_ coding:utf-8 _*_

import db_query
import sys


# Menu driven of front hand for CURD operation in Databases


def addTable():
    obj.createTable()

def cTable():
    tbl_name = raw_input("Enter Table Name")
    col_count = int(raw_input("Enter No of Columns"))

    i = 0
    if i == col_count:
        sys.exit(1)
    else:
        col = ""
        for i in range(col_count):
            col_name = raw_input("Enter Col name")
            col_type = raw_input("Enter Column Type")
            col = col + str(col_name) + " " + str(col_type) + ", "
    col = col[:-2]
    print col
    obj.createTable(tbl_name,col)


def insertTable():
    Id = input("Enter Your ID")
    name = raw_input("Enter Your Name ")
    age = raw_input("Enter Your Age")
    course = raw_input("Enter Your Course")
    city = raw_input("Enter Your City")
    obj.insertTable(Id, name, age, course, city)


def updateRow():
    u_id = raw_input('Enter id For Update record')
    name = raw_input("Enter Your Name For Update record")
    age = raw_input("Enter Your Age For Update record")
    course = raw_input("Enter Your Course For Update record")
    city = raw_input("Enter Your City For Update record")
    obj.updateRow(u_id, name, age, course, city)


def deleteRow():
    no = raw_input("Enter Id for Delete Record")
    obj.deleteRow(no)


def addColumn():
    colname = raw_input("Enter Name Of Column for Add")
    obj.addColumn(colname)


def deleteCol():
    col_name = raw_input("Enter Name of Column for Delete")
    obj.deleteCol(col_name)


def deleteTable():
    tbname = raw_input("Enter Name of Table for Delete")
    obj.deleteTable(tbname)


def listTable():
    print "1. MYSQL"
    print "2. PostgreSQL"
    print "3. Sqlite"
    name_db = raw_input("Select Database for Show Tables")
    if name_db == "1":
        obj.listTable_mysql()
    elif name_db == "2":
        obj.listTable_Postgresql()
    elif name_db == "3":
        obj.listTable_sqlite()
    else:
        print("Please Enter Valid Input")
        sys.exit(1)


def listDb():
    print "1. MYSQL"
    print "2. PostgreSQL"
    print "3. Sqlite"
    name_db = raw_input("Select Database for Show Databases")
    if name_db == "1":
        obj.listDb_mysql()
    elif name_db == "2":
        obj.listDb_Postgresql()
    elif name_db == "3":
        obj.listDb_sqlite()
    else:
        print("Please Enter Valid Input")
        sys.exit(1)


def addDB():
    print "1. MYSQL"
    print "2. PostgreSQL"
    print "3. Sqlite"
    u_db = raw_input("Select Database for Create Database")
    if u_db == "1":
        obj.addDb_mysql()
    elif u_db == "2":
        obj.addDb_postgresql()
    elif u_db == "3":
        obj.addDb_sqlite()
    else:
        print("Please Enter Valid Input")
        sys.exit(1)


def option():
    print "1  Create Table of Your Choice"
    print "2. Create Database"
    print "3. Show Tables"
    print "4  Show Database "
    print "5  Create Table"
    print "6. Read Data"
    print "7. Insert Data"
    print "8. Update Data"
    print "9. Delete Data"
    print "10. Add New Column"
    print "11  Delete Existing Column"
    print "12  Delete Table"
    print "13. Quit"

    user_input = raw_input("Which operations you want to perform?")
    if user_input == "1":
        cTable()
        option()
    elif user_input == "2":
        addDB()
        option()
    elif user_input == "3":
        listTable()
        option()
    elif user_input == "4":
        listDb()
        option()
    elif user_input == "5":
        addTable()
        option()
    elif user_input == "6":
        obj.retrieveTable()
        option()
    elif user_input == "7":
        insertTable()
        option()
    elif user_input == "8":
        updateRow()
        option()
    elif user_input == "9":
        deleteRow()
        option()
    elif user_input == "10":
        addColumn()
        option()
    elif user_input == "11":
        deleteCol()
        option()
    elif user_input == "12":
        deleteTable()
        option()
    elif user_input == "13":
        sys.exit(1)
    else:
        print "Please Enter Valid Input"
        sys.exit(1)

# Main Function .. Execution Start
def choice():
    print "Select Database:"
    print "1. MYSQL Database"
    print "2. PostgreSQL Database"
    print "3. Sqlite Databse"
    print "4. Exit"

    user = raw_input("Which database you want to access?")
    if user == "4":
        sys.exit(1)
    elif user:
        global obj
        obj = db_query.DBwrapper(user)
        option()

choice()
