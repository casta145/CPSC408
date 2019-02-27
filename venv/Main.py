import sqlite3
import sys
from Methods import Methods
from Student import Student
from sql import Connection
from Menu import Menu

Methods = Methods()
sql = Connection()
Menu = Menu()

sql.dbconnect()

while True:
    Menu.display()