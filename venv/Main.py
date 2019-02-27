from sql import Connection
from Menu import Menu

sql = Connection()
Menu = Menu()

sql.dbconnect()

while True:
    Menu.display()