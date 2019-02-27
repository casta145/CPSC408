import sqlite3
from Methods import Methods

class Menu:

    @staticmethod
    def display():
        print("What would you like to do:\n")
        print("1) Display Information")
        print("2) Create an Entry")
        print("3) Update Information")
        print("4) Delete an Entry")
        print("5) Search by Major, GPA, or Advisor")
        print("6) Exit")
        try:
            choice = int(input("(Enter a Number)\n"))
            print("\n")
        except Exception:
            print("Invalid input")
            display()
        try:
            if choice in range(1, 7) and choice:
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
                    Methods.exit()
                else:
                    print("Input Choice Error\n")
            else:
                print("Please Enter a Valid Number (1-6)")
                display()
        except ValueError:
            print("Input Invalid... Please Try Again")
            display()