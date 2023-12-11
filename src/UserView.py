from Application import Application


class UserView(Application):
    def __init__(self, app, controller):
        self.app = app
        self.controller = controller
        self.controller.add_view(self)

        # initializes widgets that handle username
        # upon pressing "enter", the user's name is updated
        self.name_input = self.app.get_lineedit_widget("name_input")
        self.name_prompt = self.app.get_label_widget("name_prompt")
        self.hello_label = self.app.get_label_widget("hello_label")
        self.name_input.returnPressed.connect(self.name_entered)

        # initializes widgets for tasks the user has
        self.task_count = self.app.get_label_widget("task_count")
        self.task_count.setVisible(False)
        self.add_task_button = self.app.get_button_widget("add_task_button")
        self.add_task_button.setVisible(False)
        self.add_task_button.clicked.connect(self.task_added)

    def add_model(self, model):
        self.model = model

    # updates the view to display the name
    # passes info off to controller to handle adding user to the database
    def name_entered(self):
        self.controller.generate_user(self.name_input.text())
        self.show_task_count()

    def say_hi(self, name):
        self.hello_label.setText(f"Hello, {name}")

    def welcome_back(self, name):
        self.hello_label.setText(f"Welcome back, {name}")

    # removes prompt and text box to prevent entering another name
    def remove_login(self):
        self.name_prompt.setParent(None)
        self.name_input.setParent(None)
        self.show_task_count()

    def task_added(self):
        self.controller.add_task()
        self.update_task_count()

    def show_task_count(self):
        self.update_task_count()
        self.task_count.setVisible(True)
        self.add_task_button.setVisible(True)

    def update_task_count(self):
        self.task_count.setText(f"You have {self.model.num_tasks} tasks")
