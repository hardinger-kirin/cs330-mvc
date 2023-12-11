# referenced
# https://realpython.com/python-pyqt-database/#connecting-pyqt-to-an-sql-database
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtSql import QSqlDatabase


class Database():
    def __init__(self, name):
        self.name = name
        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.con.setDatabaseName(name)
        self.con.open()

        # create users table
        QSqlQuery(self.con).exec(
            """
            CREATE TABLE users (
                user_id INTEGER PRIMARY KEY UNIQUE,
                user_name VARCHAR(40) NOT NULL
            )
            """
        )

        # create tasks table
        QSqlQuery(self.con).exec(
            """
            CREATE TABLE tasks (
                task_id int NOT NULL,
                user_id int NOT NULL,
                PRIMARY KEY (task_id),
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
            """
        )

    def add_user_entry(self, entry):
        QSqlQuery(self.con).exec(
            f"""
            INSERT INTO users (user_name)
            VALUES ('{entry}')
            """
        )

    def find_user_entry(self, term):
        q = QSqlQuery(self.con)
        q.exec_(
            """
            SELECT user_id, user_name from users
            """
        )
        while q.next():
            if q.value(1) == term:
                return q.value(0)
        return 0
