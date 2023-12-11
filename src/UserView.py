from Application import Application
from PyQt5.QtGui import QMovie


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
        self.input.returnPressed.connect(self.name_entered)

        # initializes widgets for tasks the user has
        self.task_count = self.app.get_label_widget("task_count")
        self.task_count.setVisible(False)
        self.add_task_button = self.app.get_button_widget("add_task_button")
        self.add_task_button.setVisible(False)
        self.add_task_button.clicked.connect(self.prompt_task)

        # initializes widgets for the cat gif, representing the user's progress
        self.gif_widget = self.app.get_label_widget("gif")
        self.gif_widget.setVisible(False)

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
        self.input.clear()
        self.show_task_count()
        self.show_cat()

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
