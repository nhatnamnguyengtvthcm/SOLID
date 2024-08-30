from datetime import datetime
from typing import Optional
from entity import Entity


class User(Entity):
    
    _name: str
    _last_login: datetime

    def get_name(self):
        return self._name
    
    def get_last_login(self):
        return self._last_login
    
    def set_name(self, name: str):
        self._name = name

    def set_last_login(self, last_login: Optional[datetime]):
        if isinstance(last_login, datetime):
            self._last_login = last_login      
        else:
            try:
                self._last_login = datetime.fromisoformat(last_login)
            except ValueError:
                raise ValueError("Invalid datetime format")
        
    
    