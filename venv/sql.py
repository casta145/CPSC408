import sqlite3

class Connection:

    #Creates a connection, checks if the database exists, and if not creates. If it does, returns to display menu
    @staticmethod
    def dbconnect():
        conn = sqlite3.connect("StudentDB.db")
        c = conn.cursor()

        c.execute("CREATE TABLE IF NOT EXISTS Student("
                  "StudentId INTEGER PRIMARY KEY AUTOINCREMENT,"
                  "FirstName varchar(25),"
                  "LastName varchar(25),"
                  "GPA REAL,"
                  "Major varchar(10),"
                  "FacultyAdvisor varchar(25));")
        conn.commit()
        return