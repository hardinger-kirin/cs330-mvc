# from Task import Task


class TaskController():
    def __init__(self, db):
        self.db = db

    def add_view(self, view):
        self.view = view
