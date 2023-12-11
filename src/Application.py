from PyQt5 import uic, QtWidgets


class Application(object):
    def __init__(self, app, ui_file):
        self.app = app
        self.ui = uic.loadUi(ui_file)

    def run(self):
        self.ui.show()
        self.app.exec()

    # searches through all widgets for a line edit child with a given label
    # if found, returns the child
    # if not, returns None
    def get_lineedit_widget(self, label):
        for widget in self.app.allWidgets():
            child = widget.findChild(QtWidgets.QLineEdit, label)
            if child is not None:
                return child
        return None

    def get_label_widget(self, label):
        for widget in self.app.allWidgets():
            child = widget.findChild(QtWidgets.QLabel, label)
            if child is not None:
                return child
        return None

    def get_button_widget(self, label):
        for widget in self.app.allWidgets():
            child = widget.findChild(QtWidgets.QPushButton, label)
            if child is not None:
                return child
        return None
