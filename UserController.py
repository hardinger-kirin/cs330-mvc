# import View
from UserDatabase import UserDatabase
from User import User


class UserController:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = UserDatabase(db_name)

    def add_view(self, view):
        self.view = view

    # checks if a user with the given name already exists
    # if not, add it to the database
    # if so, load the user's information from the database
    def generate_user(self, name):
        self.user = User(name)
        if self.db.find_entry(name) == 0:
            self.db.add_entry(name)
        else:
            pass

    def get_task_count(self):
        return self.user.get_task_count()
