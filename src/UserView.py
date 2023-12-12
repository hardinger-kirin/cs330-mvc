from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QAbstractItemView, QTableWidgetItem, \
                            QPushButton, QHeaderView, QApplication


class UserView():
    def __init__(self, app, ui_file, controller):
        self.app = app
        self.ui = uic.loadUi(ui_file)
        self.controller = controller
        self.controller.add_view(self)

        # initializes widgets that handle username
        # upon pressing "enter", the user's name is updated
        self.input = self.get_lineedit_widget("input")
        self.prompt = self.get_label_widget("prompt")
        self.hello_label = self.get_label_widget("hello_label")
        self.hello_label.setVisible(False)
        self.input.returnPressed.connect(self.name_entered)

        # initializes widgets for tasks the user has
        self.task_count = self.get_label_widget("task_count")
        self.task_count.setVisible(False)
        self.add_task_button = self.get_button_widget("add_task_button")
        self.add_task_button.setVisible(False)
        self.add_task_button.clicked.connect(self.prompt_task)

        # initializes widgets for the cat gif, representing the user's progress
        self.progress_label = self.get_label_widget("progress_label")
        self.progress_label.setVisible(False)
        self.gif_widget = self.get_label_widget("gif")
        self.gif_widget.setVisible(False)

        # initializes widgets for the task table view
        self.task_table = self.get_table_widget("task_table")
        self.task_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.task_table.setVisible(False)

    def run(self):
        self.ui.show()
        self.app.exec()

    def add_model(self, model):
        self.model = model

    # updates the view to display the name
    # passes info off to controller to handle adding user to the database
    def name_entered(self):
        self.controller.generate_user(self.input.text())
        self.show_task_count()

    def say_hi(self, name):
        self.hello_label.setText(f"Hello, {name}")

    def welcome_back(self, name):
        self.hello_label.setText(f"Welcome back, {name}")

    # removes prompt and text box to prevent entering another name
    def remove_login(self):
        self.prompt.setVisible(False)
        self.input.setVisible(False)
        self.hello_label.setVisible(True)
        self.input.clear()
        self.show_task_count()
        self.show_cat()
        self.show_progress()
        if self.model.get_task_count() != 0:
            self.show_task_table()

    def prompt_task(self):
        self.prompt.setText("Enter task name:")
        self.prompt.setVisible(True)
        self.input.setVisible(True)
        self.input.returnPressed.disconnect()
        self.input.returnPressed.connect(self.add_task)

    def add_task(self):
        self.controller.add_task(self.input.text())
        self.prompt.setVisible(False)
        self.input.setVisible(False)
        self.input.clear()
        self.task_added()

    def task_added(self):
        self.update_task_count()
        self.update_cat()
        self.update_progress()
        self.show_task_table()

    def show_task_count(self):
        self.update_task_count()
        self.task_count.setVisible(True)
        self.add_task_button.setVisible(True)

    def update_task_count(self):
        self.task_count.setText(f"You have {self.model.get_task_count()}" +
                                " tasks")

    def show_cat(self):
        self.update_cat()
        self.gif_widget.setVisible(True)

    def update_cat(self):
        if self.model.get_progress() < 1 and self.model.get_progress() != -1:
            self.gif = QMovie("Assets/sad.gif")
        else:
            self.gif = QMovie("Assets/happy.gif")
        self.gif_widget.setMovie(self.gif)
        self.gif.start()

    def show_progress(self):
        self.update_progress()
        self.progress_label.setVisible(True)

    def update_progress(self):
        progress = self.model.get_progress()
        if progress == -1:
            progress = 1
        self.progress_label.setText(f"Progress: {progress * 100}%")

    def show_task_table(self):
        self.task_table.setVisible(True)
        self.update_task_table()

    def add_db(self, db):
        self.db = db

    # referenced:
    # https://stackoverflow.com/questions/24148968/how-to-add-multiple-qpushbuttons-to-a-qtableview
    # for adding buttons to each row
    # https://stackoverflow.com/questions/26141161/pyqt4-code-not-working-on-pyqt5-qheaderview
    # for resizing columns to be dynamically stretched
    def update_task_table(self):
        # sets row and column count, initializes column titles
        self.task_table.setRowCount(self.model.get_task_count())
        self.task_table.setColumnCount(4)
        self.task_table.setHorizontalHeaderItem(0,
                                                QTableWidgetItem("Task"))
        self.task_table.setHorizontalHeaderItem(1,
                                                QTableWidgetItem("Status"))
        self.task_table.setHorizontalHeaderItem(2,
                                                QTableWidgetItem("Mark"))
        self.task_table.setHorizontalHeaderItem(3,
                                                QTableWidgetItem("Remove"))
        # loads tasks and task information
        row = 0
        for task in self.model.get_tasks():
            if task[3] == '1':
                status = "Complete"
            elif task[3] == '0':
                status = "Incomplete"
            self.task_table.setVerticalHeaderItem(row,
                                                  QTableWidgetItem(row))
            self.task_table.setItem(row, 0, QTableWidgetItem(task[2]))
            self.task_table.setItem(row, 1, QTableWidgetItem(status))

            check_comp = QPushButton('Mark')
            check_comp.pressed.connect(self.complete_task)
            self.task_table.setCellWidget(row, 2, check_comp)

            btn_rem = QPushButton('Remove')
            btn_rem.clicked.connect(self.remove_task)
            self.task_table.setCellWidget(row, 3, btn_rem)

            header = self.task_table.horizontalHeader()
            header.setSectionResizeMode(row, QHeaderView.Stretch)
            row += 1

    def complete_task(self):
        button = QApplication.focusWidget()
        index = self.task_table.indexAt(button.pos())
        if index.isValid():
            task_name = self.task_table.item(index.row(), 0).text()
            self.controller.update_task(task_name, 1)
            self.update_task_table()
            self.update_progress()
            self.update_cat()

    def remove_task(self):
        button = QApplication.focusWidget()
        index = self.task_table.indexAt(button.pos())
        if index.isValid():
            task_name = self.task_table.item(index.row(), 0).text()
            self.controller.remove_task(task_name)
            self.update_task_table()
            self.update_task_count()
            self.update_progress()

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

    def get_table_widget(self, label):
        for widget in self.app.allWidgets():
            child = widget.findChild(QtWidgets.QTableWidget, label)
            if child is not None:
                return child
        return None
