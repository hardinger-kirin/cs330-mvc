from Application import Application


class TaskView(Application):
    def __init__(self, app):
        self.app = app

        # initializes widgets for tasks
        self.task_count = self.app.get_label_widget("task_count")
        self.task_count.setVisible(False)
        self.add_task_button = self.app.get_button_widget("add_task_button")
        self.add_task_button.setVisible(False)
        self.add_task_button.released.connect(self.test)  # add task upon click

    def add_model(self, model):
        self.model = model

    def show_tasks(self, count):
        self.task_count.setText(f"You have {count} tasks")
        self.task_count.setVisible(True)
        self.add_task_button.setVisible(True)

    def test(self):
        self.task_count.setText("You have 100 tasks")
