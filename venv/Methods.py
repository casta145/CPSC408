import sys
import sqlite3
from Student import Student

class Methods:

    #Checks if the student you are looking for to update is in the database
    def validatenum(idnum):
        c.execute("SELECT StudentID FROM Student WHERE StudentId = " + str(idnum))
        check = c.fetchall()
        if check == []:
            print("Student does not exist in the Database")
            return False
        else:
            return True

    #Displays the Data in the Database
    @staticmethod
    def displayinfo():
        c.execute("SELECT * FROM Student")
        table = c.fetchall()
        for x in table:
            print(x)
        return

    #Creates a new entry for the database
    @staticmethod
    def newentry():
        try:
            print("Enter First Name:")
            first = input()
            print("Enter Last Name:")
            last = input()
            print("Enter GPA:")
            gpa = float(input())
            print("Enter Major:")
            major = input()
            print("Enter Faculty Advisor:")
            advisor = input()
            stu = Student(first, last, gpa, major, advisor)
            c.execute("INSERT INTO Student('FirstName', 'LastName', 'GPA', 'Major', 'FacultyAdvisor')"
                    "VALUES (?,?,?,?,?)", stu.getStudentTuple())
            conn.commit()
            print("Entry Successfully Created")
            return
        except ValueError:
            print("One or more of your inputs are invalid. Please Try Again...")
            Methods.newentry()

    #Updates the major, advisor, or both of a student by searching their ID
    @staticmethod
    def updateinfo():
        try:
            print("Enter if you like to update the Major, the Advisor, or Both?")
            print("(Type 'Quit' to exit)")
            ans = input().lower()
            if ans == 'quit':
                return
            elif ans == 'major':
                print("Enter the the Students ID:")
                idnum = int(input())
                print("Enter new Major:")
                newmajor = input()
                c.execute("UPDATE Student SET Major = ? WHERE StudentId = ?", (newmajor, idnum))
                conn.commit()
                print("Update Successful!\n")
                return
            elif ans == 'advisor':
                print("Enter the the Students ID:")
                idnum = int(input())
                print("Enter the new Advisor:")
                newadvisor = input()
                c.execute("UPDATE Student SET FacultyAdvisor = ? WHERE StudentId = ?", (newadvisor,idnum))
                conn.commit()
                print("Update Successful!\n")
                return
            elif ans == 'both':
                print("Enter the the Students ID:")
                idnum = int(input())
                print("Enter the new Major:")
                newmajor = input()
                print("Enter the new Advisor:")
                newadvisor = input()
                c.execute("UPDATE Student SET Major = ?, FacultyAdvisor = ? WHERE StudentId = ?", (newmajor,newadvisor,idnum))
                conn.commit()
                print("Update Successful!\n")
                return
            else:
                print("An Error occured... Please try Again\n")
                Methods.updateinfo()
        except Exception:
            print("An Error...Please try Again\n")
            Methods.updateinfo()

    #Deletes student from database by their student ID
    @staticmethod
    def delentry():
        try:
            print("Enter ID of Student you would like to delete")
            print("(or 0 to exit)")
            idnum = int(input())
            if idnum == 0:
                return
            elif validatenum(idnum):
                c.execute("DELETE FROM Student WHERE StudentId = {};".format(idnum))
                conn.commit()
                print("Deletion Successful!\n")
                return
            else:
                Methods.delentry()
        except Exception:
            print("An Error occured... Please try again\n")
            Methods.delentry()

    #searches database for students with common Major, GPA, or Advisor and prints it out
    @staticmethod
    def search():
        print("Search by Major, GPA, or Advisor")
        print("Enter your search attribute:")
        print("(or type 'quit' to exit)")
        att = input().lower()
        if att == 'quit':
            return
        elif att == 'major': #check if major exists
            print("Enter the major to search:")
            major = input().lower()
            c.execute('SELECT * FROM Student WHERE LOWER(Major) = ? ', (major,))
            table = c.fetchall()
            for x in table:
                print(x)
            return
        elif att == 'gpa': #check if gpa exists
            print("Enter the gpa to search:")
            gpa = float(input())
            c.execute('SELECT * FROM Student WHERE GPA = ?', (gpa,))
            table = c.fetchall()
            for x in table:
                print(x)
            return
        elif att == 'advisor': #check if advisor exists
            print("Enter the advisor to search:")
            advisor = input().lower()
            c.execute('SELECT * FROM Student WHERE LOWER(FacultyAdvisor) = ?', (advisor,))
            table = c.fetchall()
            for x in table:
                print(x)
            return
        else:
            print('An Error Occured... Please try again.\n')
            Methods.search()

    def exit(self):
        print("Have a Nice Day!")
        print("Goodbye!\n")
        conn.close()
        sys.exit()

conn = sqlite3.connect("StudentDB.db")
c = conn.cursor()