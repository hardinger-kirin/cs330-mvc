# referenced
# https://realpython.com/python-pyqt-database/#connecting-pyqt-to-an-sql-database
from PyQt5.QtSql import QSqlDatabase


class Database:
    def __init__(self, name):
        self.name = name
        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.con.setDatabaseName(name)
        self.con.open()
