class Model:
    def __init__(self):
        self.observers = []

    def register_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        try:
            self.observers.remove(self.tasks.index(o))
            return 1
        except ValueError:
            return 0

    def notify_observers(self):
        for o in self.observers:
            o.update()
