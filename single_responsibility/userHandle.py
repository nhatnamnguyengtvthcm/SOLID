
from pydantic import BaseModel, ValidationError

from single_responsibility.store import Store

# from .store import Store
from .user import User
import re

class UserHandler:
    def __init__(self):
        self.store = Store()
   

    def create_user(self, json_user):
        try:
            user = User(**json_user)
        except ValidationError as e:
            return "please provide a valid JSON"
        
        if not self.isValidUser(user):
            return "ERROR"
        self.store.add_user(user)
        return "SUCCESS"

    def isPresent(self, value):
        return value is not None and len(value.strip()) > 0
    
    def isValidAlphaNumeric(self, value):
        pattern = re.compile(r'^[a-zA-Z0-9]+$')
        return pattern.match(value) is not None
    
    def isValidEmail(self, email):
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return pattern.match(email) is not None

    
   
    def isValidUser(self, user: User):
        if not self.isPresent(user.get_name()):
            return False
        user.set_name(user.get_name().strip())
        if not self.isValidAlphaNumeric(user.get_name()):
            return False
        if user.get_email() is None or len(user.get_email().strip()) == 0:
            return False
        user.set_email(user.get_email().strip())
        print(user.get_email())
        if not self.isValidEmail(user.get_email()):
            return False
    
    