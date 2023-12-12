from Application import Application
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QAbstractItemView, QTableWidgetItem, QCheckBox, \
                            QPushButton, QHeaderView


class UserView(Application):
    def __init__(self, app, controller):
        self.app = app
        self.controller = controller
        self.controller.add_view(self)

        # initializes widgets that handle username
        # upon pressing "enter", the user's name is updated
        self.input = self.app.get_lineedit_widget("input")
        self.prompt = self.app.get_label_widget("prompt")
        self.hello_label = self.app.get_label_widget("hello_label")
        self.hello_label.setVisible(False)
        self.input.returnPressed.connect(self.name_entered)

        # initializes widgets for tasks the user has
        self.task_count = self.app.get_label_widget("task_count")
        self.task_count.setVisible(False)
        self.add_task_button = self.app.get_button_widget("add_task_button")
        self.add_task_button.setVisible(False)
        self.add_task_button.clicked.connect(self.prompt_task)

        # initializes widgets for the cat gif, representing the user's progress
        self.progress_label = self.app.get_label_widget("progress_label")
        self.progress_label.setVisible(False)
        self.gif_widget = self.app.get_label_widget("gif")
        self.gif_widget.setVisible(False)

        # initializes widgets for the task table view
        self.task_table = self.app.get_table_widget("task_table")
        self.task_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.task_table.setVisible(False)

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
        if self.model.get_progress() == -1 or self.model.get_progress() == 100:
            self.gif = QMovie("Assets/happy.gif")
        else:
            self.gif = QMovie("Assets/sad.gif")
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
                                                QTableWidgetItem("Complete"))
        self.task_table.setHorizontalHeaderItem(3,
                                                QTableWidgetItem("Remove"))
        row = 0
        for task in self.model.get_tasks():
            if task[3] == 1:
                status = "Complete"
            else:
                status = "Incomplete"
            self.task_table.setVerticalHeaderItem(row,
                                                  QTableWidgetItem(row))
            self.task_table.setItem(row, 0, QTableWidgetItem(task[2]))
            self.task_table.setItem(row, 1, QTableWidgetItem(status))

            self.check_comp = QCheckBox()
            self.check_comp.stateChanged.connect(self.complete_task)
            self.check_comp.setStyleSheet("margin-left:50%")
            self.task_table.setCellWidget(row, 2, self.check_comp)

            self.btn_rem = QPushButton('Remove')
            self.btn_rem.clicked.connect(self.remove_task)
            self.task_table.setCellWidget(row, 3, self.btn_rem)

            header = self.task_table.horizontalHeader()
            header.setSectionResizeMode(row, QHeaderView.Stretch)
            row += 1

    def complete_task(self):
        pass

    def remove_task(self):
        pass
