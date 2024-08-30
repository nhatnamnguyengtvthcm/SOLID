
from pydantic import BaseModel, ValidationError

from single_responsibility.store import Store
from single_responsibility.user_validate import UserValidate

# from .store import Store
from .user import User
import re

class SingleUserHandler:
    def __init__(self):
        self.store = Store()
   

    def create_user(self, json_user):
        try:
            user = User(**json_user)
        except ValidationError as e:
            return "please provide a valid JSON"
        
        user_validate = UserValidate()
        valid_user = user_validate.isValidUser(user)

        if  not valid_user:
            return "ERROR"
        self.store.add_user(user)
        return "SUCCESS"