class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} <{self.email}>"

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email
    
    def set_name(self, name: str):
        self.name = name

    def set_email(self, email: str):
        self.email = email

    def get_user(self):
        return self

    def get_user_info(self):
        return f"{self.name} <{self.email}>"