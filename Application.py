from PyQt5 import uic, QtWidgets


class Application(object):
    def __init__(self, app, ui_file, controller):
        self.app = app
        self.ui = uic.loadUi(ui_file)
        self.controller = controller
        self.controller.add_view(self)

        # initializes widgets for tasks
        self.task_count = self.get_label_widget("task_count")
        self.task_count.setVisible(False)

    def run(self):
        self.ui.show()
        self.app.exec()

    def show_tasks(self, count):
        self.task_count.setText(f"You have {count} tasks")
        self.task_count.setVisible(True)

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
