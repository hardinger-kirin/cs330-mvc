from Application import Application


class UserView(Application):
    def __init__(self, app, ui_file, controller):
        super().__init__(app, ui_file, controller)

        # initializes widgets that handle username
        # upon pressing "enter", the user's name is updated
        self.name_input = self.get_lineedit_widget("name_input")
        self.name_prompt = self.get_label_widget("name_prompt")
        self.hello_label = self.get_label_widget("hello_label")
        self.name_input.returnPressed.connect(self.name_entered)

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
