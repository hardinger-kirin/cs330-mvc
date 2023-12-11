import sys
from Database import Database
from Application import Application
from UserController import UserController
from TaskController import TaskController
from TaskView import TaskView
from UserView import UserView
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    # creates QApplication widget
    app = QApplication(sys.argv)

    # sets up my custom font
    QFontDatabase().addApplicationFont("Assets/Daydream.ttf")
    app.setFont(QFont("Daydream"))

    # sets up database
    db = Database("info.sqlite")

    # sets up controllers
    user_c = UserController(db)
    task_c = TaskController(db)

    # creates and executes an application using the view.ui file
    # separates application into model views
    a = Application(app, 'view.ui')
    user_v = UserView(a, user_c)
    task_v = TaskView(a)
    a.add_user_v(user_v)
    a.add_task_v(task_v)
    a.run()
