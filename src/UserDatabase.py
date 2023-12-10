# referenced
# https://realpython.com/python-pyqt-database/#connecting-pyqt-to-an-sql-database
from Database import Database
from PyQt5.QtSql import QSqlQuery


class UserDatabase(Database):
    def __init__(self, name):
        super().__init__(name)
        QSqlQuery().exec(
            """
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name VARCHAR(40) NOT NULL
            )
            """
        )

    def add_entry(self, name):
        QSqlQuery().exec(
            f"""
            INSERT INTO users (name)
            VALUES ('{name}')
            """
        )

    def find_entry(self, term):
        q = QSqlQuery(self.con)
        q.exec_(
            """
            SELECT id, name from users
            """
        )
        while q.next():
            if q.value(1) == term:
                return q.value(0)
        return 0
