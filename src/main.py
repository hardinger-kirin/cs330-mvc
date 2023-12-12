import sys
from Database import Database
from Controller import Controller
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
    controller = Controller(db)

    # creates and executes an application using the view.ui file
    # separates application into model views
    user_v = UserView(app, 'view.ui', controller)
    user_v.run()
