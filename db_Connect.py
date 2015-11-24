#!/usr/bin/python

"""
db_connecet will help you to connect to different kinds of databases

"""
import os, sqlite3
class db:
    #create a test database variable
    db_filename = 'test.db'
    conn = sqlite3.connect(db_filename)

    def __init__(self):
        # TODO "Add more Databases"
        print("The following Database are supported")
        print("SQLLite3")

    def pHello(self):
        print("hello From db")

    def db_connect(db_name):
        conn = sqlite3.connect(db_name)
        return conn

    def is_db_new(db_name):
        db_is_new = not os.path.exists(db_name)
        db.db_connect(db_name)

        if db_is_new:
           return  print("Need to Create Schema")
        else:
           return print("Database exits, assume schema does, too.")


    def mkdb_table(self, conn):
        # This fuction Creates a table

        conn.execute('''CREATE TABLE COMPANY
            (ID INT PRIMARY KEY     NOT NULL,
            NAME            TEXT    NOT NULL,
            AGE             INT     NOT NULL,
            ADDRESS         CHAR(50),
            SALARY          REALL);''')
        print("Table created successfully")


    def db_insert(self, conn):

        # THIS FUNCTION ISTO INSERT INO A TABLE
        conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
             VALUES (1, 'paul',32,'California', 20000.00)");
        conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
             VALUES (2, 'Allen', 25,'Texas', 15000.00)");
        conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
             VALUES (3, 'Teddy',23,'Norway', 20000.00)");
        conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
             VALUES (4, 'Mark',25,'Rich-Mond', 65000.00)");
        conn.commit()
        print("Records created successfully")


    def db_print(self,conn):
        # Prints out the db "test.db"

        cursor = conn.execute("SELECT ID, NAME, ADDRESS, SALARY from COMPANY")
        for row in cursor:
            print("ID= ", row[0])
            print("NAME= ", row[1])
            print("ADDRESS= ", row[2])
            print("SALARY= ", row[3]), "\n"
            print("Opertation done Successfully")

    def db_update(self, conn):

        # Update a row in a table
        conn.execute("UPDATE COMPANY set SALARY  = 25000.00 where ID=1")
        conn.commit()
        print("Total number of rows updated :", conn.total_changes)

        cursor = conn.execute("SELECT ID, NAME, ADDRESS, SALARY from COMPANY")
        for row in cursor:
            print("ID= ", row[0])
            print("NAME= ", row[1])
            print("ADDRESS= ", row[2])
            print("SALARY= ", row[3]), "\n"
        print("Opertation done Successfully")

    def del_from_db(self,conn):

        conn.execute("DELETE from COMPANY where ID=2")
        conn.commit()
        print("Total number of rows deleted :", conn.total_changes)

        cursor = conn.execute("SELECT ID, NAME, ADDRESS, SALARY from COMPANY")
        for row in cursor:
            print("ID= ", row[0])
            print("NAME= ", row[1])
            print("ADDRESS= ", row[2])
            print("SALARY= ", row[3]), "\n"
        print("Opertation done Successfully")
