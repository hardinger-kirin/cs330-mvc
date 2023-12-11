from User import User


class UserController():
    def __init__(self, db):
        self.db = db

    def add_view(self, view):
        self.view = view

    def get_app(self):
        return self.app

    # checks if a user with the given name already exists
    # if not, add it to the database
    # if so, load the user's information from the database
    def generate_user(self, name):
        self.user = User(name)
        self.view.add_model(self.user)
        if self.db.find_user_entry(name) == 0:
            self.view.say_hi(name)
            self.db.add_user_entry(name)
        else:
            self.view.welcome_back(name)
            self.get_tasks(self.db.find_user_entry(name))
        self.view.remove_login()

    def add_task(self, name):
        self.db.add_task_entry(self.db.find_user_entry(self.user.get_name()),
                               name)
        self.get_tasks(self.db.find_user_entry(self.user.get_name()))

    def get_tasks(self, id):
        task_list = self.db.load_tasks(id)
        if task_list is None:
            return
        else:
            self.user.set_tasks(task_list)
            self.user.set_task_count(len(task_list))
            return task_list
