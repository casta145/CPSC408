import sqlite3

class Connection:

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