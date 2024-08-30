from single_responsibility.store import Store
from single_responsibility.user import User


class UserPesistance:
    def __init__(self):
        self.store =  Store()

    def add_user(self, user: User):
        self.store.append(user)
