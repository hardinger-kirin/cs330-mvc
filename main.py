import sys
from Application import Application
from UserController import UserController
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    # creates QApplication widget
    app = QApplication(sys.argv)

    # sets up my custom font
    QFontDatabase().addApplicationFont("Daydream.ttf")
    app.setFont(QFont("Daydream"))

    # sets up user controller
    user_c = UserController("users.sqlite")

    # creates and executes an application using the view.ui file
    a = Application(app, 'view.ui', user_c)
