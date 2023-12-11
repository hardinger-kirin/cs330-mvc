import sys
from Database import Database
from Application import Application
from UserController import UserController
from UserView import UserView
from PyQt5.QtGui import QFontDatabase, QFont, QIcon
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    # creates QApplication widget
    app = QApplication(sys.argv)

    # sets up custom application icon
    app.setWindowIcon(QIcon("Assets/icon.png"))

    # sets up my custom font
    QFontDatabase().addApplicationFont("Assets/Daydream.ttf")
    app.setFont(QFont("Daydream"))

    # sets up database
    db = Database("info.sqlite")

    # sets up controllers
    user_c = UserController(db)

    # creates and executes an application using the view.ui file
    # separates application into model views
    a = Application(app, 'view.ui')
    user_v = UserView(a, user_c)
    a.run()
