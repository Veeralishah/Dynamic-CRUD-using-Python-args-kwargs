#_*_ coding:utf-8 _*_

import db_query


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

def  deleteCol():
    col_name = raw_input("Enter Name of Column for Delete")
    obj.deleteCol(col_name)

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
        pass



def option():
    print "1. Insert Data"
    print "2. Read Data"
    print "3. Update Data"
    print "4. Delete Data"
    print "5. Add Column"
    print "6  Delete Column"
    print "7. Show Tables"
    print "8  Show Database "
    print "9  Delete Table "
    print "10.Quit"

    user_input = raw_input("Which operations you want to perform?")
    if user_input == "1":
        insertTable()
        option()
    elif user_input == "2":
        obj.retrieveTable()
        option()
    elif user_input == "3":
        updateRow()
        option()
    elif user_input == "4":
        deleteRow()
        option()
    elif user_input == "5":
        addColumn()
        option()
    elif user_input == "6":
         deleteCol()
         option()
    elif user_input == "7":
        listTable()
        option()
    elif user_input == "8":
        obj.listDb()
        option()
    else:
        pass


def choice():
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
        obj.createTable()
        option()

choice()
