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
                task_id INTEGER PRIMARY KEY UNIQUE,
                user_id INTEGER NOT NULL,
                task_name VARCHAR(40) NOT NULL,
                status VARCHAR(1) NOT NULL,
                CONSTRAINT fk_users
                FOREIGN KEY (user_id)
                REFERENCES users(user_id)
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

    def add_task_entry(self, user_id, task_name):
        QSqlQuery(self.con).exec(
            f"""
            INSERT INTO tasks (user_id, task_name, status)
            VALUES ({user_id},'{task_name}', 0)
            """
        )

    def load_tasks(self, user_id):
        q = QSqlQuery(self.con)
        q.exec_(
            f"""
                SELECT * from tasks where user_id = {user_id}
            """
        )
        tasks = []
        while q.next():
            tasks.append([q.value(0), q.value(1), q.value(2),
                          q.value(3)])
        return tasks
