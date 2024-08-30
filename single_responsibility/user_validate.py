import re
from single_responsibility.user import User


class UserValidate:

    def __init__(self):
        pass

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
        if not self.isValidEmail(user.get_email()):
            return False
        return True