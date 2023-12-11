from Application import Application


class TaskView(Application):
    def __init__(self, app):
        self.app = app

    def add_model(self, model):
        self.model = model
