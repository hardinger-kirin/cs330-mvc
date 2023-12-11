

class User():
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.tasks = []
        self.num_tasks = 0
        self.progress = 0
        self.observers = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        self.notify_observers

    def get_tasks(self):
        return self.tasks

    def set_tasks(self, task_list):
        self.tasks = task_list

    def register_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def get_task_count(self):
        return self.num_tasks

    def set_task_count(self, num_tasks):
        self.num_tasks = num_tasks

    def increment_task_count(self):
        self.num_tasks += 1

    def get_progress(self):
        if self.num_tasks == 0:
            return -1

        num_complete = 0
        for array in self.tasks:
            if array[3] == 1:
                num_complete += 1
        self.progress = num_complete / self.num_tasks
        return self.progress
