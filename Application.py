from PyQt5 import uic, QtWidgets


class Application(object):
    def __init__(self, app, ui_file, controller):
        self.app = app
        self.ui = uic.loadUi(ui_file)
        # self.ui.showMaximized()
        self.ui.show()
        self.controller = controller
        self.controller.add_view(self)

        # initializes widgets that handle username
        # upon pressing "enter", the user's name is updated
        self.name_input = self.get_lineedit_widget("name_input")
        self.name_prompt = self.get_label_widget("name_prompt")
        self.hello_label = self.get_label_widget("hello_label")
        self.name_input.returnPressed.connect(self.name_entered)

        # initializes widgets for tasks
        self.task_count = self.get_label_widget("task_count")
        self.task_count.setVisible(False)

        # starts app
        self.app.exec()

    # updates the view to display the name
    # passes info off to controller to handle adding user to the database
    def name_entered(self):
        self.name_prompt.setText("")
        self.hello_label.setText(f"Hello, {self.name_input.text()}")
        self.controller.generate_user(self.name_input.text())
        # removes prompt and text box to prevent entering another name
        self.name_prompt.setParent(None)
        self.name_input.setParent(None)
        self.show_tasks(self.controller.get_task_count())

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
