from single_responsibility.user import User


class Store:
    
    def __init__(self):
        pass

    storage = []

    def add_user(self, user: User):
        self.storage.append(user)

    def get_user(self, name):
        for user in self.storage:
            if user.name == name:
                return user