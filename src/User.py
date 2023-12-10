from Model import Model


class User(Model):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.tasks = []
        self.num_tasks = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        self.notify_observers

    def get_tasks(self):
        return self.tasks

    def add_task(self, t):
        self.tasks.append(t)
        self.num_tasks += 1
        self.notify_observers

    def remove_task(self, t):
        try:
            self.tasks.remove(self.tasks.index(t))
            self.num_tasks -= 1
            self.notify_observers
            return 1
        except ValueError:
            return 0

    def get_task_count(self):
        return self.num_tasks
