import sqlite3
import sys
from Methods import Methods
from Student import Student

def display():
    print("What would you like to do:\n")
    print("1) Display Information")
    print("2) Create an Entry")
    print("3) Update Information")
    print("4) Delete an Entry")
    print("5) Search by Major, GPA, or Advisor")
    print("6) Exit")
    choice = int(input("(Enter a Number)\n"))
    print("\n")
    try:
        if choice in range(1, 7):
            if choice == 1:
                Methods.displayinfo()
            elif choice == 2:
                Methods.newentry()
            elif choice == 3:
                Methods.updateinfo()
            elif choice == 4:
                Methods.delentry()
            elif choice == 5:
                Methods.search()
            elif choice == 6:
                print("Have a Nice Day!")
                print("Goodbye!\n")
                conn.close()
                sys.exit()
            else:
                print("Input Choice Error\n")
        else:
            print("Please Enter a Valid Number (1-6)")
            display()
    except ValueError:
        print("Input Invalid... Please Try Again")
        display()

conn = sqlite3.connect("StudentDB.db")
c = conn.cursor()

c.execute ("CREATE TABLE IF NOT EXISTS Student("
           "StudentId INTEGER PRIMARY KEY AUTOINCREMENT,"
           "FirstName varchar(25),"
           "LastName varchar(25),"
           "GPA REAL," 
           "Major varchar(10),"
           "FacultyAdvisor varchar(25));")
conn.commit()

while True:
    display()