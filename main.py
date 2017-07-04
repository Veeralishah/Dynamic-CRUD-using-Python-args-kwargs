#_*_ coding:utf-8 _*_

import db_query

# Menu driven of front hand for CURD operation in Databases


def addTable():
    obj.createTable()


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
        pass


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
        pass


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
        pass


def option():
    print "1. Create Database"
    print "2. Show Tables"
    print "3  Show Database "
    print "4  Create Table"
    print "5. Read Data"
    print "6. Insert Data"
    print "7. Update Data"
    print "8. Delete Data"
    print "9. Add New Column"
    print "10  Delete Existing Column"
    print "11  Delete Table "
    print "12. Quit"

    user_input = raw_input("Which operations you want to perform?")
    if user_input == "1":
        addDB()
        option()
    elif user_input == "2":
        listTable()
        option()
    elif user_input == "3":
        listDb()
        option()
    elif user_input == "4":
        addTable()
        option()
    elif user_input == "5":
        obj.retrieveTable()
        option()
    elif user_input == "6":
        insertTable()
        option()
    elif user_input == "7":
        updateRow()
        option()
    elif user_input == "8":
        deleteRow()
        option()
    elif user_input == "9":
        addColumn()
        option()
    elif user_input == "10":
        deleteCol()
        option()
    elif user_input == "11":
        deleteTable()
        option()
    else:
        print "Please Enter Valid Input"

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
