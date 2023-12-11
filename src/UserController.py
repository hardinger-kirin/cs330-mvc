from User import User


class UserController():
    def __init__(self, db):
        self.db = db

    def add_view(self, view):
        self.view = view

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
        self.view.remove_login()

    def get_task_count(self):
        return self.user.get_task_count()

    def add_task(self):
        self.user.increment_task_count()
